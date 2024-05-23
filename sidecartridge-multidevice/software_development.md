---
layout: default
title: Software Development
nav_order: 6
nav_exclude: false
parent: SidecarTridge Multi-device
---

# Software Development
{: .no_toc }

This section is dedicated to providing developers with a comprehensive guide to software development for the SidecarT board. It covers setting up the development environment, understanding the software architecture, utilizing the API, and exploring example projects. Grasping these elements is crucial for developing robust, efficient, and innovative applications on the SidecarT platform.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Set up the development environment

### Setup a Raspberry Pi Pico development environment from scratch

If you are not familiar with the development on the Raspberry Pi Pico or RP2040, we recommend you to follow the [Getting Started with Raspberry Pi Pico](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf) guide. This guide will help you to setup the Raspberry Pi Pico development environment from scratch.

We also think it's very important to setup the picoprobe debugging hardware. The picoprobe is a hardware debugger that will allow you to debug the code running on the Raspberry Pi Pico. You can find more information in this two excellent tutorials from Shawn Hymel:
- [Raspberry Pi Pico and RP2040 - C/C++ Part 1: Blink and VS Code](https://www.digikey.es/en/maker/projects/raspberry-pi-pico-and-rp2040-cc-part-1-blink-and-vs-code/7102fb8bca95452e9df6150f39ae8422)
- [Raspberry Pi Pico and RP2040 - C/C++ Part 2 Debugging with VS Code](https://www.digikey.es/en/maker/projects/raspberry-pi-pico-and-rp2040-cc-part-2-debugging-with-vs-code/470abc7efb07432b82c95f6f67f184c0)

To support the debugging the SidecarT has four pins that are connected to the picoprobe hardware debugger. These pins are:
- UART TX: This pin is used to send the debug information from the RP2040 to the picoprobe hardware debugger.
- UART RX: This pin is used to send the debug information from the picoprobe hardware debugger to the RP2040.
- GND: Two ground pins. One MUST connect to the GND of the Raspberry Pi Pico W (the middle connector between DEBUG and SWCLK and SWDIO) and the other MUST connect to the GND of the picoprobe hardware debugger. Don't let this pins floating, otherwise the debugging will not work.

Also a good tutorial about setting up a debugging environment with the picoprobe can be found in the [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) tutorial.

Trying to develop software for this microcontroller without the right environment is frustrating and a waste of time. So please, take your time to setup the development environment properly. It will save you a lot of time in the future.

#### Configure environment variables

The following environment variables are required to be set:

- `PICO_SDK_PATH`: The path to the Raspberry Pi Pico SDK.
- `PICO_EXTRAS_PATH`: The path to the Raspberry Pi Pico Extras SDK.
- `FATFS_SDK_PATH`: The path to the FatFS SDK.

This repository contains subrepos pointing to these SDKs in root folder.

All the compile, debug and build scripts use these environment variables to locate the SDKs. So it's very important to set them properly. An option would be to set them in your `.bashrc` file if you are using Bash, or in your `.zshrc` file if you are using ZSH. 

#### Configure Visual Studio Code

To configure Visual Studio Code to work with the Raspberry Pi Pico, please follow the [Raspberry Pi Pico and RP2040 - C/C++ Part 2 Debugging with VS Code](https://www.digikey.es/en/maker/projects/raspberry-pi-pico-and-rp2040-cc-part-2-debugging-with-vs-code/470abc7efb07432b82c95f6f67f184c0) tutorial.

The `.vscode` folder contains the configuration files for Visual Studio Code. **Please modify them as follows**:

- `launch.json`: Modify the `gdbPath` property to point to the `arm-none-eabi-gdb` file in your computer.
- `launch.json`: Modify the `searchDir` property to point to the `/tcl` folder inside the `openocd` project in your computer.
- `settings.json`: Modify the `cortex-debug.gdbPath` property to point to the `arm-none-eabi-gdb` file in your computer.


#### Install Visual Studio Code extensions

- [C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack)
- [CMake](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)
- [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
- [Cortex-Debug](https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug)

## Building the firmware
### From the command line

To build a production ready firmware for the SidecarT board, follow these steps:

1. Clone this repository:

```
$ git clone https://github.com/sidecartridge/atarist-sidecart-raspberry-pico.git
```

2. Navigate to the cloned repository:

```
cd atarist-sidecart-raspberry-pico
```

3. Trigger the `build.sh` script to build the firmware:

```
./build.sh
```

4. The `dist` folder now houses the file: `sidecart-pico_w.uf2`, which needs to be copied to the RP2040 in the Raspberry Pi Pico W. This can be done by connecting the Raspberry Pi Pico W to your computer via USB and copying the file to the `RPI-RP2` drive.


### From a Github Action

In the folder `/.github` of the root directory of the project you can find the file `build.yml`. This file contains the configuration of the Github Action that will build the firmware.

The `release.yml` will create a release in Github with the firmware binary file.

### From Visual Studio Code

It's also possible to build the firmware from Visual Studio Code, but probably it's a better idea to build it in Debug mode and launch it from Visual Studio Code. Please read the section about setting up the debugging environment above.

## Development

The development on the RP2040 of the Raspberry Pi Pico is straightforward if you have setup the environment previously. The RP2040 is a Cortex-M0+ microcontroller and the development is done in C. The RP2040 is a very powerful microcontroller and it's possible to develop very complex applications for it. Apart from the C code have also to use the PIO (Programmable IO) to develop the I/O section with the Atari ST cartridge. The PIO is a very powerful peripheral that allows you to develop very complex applications in a very easy way.

Here goes a list of things to take into account when developing:

1. The source code is inside the `romemul` folder. This name could change in the future.
2. `memmap_romemul.ld` is the linker script used to link the code. It contains the different memory sections that the Sidecart needs. Please don't change these values if you don't know what you are doing. The RAM for the RP2040 has been reduced to 128Kbytes to keep the Atari ST ROMs in the RAM for performance reasons. Also, don't modify the space needed for configuration data. This data is used to store the configuration of the SidecarT board and it's used by the `CONFIGURATOR` tool.
3. CMakelists.txt is the file used by the CMake tool to build the project.

A special note about the `firmware.c` file. This file is an array generated with the python script `download_firmware.py`. This script downloads the latest version of the Atari ST firmware contained in the repository [atarist-sidecart-firmware](https://github.com/sidecartridge/atarist-sidecart-firmware). The same can apply to `firmware_floppyemul` file. This file is an array generated with the python script `download_floppyemul.py`. This script downloads the latest version of the Atari ST Floppy emulator driver contained in the repository [atarist-sidecart-floppy-emulator](https://github.com/sidecartridge/atarist-sidecart-floppy-emulator). Hence, the code embeds the Atari ST firmware in the SidecarT firmware. This is done to simplify the development and to avoid the need to flash the Atari ST firmware in the RP2040. **As a rule of thumb, if you modify any of those firmwares, you have to regenerate the `firmware.c` and `firmware_floppyemul.c` file. To do that, just run the `download_firmware.py` and `download_floppyemul.py` scripts.**

## Releases

For releases, head over to the [Releases page](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/releases). The latest release is always recommended.

For a quick tutorial about how to flash the firmware in the Raspberry Pi Pico, please read the [Quickstart](https://sidecartridge.com/quickstart).

## Changelog

The full changelog is available in the [CHANGELOG.md](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/main/CHANGELOG.md) file. 

## Resources 

- [Sidecart ROM Emulator website](https://)
- [Sidecart Atari ST Firmware](https://github.com/sidecartridge/atarist-sidecart-firmware).
- [Sidecart Atari ST Test ROM](https://github.com/sidecartridge/atarist-sidecart-test-rom).

## Contribute

Thank you for your interest in contributing to this repository! We welcome and appreciate contributions from the community. Here are a few ways you can contribute:

- Report bugs: If you find a bug in the code, please let us know by opening an issue. Be sure to include details about the error, how to reproduce it, and any possible workarounds.

- Suggest new features: Have an idea for a new feature or improvement? We'd love to hear about it. Open an issue to start a discussion.

- Contribute code: If you're a developer and want to contribute code to this project, here are a few steps to get started:
    * Fork the repository and clone it to your local machine.
    * Create a new branch for your changes.
    * Make your changes, including tests to cover your changes.
    * Run the tests to ensure everything is working.
    * Commit your changes and push them to your fork.
    * Open a pull request to this repository.


- Write documentation: If you're not a developer, you can still contribute by writing documentation, such as improved usage examples or tutorials.

- Share feedback: Even if you don't have any specific changes in mind, we welcome your feedback and thoughts on the project. You can share your feedback by opening an issue or by joining the repository's community.

We appreciate any and all contributions, and we'll do our best to review and respond to your submissions in a timely manner. Please note that all contributors are expected to follow our code of conduct (one day we will have one!). Thank you for your support!

## Licenses

The source code of the project is licensed under the GNU General Public License v3.0. The full license is accessible in the [LICENSE](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/main/LICENSE) file. 


