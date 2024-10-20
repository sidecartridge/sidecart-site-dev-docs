---
layout: default
title: Getting Started
nav_order: 3
nav_exclude: false
parent: SidecarTridge TOS

---

#  Getting Started
{: .no_toc }

This section provides guidance on the initial steps to start working with the SidecarTridge TOS emulator. It includes prerequisites, hardware installation instructions, software setup, and configuration. By following the procedures outlined in this and the upcoming sections, users can ensure a smooth start to their journey with the SidecarTridge TOS emulator.

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/sdvNxO436ck?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
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

Before you begin the installation and setup of the SidecarTridge TOS emulator, ensure you have the following items and tools:

### Required Components

#### SidecarTridge TOS Emulator Kit

This should include:
1. The SidecarTridge ROM Emulator Board
2. The SidecarTridge Atari ST Carrier Board. **The ROM Emulator Board is soldered onto this carrier board**.
3. (Optional) 3 1/2 floppy disk with the SWITCHER.TOS application. It is the program for managing TOS versions on the Atari ST. It can also be downloaded from the SidecarTridge website.
4. (Optional) USB-C cable: for connecting the SidecarTridge TOS emulator to a computer for firmware updates and TOS image transfers.
5. (Optional) RESCUE cable: for connecting an external push button to the SidecarTridge TOS emulator to enter rescue mode.

![SidecarTridge Kit](/sidecartridge-tos/assets/images/sidecartridge-kit.png)


#### Atari ST Computer
The emulator is compatible with various models, please read the [previous section to ensure compatibility](/sidecartridge-tos/before-buy/) with your Atari ST model.

### Tools and Equipment
- **Phillips Head Screwdriver**: For opening the Atari ST case.
- **Anti-Static Wrist Strap**: To prevent static discharge that could damage electronic components.
- **Small Container**: To hold screws and small parts during the disassembly of the Atari ST.
- **IC Extractor Tool**: For safely removing the ROM chips from the Atari ST motherboard. I strongly recommend using a proper IC extractor tool to avoid damaging the ROM chips or the motherboard. If you don't have one, you can use a flat-head screwdriver, but be very careful not to damage the chips or the motherboard.
- **Insulating Tape**: To avoid short circuits between the SidecarTridge TOS emulator and the Atari ST motherboard.
- **Computer with USB Port**: A Windows, macOS, or Linux computer for transferring ROM files and updating firmware.

