"""
setup.py — Platform-aware build configuration for the DRFL pybind11 extension.

Reads OS / architecture / Ubuntu version at build time and selects the
correct pre-built libraries from the vendor tree.
"""
from __future__ import annotations

import os
import platform
import struct
import sys
from pathlib import Path

from setuptools import Extension, setup

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).parent.resolve()
LIBRARY_ROOT = ROOT / "library" / "API-DRFL"
INCLUDE_DIR = LIBRARY_ROOT / "include"
LIB_ROOT = LIBRARY_ROOT / "library"
SRC_DIR = ROOT / "src"

SOURCES = [
    str(SRC_DIR / "cdrflex_bindings.cpp"),
    str(SRC_DIR / "drfl_enums.cpp"),
    str(SRC_DIR / "drfl_structs.cpp"),
    str(SRC_DIR / "drfl_wrapper.cpp"),
]

# ---------------------------------------------------------------------------
# Platform detection helpers
# ---------------------------------------------------------------------------

def _bits() -> int:
    """Pointer size in bits (32 or 64)."""
    return struct.calcsize("P") * 8


def _ubuntu_version() -> str | None:
    """
    Return Ubuntu version string (e.g. '22.04') if running on Ubuntu,
    otherwise None.
    """
    os_release = Path("/etc/os-release")
    if not os_release.exists():
        return None
    info: dict[str, str] = {}
    for line in os_release.read_text().splitlines():
        if "=" in line:
            k, _, v = line.partition("=")
            info[k.strip()] = v.strip().strip('"')
    if info.get("ID", "").lower() != "ubuntu":
        return None
    return info.get("VERSION_ID")  # e.g. "22.04"


def _best_ubuntu_version(available: list[str], detected: str | None) -> str:
    """
    Pick the best available Ubuntu version folder for *detected*.

    - Exact match → use it.
    - No match (generic Linux or unknown distro) → use the newest available.
    - Detected is newer than all available → use the newest available.
    - Detected is older than the oldest available → use the oldest available.
    """
    available_sorted = sorted(available, key=lambda v: tuple(int(x) for x in v.split(".")))

    if detected is not None:
        det_tuple = tuple(int(x) for x in detected.split("."))
        # Exact match
        if detected in available:
            return detected
        # Closest version that is ≤ detected (fall back gracefully)
        candidates = [v for v in available_sorted if tuple(int(x) for x in v.split(".")) <= det_tuple]
        if candidates:
            return candidates[-1]

    # Generic Linux or nothing found — use newest
    return available_sorted[-1]


def _arch() -> str:
    """
    Normalise machine architecture to the folder name used in the vendor tree.
    Returns 'amd64' or 'arm64'.
    """
    machine = platform.machine().lower()
    if machine in ("x86_64", "amd64"):
        return "amd64"
    if machine in ("aarch64", "arm64"):
        return "arm64"
    # Best-effort fallback
    return "amd64"


# ---------------------------------------------------------------------------
# Library selection
# ---------------------------------------------------------------------------

def _select_linux_lib_dir() -> Path:
    arch = _arch()
    ubuntu_ver = _ubuntu_version()

    bits_dir = LIB_ROOT / "Linux" / "64bits"
    arch_dir = bits_dir / arch

    if not arch_dir.exists():
        raise RuntimeError(f"No vendor libraries found for architecture '{arch}' at {arch_dir}")

    available_versions = [d.name for d in arch_dir.iterdir() if d.is_dir()]
    if not available_versions:
        raise RuntimeError(f"No Ubuntu version sub-directories found under {arch_dir}")

    chosen = _best_ubuntu_version(available_versions, ubuntu_ver)
    lib_dir = arch_dir / chosen

    print(
        f"[setup.py] Linux/{arch} — detected Ubuntu={ubuntu_ver or 'unknown'}, "
        f"using library dir: {lib_dir.relative_to(ROOT)}"
    )
    return lib_dir


