---
layout: default
title: User Guide
nav_order: 3
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /userguide
  - /userguide/
---

# User Guide
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ROM Emulation
{: .d-inline-block }

{{ site.FIRMWARE_VERSION }}
{: .label .label-green }

ROM Emulation is a pivotal feature of the Multi-device, enabling the Atari ST to treat ROM files from a microSD card or an external web server as native ROM chips. This guide covers how use and set up the ROM Emulation.

### Select the ROM to emulate

The Multi-device can be configured to emulate a ROM file from a microSD card or an external web server. This section explains how to select the ROM to emulate in both cases. 

1. Enter into the `Configurator` mode by pressing the `SELECT` button more than one second. Now, power cycle your computer and the `Configurator` boot menu will be displayed. Press LEFT SHIFT to enter into the `Configurator` application, or wait 5 seconds to boot the Atari ST normally, open the `Cartridge` drive and run the `SIDECART.TOS` file.

2. From the main menu, there are two options to emulate ROMS:

```
1. Emulate ROM image from microSD card
2. Emulate ROM image from Wi-Fi
```

For option 1, the Multi-device needs a microSD card with the ROM files. The user can learn how to format a microSD card and transfer ROM files in the [How to Format the microSD card](/sidecartridge-multidevice/how_to/#format_the_microsd_card) section. For option 2, the Multi-device needs to be connected to a Wi-Fi network. The user can learn how to connect the Multi-device to a Wi-Fi network in the [How to Connect to a Wi-Fi Network](/sidecartridge-multidevice/how_to/#connect_to_a_wifi_network) section.

{: .note }
The emulation of ROMs from Wi-Fi does not need a microSD card to work. And the emulation of ROMs from microSD card does not need to be connected to a Wi-Fi network to work.
{: .note }

3. In the ROM selection menu, the user can select the ROM to emulate from the list of ROMs available. Simply press `RETURN` or `ENTER` to select the ROM to emulate, and the Atari ST will load and prepare the ROM to be used. The Multi-device green led will blink an `E` in Morse code to indicate that the ROM is ready to be used.

4. Gently reset or power cycle the Atari ST to use the ROM. The Atari ST will boot normally and will use the ROM as if it was a physical chip.

### Disable ROM Emulation

Simply press again the `SELECT` button more than one second to enter into the `Configurator` mode and power cycle your computer.

### Set the folder hosting the ROM files

The Multi-device can be configured to use a folder in the microSD card to host the ROM files. This section explains how to configure the Multi-device to use a folder in the microSD card. 

1. **Preparation**: Ensure you have a microSD card formatted to FAT16 or exFAT. For instructions, visit [How to format the microSD card](/sidecartridge-multidevice/how_to/#format-the-microsd-card).
   
2. **Folder Creation**: On the root directory of the microSD card, create a folder named `roms`. This will serve as the storage for the ROM files. By default, the Multi-device will scan this directory for ROMs.

3. **ROM Transfers**: Copy your ROM files into the `roms` folder. Supported formats are:
   - Pure binary (Raw binary data of the ROM)
   - STEEM format (Recognized if the file begins with four zeros or has a `.STC` extension)

4. **Activation**:
   - Insert the microSD into the Multi-device and power it up. The board will auto-recognize the microSD.
   - Access `Configurator` mode by pressing the `SELECT` button, navigate to the ROM selection, and choose your desired ROM. The Atari ST will access this ROM as if it was a physical chip.

{: .note }
If you prefer a different folder name instead of `roms`, you can modify the `ROMS_FOLDER` parameter. Details can be found in the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section.
{: .note }


### Set the URL of the ROM files

The Multi-device can be configured to use a web server to host the ROM files. This section explains how to configure the Multi-device to use a web server.

1. **URL Configuration**: Point the Multi-device to your web server's ROM directory by setting the `ROMS_YAML_URL` parameter. The board expects a `roms.csv` file at this location. To know more about creating this file, see [Set up your own HTTP server for your ROMs](/sidecartridge-multidevice/how_to/#set-up-your-own-http-server-for-your-roms).

2. **HTTPS Limitation**:
{: .warning}
The Multi-device currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

3. **Finalizing Setup**: After updating the configuration, save your changes and reboot the board in `Configurator` mode.

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/DHQEe6xgJnc?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>

### Contribute to the Public ROM Database

The Multidevice board access a public ROM database, allowing users to download ROMs directly to the device. If you want to contribute to the database, follow the instructions in the [Public ROM Database](/sidecartridge-multidevice/publicromdb/) section.

### Enable ROM delay / Ripper mode

The Multi-device can be configured to add an extra step when accessing the ROM files. This is useful for example for ROMs tha require a post-activation after another software is loaded from a floppy or hard disk, like ripper-style ROMs did. This section explains how to configure the Multi-device to enable the ROM delay.

1. **Toggling Delay**: Access the `Configurator` application's main menu and press the `D` key to enable/disable the ROM delay.

{: .note }
Pressing the `D` key switches the `DELAY_ROM_EMULATION` parameter between `false` and `true`. While direct editing is possible, using the `D` key is advised to prevent potential issues.
{: .note}

2. **Usage**: When ROM delay is active, ROM emulation isn't immediate post-power-up. Activation occurs after holding down the `SELECT` button for over a second.

{: .important }
Given the `SELECT` button's dual function, you cannot access the `Configurator` mode using it directly. After enabling the ROM, press `SELECT` again to access the `Configurator` mode.
{: .important}

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/ov0FR23XvAY?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


## Floppies Emulation
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

The Floppies Emulation represents a significant enhancement to the Multi-device. With this, the Atari ST can interface with floppy images on a microSD card as though they were actual floppy disks. Here's how to get started with Floppies Emulation.

### Pre-requisite: Hosting Floppy Images on microSD

To use the Multi-device's floppy emulation feature, the floppy images must reside in a specific directory on a FAT16 or exFAT formatted microSD card.

1. **MicroSD Preparation**: The first requirement is a FAT16 or exFAT formatted microSD card. Instructions can be found in the [How to format the microSD card](/sidecartridge-multidevice/how_to/#format-the-microsd-card) guide.

{: .note}
If you've already set up ROM Emulation, your microSD is likely formatted appropriately, and you can bypass this step.
{: .note}

2. **Directory Structure**: On the microSD's root, create a `floppies` directory. This is where the board will scan for floppy images.

3. **Transferring Floppy Images**: Move your `.ST` and `.MSA` formatted floppy images into the `floppies` directory. The board recognizes these files automatically.

4. **Initialization and Configuration**:
   - Insert the microSD into the Multi-device.
   - Power up the board; it should recognize the microSD card automatically.
   - Enter `Configurator` mode by pressing the `SELECT` button. Navigate to `Emulate Floppy` menu option.
   - A menu will display the following options:
     - Floppy A: Image selection for drive A, or `<EMPTY>` if no image is selected.
     - Floppy B: Image selection for drive B, or `<EMPTY>` if no image is selected.
     - [E]xecute boot sector: Press `E` to enable or disable the execution of the boot sector of the floppy image. Sometimes the boot sector contains an antivirus or copy protection that can interfere with the emulation, so it's useful to disable it.
     - [X]BIOS interception: Press `X` to enable or disable the interception of the XBIOS calls to the floppy drive. Some software uses the XBIOS calls to access the floppy drive, so it's useful to disable it specially in versions of TOS 1.00 and TOS 1.02.
     - Temp [M]emory type: Press `M` to select the memory type to use for the temporary memory used by the floppy emulation.The default is `_dskbuf` that uses the buffer created by the operating system. The other option is `heap` and uses the heap memory. This is an advanced parameter and I don't recommend to change it unless you know what you are doing.
     - [W]eb manager: Press `W` to enable or disable the web manager to manage the floppy images from a web browser. This is an experimental feature and it's recommended to disable it when not in use.

5. **Selecting Floppy Images**:
    - [A] - Select the floppy image for drive A: Press `A` to choose the floppy image for drive A. It will display the list of floppy images available in the `floppies` folder. Select the desired image to emulate.
    - [B] - Select the floppy image for drive B: Press `B` to choose the floppy image for drive B. It will display the list of floppy images available in the `floppies` folder. Select the desired image to emulate.

6. **Ejecting Floppy Images**:
    - [SHIFT + A] - Eject the floppy image from drive A:
    - [SHIFT + B] - Eject the floppy image from drive B:

7. **Formatting a Floppy Image**:
    - [F] - Format a floppy image: Press `F` to format a floppy image in the drive A. This will create a new floppy image in the `floppies` folder with the `.ST` extension. The user can select the size of the floppy image to create and the volume name of the floppy. [Read the instructions below](#create-an-empty-writable-floppy-image).

8. **Start the emulation**: There are three more options:
    - [S] - Start emulation: Press `S` to start the emulation. The Atari ST will ask the user to press a key to reset the computer and start the emulation.

{: .note }
If `floppies` isn't your desired directory name, it can be changed. Adjust the `FLOPPIES_FOLDER` parameter. Details are available in the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section.
{: .note}

### Select a .ST or .MSA Floppy Image to Emulate

{: .note }
Starting from v0.0.11 the Floppy Emulation supports .MSA files.

The steps to select the floppy image to emulate are the same for both read-only and read-write modes. The Multi-device will convert the `.MSA` files to `.ST` files on the fly. 

### Read-Write Emulation for Floppy Images

The Multi-device's ability to emulate floppy images in read-write mode is powerful. It lets the Atari ST write to these images, but this also poses risks.

To mitigate potential data loss, when a floppy image is chosen for read-write emulation, the Multi-device creates a copy in the `FLOPPIES_FOLDER`. This duplicate has the `.rw` extension, and the Atari ST writes to it, leaving the original image untouched.

If a `.rw` duplicate already exists, the board will prioritize it over the original. It won't spawn another `.rw` file, ensuring consistency between sessions.

{: .warning }
It's important to note that the Multi-device won't validate the integrity of `.rw` files. If such a file is corrupted, the Atari ST won't be able to interface with it, either for reading or writing.
{: .warning}

### Create an empty writable floppy image

The Multi-device can be configured to create an empty writable floppy image to create our own content or have a blank floppy image to copy files from the Atari ST.

After selecting the option `[F] - Format a floppy image` . Select this option and the Multi-device will prompt for several parameters:

- `Size [1]-SS/DD (360KB), [2]-DS/DD (720KB), [3]-HD (1.44MB)`: Select the size of the floppy image to create.
- `Volume name (max 8 chars, dot, max 3 chars)`: The volume name of the floppy for the Atari ST computer. Can be empty.
- `Image name (max 255 chars)`: The name of the floppy image file stored in the microSD card. Cannot be empty.

Now the Multi-device will need a few seconds to create the empty floppy image. After that, the Atari ST will report to the user that the new image is ready to be used. The user can choose to start the image in read-only or read-write mode.

{: .note }
### Floppy image formats supported

The default format supported by the Multi-device is the `.ST` format. Starting from version v0.0.11, Multi-device can also read the `.MSA` format, converting it to `.ST` format on the fly. Under the covers, everything is a `.ST` file.

A special mention to read-write images with the extions `.rw`. All `.ST` files are read-only files. The Multi-device will create a copy of the `.ST` file with the `.rw` extension to emulate a writable floppy image.

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/toL0mca4ff8?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>

### Runtime emulation

After selecting the floppy images to emulate, device will start the emulation of the floppy images. The Atari ST will boot normally and will perform the following configuration process:

1. Detect there is a microSD card inserted in the board.
2. Detect the floppy images selected in the `Configurator` mode.
3. Connect to the WiFi network if the user has configured the board to connect to a WiFi network.
4. Set up and start a web server to host an application to manage the floppy images.
5. Modify the XBIOS calls to the floppy drive to intercept the calls and redirect them to the device.
6. Wait for the user to press `SPACE` key or timeout the configuration process.

Now, the computer will boot normally and the user can use the floppy images as if they were physical floppy disks. 

### Web server to manage the floppy images (EXPERIMENTAL)

If the user wants to swap the floppy images or eject them, the user will have to connect to the web server hosted by the device. The url of the web server is displayed in the screen of the Atari ST at boot time. The user can use a web browser to connect to the web server and manage the floppy images. It's possible to use a smartphone, tablet or computer to connect to the web server, the application is responsive and can be used in any device.

The user can insert and eject virtual floppy images from the Atari ST using the web server at any time, but it's recommended to eject the floppy images while they are not in use to prevent data corruption. Some applications do not like to have the floppy images ejected while they are using them, so the user can do it during the boot process of the Atari ST, or can also reset the computer after swapping the floppy images, the board will remember the floppy images selected in the `Configurator` and in the web server.


## Hard Disk Emulation
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

### Introduction

The Multi-device introduces a hard disk emulation feature for the Atari ST, offering a significant storage solution without the necessity for an actual hard disk. This guide details the setup and utilization of the Hard Disk Emulation feature.

Distinct from other methods, the Multi-device uniquely facilitates hard disk emulation by integrating the Atari ST's file system with that of a microSD card, managed by the RP2040 microcontroller. This method presents several benefits and drawbacks:

- **Advantages**:
  - Unlimited hard disk size, allowing the use of the full capacity of the microSD card.
  - Not affected by the infamous Bad-DMA issue, as the Multi-device doesn't rely on the Atari ST's DMA controller.
  - Compatibility across TOS versions 1.00 to 2.06.
  - Enables organizing files into folders on the microSD card, simulating multiple hard disks on a single card.
  - Facilitates easy file transfer between the microSD card and computers (PC/Mac/Linux).
  - Requires less or no memory compared to other emulation drivers.
  
- **Disadvantages**:
  - Writing operations to the hard disk are slower than reading due to the slower protocol communication with the RP2040 during write operations.
  - Not all software is compatible, particularly those making direct hardware calls to the hard disk, as the Multi-device emulates hard disk functions by intercepting GEMDOS calls.
  - The emulation driver is less mature, potentially leading to bugs or issues during use.

Despite these challenges, the benefits of Hard Disk Emulation often surpass the drawbacks, providing a reliable storage solution. Moreover, with ongoing development, the Multi-device is poised for further enhancements, promising an even more robust and user-friendly experience in the future.

### What is a GEMdrive

The concept for the GEMdrive hard disk emulation originated with the GEMDOS component of the Hatari emulator, though it's worth noting that there exists a GemDrive for the ACSI2STM project, which serves a different purpose. Initially, the plan was to borrow the GEMDOS implementation from Hatari and adapt it for use with the Multi-device. However, this strategy proved unfeasible due to the Hatari emulator's capability for extensive interaction with both the Atari ST's internals and the host computer—capabilities that the Multi-device, as a peripheral, cannot match due to its need to adhere to the Atari ST's hardware constraints. The GEMDOS code from Hatari was ultimately deemed too intricate and too intertwined with the emulator itself for direct application in the Multi-device environment. Nevertheless, the exploration of Hatari's GEMDOS code was highly informative, leading to the development of a bespoke GEMdrive code specifically tailored for the Multi-device.

The original GEMDOS driver allowed for the mounting of a Windows/OSX/Linux filesystem as an Atari ST disk drive, a functionality mirrored by the GEMdrive through its use of the microSD card filesystem, FatFS. While some advanced users may view this solution as excessive, it represents the sole method by which to provide substantial storage capacity to the Atari ST. More significantly, it marks a crucial **initial step towards realizing a network filesystem for the Atari ST.**

### Setting Up Hard Disk Emulation

To activate the hard disk emulation feature on the Multi-device, you must first ensure that the emulation files are properly placed within a designated directory on a FAT16 or exFAT formatted microSD card. While `hd` is the default directory name for these files, it can be customized to suit your preferences.

1. **MicroSD Card Setup**: Skip this step if your microSD card is already set up with ROMs and/or floppy images. Otherwise, start by formatting the microSD card to FAT16 or exFAT. Detailed formatting instructions are available in the [microSD Card Formatting Guide](/sidecartridge-multidevice/how_to/#format-the-microsd-card).

2. **Creating the Directory**: In the root directory of the microSD card, create a folder named `hd`. This folder will be scanned by the board to locate your emulated hard disk files.

3. **File Transfer**: Transfer files and folders from your PC/Mac/Linux computer to the `hd` folder on the microSD card. These will be recognized by the Multi-device as part of the emulated hard disk. Additionally, you can manage file transfers between the emulated hard disk and other hard disk drivers.

4. **Initialization and Setup**:
   - Insert the prepared microSD card into the Multi-device.
   - Turn on the board. It will automatically detect the microSD card.
   - Access the `Configurator` by pressing the `SELECT` button and navigate to the `Emulate Hard Disk` option.
   - Within this menu, you will find several settings:
     - [D]rive: Hit `D` to choose the drive letter for emulation, ranging from `C` to `Z`. Select a unique letter if using multiple hard disk drivers.
     - Temp [M]emory Type: Press `M` to pick the type of temporary memory for emulation. The default `_dskbuf` utilizes the operating system's buffer, while `heap` opts for heap memory. This setting is advanced and should only be altered with caution.
     - [R]TC Enabled: Toggle the Real Time Clock (RTC) by pressing `R`. Enabling RTC ensures accurate date and time for files and the Atari ST computer.
     - [Y]2K Patch: Press `Y` to activate the Year 2000 (Y2K) patch. This feature is crucial for ensuring the correct date and time display on the Atari ST if you don't use a program that patches the Y2K bug. This feature is only available for TOS versions 1.00 to 2.06, EmuTOS is not affected by the Y2K bug.
     - [F]ake floppy: Press `F` to enable or disable the fake floppy feature. This feature is useful for software that requires a floppy drive to be present, like the detection of AUTO folder programs or by passing the annoying 2.06 TOS floppy disk check on boot.
     - Network [T]imeout: Set the wait time for network and NTP server synchronization, with a default of 45 seconds.
5. **Starting the Emulation**:
   - Additional options include:
     - [S] - Start Emulation: Press `S` to commence hard disk emulation using the chosen drive letter.

> **Note:** If you prefer a directory name other than `hd`, you can modify the `GEMDRIVE_DRIVE` parameter in the configuration settings. For more information, refer to the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section.

### Features not supported and known issues

{: .warning }
If you can't enter into Configurator, please [read this](https://docs.sidecartridge.com/sidecartridge-multidevice/troubleshooting/#configurator-takes-very-long-to-start-and-stops-responding-or-ask-me-to-reboot-the-computer-or-show-bombs-on-the-screen)

The Multi-device's hard disk emulation feature does not support the following functionalities in version v0.0.16 and v0.0.17:

- **Volume Name**: It does not support volume names for the hard disk emulation. The Atari ST will not display the volume name of the hard disk.
- **Pipes**: The current version does not support pipes. The Atari ST will not be able to use pipes with the hard disk emulation.

All the features are planned for future releases.

The lastest adapted games for hard disk does support the GEMdrive emulation. Most of the games with HAGA and HAGE support does work with the GEMdrive emulation with TOS ranging from 1.00 to 2.06 and 1MB of RAM. 

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/QDGnY_9nJnQ?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>

## Atari ST database of floppy images
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

The Multi-device can read a database of floppy images hosted on a remote web server. This feature is built on top of the Floppies Emulation one. This is an out of the box feature that doesn't require any additional configuration besides the one explained above for the Floppies Emulation. 

### How to download and emulate a floppy image from the database

This section explains how to select the floppy image to emulate from the database:

1. Enter into the `Configurator` mode by pressing the `SELECT` button more than one second. Now, power cycle your computer and the `Configurator` boot menu will be displayed. Press LEFT SHIFT to enter into the `Configurator` application, or wait 5 seconds to boot the Atari ST normally, open the `Cartridge` drive and run the `SIDECART.TOS` file.

2. From the main menu, select the option

```
5. Download from the Floppy Images database
```

3. In the menu, there is a bar with the underscore, alphabet and numbers. Selecting the letter or number will display the list of applications starting with that letter in the name. Selecting the underscore will display the latest applications added to the database, from the newest to the oldest, which is useful to find the latest applications added to the database.

4. The user can now select the application to download pressing `RETURN` or `ENTER`. Now, the Multi-device will find the floppy image in the database that contains the application and download it to the storage folder for floppy images.

5. After the download is finished, the Atari ST will redirect the user to the Floppy Emulation menu to select how to use the floppy image.

4. From the menu the user can reset the computer. The Atari ST will boot normally and will use the floppy image as if it was a physical floppy disk.

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/Cee2fCGCBvI?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


### Set the URL of the database and images files

{: .warning }
For avanced users only.

The Multi-device can be configured to use a web server to host both the database and images files. It's not necessary to have both in the same server. 

1. **URL Configuration**: Point the Multi-device to your web server's Atari ST database by setting the `FLOPPY_DB_URL` parameter. The board expects a folder named `db` and a file for each alphabet letter and number. Each of these files in Comma Separated Values (CSV) format contains the list of disk files urls. See [Set up your own HTTP server for your Atari ST database](/sidecartridge-multidevice/how_to/#set-up-your-own-http-server-for-your-atari-st-database).

2. **HTTPS Limitation**:
{: .warning}
The Multi-device currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

3. **Finalizing Setup**: After updating the configuration, save your changes and reboot the board in `Configurator` mode.


## Real Time Clock (RTC)
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

Starting from the version v0.0.11 of the firmware, the Multi-device can be configured to be a Real Time Clock (RTC) for the Atari ST. This section explains how to configure the Multi-device to be a RTC.

### Enter into the RTC configuration menu

The menu to configure the RTC is available in the `Configurator` application. To access it, press the `6` option in the main menu. The following menu will be displayed:

```
NTP Server: <<value in the RTC_NTP_SERVER_HOST and RTC_NTP_SERVER_PORT configuration parameter>>
RTC Type: <<value in the RTC_TYPE configuration parameter>>
RTC UTC Offset: <<value inthe RTC_UTC_OFFSET>>

Options:
[1] - Set SIDECART RTC with a custom firmware
[2] - Set DALLAS 1216 RTC with cartridge emulation
[U] - Change UTC offset
[H] - Change NTP server host
[P] - Change NTP server port
[Y] - Toogle Y2K patch

[B] - Boot emulator

Press an option key or [ESC] to exit:
```

### Set the NTP parameters

The user can change the NTP server host and port by pressing the `H` and `P` keys respectively. The default values are `pool.ntp.org` for the host and `123` for the port, which are the most common values and should work for most users.

### Set the UTC offset

The user can change the UTC offset by pressing the `U` key. The default value is `0`, which means the UTC offset is null. The NTP time returned by any server does not know about timezones, so the Multi-device needs to know the UTC offset to be able to convert the UTC time to the local time. The UTC offset is expressed in positive or negative hours.

Also note that the Atari ST does not know about timezones either, so the RTC time will be the local time of the Atari ST.

### Change the RTC type

For the version v0.0.11, there are two RTC types available: `SIDECART` and `DALLAS`. The user can change the RTC type by pressing the `1` or `2` keys. The default value is `SIDECART`. Each type has different characteristics:

- `SIDECART`: This is the default RTC type. To set the date and time it uses a small cartridge firmware at boot time that sets the date and time in the Atari ST computer. This firmware is executed at boot time as an executable cartridge and does not impact in the overall performance or memory usage of the system.

- `DALLAS`: This RTC type emulates a DALLAS 1216 RTC integrated chip. To set the date and time the user must use a program that reads the values provided by the DALLAS 1216 emulator and sets the date and time in the Atari ST computer. There are several programs that can do this, but I strongly recommend the [tools created by Troed Sångberg](https://blog.troed.se/projects/dallas-rtc-sync-tos-y2k-fix/).

### Toogle the Y2K patch

This feature is crucial for ensuring the correct date and time display on the Atari ST if you don't use a program that patches the Y2K bug. This feature is only available for TOS versions 1.00 to 2.06, EmuTOS is not affected by the Y2K bug.


{: .note}
Both solutions workaround the Y2K problem, or any problem with dates this century. So far.
{: .note}

### Boot the emulator

To Boot the emulator, press the `B` key. The Multi-device will reboot and depending on the RTC type chosen the flow will differ:

- `SIDECART`: The Multi-device will boot the cartridge firmware that will set the date and time in the Atari ST computer. After that, the Atari ST will boot normally. The firmware will report how the process goes in the screen. This is important because the RP2040 must query the NTP server to get the time and set it in the Atari ST computer, and this can take several seconds. The Atari ST will not boot until the date and time are set, or fails. 

- `DALLAS`: The Atari ST will boot normally. As explained above, the user must use a program that reads the values provided by the DALLAS 1216 emulator and sets the date and time in the Atari ST computer. Please keep in mind that DALLAS RTC emulation will only provide a valid date and time once the RP2040 obtains a valid date and time from the NTP server.

{: .warning}
The Multi-device will not return a valid date and time until it obtains a valid date and time from the NTP server. In the SIDECART RTC type, the Atari ST will not boot until the date and time are set, or fails. In the DALLAS RTC type, the Atari ST will boot normally, but the date and time will be invalid until the user sets them with a program.
{: .warning}

## Boot a ROM image from the microSD card in 'Rescue Mode'
{: .d-inline-block }

{{ site.FIRMWARE_VERSION }}
{: .label .label-green }

The Multi-device can be a very helpful device to troubleshoot damaged computers. A good use case is bypass the configurator and let the Multi-device to run a "default ROM" when plugged. This new feature is called "Rescue Mode", and it will boot a ROM image from the microSD card when the Multi-device is plugged in the Atari ST without interacting with the configurator.

### How to enable the Rescue Mode
To enable the Rescue Mode, the user must create a file named `.romrescue` in the root of the microSD card. The content of the file must be the name of the ROM image to boot as found in the `ROMS_FOLDER` (`roms` by default) configuration parameter. It's important to note that the user does not have to include the full path, just the name of the ROM image.

For example, if the user wants to boot a diagnostic ROM image named `ST Test v4.4.img` located in the `roms` folder, the content of the `.romrescue` file must be `ST Test v4.4.img`.

### First boot after enabling the Rescue Mode
After saving the `.romrescue` file in the microSD card, insert the microSD card in the Multi-device and power on the Atari ST. Now, press the `SELECT` button more than one second to enter into the `Configurator` mode. Now the Multi-device will automatically read the `.romrescue` file and will save its content in the FLASH memory of the RP2040. 

### Next boots
After that, the Multi-device will reboot in `ROM_EMULATION` mode and the Atari ST will boot the ROM image specified. 

### How to disable the Rescue Mode
To disable the Rescue Mode, the user must delete the `.romrescue` file from the microSD card, or rename it. After that, if the user press the `SELECT` button for more than one second, the Multi-device will start in the `Configurator` mode as usual.


## Configurator Application
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

The Configurator application serves as the central interface for the Multi-device's configurations. It's alternately known as the `firmware` or the `firmware application`. This guide will walk you through the nuances of the Configurator application.

### Boot Mode Adjustments

Upon the initial power-up of the Multi-device, or when the `SELECT` button is held for over 1 second, the Configurator is invoked. This application resides in the `Cartridge` drive, which is visible upon starting the Atari ST.

The behavior when pressing `SELECT` for over 1 second is configurable. The Multi-device can either:

1. Swiftly transition to the `Configurator` mode, or
2. Delay this transition until the Atari ST's next full power cycle (not just a reset).

This behavior is determined by the `SAFE_CONFIG_REBOOT` parameter.

Immediately transitioning can be jarring for ongoing Atari ST applications. Especially for applications or drivers overseeing other storage devices, this abrupt switch can lead to compatibility concerns. As a preventive measure, the Multi-device can be set to defer this transition until the subsequent power cycle.

By default, `SAFE_CONFIG_REBOOT` is set to `true`. This means the Multi-device will hold off until the next power cycle before transitioning to `Configurator` mode. Altering this behavior involves tweaking the `SAFE_CONFIG_REBOOT` parameter. Further insights can be found in the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section.

{: .note}
There are valid scenarios where setting `SAFE_CONFIG_REBOOT` to `false` makes sense. For instance, developers frequently adjusting the Multi-device configuration might find repeatedly waiting for a power cycle tedious. However, exercise this option judiciously.
{: .note}

### Count the number files in the folders of the microSD card

The Multi-device can be configured to count the number of files in the folders of the microSD card. This feature is useful to know how many ROMs or floppy images and files in the hard disk folders are available. This feature is configured by default, but the user can disable it if the number of files is too big and the Multi-device is slow to boot.

To disable this feature, the user must set the `FILE_COUNT_ENABLED` parameter to `false`. The user can learn more about this parameter in the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section. To return to the default behavior, the user must set the `FILE_COUNT_ENABLED` parameter to `true`.

### Dark mode

The Multi-device can be configured to use a dark mode in the Configurator application for medium resolution mode. This feature is useful for old CRT monitors that can have problems with the white background of the Configurator application. By default the dark mode is disabled, but the user can enable it by setting the `CONFIGURATOR_DARK` parameter to `true`. The user can learn more about this parameter in the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section. To return to the default behavior, the user must set the `CONFIGURATOR_DARK` parameter to `false`.

### Latest release verification

The Multi-device can be configured to check for the latest release of the firmware available. When the board is connected to the internet, it will check for the latest release and display a blinking exclamation mark at the right side of the current version number at the top bar of the Configurator application. This section explains how to configure the Multi-device to check for the latest release.

{: .note}
You have to be connected to the internet to check for the latest release.
{: .note}

1. **URL Configuration**: The parameter `LATEST_RELEASE_URL` has to point to a file hosted on a web server. This file has to contain the latest release version number in the first line. The Multi-device will check this file and compare the version number with the current version number. If the version number is different, the Multi-device will display a blinking exclamation mark as explained above.

2. **HTTPS Limitation**:
{: .warning}
The Multi-device currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

### The STABLE and BETA release distribution workflows

The Multi-device Latest release verification can be configured to check for new releases of type STABLE or BETA. With the growing user base of Multi-device, the need for extensive and stability-focused testing is becoming increasingly important. To address this, we propose introducing two distinct release workflows. This approach aims to balance the needs of our diverse user community, ranging from makers to those seeking more stable and reliable software.

1. **BETA Release Workflow**: This caters to users who are interested in testing the latest features and providing valuable feedback. It allows us to incorporate user experiences into development, ensuring that the software meets a wide range of needs and use cases.

2. **STABLE Release Workflow**: Aimed at users who prioritize stability and reliability. This workflow focuses on delivering a polished and thoroughly tested version of the software, thereby reducing support queries and enhancing user satisfaction.

This is controlled through the `LATEST_RELEASE_URL` parameter in the configuration.

If `LATEST_RELEASE_URL` points to `http://atarist./version.txt`, users will be notified about the availability of a new STABLE (or latest) release.

If `LATEST_RELEASE_URL` points to `http://atarist./beta.txt`, users will be alerted when a new BETA release is available.

In both cases, the Multi-device will check for the latest release and display a blinking exclamation mark at the right side of the current version number at the top bar of the Configurator application. 

To download the STABLE (latest) or BETA release, navigate to the [Download page](https://sidecartridge.com/downloads/) and download the appropriate file. Then, follow the [Update the firmware](/sidecartridge-multidevice/how_to/#update-the-firmware) guide.

## Mass Storage Mode
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

As of Beta release v0.0.17, the SidecarTridge multidevice board introduces the Mass Storage Mode feature, enabling users to access the microSD card as a mass storage device when connected to a computer via USB. This mode facilitates seamless file transfers between the microSD card and the computer, enhancing the SidecarTridge's versatility and user experience.

One of the most annoying things when using the SidecarTridge board is the need to remove the microSD card from the device and use a standard card reader to transfer files. The Mass Storage Mode eliminates this inconvenience, allowing users to access the microSD card directly from their computer, streamlining the file management process.

### Enabling Mass Storage Mode

The Mass Storage Mode can only be enabled when the SidecarTridge board, with a microSD card inserted in its microSD card reader, is connected to a computer via USB and the SidecarTridge board is also in `Configurator` mode. The USB port provides both communication with the computer and power to the SidecarTridge board. When properly connected, the small green LED on the Raspberry Pi Pico W/WH will stay on steadily. Wait a few seconds for the computer to recognize the SidecarTridge board as a mass storage device, and you're ready to go. 

{: .note}
The mass storage device is not very fast compared to a standard card reader or a USB stick. So if it looks slow, it's normal.
{: .note}

### Preparing the microSD card for the first time

The first time the user enables the Mass Storage Mode, the microSD card should be formatted to FAT16 or exFAT. This is a one-time operation and the user doesn't need to format the microSD card every time the Mass Storage Mode is enabled. Please see the the chapter [Format the microSD card](/sidecartridge-multidevice/how_to/#format-the-microsd-card) for more information.

{:refdef: style="text-align: center;"}
![SidecarTridge multi-device Mass Storage Mode](/sidecartridge-multidevice/assets/images/mass-storage.gif)
{: refdef}

Also, the user should create the default folders and configurations files in the microSD card:

- `roms` folder: This folder should contain the ROM images to be used by the SidecarTridge board. 
- `floppies` folder: This folder should contain the floppy images to be used by the SidecarTridge board. The floppy images should be in the `.ST`  and `.MSA` format.
- `hd` folder: This folder should contain the files to be used by the SidecarTridge board as a hard disk. 

Also the user can configure the default password in the[.wifipass](/sidecartridge-multidevice/how_to/#configure-the-wifi-password-in-a-file-in-the-microsd-card) file, or the default bootable ROM in the [.romrescue](/sidecartridge-multidevice/how_to/#boot-a-rom-image-from-the-microsd-card-in-rescue-mode) file.

### Disabling Mass Storage Mode

Simply do not power the SidecarTridge board from the USB port. If the power is not coming from the USB port, the SidecarTridge board will boot normally in your Atari ST computer.

### Fully disabling the Mass Storage Mode

If the user wants to fully disable the Mass Storage Mode, the user should set the `SD_MASS_STORAGE` parameter to `false`. The user can learn more about this parameter in the [Configuration Parameters](/sidecartridge-multidevice/parameters/) section. To return to the default behavior, the user must set the `MASS_STORAGE_ENABLED` parameter to `true`.

When the Mass Storage Mode is disabled, the SidecarTridge board will not enter in the Mass Storage Mode when connected to a computer via USB.

## Enhanced Network Configuration
{: .d-inline-block }

{{ site.FIRMWARE_BETA_VERSION }}
{: .label .label-purple }

As of Beta release v0.0.15, the Multi-device introduces the capability to adjust a range of network settings, designed to aid in diagnosing and resolving Wi-Fi and other network-related challenges. These settings are accessible through the **[C. Multi-device Configuration](/sidecartridge-multidevice/parameters/)** menu.

### Viewing Network Status

To get an overview of the current network configuration and status, navigate to the **W. Wi-Fi Configuration** menu. Here, you will find detailed information that is essential for identifying and addressing network issues:

- **SSID:** The name of the Wi-Fi network (SSID), which can be set using the `WIFI_SSID` parameter.
- **Auth Mode:** Specifies the authentication mode used by the Wi-Fi network, adjustable via the `WIFI_AUTH` parameter.
- **Scan Interval:** Defines the duration, in seconds, between consecutive Wi-Fi network scans. This setting helps in refreshing the network list periodically, based on the `WIFI_SCAN_SECONDS` parameter.
- **Country:** Sets the country code for the Wi-Fi network. Initially configured to a default value that accommodates a broad range of networks globally, it may need adjustment to match the ISO-3166-alpha-2 code of your specific country for optimal performance. This is modifiable through the `WIFI_COUNTRY` parameter.
- **Status:** Provides real-time insights into the connection's current state.
- **IP Address:** Displays the Multi-device's IP address within the Wi-Fi network.
- **Gateway:** Shows the gateway's IP address for the Wi-Fi network.
- **Netmask:** Indicates the network's subnet mask.
- **DNS Server:** Reveals the DNS server's IP address used by the Wi-Fi network.
- **MAC Address:** Lists the MAC address of the Multi-device within the network.
- **Check Interval:** The frequency, in seconds, at which the Multi-device reviews the network's status, controlled by the `NETWORK_STATUS_SEC` parameter.
- **File Download Timeout:** The maximum wait time, in seconds, for downloading a file over the Wi-Fi network, set using the `DOWNLOAD_TIMEOUT_SEC` parameter.

These configurable options empower users to fine-tune their network settings, facilitating improved connectivity and troubleshooting capabilities.

### Adjusting the authentication mode

#### Configuring Authentication Mode

The Multi-device employs a smart mechanism to determine the Wi-Fi network's authentication mode, enhancing the ease of connectivity. This section guides you through adjusting the authentication settings to ensure a successful network connection.

#### Default Authentication Behavior

Upon attempting to connect to a Wi-Fi network, the Multi-device initially endeavors to intelligently ascertain the network's authentication mode under the following conditions:

- If the `WIFI_PASSWORD` parameter is populated (i.e., the string length is greater than 0) or if a `.wifipass` file is present at the root of the microSD card, the board attempts to automatically identify the correct authentication mode for the specified SSID.

- Conversely, if the `WIFI_PASSWORD` parameter is left blank and there is no `.wifipass` file found, the board defaults to using the `OPEN` authentication mode. This mode is denoted by the value `0` in the `WIFI_AUTH` parameter, indicating no encryption or password protection.

#### Manual Configuration of Authentication Mode

There may be instances where automatic detection does not yield the correct authentication mode, or you might prefer to specify a particular mode for your network connection. For such scenarios, you can manually set the `WIFI_AUTH` parameter to one of the predefined values to enforce a specific authentication protocol:

- `0`: OPEN (no encryption)
- `1`, `2`: WPA TKIP PSK (Temporal Key Integrity Protocol with Pre-Shared Key)
- `3`, `4`, `5`: WPA2 AES PSK (Wi-Fi Protected Access II with Advanced Encryption Standard and Pre-Shared Key)
- `6`, `7`, `8`: WPA/WPA2 MIXED PSK (Mixed mode supporting both WPA and WPA2 standards)

#### Troubleshooting Connectivity Issues

Should you encounter difficulties in establishing a connection or receiving a valid IP address from the DHCP server, it is recommended to experiment with the different `WIFI_AUTH` values. Switching between authentication modes can help identify a compatible setting that facilitates a successful connection to the network.

By understanding and leveraging the `WIFI_AUTH` parameter, you can fine-tune the Multi-device's network authentication to match the security requirements of your Wi-Fi network, ensuring a stable and secure connection.

### Configuring the Country Code for Wi-Fi

The Multi-device facilitates precise control over Wi-Fi connectivity through the `WIFI_COUNTRY` parameter. This setting allows users to define the country code corresponding to their Wi-Fi network, optimizing performance by aligning with local network regulations and bands.

#### Default Configuration

By default, the `WIFI_COUNTRY` parameter is preset to `XX`, activating a *Worldwide* mode. This mode is designed to ensure broad compatibility across global networks. Nonetheless, for enhanced connectivity and to leverage region-specific network optimizations, adjusting this parameter to reflect your location's ISO-3166-alpha-2 code is advisable.

#### How to Set Your Country Code

To tailor the `WIFI_COUNTRY` parameter to your locale, reference the ISO-3166-alpha-2 code corresponding to your country. Below is a markdown-formatted list of countries with their respective codes:

- Argentina: `AR`
- Australia: `AU`
- Austria: `AT`
- Belgium: `BE`
- Brazil: `BR`
- Canada: `CA`
- Chile: `CL`
- China: `CN`
- Colombia: `CO`
- Czech Republic: `CZ`
- Denmark: `DK`
- Estonia: `EE`
- Finland: `FI`
- France: `FR`
- Germany: `DE`
- Greece: `GR`
- Hong Kong: `HK`
- Hungary: `HU`
- Iceland: `IS`
- India: `IN`
- Israel: `IL`
- Italy: `IT`
- Japan: `JP`
- Kenya: `KE`
- Latvia: `LV`
- Liechtenstein: `LI`
- Lithuania: `LT`
- Luxembourg: `LU`
- Malaysia: `MY`
- Malta: `MT`
- Mexico: `MX`
- Netherlands: `NL`
- New Zealand: `NZ`
- Nigeria: `NG`
- Norway: `NO`
- Peru: `PE`
- Philippines: `PH`
- Poland: `PL`
- Portugal: `PT`
- Singapore: `SG`
- Slovakia: `SK`
- Slovenia: `SI`
- South Africa: `ZA`
- South Korea: `KR`
- Spain: `ES`
- Sweden: `SE`
- Switzerland: `CH`
- Taiwan: `TW`
- Thailand: `TH`
- Turkey: `TR`
- United Kingdom: `GB`
- United States: `US`
- Worldwide: `XX`

Note: If your country is not listed, the `Worldwide` mode (`XX`) is recommended to ensure compatibility across various global networks.

#### Troubleshooting and Performance Optimization

Experimenting with different `WIFI_COUNTRY` settings may be necessary to resolve connectivity issues or optimize network performance. Although setting the `WIFI_COUNTRY` parameter to your country's ISO-3166-alpha-2 code is generally recommended, varying this setting could yield improvements in connection stability, speed, or latency. Adjusting the country code offers a strategic approach to fine-tuning Wi-Fi performance for your specific environment.

### Troubleshooting Wi-Fi Network Detection

Detecting Wi-Fi networks with the Multi-device can sometimes be challenging due to various external factors such as environmental conditions, network congestion, and signal interference. If you're experiencing issues with finding your Wi-Fi network, adjusting the `WIFI_SCAN_SECONDS` parameter may improve the situation.

#### Adjusting Scan Frequency

The `WIFI_SCAN_SECONDS` parameter controls how often the Multi-device scans for available Wi-Fi networks. Decreasing this value causes the board to search for networks more frequently, which might increase the chances of successfully detecting your Wi-Fi network.

#### Considerations

While lowering the `WIFI_SCAN_SECONDS` value can aid in detecting Wi-Fi networks more readily, it's important to be mindful of potential drawbacks:

- **Resource Consumption:** More frequent scanning consumes additional computational resources. This heightened activity can impact the performance of the Configurator application, potentially leading to a less responsive user experience.

#### Power management configuration

Starting in version v1.0.0, it can be modified to adjust the power management configuration of the Wi-Fi module. The `WIFI_POWER` parameter can be set to the following values:

0 - power management disabled 
1 - Maximize performance 
2 - Aggresive power management 
3 - Default chip values 
4 - No power saving

The default configuration of the CYW43 module is 3, but the default configuration has been change to no power management since the Atari computer can deliver enough power to the Multi-device. Try different values to see if the Wi-Fi module can connect to the network faster or get better RSSI values.

#### Display RSSI values

Starting in version v1.0.0, the Multi-device can display the RSSI values of the Wi-Fi networks. The RSSI values are displayed in the `W. Wi-Fi Configuration` menu when scanning for Wi-Fi networks. The RSSI values are displayed in dBm and can be used to determine the signal strength of the Wi-Fi networks. The RSSI values are displayed in the `RSSI` column. It's also possible to display the current RSSI value of the connected Wi-Fi network if the parameter `WIFI_RSSI` is set to `true`. By default, the `WIFI_RSSI` parameter is set to `false` because it can slow down the user interface.

As a reference, the following table provides a general overview of RSSI values and their corresponding signal strengths:

| **RSSI Value (dBm)**  | **Signal Strength**        | **Probability of Good Connectivity**          |
|-----------------------|----------------------------|-----------------------------------------------|
| -30 dBm to -50 dBm    | Excellent                  | Very high, fast, and reliable connection.     |
| -51 dBm to -60 dBm    | Good                       | High, stable connection with good speed.      |
| -61 dBm to -70 dBm    | Fair                       | Moderate, generally reliable but slower.      |
| -71 dBm to -80 dBm    | Weak                       | Low, possible connection issues or dropouts.  |
| -81 dBm to -90 dBm    | Poor                       | Very low, frequent dropouts, slow speeds.     |
| -91 dBm and below     | Unusable                   | Extremely low, likely no connection at all.   |


Below -80 dBm, the signal strength is considered weak, potentially leading to connectivity issues. By monitoring the RSSI values, you can identify networks with stronger signals, enabling you to connect to more reliable Wi-Fi networks.

A network below -85db is considered too weak to connect to.

#### Finding the Right Balance

Finding the optimal setting for `WIFI_SCAN_SECONDS` involves balancing the need for effective network detection with maintaining good system performance. 

### Diagnosing Network Detection and Connectivity Issues

Ensuring seamless network detection and connection is critical for the optimal operation of the Multi-device. This process involves establishing a Wi-Fi connection followed by acquiring an IP address from the DHCP server. Understanding and managing these steps can significantly enhance your network interaction experience.

#### Initial Connection and IP Address Acquisition

Once a Wi-Fi connection is successfully established, the Multi-device seeks to obtain an IP address from the DHCP server. A failure to secure a valid IP address results in the absence of displayed network details, indicating an incomplete connection.

If the signal strength is weak or the network is congested, the board may struggle to connect to the Wi-Fi network and acquire an IP address. In such cases, adjusting the `WIFI_CONNECT_TIMEOUT` parameter to a lower value can help improve the connectivity because the device will retry to connect to the network faster, but a failure to connect to the network is probably caused by a weak signal.

The IP address acquisition process can be slow due to network latency or DHCP server issues. The device will wait for a valid IP address for the time specified in the `WIFI_CONNECT_TIMEOUT` parameter. If the device doesn't get a valid IP address in this time, it will retry to connect to the network. 

If you suspect network latency or DHCP server delays are hindering the IP address acquisition process, consider disabling the network configuration acquisition from the DHCP server by setting the `WIFI_DHCP` parameter to `false`. This will allow you to manually set the IP address, gateway, and DNS server values, potentially expediting the connection process. To setup the IP address, gateway, and DNS server values, use the `WIFI_IP`, `WIFI_GATEWAY`, `WIFI_NETMASK` and `WIFI_DNS` parameters respectively and reboot the device after setting the values.

#### Monitoring Network Status

The frequency at which the Multi-device checks the network status is determined by the `NETWORK_STATUS_SEC` parameter. This check occurs periodically:

- **Without a Valid IP Address:** If the board hasn't received a valid IP from the DHCP server, it performs status checks every `NETWORK_STATUS_SEC` seconds to attempt to resolve this issue.
- **With a Valid IP Address:** Once a valid IP is obtained, the board continues to monitor the network at the same interval, ensuring the connection remains active.

Certain DHCP servers may exhibit delays in IP allocation. To counteract potential wait times, you might consider reducing the `NETWORK_STATUS_SEC` value, potentially to as low as 3 seconds, to prompt more frequent attempts at acquiring an IP address.

#### Adjusting the `NETWORK_STATUS_SEC` Parameter

Modifying the `NETWORK_STATUS_SEC` parameter to a lower figure can lead to increased CPU usage and additional network traffic, as the board will more aggressively seek to establish or maintain its network connection. It's advisable to approach adjustments to this parameter with caution. The default setting of 10 seconds is generally sufficient for obtaining a valid IP address in most scenarios without unduly taxing system resources.

#### Finding the Optimal Balance

Adjusting network settings on the Multi-device, especially the `NETWORK_STATUS_SEC` parameter, requires a careful balance between ensuring quick network connectivity and maintaining overall system performance. Experimenting with different settings can help identify the most effective configuration for your specific network environment and usage requirements.

### Managing MAC Address Restrictions

The MAC address serves as a fixed, unique identifier for the Multi-device's network interface, essential for communication within the physical network segment. It's important to note that the MAC address of the Multi-device cannot be altered.

#### Understanding MAC Address Filtering

Many networks implement MAC address filtering as a security measure, controlling access by explicitly permitting or blocking devices based on their MAC addresses. This approach ensures only recognized devices can connect to the network.

#### Integrating the Multi-device with MAC Address Filtering

Should your network employ MAC address filtering, you must register the Multi-device's MAC address with your router to grant it network access. You can find the MAC address listed within the `W. Wi-Fi Configuration` menu of the Multi-device.

#### Steps to Add the Multi-device MAC Address to Your Router

1. Access the `W. Wi-Fi Configuration` menu on your Multi-device to locate its MAC address.
2. Log into your router's administration interface. This typically involves entering the router's IP address in a web browser and signing in with your credentials.
3. Navigate to the MAC address filtering section. The exact location of this setting can vary depending on your router's brand and firmware.
4. Enter the Multi-device's MAC address into the list of allowed devices. You may need to select an option to "Add" or "Allow" a new device.
5. Save your changes and, if necessary, restart the router for the new settings to take effect.

By ensuring the Multi-device's MAC address is recognized and permitted by your network's filtering rules, you'll facilitate a smooth connection process, allowing the board to communicate effectively with other devices on the network.

### Adjusting the File Download Timeout Setting

The `DOWNLOAD_TIMEOUT_SEC` parameter on the Multi-device plays a critical role in defining the time limit for file downloads over the Wi-Fi network. This setting is crucial for efficiently managing the retrieval of ROM and floppy images, ensuring that these resources are accessed in a timely manner.

#### Understanding the Default Timeout Duration

Initially, the default timeout was set at 30 seconds. Based on user feedback concerning download times, this has been extended to 60 seconds. This adjustment aims to offer a more accommodating window for file downloads, catering to varying network speeds and file sizes.

#### Evaluating and Customizing the Timeout

Given that the files targeted for download typically do not exceed 1MB, the default 60-second timeout should suffice for the majority of use cases. Nonetheless, the primary bottleneck in the download process is not the file size but rather the latency involved in establishing a connection to the server, initiating the download, and processing each segment of the file. The RP2040 microcontroller, with its limited memory and computational capabilities, processes downloads more slowly compared to standard computers, making latency a more significant factor than bandwidth.

#### When to Modify the `DOWNLOAD_TIMEOUT_SEC` Parameter

- **Increasing the Timeout:** If you experience difficulties in completing downloads within the 60-second window, it may be necessary to extend the `DOWNLOAD_TIMEOUT_SEC` duration. This adjustment can accommodate slower server response times or any network latency issues, ensuring that downloads can complete successfully.
  
- **Decreasing the Timeout:** Conversely, if downloads are consistently finishing well before the 60-second mark, you might consider reducing the timeout setting. This can streamline the network interaction process, preventing unnecessary delays in cases where downloads are completed more swiftly.

Adjusting the `DOWNLOAD_TIMEOUT_SEC` parameter allows you to tailor the download experience to your specific network conditions and the performance of the Multi-device. Experimenting with different settings can help identify the optimal timeout duration for your setup, balancing efficiency with reliability in file retrieval operations.

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/BStDWGTrfuw?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>
