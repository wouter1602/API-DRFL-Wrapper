#!/usr/bin/env python3
"""
install.py — Build the DRFL extension, generate pybind11 stubs, and install
             everything into the currently active virtual environment.

Usage:
    python install.py [--skip-stubs] [--editable] [--verbose]

Requirements:
    pip install pybind11 pybind11-stubgen build
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

HERE = Path(__file__).parent.resolve()
STUBS_DIR = HERE / "stubs"


def _run(cmd: list[str], **kwargs) -> None:
    """Run a subprocess, raising on failure."""
    print(f"\n[install.py] $ {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, check=True, **kwargs)


def _python() -> str:
    """Absolute path to the active venv's Python interpreter."""
    return sys.executable


def _pip() -> list[str]:
    return [_python(), "-m", "pip"]


def _assert_venv() -> None:
    if sys.prefix == sys.base_prefix:
        print(
            "[install.py] WARNING: No virtual environment detected. "
            "It is strongly recommended to activate a venv before running this script."
        )


def _check_tool(module: str, install_hint: str) -> None:
    result = subprocess.run(
        [_python(), "-c", f"import {module}"],
        capture_output=True,
    )
    if result.returncode != 0:
        print(f"[install.py] '{module}' not found — installing…")
        _run([*_pip(), "install", install_hint])


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------

def step_check_dependencies() -> None:
    print("\n── Checking build dependencies ──────────────────────────────")
    _check_tool("pybind11", "pybind11>=2.11")
    _check_tool("build", "build")


def step_build_and_install(editable: bool, verbose: bool) -> None:
    print("\n── Building & installing extension ──────────────────────────")
    if editable:
        # In-place build; the .so/.pyd ends up next to setup.py
        cmd = [*_pip(), "install", "--no-build-isolation", "-e", str(HERE)]
    else:
        cmd = [*_pip(), "install", "--no-build-isolation", str(HERE)]

    if verbose:
        cmd.append("-v")

    _run(cmd, cwd=HERE)


def step_generate_stubs(verbose: bool) -> None:
    print("\n── Generating stubs with pybind11-stubgen ───────────────────")

    _check_tool("pybind11_stubgen", "pybind11-stubgen")

    STUBS_DIR.mkdir(exist_ok=True)

    cmd = [
        _python(), "-m", "pybind11_stubgen",
        "doosan_drfl",
        "--output-dir", str(STUBS_DIR),
    ]
    # if verbose:
    #     cmd.append("--verbose")

    _run(cmd, cwd=HERE)

    # Copy generated stubs next to the installed package so IDEs pick them up.
    generated = STUBS_DIR / "doosan_drfl"
    if generated.exists():
        stub_file = generated / "__init__.pyi"
        if not stub_file.exists():
            # pybind11-stubgen may produce drfl.pyi at the root of the output dir
            stub_file = STUBS_DIR / "doosan_drfl.pyi"

        if stub_file.exists():
            # Find the installed .so/.pyd location inside the venv
            result = subprocess.run(
                [_python(), "-c",
                 "import doosan_drfl, pathlib; "
                 "print(pathlib.Path(doosan_drfl.__file__).parent)"],
                capture_output=True, text=True,
            )
            if result.returncode == 0:
                install_dir = Path(result.stdout.strip())
                dest = install_dir / stub_file.name
                shutil.copy2(stub_file, dest)
                print(f"[install.py] Stub copied → {dest}")
            else:
                print(f"[install.py] Could not locate installed doosan_drfl package: {result.stderr.strip()}")
        else:
            print(f"[install.py] WARNING: Could not find generated stub file in {STUBS_DIR}")
    else:
        print(f"[install.py] WARNING: pybind11-stubgen did not produce output in {STUBS_DIR}")


def step_verify() -> None:
    print("\n── Verifying installation ────────────────────────────────────")
    result = subprocess.run(
        [_python(), "-c", "import doosan_drfl; print('doosan_drfl loaded from:', doosan_drfl.__file__)"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print(f"[install.py] ✓ {result.stdout.strip()}")
    else:
        print(f"[install.py] ✗ Import failed:\n{result.stderr}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build and install the DRFL Python extension into the active venv."
    )
    parser.add_argument(
        "--skip-stubs",
        action="store_true",
        help="Skip pybind11-stubgen stub generation.",
    )
    parser.add_argument(
        "--editable", "-e",
        action="store_true",
        help="Install in editable mode (pip install -e). "
             "The .so/.pyd will be built in-place.",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Pass --verbose to pip and pybind11-stubgen.",
    )
    args = parser.parse_args()

    _assert_venv()
    step_check_dependencies()
    step_build_and_install(editable=args.editable, verbose=args.verbose)

    if not args.skip_stubs:
        step_generate_stubs(verbose=args.verbose)

    step_verify()

    print("\n[install.py] ✓ Done.")


if __name__ == "__main__":
    main()
