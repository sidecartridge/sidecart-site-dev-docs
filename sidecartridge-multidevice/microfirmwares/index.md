---
layout: default
title: Microfirmwares for the Firmware V2.0 (ALPHA)
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares
  - /microfirmwares/
---

# Microfirmwares for the Firmware V2.0 (ALPHA)
{: .no_toc }

{: .warning }
This is an **ALPHA** version of the firmware, and it is not recommended for production use. It is intended for developers and makers who want to experiment with the Multi-device board and contribute to its development with code or just submitting bugs. If you are a novice user, please refer to the [previous version of the firmware](https://docs.sidecartridge.com/sidecartridge-multidevice/userguide/) for a more stable experience.


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Microfirmwares

### What is a microfirmware?

A Microfirmware app is a small, self-contained program that runs on a standalone RP2040 or RP235x chip, along with a companion firmware on your computer that talks to it. Together, they provide the features of the device.

Here’s how it works:

### Microfirmware App Core
This is the main program running on the RP2040 chip. It manages things like reading the microSD card, talking to the computer, and (if needed) providing a web interface.

#### Global Settings
These are settings for the whole device, stored in flash memory. The Microfirmware app reads them to know how the device is configured, but does not change them.

#### Local Settings
Each Microfirmware app can have its own settings, also stored in flash. These are used just by that app, so one app’s settings won’t affect another.

#### Computer Firmware
On the computer side, there is a small program (called the Booster app) that acts as a terminal and communicates with the Microfirmware app. Because this runs in the computer’s ROM, it’s harder to update and debug. Most testing and debugging happens on the Microfirmware app side.

The Booster App is designed to manage the Microfirmware apps on the device, allowing users to download, install, update, and launch them easily. It also provides a web interface for managing the apps.

The available Microfirmware apps are listed in a public repository, which the Booster app connects to. Users can browse and install apps from this repository, or upload their own apps to the device. They can also install their own repository for themselves or others to use.

### Developing Microfirmware Apps

To develop your own Microfirmware apps, there is a  [template repository](https://github.com/sidecartridge/md-microfirmware-template) and follow the instructions in the [Programming Guide](/sidecartridge-multidevice/programming/).

Each Microfirmware app should be a self-contained program that can run on the RP2040 or RP235x chip. It should include the necessary code to read the microSD card, communicate with the computer, and provide any additional features you want. 

### Available Microfirmware Apps

The following Microfirmware apps are available in the public repository:
- [ROM Emulator](/sidecartridge-multidevice/microfirmwares/rom_emulator/): An emulator for ROM files, allowing you to run games and applications from the microSD card or from a remote server.
- [Real Time Clock Emulator](/sidecartridge-multidevice/microfirmwares/rtc_emulator/): An emulator for real-time clock functionality, allowing you to set and read the current time and date from a remote NTP server. It also emulates a DTC2126 chip.
- [Drives Emulator](/sidecartridge-multidevice/microfirmwares/drives_emulator/): An emulator for hard disk and floppy disk drives, allowing you to access and manage disk images stored on the microSD card. It also includes a Real Time Clock emulator. 


[Previous: User Guide](/sidecartridge-multidevice/userguide_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: ROM Emulator](/sidecartridge-multidevice/microfirmwares/rom_emulator/){: .btn }