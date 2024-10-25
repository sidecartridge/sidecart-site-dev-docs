---
layout: default
title: Troubleshooting
nav_order: 8
nav_exclude: false
parent: SidecarTridge TOS
---

# Troubleshooting
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Preparing the SidecarTridge TOS files

{: .warning}
UPGRADE TO VERSION FIRMWARE VERSION 2. In version 1 of the firmware, the top issue is the fragmentation of the filesystem. Please read [The Mini-FAT16 Filesystem](/sidecartridge-tos/getting-started/#the-mini-fat16-file-system) first to save headaches later.

### Some of the TOS images are not recognized by the Atari ST in Firmware version <=1.0.4

It is possible that the TOS image is not correctly flashed on the SidecarTridge TOS due to fragmentation issues. To solve this issue:

1. copy the TOS images in small batches
2. use the `DEFRAG` command in the SidecarTridge TOS to defragment the filesystem as described in the [Copying TOS image files section](/sidecartridge-tos/getting-started/#copying-tos-image-files) section.
3. verify that the TOS image is correctly flashed on the SidecarTridge TOS. Check the information in the file `INFO.TXT` to see if the TOS image is correctly flashed.
4. Repeat the process until all the TOS images are correctly recognized by the Atari ST.

As a rule of thumb, upgrade to firmware version 2.0. Fragmentation is no longer an issue.

### The `Sidecartrdg` volume is not recognized by the host computer when the device is connected to a USB power source in Firmware version <=1.0.4

Depending on the host computer's operating system and USB port manufacturer it can take more than 10 miliseconds to set the power signals in the USB port. This can cause the device to not be recognized by the host computer. To solve this issue, press the RESET button on the TOS emulator board for a few seconds until the `Sidecartrdg` volume appears on the host computer.

As a rule of thumb, upgrade to firmware version 2.0. Fragmentation is no longer an issue.

### The `Sidecartrdg` volume (Firmware version <=1.04) or `ROMEMUL` volume (Firmware version >= 2.0.0) are not recognized by the host computer when the device is connected to the Atari ST

If the SidecarTridge TOS takes the power from the Atari ST it will not be recognized by the host computer and the device will start working in the TOS emulator mode and not in the mass storage mode. To solve this issue, double check that your Atari ST is powered off when you connect the SidecarTridge TOS to the Atari ST.

### When I copy a TOS image to the SidecarTridge TOS, the file is not recognized or stored correctly

The host computers implement in the external storage devices a cache mechanism that can cause the file to be stored incorrectly. To solve this issue, **eject the SidecarTridge TOS volume ALWAYS from the host computer when you finish copying the TOS images**.

## Atari ST Issues

### The Atari ST does not boot when the SidecarTridge TOS is connected

Ensure that the TOS images are correctly flashed on the SidecarTridge TOS:

1. Try first with the default firmware version that comes with the EmuTOS image. It should work out of the box.
2. Modify the file `DEFAULT.TXT` with the name of the TOS image you want to use.
3. Verify that the TOS image size is correct for your Atari ST model. As a rule of thumb, the TOS image size should be 192KB for ST/STF/STFM models and 256KB for STE/MegaSTE models.
4. Verify that the TOS image is correctly flashed on the SidecarTridge TOS.
5. After making any change in the volume, gently eject the SidecarTridge TOS volume from the host computer.

### The Atari ST boots with a black screen or garbage characters

Some USB cables can set some signals on the USB port that can interfere with the SidecarTridge TOS Emulator. To solve this issue, fully unplug the USB cable from the SidecarTridge TOS and try again.


## SWITCHER.TOS Issues

### The SWITCHER.TOS program returns an error when reading the list of available TOS images

Check that the version of the SWITCHER.TOS program is the same as the firmware version of the SidecarTridge TOS. The SWITCHER.TOS program is included in the volume since version 2.0.0. If you have updated the firmware, you should also update the SWITCHER.TOS program.

### The SWITCHER.TOS program hangs when loading available TOS images

The SWITCHER.TOS program can hang when loading the available TOS images if the USB cable is connected to the SidecarTridge TOS. To solve this issue, fully unplug the USB cable from the SidecarTridge TOS. Some USB cables can set some signals on the USB port that can interfere with the SidecarTridge TOS Emulator.

### Cannot upload TOS images with names longer than 8 characters and three-letter extension

The SWITCHER.TOS program supports long filenames up to 64 characters. However, the Atari ST operating system only supports filenames with 8 characters and three-letter extension. To solve this issue and upload TOS images with long filenames, use the mass storage mode of the SidecarTridge TOS and copy the TOS images directly to the `ROMEMUL` volume from a host computer.


[Previous: Compatibility](/sidecartridge-tos/compatibility/){: .btn .mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }
[Next: FAQ](/sidecartridge-tos/faq/){: .btn }