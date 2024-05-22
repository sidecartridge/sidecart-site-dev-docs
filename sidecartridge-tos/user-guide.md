---
layout: minimal
title: User Guide
nav_order: 3
nav_exclude: true

---

# User Guide
{: .no_toc }

This section provides guidance on the initial steps on the day in day out operation of the SidecarTridge TOS emulator. How to power on the Atari ST, switch between TOS versions, and how to use the rescue mode.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Powering On the Atari ST

Simply turn on the Atari ST as you would normally do. The SidecarTridge TOS emulator will automatically boot the active TOS version. If you have not selected an active TOS version, the SidecarTridge TOS emulator will boot the default EmuTOS version provided with the kit.

## The SWITCHER.TOS Program

The SWITCHER.TOS program is a utility that allows you to switch between TOS versions. This program can be downloaded from the main page of the documentation here, or can be ordered on a physical diskette. The SWITCHER.TOS program is a TOS program that can be run from the desktop.

![SidecarTridge Switcher app](/sidecartridge-tos/assets/images/sidecartridge-switcher-desktop.png)

## Select a New Active Default TOS Version

Open the application like any other application in your Atari ST. The SWITCHER.TOS program will display a list of available TOS ROMs with the following information:

- **TOS ROM images**: The list of available TOS ROM images.
- **Default TOS ROM**: The currently active TOS ROM or the default TOS ROM.
- **Rescue TOS ROM**: The TOS ROM used for the rescue mode.

![SidecarTridge Switcher list](/sidecartridge-tos/assets/images/sidecartridge-switcher-list.png)

The user can select any TOS ROM from the list to make it the active TOS ROM. Use the arrow keys to navigate the list and press the `RETURN` key to select the desired TOS ROM. The SWITCHER.TOS program will then reboot the Atari ST with the selected TOS ROM.

![SidecarTridge Switcher selected](/sidecartridge-tos/assets/images/sidecartridge-switcher-select.gif)
This is the recommended way to switch between TOS versions. 

## Rescue Mode 

It's possible that a new active TOS ROM is corrupted or not working correctly. In this case, we have two options:

1. Rewrite the TOS ROM images on the Flash as described in the [Getting Started](/sidecartridge-tos/getting-started/) section.
2. Use the rescue mode.

We think the rewriting of the TOS ROM images is a good option if you have easy access to a computer with a USB port and can connect the SidecarTridge TOS emulator to it with your Atari ST computer case open. If your TOS images are not going to change very often this can be the best option, but if you plan to change ROM images frequently because you are testing different TOS versions or you are developing your own TOS ROM, the rescue mode is the best option.

The rescue mode is a signal that can be sent to the SidecarTridge TOS emulator to force it to boot the rescue TOS ROM selected. The rescue mode is activated by short cutting the `RESCUE` jumper on the reverse side of the SidecarTridge TOS emulator. Since a jumper is not the most user-friendly way to activate the rescue mode, we have included a rescue mode cable and button on the SidecarTridge TOS emulator optionally.

![SidecarTridge Rescue Mode](/sidecartridge-tos/assets/images/sidecartridge-rescue-mode.png)

So to force booting the rescue TOS ROM, you have to do as follows:

1. Turn off the Atari ST.
2. Connect the rescue mode cable to the SidecarTridge TOS emulator.
3. Press the rescue mode button and keep it pressed.
4. Turn on the Atari ST.
5. Release the rescue mode button when the Atari ST is turned on.

The Atari ST will boot the rescue TOS ROM. Now you can then use the SWITCHER.TOS program to select a new active TOS ROM.



[Previous: Hardware Installation](/sidecartridge-tos/hardware-installation/){: .btn .mr-4 }
[Back to Top](/sidecartridge-tos){: .btn .mr-4 }
[Next: Troubleshooting](/sidecartridge-tos/troubleshooting/){: .btn }
