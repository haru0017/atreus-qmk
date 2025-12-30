import argparse
import shutil
import subprocess
import sys
from pathlib import Path

KEYBOARD = "keyboardio/atreus"
KEYMAP = "via"
QMK_HOME = Path("qmk_firmware").resolve()
KEYMAP_SRC = Path("keyboard/atreus/keymaps/via")
KEYMAP_DEST = QMK_HOME / "keyboards/keyboardio/atreus/keymaps" / KEYMAP

REQUIRED_TOOLS = [
    "qmk",
    "avr-gcc",  # avr-libc is required but not checked explicitly
    "avrdude",
    "dfu-programmer",
    "dfu-util",
    "dos2unix",
]


def prepare_keymap() -> None:
    """Copy external via keymap into qmk_firmware for compilation."""
    if KEYMAP_DEST.exists():
        shutil.rmtree(KEYMAP_DEST)
    shutil.copytree(KEYMAP_SRC, KEYMAP_DEST)


def run(cmd: list[str]) -> None:
    print(f"+ {' '.join(cmd)}")
    subprocess.check_call(cmd, cwd=QMK_HOME)


def which(tool: str) -> str | None:
    """Return full path if tool exists, else None"""
    return shutil.which(tool)


def check_tools() -> None:
    missing = []
    for t in REQUIRED_TOOLS:
        if not which(t):
            missing.append(t)

    if missing:
        print("Missing required tools:")
        for t in missing:
            print(f"  - {t}")
        sys.exit(1)

    print("All required tools found.")


def ensure_qmk_firmware() -> None:
    if not QMK_HOME.exists():
        print("qmk_firmware submodule not found.")
        print("Did you forget: git submodule update --init --recursive ?")
        sys.exit(1)


def compile_firmware() -> None:
    ensure_qmk_firmware()
    run(
        [
            "qmk",
            "compile",
            "-kb",
            KEYBOARD,
            "-km",
            KEYMAP,
        ],
    )


def flash_firmware() -> None:
    ensure_qmk_firmware()
    run(
        [
            "qmk",
            "flash",
            "-kb",
            KEYBOARD,
            "-km",
            KEYMAP,
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyboardio Atreus QMK build/flash helper")
    parser.add_argument(
        "command",
        choices=["compile", "flash"],
        help="Action to perform",
    )
    args = parser.parse_args()

    if args.command == "compile":
        check_tools()
        prepare_keymap()
        compile_firmware()
    elif args.command == "flash":
        check_tools()
        flash_firmware()


if __name__ == "__main__":
    main()