### Software and Files
- **TOS Image Files**: Ensure you have the necessary TOS image files ready for transfer. These can be downloaded from reputable sources like [Avtandil website](https://avtandil.narod.ru/tose.html), [EmuTOS website](https://emutos.sourceforge.io/), or other trusted sources.
- **SWITCHER.TOS Program**: A program for selecting and managing TOS versions on the Atari ST. This program is required to switch between TOS versions and can be downloaded from the SidecarTridge website.

{: .note }
The SidecarTridge TOS emulator comes with a default EmuTOS image pre-installed and ready to boot. Since the original TOS image files are copyrighted, it's up to you to find the TOS images for your Atari ST model. At this moment every single TOS version found and tested on the internet is working with the SidecarTridge TOS emulator. Please read the [Compatibility](/sidecartridge-tos/compatibility/) section for a full list of tested TOS versions.

**By having these prerequisites in place, you will be well-prepared to proceed with the installation and setup of your SidecarTridge TOS emulator.**

## Unboxing and Inspecting the Components

### SidecarTridge TOS Emulator Kit

When you receive your SidecarTridge TOS emulator kit, carefully unbox and inspect the components to ensure everything is included and in good condition. All kits should contain the following items:

1. **SidecarTridge ROM Emulator Board soldered onto the Carrier Board**: This is the main component that will replace the ROM chips on your Atari ST motherboard.
2. **RESCUE cable and push button**: This cable allows you to connect an external push button to the SidecarTridge TOS emulator for entering rescue mode. 
3. **SidecarTridge QR Code card**: This card contains a QR code that links to the SidecarTridge website for firmware updates and documentation.

### Additional Components

If you have purchased additional components like the USB-C cable or the SWITCHER.TOS floppy disk, ensure they are also included in the package.

## Preparing the ROM Images

### Connecting the Device to a Computer

The SidecarTridge TOS emulator has two modes: mass storage mode for transferring TOS image files and ROM emulation mode for booting the Atari ST with the selected TOS image. This section focuses on mass storage mode.

To enter mass storage mode, plug the SidecarTridge TOS emulator into the USB-C cable and connect it to your computer. It can be connected to both the Atari ST and your computer simultaneously but will enter mass storage mode when powered on from the USB-C cable.

{: .note }
If the `ROMEMUL` volume does not appear on your computer, ensure the USB cable is properly connected and press the `RESET` button on the SidecarTridge TOS ROM Board for a few seconds to enter mass storage mode.

Open the `ROMEMUL` volume on your computer to access firmware files and TOS image files. The following files should be present:

- `INDEX.HTM`: Opens the SidecarTridge TOS documentation website.
- `INFO.TXT`: Contains information about the firmware version installed in the SidecarTridge TOS emulator.
- `DEFAULT.TXT`: Contains the name of the default active TOS image file.
- `RESCUE.TXT`: Contains the name of the rescue TOS image file.

There are also system files and directories starting with a dot (.) used by the SidecarTridge TOS emulator and an EmuTOS image file for your computer. For STF, STFM, and Mega ST models, the file is 192KBytes; for STE and Mega STE models, the file is 256KBytes.

{: .note }
There may be an offset of 4KBytes between the actual size of the image and the displayed file size due to the 4KBytes cluster size used by the SidecarTridge TOS emulator's FAT12 file system.

![SidecarTridge Volume](/sidecartridge-tos/assets/images/sidecartridge-volumeV2.png)

### The FAT12 File System

The SidecarTridge TOS emulator uses a FAT12 file system with a 4KBytes cluster size. This means TOS images are stored in 4KBytes blocks, and file sizes are rounded up to the nearest 4KBytes boundary. The FAT12 file system is compatible with most operating systems, including Windows, macOS, and Linux.

To copy TOS image files to the SidecarTridge TOS emulator, drag and drop them into the `ROMEUL` volume. The emulator will automatically store the TOS images in the file system.

### Copying TOS Image Files

Before copying TOS image files to the SidecarTridge TOS emulator, it is strongly recommended to first copy all files to a folder on your computer. This way, you can easily restore them if needed.

{: .note}
Starting with the SidecarTridge TOS emulator firmware version 2 and above, the emulator will automatically defragment the flash memory after copying files.

#### Create a Folder for the TOS Images

Create a folder on your desktop named `TOS Images` to store and organize your TOS image files. For example, using a MacBook Pro with macOS:

1. **Download TOS Images**: Collect a list of TOS images from the internet and store them in the folder. Refer to the [Compatibility](/sidecartridge-tos/compatibility/#list-of-supported-tos-versions-tested-with-the-sidecartridge-tos-emulator) section for tested versions.
   
   ![SidecarTridge Source Folder Example](/sidecartridge-tos/assets/images/sidecartridge-source-folder.png)

2. **Rename Files for Clarity**: Rename files to a readable format, such as `TOS Version - Language - Screen Hertz.img`. For example, `tos106uk.img` becomes `TOS 1.06 - English-UK - 50Hz`. This helps when selecting the TOS version with the `SWITCHER.TOS` program.

   ![SidecarTridge Source Folder Renamed Example](/sidecartridge-tos/assets/images/sidecartridge-source-folder-renamed.png)

With the TOS image files organized and renamed, you can proceed to copy them to the SidecarTridge TOS emulator.

#### Copying the TOS Images on macOS

You can simply drag and drop the TOS image files from the `TOS Images` folder to the `ROMEMUL` volume. The files will be copied to the emulator's storage space and will be accessible for booting the Atari ST with the selected TOS image.

When dragging and dropping files from a Mac to the SidecarTridge TOS emulator, macOS creates temporary hidden files that are not supported by the SidecarTridge TOS emulator. To avoid this, it is recommended to open a Terminal window to copy the files to the SidecarTridge TOS emulator.

```bash
cp -R /path/to/TOS\ Images/* /Volumes/ROMEMUL/
```

#### Copying the TOS Images on Windows

In Windows, you can also drag and drop the TOS image files from the `TOS Images` folder to the `ROMEMUL` volume. Please follow the same guidelines as in macOS to avoid fragmentation and ensure the files are copied correctly.

#### Copying the TOS Images on Linux

In Linux, you can use the `cp` command to copy the TOS image files from the `TOS Images` folder to the `ROMEMUL` volume. Please follow the same guidelines as in macOS and Windows to avoid fragmentation and ensure the files are copied correctly.

```bash
cp -R /path/to/TOS\ Images/* /media/username/ROMEMUL/
```

**Note:** Depending on the Linux distribution, the mount point of the SidecarTridge TOS emulator may vary. Replace `/media/username/ROMEMUL/` with the correct mount point of the emulator.

### Modifying the Default and Rescue TOS Images

The SidecarTridge TOS emulator allows you to set a default active TOS image and a rescue TOS image. The *default* TOS image is the one that will boot when the Atari ST is powered on, while the *rescue* TOS image is used in case of a boot failure as a fallback option by enabling the rescue mode. You can set the `RESCUE` signal on the SidecarTridge TOS emulator using the RESCUE connector and a push button.

The *default* image can be changed by editing the `DEFAULT.TXT` file in the `ROMEMUL` volume or by using the `SWITCHER.TOS` program on the Atari ST. 

The *rescue* image can ONLY be changed by editing the `RESCUE.TXT` file in the `ROMEMUL` volume.

{: .warning}
We strongly recommend using the `SWITCHER.TOS` program to change the *default* TOS image. Change the *rescue* TOS image only when necessary, as it is a critical setting that should be used in case of boot failure. 

To change the *default* and *rescue* TOS images using the `SWITCHER.TOS` program, please refer to the [Switching Between TOS Versions](#switching-between-tos-versions) section in the User Guide.

Changing the *default* and *rescue* TOS images by editing the `DEFAULT.TXT` and `RESCUE.TXT` files is straightforward. Open the `DEFAULT.TXT` file in the `ROMEMUL` volume and replace the name of the default TOS image with the desired TOS image file name. For example, to set `TOS 2.06 - SuperTOS - 50Hz` as the default TOS image, the `DEFAULT.TXT` file should contain exactly the name of the file (including the extension if it exists):

```
TOS 2.06 - SuperTOS - 50Hz
```

{: .note }
macOS and Windows operating systems may create hidden files when copying files to the SidecarTridge TOS emulator. These hidden files are not going to damage your device or your installation, but they will not be recognized by the emulator. To avoid this, use the Terminal in macOS or the Command Prompt in Windows to copy the files.

After editing the `DEFAULT.TXT` and `RESCUE.TXT` files, save the changes and eject the `ROMEMUL` volume from your computer. When ejecting the volume, the SidecarTridge TOS emulator will automatically reindex the TOS images and update the default and rescue TOS images.

{: .warning}
As a rule of thumb, ALWAYS eject the `ROMEMUL` volume after making any changes to the files. This will ensure that the changes are correctly saved and reflected in the emulator.


## Firmware Installation

The SidecarTridge TOS emulator comes with pre-installed firmware and a default EmuTOS image. However, it is recommended to check for the latest firmware version and update if necessary. The firmware update process is straightforward and can be done using a computer with a USB port.

We assume that you have already connected the SidecarTridge TOS emulator to your computer using the USB-C cable and that the `ROMEMUL` volume is accessible. If you have not done so, please refer to the [Connecting the Device to a Computer](#connecting-the-device-to-a-computer) section.

### Obtaining the Installed Firmware Version

TODO

### Upgrading the Firmware

If there is a newer firmware version available, you can proceed with the firmware update process. Download the latest firmware version from the main page of the [SidecarTridge TOS documentation website](/sidecartridge-tos/) and store it in a temporary location on your computer.

To update the firmware, follow these steps:
1. Hold the `RESET` button on the SidecarTridge TOS ROM Board.
2. While holding the `RESET` button, hold the `BOOT` button.
3. Release the `RESET` button.
4. Release the `BOOT` button.

![SidecarTridge Firmware Update](/sidecartridge-tos/assets/images/sidecartridge-firmware-update.gif)

The SidecarTridge TOS emulator will enter the firmware update mode and appear as a USB mass storage device on your computer with the name `RPI-RP2`. Copy the firmware file to the root directory of the mass storage device and wait for the firmware update process to complete. If, after the update, the SidecarTridge TOS emulator does not reboot, press the `RESET` button for a few seconds to restart the device.

The firmware update process is now complete, and you can proceed to the next section to verify the installation.

{: .note }
The firmware update process is straightforward and will not affect the TOS images stored on the SidecarTridge TOS emulator. However, it is recommended to back up the TOS images before updating the firmware to avoid any data loss.


[Previous: Before You Buy](/sidecartridge-tos/before-buy/){: .btn .mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }
[Next: Hardware Installation](/sidecartridge-tos/hardware-installation/){: .btn }
