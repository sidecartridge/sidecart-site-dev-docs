---
layout: default
title: Changelog
nav_order: 10
nav_exclude: false
parent: SidecarTridge TOS
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

### 2.1.0 (2024-11-21) - Commands release

This firmware release adds some maintenance commands and modifies the creation of the INFO.TXT file to avoid issues when powering on the device.

#### Changes

- When plugged to the USB port in mass storage mode when the user eject the `ROMEMUL` volume it does not automount again automatically. The user must press `RESET` button or unplug and plug again the USB connector.

#### New Features

- The commands feature of the version 1.x is back. Now, if a user creates a folder or file with the following names, it will trigger an action in the device when ejected:

- `REBOOT`: When the volume is ejected, the device will try to mount again the volume again.
- `RESET`: When the volume is ejected, the device will enter in BOOTSEL mode. The volume `RPI-RP2` will be mounted again and the user can flash a new firmware.

The files or folders will be deleted after the action is triggered.

#### Fixes

- The creation of the `INFO.TXT` file was modified to avoid issues when powering on the device. Now, when powering on the device there is not any write operation in the mass storage device until the user decides to do it. This avoids issues with some users pressing repeatedly the `RESET` button when powering on the device and not completing the boot process.

### 2.0.0 (2024-10-15) - FAT12 and Upload release

This firmware release adds support for FAT12 filesystems and the ability to upload images to the Sidecartridge ROM Emulator from the SWITCHER.TOS app.

### 1.0.4 (2024-06-01) - First production release

First production release of the Sidecartridge ROM Emulator.

## SWITCHER.TOS Changelog

### 2.1.0 (2024-11-21) - Renaming images release

This release adds a feature to rename the images. Now the user can rename the images to a custom name and the SWITCHER.TOS will show the custom name in the menu.

#### Changes
- To delete a file, the user has to confirm the deletion by accepting with an uppercase `Y` or rejecting with any other key.

#### New Features
- The user can rename the images to a custom Long File Name (LFN) of up to 64 characters.

### 2.0.0 (2024-10-15) - Upload release

This release adds support for FAT12 filesystems and the ability to upload images to the Sidecartridge ROM Emulator from the SWITCHER.TOS app.

### 1.0.4 (2024-06-01) - First production release

First production release of the SWITCHER.TOS app.

## Hardware Changelog (ROM Emulator)

### 1.1.1 (2024-10-01) - Minor changes

#### Changes

- Larger pads for the `RESET` and `BOOTSEL` buttons.

#### Fixes

- Swap the UART pins to match the Raspberry Pi Pico pinout.

### 1.1.0 (2024-06-01) - First production batch

First production batch of the Sidecartridge ROM Emulator.



[Previous: FAQ](/sidecartridge-tos/faq/){: .btn mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }