#!/usr/bin/env python3
"""
Dynamic build configuration for doosan_drfl.
Static metadata lives in pyproject.toml; this file handles only the parts
that cannot be expressed in TOML: OS/arch detection, the C++ extension
definition, and custom build commands.
"""

import os
import sys
import platform
import subprocess
import shutil
import pybind11
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install


# ---------------------------------------------------------------------------
# Platform / architecture helpers
# ---------------------------------------------------------------------------

def get_build_config():
    """
    Return library_dirs, libraries, and extra_link_args for the current
    OS and architecture.
    """
    system  = sys.platform
    machine = platform.machine()

    arch_map = {
        'x86_64': 'amd64', 'AMD64':   'amd64',
        'aarch64': 'arm64', 'arm64':   'arm64',
        'i386':   '32bits', 'i686':    '32bits',
    }
    arch      = arch_map.get(machine, 'unknown')
    base_path = "../library/API-DRFL/library"

    # --- Windows -----------------------------------------------------------
    if system == 'win32':
        if arch == 'amd64':
            lib_dir = os.path.join(base_path, 'Windows', '64bits')
        elif arch == '32bits':
            lib_dir = os.path.join(base_path, 'Windows', '32bits')
        else:
            raise ValueError(f"Unsupported Windows architecture: {machine}")

        return {
            'library_dirs':    [lib_dir],
            'libraries':       ['DRFLWin64', 'PocoFoundation64', 'PocoNet64'],
            'extra_link_args': [],
        }

    # --- Linux -------------------------------------------------------------
    elif system == 'linux':
        dist_name = dist_version = None
        try:
            import distro
            dist_name, dist_version = distro.id(), distro.version()
        except ImportError:
            if os.path.exists('/etc/os-release'):
                with open('/etc/os-release') as f:
                    for line in f:
                        if line.startswith('ID='):
                            dist_name    = line.split('=')[1].strip().strip('"')
                        elif line.startswith('VERSION_ID='):
                            dist_version = line.split('=')[1].strip().strip('"')

        supported_ubuntu = ['18.04', '20.04', '22.04', '24.04']
        newest_ubuntu    = '24.04'

        if dist_name == 'ubuntu':
            if dist_version not in supported_ubuntu:
                raise ValueError(
                    f"Unsupported Ubuntu version: {dist_version}. "
                    f"Supported: {', '.join(supported_ubuntu)}"
                )
            if arch not in ('amd64', 'arm64'):
                raise ValueError(f"Unsupported Ubuntu architecture: {machine}")

            return {
                'library_dirs':    [os.path.join(base_path, 'Linux/64bits', arch, dist_version)],
                'libraries':       ['DRFL', 'PocoFoundation', 'PocoNet'],
                'extra_link_args': [],
            }

        # Generic Linux (Arch, Fedora, Debian, …)
        if arch in ('amd64', 'arm64'):
            generic_dir = os.path.join(base_path, 'Linux/64bits', arch, 'generic')
            poco_dir    = os.path.join(base_path, 'Linux/64bits', arch, newest_ubuntu)
            print(
                f"ℹ️  Generic Linux: bundled Poco from Ubuntu {newest_ubuntu} will be used."
            )
            return {
                'library_dirs':    [generic_dir, poco_dir],
                'libraries':       ['DRFL', 'PocoFoundation', 'PocoNet'],
                'extra_link_args': [f'-Wl,-rpath,{os.path.abspath(poco_dir)}'],
            }

        raise ValueError(f"Unsupported Linux architecture: {machine}")

    raise OSError(f"Unsupported operating system: {system}")


# ---------------------------------------------------------------------------
# Custom commands
# ---------------------------------------------------------------------------

