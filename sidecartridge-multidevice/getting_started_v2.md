---
layout: default
title: Getting Started Firmware V2.0 (ALPHA)
nav_order: 2
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /getting_started_v2/
  - /getting_started_v2
---

# Getting Started
{: .no_toc }

This section provides guidance on the initial steps to start working with the SidecarTridge Multi-device board with the latest firmware v2. If you are a developer or maker it includes prerequisites, board assembly instructions, setup and configuration. Developers and Makers can also ensure a smooth start to their journey with the Multi-device board by following the procedures outlined in this and coming sections.

{: .warning }
This is an **ALPHA** version of the firmware, and it is not recommended for production use. It is intended for developers and makers who want to experiment with the Multi-device board and contribute to its development with code or just submitting bugs. If you are a novice user, please refer to the [previous version of the firmware](https://docs.sidecartridge.com/sidecartridge-multidevice/getting_started/) for a more stable experience.

{: .important }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Prerequisites for All Users

### Skills
To begin with the Multi-device board, **all users are required to have a minimum experience with computers**. Power on, power off, and basic knowledge of how to use a computer is enough to get started. However, it’s desirable for users to be familiar with the Atari ST computer series, its hardware, and software.

### Hardware
Users will need the following hardware:

- An Atari ST computer series: ST, STE, or MegaST or MegaSTE. It's worth noting that the Multi-device board can emulate a physical floppy drive, so an Atari ST without a (or a broken) floppy drive can still be used with the Multi-device board. The Multi-device board is also compatible with TOS versions ranging from 1.00 to 2.06 and EmuTOS, almost every single ST and STE series compute sold.

{:refdef: style="text-align: center;"}
![Atari 520ST](https://sidecartridge.com/assets/images/quickstart/atari520st.jpeg)
{: refdef}


- A Multi-device board

{:refdef: style="text-align: center;"}
![SidecarT without Raspberry Pi Pico](/sidecartridge-multidevice/assets/images/BOARD-3.1-KIT-TOP.png)
{: refdef}


- A [Raspberry Pi Pico WH (Reference SC0919)](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#raspberry-pi-pico-w-and-pico-wh), which already comes with the necessary 40-pin connectors to attach to the SidecarT's motherboard, or a [Raspberry Pi Pico W (Reference SC0918)](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#raspberry-pi-pico-w-and-pico-wh).

{:refdef: style="text-align: center;"}
![Raspberry Pi Pico WH](https://sidecartridge.com/assets/images/quickstart/raspberry-pi-pico-rp2040-wh.png)
{: refdef}

{: .important }
Since revision 3.1 of the board, the Raspberry Pi Pico W can be directly soldered to the board. If you want to use a Raspberry Pi Pico WH, you will have to solder two 20-pin female headers connectors to the board. You can find them in [our store here](https://store.sidecartridge.com/products/pair-of-2-54mm-square-plugin-2p-female-headers), or in any electronic store.


- A USB A to micro USB *data* cable to install and update the Multi-device firmware on the Raspberry Pi Pico W. It's important to note the emphasis on a "data" cable - a simple charging cable won't suffice.

{:refdef: style="text-align: center;"}
![USB A to micro USB](https://sidecartridge.com/assets/images/quickstart/microusb.jpeg)
{: refdef}


- Since the firmware version 2.0, a microSD card [formatted as FAT16 or exFAT](https://docs.sidecartridge.com/sidecartridge-multidevice/how_to/#format-the-microsd-card) is required.

## Initial Setup and Configuration

### Firmware Installation

{: .important }
Since this is a new version of the firmware and still in **ALPHA** stage, you will need to install the bootloader on your Raspberry Pi Pico W. This is a one-time process that allows the Multi-device board to run the new firmware. Go for the option that best suits you. Both options will install the bootloader on your Raspberry Pi Pico W.

### Option 1: Using the drag-and-drop method
1. Connect the Raspberry Pi Pico W micro USB connector to your computer while holding the **BOOTSEL** button.
2. Your computer should recognize the device as the mass storage device `RPI-RP2`. Now you can release the **BOOTSEL** button.
3. Drag and drop the [Full Release](https://github.com/sidecartridge/rp2-booster-bootloader/releases/download/nightly/rp-booster-v1.0.0alpha-full.uf2) file to the `RPI-RP2` drive.
4. Wait for the file to be copied. When the copy is complete you can disconnect the Raspberry Pi Pico W from your computer.

### Option 2: Using picotool

With this method you must [first install the picotool](https://github.com/raspberrypi/picotool) helper tool, which is a command-line utility for managing Raspberry Pi devices based on the RP2040 microcontroller.

1. Connect the Raspberry Pi Pico W micro USB connector to your computer while holding the **BOOTSEL** button.
2. Your computer should recognize the device as the mass storage device `RPI-RP2`. Now you can release the **BOOTSEL** button.
3. Flash the bootloader on your board:
```bash
picotool load -xv dist/rp-booster-$VERSION.uf2
```

### Initial Factory Configuration

1. Format a microSD card with either **exFAT** or **FAT32** file system and insert it into the SidecarTridge Multidevice board.

2. Plug the SidecarTridge Multidevice into the **cartridge port** of your Atari ST series computer.

3. Power on the Atari ST computer.

4. The Booster app will automatically start in **Factory (Fabric) mode**, showing the following message on screen:

   ![Booster Factory Mode step 1](/sidecartridge-multidevice/assets/images/BOOSTER-FABRIC-1.png)

   This screen confirms that the Booster app is running in Factory mode and is ready to be configured.  
   Scan the **QR code** with your smartphone to connect to the WiFi network created by the Booster app, or manually connect via your WiFi settings.  
   The default network details are:
   - **SSID**: `SIDECART`  
   - **Password**: `sidecart`

5. Once connected to the WiFi, the Booster app will detect the connection and show the following screen:

   ![Booster Factory Mode step 2](/sidecartridge-multidevice/assets/images/BOOSTER-FABRIC-2.png)

   This screen invites you to open a web browser and navigate to either:
   - `http://sidecart.local`  
   - or `http://192.168.4.1` (if `.local` domains aren’t supported)

6. In your web browser, enter the URL shown above to access the web interface.  
   You’ll be prompted to configure your home or office WiFi network.  
   Select your WiFi SSID from the list (you can click **Refresh** if it doesn’t appear), then click it to continue.  
   In this example, the network is `CHISMEROUTER`.

   ![Booster Factory Mode step 3](/sidecartridge-multidevice/assets/images/BOOSTER-FABRIC-3.png)

7. Enter your WiFi password and click the **Connect** button.

   ![Booster Factory Mode step 4](/sidecartridge-multidevice/assets/images/BOOSTER-FABRIC-4.png)

8. The Booster app will save the WiFi credentials to flash memory and reboot.  
   It will then connect to your WiFi network and show this message:

   ![Booster Factory Mode step 5](/sidecartridge-multidevice/assets/images/BOOSTER-FABRIC-5.png)

   Meanwhile, the device will also display a reboot message on the Atari screen:

   ![Booster Factory Mode step 6](/sidecartridge-multidevice/assets/images/BOOSTER-FABRIC-6.png)

9. After rebooting, the Booster app will attempt to connect to your configured WiFi network:

   ![Booster Manager Mode step 1](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-1.png)

10. Once connected successfully, the screen will show:

    ![Booster Maneger Mode step 2](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-2.png)

    Your WiFi setup is now complete. From now on, the Booster app will boot directly into **Manager mode**.  
    See the next section for details on using Manager mode.

## Prerequisites for Developers and Makers

### Skills
To begin with the Multi-device board, **developers are required to have a minimum experience with C**. However, it’s desirable for developers to be proficient in C, 68000 Assembler, Microcontroller development, and have a deep understanding of Atari ST peculiarities. To contribute effectively to the Multi-device project, having a foundation in certain skills will be beneficial. Here’s a breakdown:

- **C Programming**: Essential for software development and firmware writing. Ensure you have a grasp on data structures, memory management, and algorithm development within C.

- **68000 Assembler**: Crucial for understanding and working with low-level part of the firmware for Atari ST.

- **Microcontroller Development**: Familiarity with microcontrollers, especially with Raspberry Pi Pico's microcontroller RP2040, is vital. You should understand how to write, test, and debug firmware, manage I/O operations, and deal with real-time constraints.

- **Atari ST Knowledge**: A robust understanding of Atari ST hardware and software, its system call and memory management will significantly boost your contribution efforts.

- **Version Control/Git**: Ability to effectively use git, manage branches, resolve merge conflicts, and understand the workflow to keep the codebase stable and collaborative.

- **Testing and Debugging**: Practical know-how on debugging, writing test cases, and validating hardware/software integration ensures a robust build.

- **Visual Studio Code Expertise**: Familiarity with using Visual Studio Code, configuring workspaces, managing extensions, and utilizing its debugging capabilities will facilitate a smoother development experience.

- **GCC**: Understanding how to utilize GCC for compiling C and C++ code, managing dependencies, and debugging is vital for software development in this project.

- **VASM**: Knowledge of using the VASM assembler, its syntax, and how to compile assembly code, particularly for the 68000, will enable efficient low-level development.

- **Makefile**: Know-how on writing and managing Makefiles to automate build processes, manage dependencies, and optimize the development workflow.

- **Integration with GDB**: Skills in using GDB for debugging software, setting breakpoints, inspecting variables, and analyzing program flow, especially in conjunction with Visual Studio Code, are essential for troubleshooting and ensuring software stability.

And if you want to contribute to the harware, skills in reading schematics, understanding electronic components, and practical skills like soldering will facilitate working with the hardware aspects of Multi-device.
    
{: .note }
Even if you’re not an expert in all these areas, your contribution is still valuable. Engage, learn, and grow with the Multi-device community!

### Hardware
Additionally, developers need the following hardware:
- An Atari ST computer series: ST, STE, or Mega (See above)

- A Multi-device board (See above)

- A [Raspberry Pi Pico W or WH board](https://www.raspberrypi.com/products/raspberry-pi-pico/?variant=raspberry-pi-pico-wh) to connect it to the Multi-device board. The `W` stands for **Wireless** and the `H` stands for **Header**. The `H` version comes with the header pins already soldered to the board and a JST debugger connector needed to connect the Raspberry Pi Debug Board. Since version 3.1 of the board, it's also possible to get the debug signals directly on the JST connector of the board.

{:refdef: style="text-align: center;"}
![Raspberry Pi Pico WH](https://sidecartridge.com/assets/images/quickstart/raspberry-pi-pico-rp2040-wh.png)
{: refdef}


- A [Raspberry Pi Debug board](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) or an equivalent debug board to connect it to the Multi-device board

{:refdef: style="text-align: center;"}
![Raspberry Pi Pico WH](/sidecartridge-multidevice/assets/images/debug-probe.jpg)
{: refdef}

- A [Mini JST SH 1.0mm pitch double 3xpin female connectors](https://store.sidecartridge.com/products/mini-jst-sh-1-0mm-pitch-double-3xpin-female-connectors-10cm) to connect the UART pins from the Raspberry Pi Pico W to the Raspberry Pi Debug board

{:refdef: style="text-align: center;"}
![Mini JST SH 1.0mm pitch double 3x](https://store.sidecartridge.com/cdn/shop/files/dual-jst-sh-1mm-3-female-pins-10cm.png?v=1718732895&width=1426)
{: refdef}

- A Windows PC, Linux or a Mac with a USB port to connect to the Raspberry Pi Debug board and the Raspberry Pi Pico W board to program it

{: .note }
These prerequisites are considered as a minimum baseline. Being well-versed with the aforementioned technologies and having the required hardware will ensure a seamless initial experience with the Multi-device board.

### Board Assembly
Anyone with the requisite skills can opt to build their own Multi-device board. The schematics needed to assemble the board can be found in the [Github repository](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/tree/main/schematics). It provides detailed blueprints to guide users through the assembly process.

However, it is worth noting that acquiring the board through our [online shop](https://store.sidecartridge.com) is likely to be both cheaper and more convenient, given the complexities involved in assembling the board.

{: .warning }
Assembling the board independently can be a rewarding and enriching learning experience for those who are interested in a hands-on approach to understanding the intricate workings of the Multi-device board. Obviously, it is not recommended for those who are new to hardware development.
