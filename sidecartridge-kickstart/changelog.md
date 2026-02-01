---
layout: default
title: Changelog
nav_order: 11
nav_exclude: false
parent: SidecarTridge Kickstart
---

# Changelog
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Firmware Changelog

### 3.1.0 (2026-02-01) - Maintenance release
This firmware release includes several maintenance improvements and bug fixes.

#### Changes
- Improved writing performance with writing blocks protocol.
- Better handling of USB disconnections during file transfers.
- Lowered the speed of the access to the flash memory to improve stability to accomodate some flash memory chip series.
- New unomunt procedure when the user ejects the `ROMEMUL` volume to avoid data corruption issues with some operating systems (Windows) that expect the device to wait for some time before actually unmounting the volume.
- Power saving procedures improved to reduce power consumption when detecting the device is connected to the USB-C port.
- Power off the VOL LED when the device ends unmounting and placed in low power mode.

#### New Features
No new features in this release.

#### Fixes
- Fixed an issue where the FAT12 filesystem could become corrupted when uploading images on a fragmented drive.
- Fixed an issue in the sector count calculation where the RP2350 microcontroller could misbehave rounding numbers, leading to corrupted FAT12 filesystems in some cases.



### 3.0.0 (2025-06-01) - v3 release
This firmware release is the first stable release of the SidecarTridge Kickstart v3 board. It includes several new features and improvements over the previous versions.

#### Changes
- The firmware is now based on the RP2350 microcontroller, which provides more features and better performance.
- The firmware now supports 512KB ROMs.
- The upload feature now display the progress in blocks of 64KB, which is more efficient and faster.

#### New Features
- The firmware now supports the RP2350 microcontroller, which provides more features and better performance.
- There is a new red LED indicator that lights up when the board is powered on.
- There is a new green LED indicator that lights up when the firmware is running.
- There is a new orange LED indicator that lights up when the internal USB drive is mounted or transferring data.
- There is a new CONFIG.TXT file that allows the user to configure some advanced firmware options.
- The parameter READ_BUS_TICKS in the CONFIG.TXT file allows the user to configure the number of ticks to wait for the bus to be ready before reading it. This is useful for some Atari ST and Amiga motherboards that require more time to read the bus. Each tick is 12.5ns.
- The parameter USE_OE in the CONFIG.TXT file allows the user to configure if the OE signal is used or not. Not strictly necessary for Atari and Amiga computers.
- Support for Commodore Amiga.

## SWITCHER Changelog

### 3.0.1 (2025-11-01) - SWITCHER Amiga OS compatibility fix
This firmware release addresses a compatibility issue with the SWITCHER program on Amiga OS.

#### Changes
- The SWITCHER program can run correctly on Amiga OS, Amiga TOS and Atari ST TOS without causing system instability.

#### Fixes
- Memory access violation when running SWITCHER on Amiga OS on small stack size systems.

## Hardware Changelog (ROM Emulator)

### 3.0.0 (2025-06-01) - v3 release
This hardware release is the first stable release of the SidecarTridge Kickstart v3 board with the RP2350 microcontroller. It includes several new features and improvements over the previous versions:
- The board is now based on the RP2350 microcontroller, which provides more features and better performance.
- The board now supports 512KB ROMs.
- The board includes three LED indicators: a red LED that lights up when the board is powered on, a green LED that lights up when the firmware is running, and an orange LED that lights up when the internal USB drive is mounted or transferring data.
- Support for the firmware v3.0.0 and later.



[Previous: FAQ](/sidecartridge-kickstart/faq/){: .btn mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
