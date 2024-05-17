---
layout: default
title: Getting Started
nav_order: 2
nav_exclude: true

---

# Getting Started
{: .no_toc }

This section provides guidance on the initial steps to start working with the SidecarTridge TOS emulator. It includes prerequisites, hardware installation instructions, software setup, and configuration. By following the procedures outlined in this and the upcoming sections, users can ensure a smooth start to their journey with the SidecarTridge TOS emulator.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Before You Buy

The SidecarTridge TOS emulator is designed to work with specific Atari ST models and motherboards. There are different versions of the device to accommodate various motherboard configurations. **Please follow these steps before purchasing the emulator**:

### Check Your Atari ST Motherboard Model

To learn more about your Atari ST motherboard model, open the case and look for the model number printed on the board, usually located in the middle bottom of the motherboard. Refer to the [Compatibility](/sidecartridge-tos/compatibility) section for a list of supported motherboards. If your motherboard model is not listed, please contact us for further assistance. If your motherboard model number is listed, proceed to the next step.

### Determine the Number of ROMs

At this moment, the SidecarTridge TOS emulator supports Atari ST motherboards with two ROM chips. If your motherboard has a different number of ROMs, you'll need to wait for the next version of the SidecarTridge TOS emulator with support for six ROMs.

### ROMs Plugged or Soldered

If your ROMs are plugged, congratulations, you can proceed with the purchase. If they are soldered, you will need to desolder them and plug them into sockets. 

{: .warning}
If you are not comfortable with desoldering and soldering, please seek professional help to avoid damaging your Atari ST motherboard. We strongly recommend using an experienced technician to perform this task.

### Purchase the Right SidecarTridge TOS Emulator Kit

Once you have verified the compatibility of your Atari ST motherboard, you can proceed to purchase the appropriate SidecarTridge TOS emulator kit. Ensure you select the correct kit based on your motherboard model number and the number of ROMs.

| SidecarTridge TOS Emulator Kit | Supported Motherboards           | Number of ROMs |
|--------------------------------|----------------------------------|----------------|
| [STF and STFM Kit]()           | 070789-001, C103175-001, C103414-001 | 2              |
| [STE Kit]()                    | CA4003290                        | 2              |
| [Mega STE Kit]()               | CA400677                         | 2              |

## Prerequisites

Before you begin the installation and setup of the SidecarTridge TOS emulator, ensure you have the following items and tools:

### Required Components

- **SidecarTridge TOS Emulator Kit**: This should include:
  1. The SidecarTridge ROM Emulator Board
  2. The SidecarTridge Atari ST Carrier Board. **The ROM Emulator Board is soldered onto this carrier board**.
  3. (Optional) 3 1/2 floppy disk with the SWITCHER.TOS application. It is the program for managing TOS versions on the Atari ST. It can also be downloaded from the SidecarTridge website.
  4. (Optional) USB-C cable: for connecting the SidecarTridge TOS emulator to a computer for firmware updates and TOS image transfers.
  5. (Optional) RESCUE cable: for connecting an external push button to the SidecarTridge TOS emulator to enter rescue mode.

- **Atari ST Computer**: The emulator is compatible with various models, please read the previous section to ensure compatibility with your Atari ST model.

### Tools and Equipment
- **Phillips Head Screwdriver**: For opening the Atari ST case.
- **Anti-Static Wrist Strap**: To prevent static discharge that could damage electronic components.
- **Small Container**: To hold screws and small parts during the disassembly of the Atari ST.
- **IC Extractor Tool**: For safely removing the ROM chips from the Atari ST motherboard. I strongly recommend using a proper IC extractor tool to avoid damaging the ROM chips or the motherboard. If you don't have one, you can use a flat-head screwdriver, but be very careful not to damage the chips or the motherboard.
- **Insulating Tape**: To avoid short circuits between the SidecarTridge TOS emulator and the Atari ST motherboard.
- **Computer with USB Port**: A Windows, macOS, or Linux computer for transferring ROM files and updating firmware.

