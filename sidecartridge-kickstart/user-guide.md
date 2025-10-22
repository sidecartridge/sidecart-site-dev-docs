---
layout: default
title: User Guide
nav_order: 5
nav_exclude: false
parent: SidecarTridge Kickstart
---

# User Guide
{: .no_toc }

This section provides guidance on the initial steps and daily operation of the SidecarTridge Kickstart Emulator, including how to power on the Amiga, switch between Kickstart or custom ROMs, and use the rescue mode.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Powering on the Kickstart Emulator

The SidecarTridge Kickstart Emulator has a built-in red LED indicator that lights up when the board is powered on. It will light up when the Amiga is powered on, or when the SidecarTridge Kickstart Emulator is powered via USB.

## Powering On the Amiga

Simply turn on the Amiga as you normally would. The SidecarTridge Kickstart Emulator will automatically boot the active Kickstart version, lighting up a green LED indicator when the firmware is running.

## Powering On USB-connected to a PC/Mac/Linux Computer
When the SidecarTridge Kickstart Emulator is connected to a computer via USB, it will automatically start in USB Mass Storage mode. This allows you to access the internal flash memory of the SidecarTridge Kickstart Emulator as a USB drive on your computer. It will light up an orange LED indicator when the internal USB drive is mounted. When transferring files to the internal USB drive, this LED will blink to indicate data transfer activity.

{: .warning}
The SidecarTridge Kickstart Emulator will not boot the Amiga when connected to a computer via USB. To boot the Amiga, you must disconnect the USB cable and power on the Amiga as usual.

## The SWITCHER Program

The SWITCHER program is a utility that allows you to switch between Kickstart versions. This program can be obtained through different ways:
- copied from the SidecarTridge Kickstart Emulator internal USB drive, inside the `/AMIGA` folder.
- downloaded from the main page of the documentation

SWITCHER can be run from the Amiga Workbench desktop like any other Amiga program.

![SidecarTridge Switcher app](/sidecartridge-kickstart/assets/images/sidecartridge-switcher-desktop.png)

## Select a New Active Default Kickstart Version

{: .note}
Unplug the SidecarTridge Kickstart Emulator from the USB port before running the SWITCHER program. Some cables may set some signals on the USB port that can interfere with the SidecarTridge Kickstart Emulator.

Open the SWITCHER application. The program will display a list of available Kickstart ROMs, custom ROMs with the following information:

- **ROM images**: The list of available ROM images.
- **Default or Active ROM**: The currently active or default ROM, marked with a `A` letter.
- **Rescue ROM**: The ROM used for the rescue mode, marked with a `R` letter.

![SidecarTridge Switcher list](/sidecartridge-kickstart/assets/images/sidecartridge-switcher-list.png)

Use the arrow keys to navigate the list and press the `RETURN` key to select the desired ROM. The program will then reboot the Amiga with the selected ROM.

![SidecarTridge Switcher selected](/sidecartridge-kickstart/assets/images/sidecartridge-switcher-select.png)

{: .note}
This is the recommended way to switch between ROM versions. It is also possible to switch ROM versions modifying the `DEFAULT.TXT` file as described in the [Getting Started](/sidecartridge-kickstart/getting-started/) section, but this method is not recommended for daily use.

## Rescue Mode

If a new active ROM is corrupted or not working correctly, you have two options:

1. Rewrite the ROM images on the flash memory as described in the [Getting Started](/sidecartridge-kickstart/getting-started/) section.
2. Use the rescue mode.

Rewriting the ROM images is a good option if you have easy access to a computer with a USB port and can connect the SidecarTridge Kickstart Emulator to it with your Amiga computer case open. This is suitable if your ROM images are not going to change frequently. However, if you plan to change ROM images often, the rescue mode is the best option.

The rescue mode can be activated by short-circuiting the `RESCUE` jumper on the reverse side of the SidecarTridge Kickstart Emulator. For user convenience, a rescue mode cable and button are included with the emulator.

