---
layout: default
title: "DEPRECATED: User Guide (v1.0 firmware)"
nav_order: 11
nav_exclude: true
parent: SidecarTridge TOS
---

{: .warn }
This is a deprecated version of the User Guide for the SidecarTridge TOS emulator with firmware version 1.0. Upgrade to the latest firmware version and refer to the [latest User Guide](/sidecartridge-tos/user-guideV2/) for the most up-to-date information.

# User Guide
{: .no_toc }

This section provides guidance on the initial steps and daily operation of the SidecarTridge TOS Emulator, including how to power on the Atari ST, switch between TOS versions, and use the rescue mode.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Powering On the Atari ST

Simply turn on the Atari ST as you normally would. The SidecarTridge TOS Emulator will automatically boot the active TOS version. If no active TOS version is selected, the emulator will boot the default EmuTOS version provided with the kit.

## The SWITCHER.TOS Program

The SWITCHER.TOS program is a utility that allows you to switch between TOS versions. This program can be downloaded from the main page of the documentation or ordered on a physical diskette. SWITCHER.TOS can be run from the desktop like any other TOS program.

![SidecarTridge Switcher app](/sidecartridge-tos/assets/images/sidecartridge-switcher-desktop.png)

## Select a New Active Default TOS Version

{: .note}
Unplug the SidecarTridge TOS Emulator from the USB port before running the SWITCHER.TOS program. Some cables may set some signals on the USB port that can interfere with the SidecarTridge TOS Emulator.

Open the SWITCHER.TOS application. The program will display a list of available TOS ROMs with the following information:

- **TOS ROM images**: The list of available TOS ROM images.
- **Default TOS ROM**: The currently active TOS ROM or the default TOS ROM.
- **Rescue TOS ROM**: The TOS ROM used for the rescue mode.

![SidecarTridge Switcher list](/sidecartridge-tos/assets/images/sidecartridge-switcher-list.png)

Use the arrow keys to navigate the list and press the `RETURN` key to select the desired TOS ROM. The program will then reboot the Atari ST with the selected TOS ROM.

![SidecarTridge Switcher selected](/sidecartridge-tos/assets/images/sidecartridge-switcher-select.gif)

{: .note}
This is the recommended way to switch between TOS versions. It is also possible to switch TOS versions modifying the `DEFAULT.TXT` file as described in the [Getting Started](/sidecartridge-tos/getting-started/) section, but this method is not recommended for daily use.

## Rescue Mode

If a new active TOS ROM is corrupted or not working correctly, you have two options:

1. Rewrite the TOS ROM images on the flash memory as described in the [Getting Started](/sidecartridge-tos/getting-started/) section.
2. Use the rescue mode.

Rewriting the TOS ROM images is a good option if you have easy access to a computer with a USB port and can connect the SidecarTridge TOS Emulator to it with your Atari ST computer case open. This is suitable if your TOS images are not going to change frequently. However, if you plan to change ROM images often, the rescue mode is the best option.

The rescue mode can be activated by short-circuiting the `RESCUE` jumper on the reverse side of the SidecarTridge TOS Emulator. For user convenience, a rescue mode cable and button are included with the emulator.

![SidecarTridge Rescue Mode](/sidecartridge-tos/assets/images/sidecartridge-rescue.png)

To force boot the rescue TOS ROM, follow these steps:

1. Turn off the Atari ST.
2. Connect the rescue mode cable to the SidecarTridge TOS Emulator.
3. Press and hold the rescue mode button.
4. Turn on the Atari ST.
5. Release the rescue mode button once the Atari ST is powered on.

The Atari ST will boot the rescue TOS ROM. You can then use the SWITCHER.TOS program to select a new active TOS ROM.

## Select a new Rescue TOS ROM

The recue TOS cannot be changed using the SWITCHER.TOS program or the internal API call to switch TOS ROMs. To change the rescue TOS ROM, you must modify the `RESCUE.TXT` file as described in the [Getting Started](/sidecartridge-tos/getting-started/) section.

[Previous: Hardware Installation](/sidecartridge-tos/hardware-installation/){: .btn .mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }
[Next: Compatibility](/sidecartridge-tos/compatibility/){: .btn }