### Software and Files
- **TOS Image Files**: Ensure you have the necessary TOS image files ready for transfer. These can be downloaded from reputable sources like [Avtandil website](https://avtandil.narod.ru/tose.html), [EmuTOS website](https://emutos.sourceforge.io/), or other trusted sources.
- **SWITCHER.TOS Program**: A program for selecting and managing TOS versions on the Atari ST. This program is required to switch between TOS versions and can be downloaded from the SidecarTridge website.

{: .note }
The SidecarTridge TOS emulator comes with a default EmuTOS image pre-installed and ready to boot. Since the original TOS image files are copyrighted, it's up to you to find the TOS images for your Atari ST model. At this moment every single TOS version found and tested on the internet is working with the SidecarTridge TOS emulator. Please read the [Compatibility](/sidecartridge-tos/compatibility) section for a full list of tested TOS versions.

**By having these prerequisites in place, you will be well-prepared to proceed with the installation and setup of your SidecarTridge TOS emulator.**

## Unboxing and Inspecting the Components

### SidecarTridge TOS Emulator Kit

When you receive your SidecarTridge TOS emulator kit, carefully unbox and inspect the components to ensure everything is included and in good condition. All kits should contain the following items:

1. **SidecarTridge ROM Emulator Board soldered onto the Carrier Board**: This is the main component that will replace the ROM chips on your Atari ST motherboard.
2. **RESCUE cable and push button**: This cable allows you to connect an external push button to the SidecarTridge TOS emulator for entering rescue mode. 
3. **SidecarTridge QR Code card**: This card contains a QR code that links to the SidecarTridge website for firmware updates and documentation.

### Additional Components

If you have purchased additional components like the USB-C cable or the SWITCHER.TOS floppy disk, ensure they are also included in the package.

## Firmware Installation

The SidecarTridge TOS emulator comes with a pre-installed firmware version and a default EmuTOS image. However, it is recommended to check for the latest firmware version and update if necessary. The firmware update process is straightforward and can be done using a computer with a USB port.

### Connecting the Device to a Computer

Connect the SidecarTridge TOS emulator to your computer using the USB-C cable. The emulator will appear as a USB mass storage device on your computer with the volume name `SidecarTrdg`.

{: .note }
If the `SidecarTrdg` volume does not appear on your computer, ensure the USB cable is properly connected and press the `RESET` button on the SidecarTridge TOS ROM Board for a few seconds. This will ensure the device enters the mass storage mode.

Now, open the `SidecarTrdg` volume on your computer to access the firmware files and TOS image files. The following files should be present:

- `INDEX.HTM`: Opening this file in a web browser will open the SidecarTridge TOS documentation website.
- `INFO.TXT`: This file contains information about the firmware version and the installed TOS images. 
- `DEFAULT.TXT`: This file contains the name of the default active TOS image file.
- `RESCUE.TXT`: This file contains the name of the rescue TOS image file.

There is also some system files and directories starting with a dot (.) that are used by the SidecarTridge TOS emulator, and a EmuTOS image file for your computer. For STF, STFM and Mega ST models the file is 192KBytes, for STE and Mega STE models the file is 256KBytes.

{: .note }
It could be an offset of 4KBytes between the real size of the image and the size of the file displayed. This is because the SidecarTridge TOS emulator uses a FAT16 file system to store the TOS images with a 4KBytes cluster size.

![SidecarTridge Volume](/sidecartridge-tos/assets/images/sidecartridge-volume.png)

### Obtaining the Installed Firmware Version

Now open the `INFO.TXT` file to check the installed firmware version. The file should contain information similar to the following:

```
SidecarTridge ROM chip emulator v1.0.0 - (C)2024 GOODDATA LABS SL

Total ROMs:	1
Default ROM index:	0	address: 0x10040000	block size: 48
Rescue ROM index:	0	address: 0x10040000	block size: 48

ROM images:
EmuTOS 1.3.0 192KB UK.img: 	start address: 0x10040000, blocks: 48 metadata: 0x30030

FLASH fragmentation:
GAP: 0, start address: 10070000, blocks: 3982

Summary:
Total:			16208896 bytes
Free:			16310272 bytes
Fragmented:		0 bytes
Fragmented space:	0.00%
Max free space:		100.63%

Open the INDEX.HTM file to access instructions online
Edit the DEFAULT.TXT and RESCUE.TXT files to modify the default and rescue TOS images
```

The firmware version is displayed at the top of the file in the format `SidecarTridge ROM chip emulator v1.0.0`. If there is a newer firmware version available, you can proceed with the firmware update process in the next section. If the firmware version is up-to-date, you can skip the firmware update and proceed with the [Preparing the ROM Images](#preparing-the-rom-images) section.

### Upgrading the Firmware

If there is a newer firmware version available, you can proceed with the firmware update process. Download the latest firmware version from the main page of the [SidecarTridge TOS documentation website](/sidecartridge-tos/index.md) and store it in a temporary location on your computer.

To update the firmware, follow these steps:
1. Hold the `RESET` button on the SidecarTridge TOS ROM Board.
2. While holding the `RESET` button, hold the `BOOT` button.
3. Release the `RESET` button.
4. Release the `BOOT` button.

The SidecarTridge TOS emulator will enter the firmware update mode and appear as a USB mass storage device on your computer with the name `RPI-RP2`. Copy the firmware file to the root directory of the mass storage device and wait for the firmware update process to complete. If after the update the SidecarTridge TOS emulator does not reboot, press the `RESET` button for a few seconds to restart the device.

The firmware update process is now complete, and you can proceed with the [Preparing the ROM Images](#preparing-the-rom-images) section.

{: .note }
The firmware update process is straightforward and will not affect the TOS images stored on the SidecarTridge TOS emulator. However, it is recommended to back up the TOS images before updating the firmware to avoid any data loss.

## Preparing the ROM Images
- Connecting the Device to a Computer
- The Mini-FAT16 File System
- Copying TOS Image Files
- Obtaining Information about the TOS Images and Flash Status
- Modifying the Default and Rescue TOS Images
- Advanced Commands

## Unplugging the Atari ST ROMs
- Opening the Atari ST Case
- Removing the Atari ST ROMs

## Plugging the SidecarTridge TOS Emulator
- Connecting the SidecarTridge Atari ST Model Carrier Board
- Securing the Boards

## Closing the Atari ST Case

## Initial Setup
- Powering On the Atari ST
- The SWITCHER.TOS Program
- Verifying the Installation
- Selecting a New Active Default TOS Version
- Switching Between TOS Versions

## Rescue Mode
- Booting with the Rescue TOS
- Restoring the Default TOS