![SidecarTridge Rescue Mode](/sidecartridge-kickstart/assets/images/sidecartridge-rescue-board.png)

To force boot the rescue ROM, follow these steps:

1. Turn off the Amiga.
2. Connect the rescue mode cable to the SidecarTridge Kickstart Emulator (if not already connected).
3. Press and hold the rescue mode button.
4. Turn on the Amiga.
5. Release the rescue mode button once the Amiga is powered on.

The Amiga will boot the rescue ROM. You can then use the SWITCHER program to select a new active ROM.

## ROM Management from the Amiga Computer

### Overview
 
It is possible to upload, delete and rename a new ROM image from any Amiga computer. This feature is useful if you want to upload a new ROM image without the need of a computer with a USB port and/or the need to open the Amiga computer case.

### Uploading a new ROM from the Amiga computer

To upload a new Kickstart or custom ROM image from the Amiga computer, press the [`U`]pload key in the SWITCHER program. The program will show you a file system browser to select the ROM image to upload from your computer. Navigate to the desired ROM image and press the `RETURN` key to start the upload process.

{: .warning}
The upload, rename and delete features cannot be interrupted. Do not turn off the Amiga computer while the upload or delete process is in progress. It may damage the storage memory of the SidecarTridge Kickstart Emulator needing a reflash of the firmware.


![SidecarTridge Switcher upload](/sidecartridge-kickstart/assets/images/sidecartridge-switcher-upload.png)

The SWITCHER program will upload the Kickstart or custom ROM image to the SidecarTridge Kickstart Emulator. This process may take a few minutes depending on the size of the Kickstart ROM image. Once the upload is complete, the application will verify that the new image is correct and will reindex the Kickstart ROM images list.

The uploaded Kickstart ROM image will be available in the list of Kickstart ROM images. You can now select the new Kickstart ROM image as the active default Kickstart ROM.

### Deleting a ROM from the Amiga computer

To delete a ROM image from the Amiga computer, select the ROM image you want to delete from the list of ROM images and press the [`D`]elete key in the SWITCHER program. The program will ask you to confirm the deletion of the ROM image. The SWITCHER program will delete the ROM image from the SidecarTridge Kickstart Emulator and reindex the ROM images list.

![SidecarTridge Switcher delete](/sidecartridge-kickstart/assets/images/sidecartridge-switcher-delete.png)

{:.note}
It is not possible to delete the default ROM image or the rescue ROM image. If you want to delete the default ROM image, you must first select a new default ROM image. If you want to delete the rescue ROM image, you also must first select a new rescue ROM image.

### Renaming a ROM from the Amiga computer

To rename a ROM image from the Amiga computer, select the ROM image you want to rename from the list of ROM images and press the [`R`]ename key in the SWITCHER program. The program will ask you to enter the new name for the ROM image. The SWITCHER program will rename the ROM image and reindex the ROM images list.

The new name must be valid Long File Name (LFN) of up to 64 characters in the ASCII range 32-126. The SWITCHER program will check the new name and will reject it if it is not valid or longer than 64 characters.

The new name will be rejected if it is already in use by another ROM image.

![SidecarTridge Switcher rename](/sidecartridge-kickstart/assets/images/sidecartridge-switcher-rename.png)

{:.note}
As the delete feature, it is not possible to rename the default ROM image or the rescue ROM image. If you want to rename the default or rescue ROM image, you must first select a new default ROM image.



## Select a new Rescue ROM

The rescue ROM cannot be changed using the SWITCHER program or the internal API call to switch ROMs. To change the rescue ROM, you must modify the `RESCUE.TXT` file as described in the [Getting Started](/sidecartridge-kickstart/getting-started/) section. If you still want to change the rescue ROM using the SWITCHER program, you can do so by [following these steps](/sidecartridge-kickstart/troubleshooting/#cant-change-the-rescue-and-defaultactive-images-from-the-host-computer) at your own risk.

[Previous: Hardware Installation](/sidecartridge-kickstart/hardware-installation/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Advanced Settings](/sidecartridge-kickstart/advanced-settings/){: .btn }
