---
layout: default
title: Introduction
nav_order: 1
nav_exclude: true
parent: ACSI2STM Hard Disk for Atari ST
---

# Introduction
{: .no_toc }

This chapter provides a concise overview of the ACSI2STM Hard Disk device, explaining its purpose, features, and benefits for Atari ST / Mega ST / STe / Mega STe computers.

## Overview

The ACSI2STM is an open-source hard drive emulator designed for Atari ST computers, enabling the use of SD cards as storage devices. Powered by an STM32 microcontroller, it bridges the Atari’s ACSI port with modern SD cards, providing a cost-effective, reliable, and versatile solution for expanding storage on vintage Atari systems.

## Features and Benefits

## Key Features:

- **Broad Compatibility**: Supports Atari models such as 520 STF, 1040 STE, Mega ST, and Mega STE.  
- **Operating Modes**:
  - **GemDrive Mode**: Offers seamless access to SD cards formatted with FAT16, FAT32, or ExFAT. This mode eliminates the need for additional drivers, making it easy to transfer files between your Atari and modern PCs.
  - **ACSI Mode**: Emulates traditional ACSI hard drives and supports multiple partitions. This mode requires Atari-compatible hard disk drivers, offering enhanced compatibility with legacy software.
- **Real-Time Clock (RTC)**: Includes UltraSatan-compatible RTC functionality, enabling accurate timekeeping on the Atari. A 3V lithium battery (CR2032 not included) is required for this feature.
- **Firmware Upgradeable**: The ACSI2STM firmware can be updated directly from the Atari, ensuring compatibility with future enhancements and bug fixes.

## Intended Audience

The ACSI2STM Hard Disk device is a perfect replacement for traditional hard drives in Atari ST, Mega ST, STe, and Mega STe computers. It is ideal for users who just want to plug and play without the hassle of setting up old storage solutions.

## Project Background

The ACSI2STM project was initiated to provide a modern storage solution for Atari ST computers, leveraging the capabilities of SD cards and STM32 microcontrollers. The project is open-source, allowing users to contribute to its development and customize the firmware to suit their needs. We strongly encourage users to explore the project’s [GitHub repository](https://github.com/retro16/acsi2stm) for more information and to contribute to its growth. 

The project is released under the [GNU General Public License v3.0](https://github.com/retro16/acsi2stm/blob/stable/LICENSE), ensuring that the source code and schematics are freely available for anyone to use, modify, and distribute.

The ACSI2STM device manufactured by SidecarTridge is a derivative of the original project with the following modifications:
- The size of the PCB has been reduced some milimiters to avoid cabling issues in the Atari Mega ST model.
- The 32Mhz crystal has been added to the PCB to improve the stability of the device (I don't know the reason why it was not included in the original project).
- The jumpers settings have been left in the PCB to allow the user to change the configuration without the need of soldering.

All the changes made to the original project have been shared with the community with a pull request to the original project that you can find [here](https://github.com/retro16/acsi2stm/pull/77). The pull request has not been accepted yet.


## Key Hardware Components

The ACSI2STM Hard Disk device provided by the SidecarTridge project consists of the following components:

1. **ACSI2STM PCB**: The main board that houses the STM32 microcontroller, SD card slot, and other components. The PCB has all the components soldered and tested, including the DB-19 pins for the Atari ACSI port.

4. **IDC-20 Connector**: An optional connector that expands the ACSI port to support additional devices like Satan Disk. This connector is not soldered to the PCB and must be installed by the user.

5. **Pre-installed Firmware**: The ACSI2STM device comes with the latest stable firmware pre-installed, ensuring that it is ready for use out of the box.

---

[Previous: Index](/acsi2stm-atari-st/){: .btn .mr-4 }
[Main](/acsi2stm-atari-st/){: .btn .mr-4 }
[Next: Before You Buy](/acsi2stm-atari-st/before-buy/){: .btn .mr-4 }
