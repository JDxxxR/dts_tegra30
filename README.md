# DTS pinmux converter script for tegra30

> **Disclaimer:** Use on own risk. No warranty. This is a just-for-fun script. Check `TODO` in the sources if anything applies for your use case. Possibly you may also search for something like this converter [https://github.com/NVIDIA/tegra-pinmux-scripts](https://github.com/NVIDIA/tegra-pinmux-scripts) from nvidia. 

## About

This script should help by converting the tegra30 pinmux configuration from board-files (`board-*-t30*-pinmux.c`) to DTS.

Only a few pinmux macros are supported:

- `DEFAULT_PINMUX`
- `I2C_PINMUX`
- `VI_PINMUX`
- `SET_DRIVE`

## Preparation

1. Find the board files for your T30 board
2. Create a directory with the codename of your board in `boards/` 
3. Copy all the used blocks, grouped by the macro (see supported above) into a file with the respective name 
    - Make sure to only copy lines that are actually touched in the code (e.g. used by a specific model)
    - Remove all comments (e.g. `/* ... */`, `// ...`)
    - Remove all trailing whitespace from the lines
    - Make sure at the end of each file there is only one newline (`\n`), its needed
4. Adjust the file path in the scripts (see below) to the file paths you just created

If unsure, please check already included boards.

## Running scripts

```bash
python3 convert_default.py
python3 convert_drive.py
python3 convert_i2c.py
python3 convert_vi.py
```

## Trial and error

Once done, the generated pinmux configuration could be tested on the device. **Please do not expect it to work out of the box**. There might be some problems including, but not limited to:

- `invalid group "xxxx" for function "xxxx"`
- `Config param xxxx (nvidia,open-drain) not supported on group xxxx`
- `Config param xxxx (nvidia,low-power-mode) not supported on group xxxx`
- `Config param xxxx (nvidia,high-speed-mode) not supported on group xxxx`
- `not freeing pin xxxx (xxxx xxxx) as part of deactivating group xxxx - it is already used for some other setting`

Some those things are related to duplicated usage of pinmux macros on specific pingroups in the board files.
