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

## Firmware Installation
- Connecting the Device to a Computer
- Upgrading the Firmware

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