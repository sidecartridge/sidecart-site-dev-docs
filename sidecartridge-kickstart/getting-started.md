---
layout: default
title: Getting Started
nav_order: 3
nav_exclude: false
parent: SidecarTridge Kickstart

---

#  Getting Started
{: .no_toc }

This section provides guidance on the initial steps to start working with the SidecarTridge Kickstart emulator. It includes prerequisites, hardware installation instructions, software setup, and configuration. By following the procedures outlined in this and the upcoming sections, users can ensure a smooth start to their journey with the SidecarTridge Kickstart emulator.

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/-0YuK57OUrY?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## Prerequisites

Before you begin the installation and setup of the SidecarTridge Kickstart emulator, ensure you have the following items and tools:

### Required Components

#### SidecarTridge Kickstart Emulator Kit

This should include:
1. The SidecarTridge ROM Emulator Board
2. The SidecarTridge Amiga Carrier Board. **The ROM Emulator Board is soldered onto this carrier board**.
3. RESCUE cable: for connecting an external push button to the SidecarTridge Kickstart emulator to enter rescue mode.

![SidecarTridge Kit](/sidecartridge-kickstart/assets/images/sidecartridge-kickstart-kit.png)

#### Amiga Computer
The emulator is compatible with various models, please read the [previous section to ensure compatibility](/sidecartridge-kickstart/before-buy/) with your Amiga model.

### Tools and Equipment
-  **USB-C cable**: for connecting the SidecarTridge Kickstart emulator to a computer for firmware updates and Kickstart image transfers.
- **Phillips Head Screwdriver**: For opening the Amiga case.
- **Anti-Static Wrist Strap**: To prevent static discharge that could damage electronic components.
- **Small Container**: To hold screws and small parts during the disassembly of the Amiga.
- **IC Extractor Tool**: For safely removing the ROM chips from the Amiga motherboard. I strongly recommend using a proper IC extractor tool to avoid damaging the ROM chips or the motherboard. If you don't have one, you can use a flat-head screwdriver, but be very careful not to damage the chips or the motherboard.
- **Insulating Tape**: To avoid short circuits between the SidecarTridge Kickstart emulator and the Amiga motherboard. Not strictly necessary, but recommended.
- **Computer with USB Port**: A Windows, macOS, or Linux computer for transferring ROM files and updating firmware.