class BuildExtWithStubs(build_ext):
    """Generate .pyi stubs after the extension is compiled."""

    def run(self):
        super().run()
        self._generate_stubs('doosan_drfl')

    def _generate_stubs(self, module_name):
        stub_generators = [
            ('pybind11_stubgen', 'pybind11-stubgen'),
            ('stubgen',          'mypy'),
        ]
        stub_dir  = os.path.join(os.path.dirname(__file__), 'stubs')
        stub_file = f"{module_name}.pyi"

        # Make the just-built extension importable whether we're doing
        # "build_ext --inplace" (ext lands in source dir) or "pip install ."
        # (ext lands in a temp dir like build/lib.linux-x86_64-3.x).
        search_paths = [
            os.path.abspath(self.build_lib),             # pip install / build
            os.path.dirname(os.path.abspath(__file__)),  # --inplace
        ]
        env = os.environ.copy()
        existing = env.get('PYTHONPATH', '')
        env['PYTHONPATH'] = os.pathsep.join(filter(None, search_paths + [existing]))

        for generator, package_name in stub_generators:
            try:
                probe = subprocess.run(
                    [sys.executable, '-m', generator, '--help'],
                    capture_output=True, text=True, timeout=10,
                )
                if probe.returncode != 0:
                    continue

                print(f"\n{'='*60}\nGenerating stubs with {generator}...\n{'='*60}")
                os.makedirs(stub_dir, exist_ok=True)

                cmd = (
                    [sys.executable, '-m', generator, module_name, '-o', stub_dir]
                    if generator == 'pybind11_stubgen'
                    else [sys.executable, '-m', generator, '-m', module_name, '-o', stub_dir]
                )
                result = subprocess.run(cmd, capture_output=True, text=True, env=env)

                if result.returncode == 0:
                    src = os.path.join(stub_dir, stub_file)
                    dst = os.path.join(os.path.dirname(__file__), stub_file)
                    if os.path.exists(src):
                        shutil.copy2(src, dst)
                    print(f"✔️  Stubs written to {dst}")
                    return True

                print(f"❌ {generator} failed:\n{result.stderr}")

            except Exception as exc:
                print(f"⚠️  {generator} unavailable: {exc}")

        print(
            "\n⚠️  Could not generate stubs automatically.\n"
            "   Install one of:\n"
            "     pip install pybind11-stubgen   (preferred)\n"
            "     pip install mypy               (fallback)\n"
            "   Then re-run: python setup.py build_ext --inplace"
        )
        return False


class InstallToVenv(install):
    """
    Build and install doosan_drfl into the active virtual environment.

    Usage:
        python setup.py install_venv
    """

    description = 'Build and install doosan_drfl into the active virtual environment'

    def run(self):
        venv = os.environ.get('VIRTUAL_ENV')
        if not venv:
            print(
                "\n❌ No active virtual environment detected.\n"
                "   Activate one first:  source /path/to/venv/bin/activate\n"
                "   Then re-run:         python setup.py install_venv"
            )
            sys.exit(1)

        print(f"\n{'='*60}\nInstalling into venv : {venv}\nInterpreter          : {sys.executable}\n{'='*60}\n")
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '.', '--no-build-isolation'],
            cwd=os.path.dirname(os.path.abspath(__file__)),
        )
        if result.returncode != 0:
            print(f"\n❌ Installation failed (exit code {result.returncode}).")
            sys.exit(result.returncode)
        print("\n✔️  doosan_drfl installed. 'import doosan_drfl' now works from any directory.")


# ---------------------------------------------------------------------------
# Extension
# ---------------------------------------------------------------------------

try:
    build_cfg        = get_build_config()
    abs_library_dirs = [os.path.abspath(d) for d in build_cfg['library_dirs']]
    print("Library directories:")
    for d in abs_library_dirs:
        print(f"  {d}")
except Exception as exc:
    print(f"Error detecting library configuration: {exc}")
    sys.exit(1)

ext_modules = [
    Extension(
        'doosan_drfl',
        sources=[
            './drfl_wrapper.cpp',
            './cdrflex_bindings.cpp',
            './drfl_structs.cpp',
            './drfl_enums.cpp',
        ],
        include_dirs=[
            pybind11.get_include(),
            '../library/API-DRFL/include',
        ],
        library_dirs=abs_library_dirs,
        libraries=build_cfg['libraries'],
        language='c++',
        extra_compile_args=['-std=c++17', '-DDRCF_VERSION=2'],
        extra_link_args=build_cfg['extra_link_args'],
    ),
]

setup(
    ext_modules=ext_modules,
    cmdclass={
        'build_ext':    BuildExtWithStubs,
        'install_venv': InstallToVenv,
    },
)