def _select_windows_lib_dir() -> Path:
    bits = _bits()
    sub = "64bits" if bits == 64 else "32bits"
    lib_dir = LIB_ROOT / "Windows" / sub
    if not lib_dir.exists():
        raise RuntimeError(f"No vendor libraries found at {lib_dir}")
    print(f"[setup.py] Windows {bits}-bit — using library dir: {lib_dir.relative_to(ROOT)}")
    return lib_dir


def _platform_extension_kwargs() -> dict:
    """
    Return the platform-specific keyword arguments for the Extension.
    Keys: library_dirs, libraries, extra_objects, extra_link_args, runtime_library_dirs
    """
    system = sys.platform

    if system == "win32":
        lib_dir = _select_windows_lib_dir()
        bits = _bits()
        prefix = "Win64" if bits == 64 else "Win32"
        poco_suffix = "64" if bits == 64 else ""

        return dict(
            library_dirs=[str(lib_dir)],
            # Link against the import libs (.dll.a for MinGW, .lib for MSVC)
            extra_objects=[
                str(lib_dir / f"DRFL{prefix}.dll.a"),
            ],
            extra_link_args=[],
            libraries=[],  # Poco DLLs are runtime-loaded; ship alongside the wheel
            define_macros=[("DRFL_WINDOWS", None)],
        )

    elif system.startswith("linux"):
        lib_dir = _select_linux_lib_dir()

        # Check if system Poco is available (non-Ubuntu distros)
        ubuntu_ver = _ubuntu_version()
        use_system_poco = ubuntu_ver is None  # not Ubuntu → use system libs

        kwargs = dict(
            library_dirs=[str(lib_dir)],
            extra_objects=[str(lib_dir / "libDRFL.a")],  # always use vendored DRFL
            extra_link_args=[],
            define_macros=[("DRFL_LINUX", None)],
        )

        if use_system_poco:
            # Let the linker find Poco from the system
            kwargs["libraries"] = ["PocoFoundation", "PocoNet"]
            print("[setup.py] Non-Ubuntu distro — linking against system Poco libraries")
        else:
            # Use vendored Poco .so files with embedded RPATH
            kwargs["libraries"] = ["PocoFoundation", "PocoNet"]
            kwargs["library_dirs"].append(str(lib_dir))
            kwargs["extra_link_args"] = [f"-Wl,-rpath,{lib_dir}"]

        return kwargs

    # elif system.startswith("linux"):
    #     lib_dir = _select_linux_lib_dir()
    #     return dict(
    #         library_dirs=[str(lib_dir)],
    #         libraries=["DRFL", "PocoFoundation", "PocoNet"],
    #         runtime_library_dirs=[str(lib_dir)],  # embed RPATH
    #         extra_link_args=[f"-Wl,-rpath,{lib_dir}"],
    #         define_macros=[("DRFL_LINUX", None)],
    #     )

    elif system == "darwin":
        # macOS is not listed in the vendor tree; raise early with a clear message.
        raise RuntimeError("macOS is not supported by the DRFL vendor libraries.")

    else:
        raise RuntimeError(f"Unsupported platform: {system}")


# ---------------------------------------------------------------------------
# pybind11 include dirs
# ---------------------------------------------------------------------------

def _pybind11_includes() -> list[str]:
    try:
        import pybind11
        return pybind11.get_include()
    except ImportError:
        raise ImportError(
            "pybind11 is required to build this package. "
            "Install it with:  pip install pybind11"
        )


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build_extension() -> Extension:
    platform_kwargs = _platform_extension_kwargs()

    return Extension(
        name="doosan_drfl",
        sources=SOURCES,
        include_dirs=[
            str(INCLUDE_DIR),
            _pybind11_includes(),
        ],
        language="c++",
        extra_compile_args=[
            "-std=c++17",
            "-O2",
            "-fvisibility=hidden",  # reduces symbol leakage on Linux
            "-DDRCF_VERSION=2",
            "-DPYBIND11_DETAILED_ERROR_MESSAGES"
        ] if sys.platform != "win32" else ["/std:c++17", "/O2", "/DDRCF_VERSION=2"],
        **platform_kwargs,
    )

setup(
    name="doosan_drfl",
    version="1.0",
    ext_modules=[build_extension()],
)
