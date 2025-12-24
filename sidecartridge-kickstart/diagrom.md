---
layout: default
title: Diagnosing your Amiga with DIAGROM and Kickstart Emulator
nav_order: 8.5
nav_exclude: false
parent: SidecarTridge Kickstart

---

# Diagnosing your Amiga with DIAGROM and Kickstart Emulator
{: .no_toc }

Use this chapter to install and run DiagROM 1.3 on the SidecarTridge Kickstart emulator. [DiagROM](https://www.diagrom.com/) is a diagnostic ROM by John "Chucky/The Gang" Hertell that helps you test and troubleshoot classic Amiga hardware.

{: note }
This software is provided by a third party and is not affiliated with SidecarTridge, but the developer asks that if you find it useful, please consider a donation to a charity of your choice. See [diagrom.com](https://www.diagrom.com/) for details.

![DIAGROM](/sidecartridge-kickstart/assets/images/DIAGROM-MENU.jpeg){: .img-center }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## What you need

- A SidecarTridge Kickstart emulator installed and working on your Amiga.
- A computer with USB to access the `ROMEMUL` volume (see [Getting Started](/sidecartridge-kickstart/getting-started/#connecting-the-device-to-a-computer)).
- The DiagROM 1.3 Amiga ROM image downloaded from [diagrom.com](https://www.diagrom.com/).

{: .note }
DiagROM 1.x is listed as compatible with the SidecarTridge Kickstart emulator in the [Compatibility](/sidecartridge-kickstart/compatibility/) table.

## Download DiagROM 1.3

1. Open [diagrom.com](https://www.diagrom.com/) and follow the download instructions for the Amiga version.
2. Select the **`DiagROM`** file inside the DiagROM 1.3 zip file. This file matches the A500/A2000 512KB layout required by the emulator.
3. Rename the file to `DiagROM.rom` for easier identification.


{: .note }
You don't need byte swapping or conversion; the `DiagROM` file is ready to use as-is with the SidecarTridge Kickstart emulator.

## Copy DiagROM to the SidecarTridge Kickstart emulator

1. Connect the SidecarTridge Kickstart emulator to your computer using the USB-C cable.
2. Open the `ROMEMUL` volume.
3. Copy the `DiagROM.rom` 1.3 ROM image file to the root of `ROMEMUL`.
4. Edit `DEFAULT.TXT` and set the `DiagROM.rom` file name as the default ROM.
5. Edit `RESCUE.TXT` and set the `DiagROM.rom` file name as the rescue ROM (optional).
6. Eject the `ROMEMUL` volume safely.

{: .warning }
Always eject the `ROMEMUL` volume after copying files so the emulator reindexes the ROM list.


## Boot and run diagnostics

1. Disconnect the SidecarTridge Kickstart emulator from your computer and connect it to your Amiga.
2. Power on the Amiga.
3. DiagROM should boot directly and present the diagnostics screen.
4. Use the on-screen tests to check RAM, CPU, and custom chips.

If DiagROM does not boot, confirm the ROM image is 512KB, re-copy it to `ROMEMUL`, and ensure it is selected as the default ROM.

[Previous: Kickstart ROM Conversion](/sidecartridge-kickstart/kickstart-conversion/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Troubleshooting](/sidecartridge-kickstart/troubleshooting/){: .btn }
