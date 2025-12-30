# Keyboardio Atreus QMK Firmware Helper

This repository provides a reproducible environment to build and flash the **Keyboardio Atreus** firmware with **QMK** and **VIA**.

## Purpose

- Build Keyboardio Atreus QMK firmware in CI.
- Compile and flash the same firmware locally.

## Getting Started

Clone this repository including the QMK firmware submodule:

```bash
git clone --recurse-submodules https://github.com/haru0017/atreus-qmk.git
cd atreus-qmk
````

Initialize Python environment once:

```bash
uv sync --frozen
```

## Building & Flashing

Compile firmware:

```bash
make compile
```

Flash firmware to your Atreus:

```bash
make flash
```

## Links

* [QMK Atreus keyboard](https://github.com/qmk/qmk_firmware/tree/master/keyboards/keyboardio/atreus)

## License

* This repository: **MIT License**
* `keyboards/keyboardio/atreus/keymaps/via/keymap.c`: **GPLv2 or later** (derivative work of QMK Firmware)
* `qmk_firmware/` submodule: **GPL License** (as provided by the upstream QMK project)