### Software and Files
- **ROM Image Files**: Ensure you have the necessary Kickstart image files ready for transfer. These can be downloaded from reputable sources like [Amiga Forever](https://www.amigaforever.com/). Please read the [Kickstart conversion guide](/sidecartridge-kickstart/kickstart-conversion/) if you need help converting your Kickstart ROM files to the required format. Also you can use custom ROM images if you have developed your own, or obtained them from other sources like [DiagROM](https://diagrom.com/) or [EmuTOS](https://emutos.sourceforge.io/).
- **SWITCHER Program**: A program for selecting and managing ROM versions on the Amiga. This program is required to upload new ROM images or switch between Kickstart versions and can be downloaded from the SidecarTridge website or copied from the `ROMEMUL` volume when connecting the SidecarTridge Kickstart emulator to a computer. The folder `AMIGA`contains the `SWITCHER` program as an executable file, a .ADF disk image and also in .ST format for EmuTOS.

{: .note }
The SidecarTridge Kickstart emulator does not come with Kickstart image files due to legal restrictions. Users must obtain their own Kickstart images from legitimate sources.

**By having these prerequisites in place, you will be well-prepared to proceed with the installation and setup of your SidecarTridge Kickstart emulator.**

## Unboxing and Inspecting the Components

### SidecarTridge Kickstart Emulator Kit

When you receive your SidecarTridge Kickstart emulator kit, carefully unbox and inspect the components to ensure everything is included and in good condition. All kits should contain the following items:

1. **SidecarTridge ROM Emulator Board soldered onto the Carrier Board**: This is the main component that will replace the ROM chips on your Atari ST motherboard.
2. **RESCUE cable and push button**: This cable allows you to connect an external push button to the SidecarTridge Kickstart emulator for entering rescue mode.

The board and the sticker on the box contain a QR code that links to the SidecarTridge Kickstart documentation website, providing access to the quickstart, user guide, compatibility information, and other resources.

### Additional Components

If you have purchased additional components like the USB-C cable, ensure they are also included in the package.

## Preparing the ROM Images

{: .warning}
As a rule of thumb, **ALWAYS** eject the `ROMEMUL` volume after making any changes to the files. This will ensure that the changes are correctly saved and reflected in the emulator.

### Connecting the Device to a Computer

The SidecarTridge Kickstart emulator has two modes: mass storage mode for transferring Kickstart image files and ROM emulation mode for booting the Atari ST with the selected Kickstart image. This section focuses on mass storage mode.

To enter mass storage mode, plug the SidecarTridge Kickstart emulator into the USB-C cable and connect it to your computer. It can be connected to both the Amiga and your computer simultaneously but will enter mass storage mode when powered on from the USB-C cable.

{: .note }
If the `ROMEMUL` volume does not appear on your computer, ensure the USB cable is properly connected and press the `RESET` button on the SidecarTridge Kickstart ROM Board for a few seconds to enter mass storage mode.

Open the `ROMEMUL` volume on your computer to access firmware files, Kickstart image files and custom ROM files. First time users should see the following files in the root directory:

- `INDEX.HTM`: Opens the SidecarTridge Kickstart documentation website.
- `INFO.TXT`: Contains information about the firmware version installed in the SidecarTridge Kickstart emulator.
- `AMIGA`: A folder containing the SWITCHER application in different formats. **You must copy this executable to your AMIGA computer to manage your Kickstart versions. You can learn to use in the [User Guide](/sidecartridge-kickstart/user-guide/)**
- `DEFAULT.TXT`: Contains the name of the default active Kickstart or custom ROM image file.
- `RESCUE.TXT`: Contains the name of the rescue Kickstart image or custom ROM image file.
- `CONFIG.TXT`: This file contains the advanced configuration settings for the emulator. The settings helps to adjust the speed of the address bus when the emulator runs in computers with very noisy buses, or when the computer has accelerated boards.

{: .note }

There are also metadata system files and directories starting with a dot (.) used by the host computer and not the SidecarTridge Kickstart emulator. Just ignore them.

{: .note }
There may be an offset of 4KBytes between the actual size of the image and the displayed file size due to the 4KBytes cluster size used by the SidecarTridge Kickstart emulator's FAT12 file system.

![SidecarTridge Volume](/sidecartridge-kickstart/assets/images/sidecartridge-volume.png)

### The FAT12 File System

The SidecarTridge Kickstart emulator uses a FAT12 file system with a 4KBytes cluster size. This means ROM images are stored in 4KBytes blocks, and file sizes are rounded up to the nearest 4KBytes boundary. The FAT12 file system is compatible with most operating systems, including Windows, macOS, and Linux.

To copy ROM image files to the SidecarTridge Kickstart emulator, drag and drop them into the `ROMEMUL` volume. The emulator will automatically store the ROM images in the file system.

### Copying ROM Image Files

Before copying ROM image files to the SidecarTridge Kickstart emulator, it is strongly recommended to first copy all files to a folder on your computer. This way, you can easily restore them if needed.

#### Create a Folder for the ROM Images

Create a folder on your desktop named `ROM Images` to store and organize your ROM image files. For example, using a MacBook Pro with macOS:

1. **Download ROM Images**: Collect a list of ROM images from the internet and store them in the folder. Refer to the [Compatibility](/sidecartridge-kickstart/compatibility/#list-of-supported-kickstart-versions-tested-with-the-sidecartridge-tos-emulator) section for tested versions.

   ![SidecarTridge Source Folder Example](/sidecartridge-kickstart/assets/images/sidecartridge-source-folder.png)

2. **(Optional) Rename Files for Clarity**: Rename files to a readable format. This helps when selecting the ROM version with the `SWITCHER` program.

   ![SidecarTridge Source Folder Renamed Example](/sidecartridge-kickstart/assets/images/sidecartridge-source-folder-renamed.png)

With the ROM image files organized and renamed, you can proceed to copy them to the SidecarTridge ROM emulator.

#### Copying the ROM Images on macOS

You can simply drag and drop the ROM image files from the `ROM Images` folder to the `ROMEMUL` volume. The files will be copied to the emulator's storage space and will be accessible for booting the Atari ST with the selected ROM image.

When dragging and dropping files from a Mac to the SidecarTridge Kickstart emulator, macOS creates temporary hidden files that are not supported by the SidecarTridge Kickstart emulator. To avoid this, it is recommended to open a Terminal window to copy the files to the SidecarTridge Kickstart emulator.

```bash
cp -R /path/to/ROM\ Images/* /Volumes/ROMEMUL/
```

#### Copying the ROM Images on Windows

In Windows, you can also drag and drop the ROM image files from the `ROM Images` folder to the `ROMEMUL` volume. Please follow the same guidelines as in macOS to avoid fragmentation and ensure the files are copied correctly.

#### Copying the ROM Images on Linux

In Linux, you can use the `cp` command to copy the ROM image files from the `ROM Images` folder to the `ROMEMUL` volume. Please follow the same guidelines as in macOS and Windows to avoid fragmentation and ensure the files are copied correctly.


```bash
cp -R /path/to/ROM\ Images/* /media/username/ROMEMUL/
```

{: .note }
Depending on the Linux distribution, the mount point of the SidecarTridge Kickstart emulator may vary. Replace `/media/username/ROMEMUL/` with the correct mount point of the emulator.

### Setting the Default and Rescue ROM Images
{: note}
The first time you set up the SidecarTridge Kickstart emulator, you need to set the default and rescue ROM images. This is a mandatory step to ensure the SidecarTridge Kickstart emulator knows which Kickstart image to use as the default and rescue ROM images.

The SidecarTridge Kickstart emulator allows you to set a default active ROM image and a rescue ROM image. The *default* ROM image is the one that will boot when the Amiga is powered on, while the *rescue* ROM image is used in case of a boot failure as a fallback option by enabling the rescue mode. You can set the `RESCUE` signal on the SidecarTridge Kickstart emulator using the RESCUE connector and a push button.

The *default* image can be changed by editing the `DEFAULT.TXT` file in the `ROMEMUL` volume or by using the `SWITCHER` program on the Amiga computer.

The *rescue* image can ONLY be changed by editing the `RESCUE.TXT` file in the `ROMEMUL` volume.

{: .warning}
We strongly recommend using the `SWITCHER` program to change the *default* ROM image. Change the *rescue* ROM image only when necessary, as it is a critical setting that should be used in case of boot failure.

To change the *default* and *rescue* ROM images using the `SWITCHER` program, please refer to the [Switching Between ROM Versions](#switching-between-rom-versions) section in the User Guide.

Changing the *default* and *rescue* ROM images by editing the `DEFAULT.TXT` and `RESCUE.TXT` files is straightforward. Open the `DEFAULT.TXT` file in the `ROMEMUL` volume and replace the name of the default ROM image with the desired ROM image file name. For example, to set `Kickstart 1.3.img` as the default ROM image, the `DEFAULT.TXT` file should contain exactly the name of the file (including the extension if it exists):

```
Kickstart 1.3.img
```

{: .note }
macOS and Windows operating systems may create hidden files when copying files to the SidecarTridge Kickstart emulator. These hidden files are not going to damage your device or your installation, but they will not be recognized by the emulator. To avoid this, use the Terminal in macOS or the Command Prompt in Windows to copy the files.

After editing the `DEFAULT.TXT` and `RESCUE.TXT` files, save the changes and eject the `ROMEMUL` volume from your computer. When ejecting the volume, the SidecarTridge Kickstart emulator will automatically reindex the Kickstart images and update the default and rescue Kickstart images.

{: .warning}
Have you already read that as a rule of thumb, **ALWAYS** eject the `ROMEMUL` volume after making any changes to the files? No? Ok, this is a reminder to ensure that the changes are correctly saved and reflected in the emulator.

### Magic File and Folder names
{: .d-inline-block }

The SidecarTridge Kickstart emulator recognizes specific file and folder names that trigger actions when the volume is ejected. These magic names are used to perform maintenance tasks on the device without the need for additional tools or software.

The following magic names are recognized by the SidecarTridge Kickstart emulator:
- `REBOOT`: When the volume is ejected, the device will try to mount the volume again.
- `RESET`: When the volume is ejected, the device will enter BOOTSEL mode. The volume `RPI-RP2` or `RP2350` will be mounted again, and the user can flash a new firmware.

The files or folders with these magic names will be deleted after the action is triggered.


## Firmware Installation

The SidecarTridge Kickstart emulator does come with pre-installed firmware, but not a default Kickstart image. However, it is recommended to check for the latest firmware version and update if necessary. The firmware update process is straightforward and can be done using a computer with a USB port.

We assume that you have already connected the SidecarTridge Kickstart emulator to your computer using the USB-C cable and that the `ROMEMUL` volume is accessible. If you have not done so, please refer to the [Connecting the Device to a Computer](#connecting-the-device-to-a-computer) section.

### Obtaining the Installed Firmware Version

To learn the firmware version installed on the SidecarTridge Kickstart emulator, open the `INFO.TXT` file in the `ROMEMUL` volume. The file contains information about the firmware version, the date of the firmware, the microcontroller used, the board ID, and the flash size. For example:

```
SidecarTridge ROM emulator. (C) 2024 GOODDATA LABS SL
Version: v2.0.0
Date: 2024-10-21 16:09:45
Mode: RELEASE
Microcontroller: RP2040-B2
Board ID: e46358c8071c0c29
Flash size: 16777216 bytes
```

The firmware version is displayed as `Version: vX.Y.Z`, where `X.Y.Z` is the major, minor, and patch version numbers. In this example, the firmware version is `v2.0.0`. 


[Previous: Before You Buy](/sidecartridge-kickstart/before-buy/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Hardware Installation](/sidecartridge-kickstart/hardware-installation/){: .btn }
