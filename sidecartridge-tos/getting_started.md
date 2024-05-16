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

## Prerequisites

Before you begin the installation and setup of the SidecarTridge TOS emulator, ensure you have the following items and tools:

## Required Components

- **SidecarTridge TOS Emulator Kit**: This should include the SidecarTridge ROM Emulator Board, the SidecarTridge Atari ST Model Carrier Board, a USB-C cable (Optional), and the RESCUE cable (Optional).
- **3 1/2 inch Floppy Disk**: With the SWITCHER.TOS program for managing TOS versions on the Atari ST. This program can also be downloaded from the SidecarTridge website.
- **A USB-C cable (not included in the kit)**: for connecting the SidecarTridge TOS emulator to a computer for firmware updates and TOS image transfers.
- **RESCUE cable (not included in the kit)**: for connecting an external push button to the SidecarTridge TOS emulator to enter rescue mode.
- **Atari ST Computer**: The emulator is compatible with various models, including the ST, STE, Mega ST, and Mega STE. The following list of motherboards and carrier boards is supported:

Here is a markdown table with the information extracted and formatted as requested:

Sure, here is the revised table with the model column removed and the required information:

#### Supported Atari ST Motherboards and Carrier Boards

{: .info}
Carrier boards for non supported motherboards are in active development. Please check the SidecarTridge website for updates.
{: .warning}

##### Atari ST series

| Motherboard Model Number | Number of ROMs | Carrier Board   |
|--------------------------|----------------|-----------------|
| C070115 Rev. 2           |                | Not supported   |
| C070243 Rev. C           |                | Not supported   |
| C070243 Rev. E           |                | Not supported   |
| C070243 Rev. F           |                | Not supported   |
| C070243 Rev. H           |                | Not supported   |
| C070243 Rev. I           |                | Not supported   |
| C070523-001 Rev. C       |                | Not supported   |
| C070523-001 Rev. D       |                | Not supported   |
| C070789-001 Rev. A       |       2        | Supported       |
| C070789-001 Rev. B       |       2        | Supported       |
| C070789-001 Rev. C       |       2        | Supported       |
| C070789-001 Rev. D       |       2        | Supported       |
| C070789-001 Rev. F       |       2        | Supported       |
| C070859                  |       2        | Supported       |
| C103088 Rev. 3.1         |                | Not supported   |
| C103253 Rev. 3.1         |                | Not supported   |
| C103088 Rev. 5.3         |                | Not supported   |
| C103253 Rev. 5.3         |                | Not supported   |
| C103175-001 Rev. 1       |       2        | Supported       |
| C103175-001 Rev. 1.1     |       2        | Supported       |
| C103225 Rev. 1           |                | Not supported   |
| C103414-001 Rev. 1       |       2        | Supported       |
| C103414-001 Rev. 1.1     |       2        | Supported       |

##### Atari Mega ST series

| Motherboard Model Number | Number of ROMs | Carrier Board   |
|--------------------------|----------------|-----------------|
| C100167-001 Rev. 4.0     |                | Not supported   |
| C100167-001 Rev. B       |                | Not supported   |
| C100167-001 Rev. 5.0     |                | Not supported   |


##### Atari STE series

| Motherboard Model Number | Number of ROMs | Carrier Board   |
|--------------------------|----------------|-----------------|
| CA4003290                |       2        | Supported       |


##### Atari Mega STE series

| Motherboard Model Number | Number of ROMs | Carrier Board   |
|--------------------------|----------------|-----------------|
| CA400677 Rev. F          |       2        | Supported       |


{: .warning}
If you can't find your motherboard model number in the list, or have any doubts about compatibility, please contact us for further assistance.



## Tools and Equipment
- **Phillips Head Screwdriver**: For opening the Atari ST case.
- **Anti-Static Wrist Strap**: To prevent static discharge that could damage electronic components.
- **Small Container**: To hold screws and small parts during the disassembly of the Atari ST.
- **IC Extractor Tool**: For safely removing the ROM chips from the Atari ST motherboard. I strongly recommend using a proper IC extractor tool to avoid damaging the ROM chips or the motherboard. If you don't have one, you can use a flat-head screwdriver, but be very careful not to damage the chips or the motherboard.
- **Insulating Tape**: To avoid short circuits between the SidecarTridge TOS emulator and the Atari ST motherboard.
- **Computer with USB Port**: A Windows, macOS, or Linux computer for transferring ROM files and updating firmware.

## Software and Files
- **TOS Image Files**: Ensure you have the necessary TOS image files ready for transfer. These can be downloaded from reputable sources like [Avtandil website](https://avtandil.narod.ru/tose.html), [EmuTOS website](https://emutos.sourceforge.io/), or other trusted sources.
- **SWITCHER.TOS Program**: A program for selecting and managing TOS versions on the Atari ST. This program is required to switch between TOS versions and can be downloaded from the SidecarTridge website.

By having these prerequisites in place, you will be well-prepared to proceed with the installation and setup of your SidecarTridge TOS emulator.

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