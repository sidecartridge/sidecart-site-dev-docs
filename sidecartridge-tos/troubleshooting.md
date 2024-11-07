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

## Hardware Issues

{: .warning}
UPGRADE TO VERSION FIRMWARE VERSION 2. In version 1 of the firmware, the top issue is the fragmentation of the filesystem. This issue is solved in version 2.

### The `ROMEMUL` volume is not recognized by the host computer when the device is connected to a USB power source

If the `ROMEMUL` volume is not recognized by the host computer when the device is connected to a USB power source, we need to figure out if the issue is related to the USB power source or the SidecarTridge TOS device. To solve this issue, follow these steps:

#### Check the USB connection

Verify that the cable is correctly connected to the SidecarTridge TOS device and the USB power source. Try using a different USB cable or USB power source to see if the issue is related to the USB connection.

#### Enter into BOOTSEL mode

The BOOTSEL mode is the mode to flash the firmware on the SidecarTridge TOS device. To enter into BOOTSEL mode, this is the well-known procedure for the RP2040 microcontroller:

1. Hold down the `RESET` button on the SidecarTridge TOS ROM Board.
2. While holding `RESET`, press and hold the `BOOT` button.
3. Release the `RESET` button.
4. Release the `BOOT` button.

Alternatively, you can do this without using the RESET button:

1. Unplug the device from the USB connector and power off the computer.
2. Hold the `BOOT` button.
3. Plug in the USB connector.
4. Release the `BOOT` button.

If the `RPI-RP2` volume does not appear on your computer, check that the USB cable is correctly connected to the SidecarTridge TOS device and the USB power source.

If the `RPI-RP2` volume appears, try reinstalling the firmware: [Firmware Installation Guide](https://docs.sidecartridge.com/sidecartridge-tos/getting-startedV2/#firmware-installation)


### The `ROMEMUL` volume are not recognized by the host computer when the device is connected to the Atari ST

If the SidecarTridge TOS takes the power from the Atari ST it will not be recognized by the host computer and the device will start working in the TOS emulator mode and not in the mass storage mode. To solve this issue, double check that your Atari ST is powered off when you connect the SidecarTridge TOS to the Atari ST.

### When I copy a TOS image to the SidecarTridge TOS, the file is not recognized or stored correctly

The host computers implement in the external storage devices a cache mechanism that can cause the file to be stored incorrectly. To solve this issue, **eject the SidecarTridge TOS volume ALWAYS from the host computer when you finish copying the TOS images**.

### The SidecarTridge TOS does not respond to the RESET button

If the SidecarTridge TOS does not respond to the RESET button we need to figure out if the device enters into the BOOTSEL mode. Follow these steps described in the previous section.

If the device enters into the BOOTSEL mode, try pressing the RESET button again. If the device does not respond to the RESET button, try cleaning the RESET button with isopropyl alcohol: Occasionally, micro-buttons can stop responding due to dust, grease, or flux buildup. Apply isopropyl alcohol (IPA) to the buttons, press them multiple times while wet, and allow the IPA to evaporate.

### The SidecarTridge TOS does not respond to the BOOT button

If the SidecarTridge TOS does not respond to the BOOT button after following the procedure to enter into the BOOTSEL mode, try cleaning the BOOT button with isopropyl alcohol as described in the previous section.


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