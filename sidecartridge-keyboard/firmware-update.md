---
layout: default
title: Firmware Update
nav_order: 6
nav_exclude: false
parent: SidecarTridge Keyboard
---

# Firmware Update
{: .no_toc }

Use this chapter when you need to install a newer firmware release on the SidecarTridge Keyboard Emulator.

Firmware updates are installed through the micro-USB connector and do not require the Atari computer to be powered on.

There are two supported update methods:

* `Web flash mode`: use the browser-based installer
* `Manual mode`: copy the firmware file to the device in BOOTSEL mode

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## When to update

You only need to update the firmware when:

* a new release adds features you want to use
* a newer release improves compatibility or fixes bugs
* you are asked to update while troubleshooting a problem

If the device already works correctly for your setup, a firmware update is optional.

## What you need

Before starting, prepare:

* the SidecarTridge Keyboard Emulator
* a micro-USB cable
* a Windows, macOS, or Linux computer
* the latest stable firmware file for the SidecarTridge Keyboard Emulator

Download the firmware from the SidecarTridge downloads page:

[https://sidecartridge.com/downloads/](https://sidecartridge.com/downloads/)

Make sure you select the firmware intended for the keyboard emulator.

## Web flash mode

If you are using a Chromium-based browser, you can update the firmware directly from the official web installer page:

[https://sidecartridge.com/assets/html/sidecartridge-firmware-installer.html](https://sidecartridge.com/assets/html/sidecartridge-firmware-installer.html)

This method does not require any extra application or flashing tool.

### Browser requirements

The web installer requires:

* a Chromium-based browser
* WebUSB support
* the device connected through the micro-USB cable

If the browser does not support web flashing, the installer page will tell you to use the manual BOOTSEL procedure instead.

### Using the web installer

To update the firmware with the web installer:

* connect the device to your computer using the micro-USB cable
* open the firmware installer page in a Chromium-based browser
* put the board in BOOTSEL mode
* click `Detect MCU`
* select the correct device family and firmware
* click `Load firmware`
* grant USB access when the browser asks for permission
* click `Flash`

The installer guides the process in four stages:

* detect the MCU in BOOTSEL mode
* select the device family and firmware
* grant USB access and flash the firmware
* confirm the successful installation

When the flashing process finishes, the device reboots and the new firmware is installed.

## Manual mode

### Entering BOOTSEL mode

To flash new firmware, the RP2350 microcontroller on the device must be started in BOOTSEL mode.

Physical access to the board buttons is required for this step. On Croissant, that usually means opening the computer again to access the board. On Soufflè, the board is externally accessible.

To enter BOOTSEL mode:

* connect the device to your computer using the micro-USB cable
* hold down the `BOOTSEL` button for a few seconds
* while holding `BOOTSEL`, press and hold the `RESET` button
* release the `RESET` button
* gently release the `BOOTSEL` button

If the procedure succeeds, a new removable drive named `RP2350` should appear on your computer.

### Copying the firmware file

Once the `RP2350` drive appears:

* open the `RP2350` drive
* locate the downloaded firmware file on your computer
* copy the firmware file to the `RP2350` drive

After the file is copied, the device should automatically flash the new firmware and reboot.

Once the process is finished:

* disconnect the micro-USB cable
* reconnect the device to its normal setup
* power on the Atari computer and verify that the device starts normally

## Notes and recovery

If the `RP2350` drive does not appear, repeat the BOOTSEL procedure and make sure the buttons are pressed in the correct order.

If the firmware update does not complete or the device does not boot correctly afterwards, repeat the flashing procedure with the latest stable firmware file.

If problems persist, continue with the troubleshooting chapter:

[Troubleshooting](/sidecartridge-keyboard/troubleshooting/)

[Previous: User Guide](/sidecartridge-keyboard/user-guide/){: .btn .mr-4 }
[Main](/sidecartridge-keyboard/){: .btn .mr-4 }
[Next: Compatibility](/sidecartridge-keyboard/compatibility/){: .btn }
