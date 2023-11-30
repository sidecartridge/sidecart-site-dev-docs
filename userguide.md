---
layout: default
title: User Guide
nav_order: 3
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

ROM Emulation is a pivotal feature of the SidecarT board, enabling the Atari ST to treat ROM files from a microSD card or an external web server as native ROM chips. This guide covers how use and set up the ROM Emulation.

### Select the ROM to emulate

The SidecarT board can be configured to emulate a ROM file from a microSD card or an external web server. This section explains how to select the ROM to emulate in both cases. 

1. Enter into the `Configurator` mode by pressing the `SELECT` button more than one second. Now, power cycle your computer and the `Configurator` boot menu will be displayed. Press LEFT SHIFT to enter into the `Configurator` application, or wait 5 seconds to boot the Atari ST normally, open the `Cartridge` drive and run the `SIDECART.TOS` file.

2. From the main menu, there are two options to emulate ROMS:

```
1. Emulate ROM image from microSD card
2. Emulate ROM image from Wi-Fi
```

For option 1, the SidecarT board needs a microSD card with the ROM files. The user can learn how to format a microSD card and transfer ROM files in the [How to Format the microSD card](/how_to#format_the_microsd_card) section. For option 2, the SidecarT board needs to be connected to a Wi-Fi network. The user can learn how to connect the SidecarT board to a Wi-Fi network in the [How to Connect to a Wi-Fi Network](/how_to#connect_to_a_wifi_network) section.

{: .note }
The emulation of ROMs from Wi-Fi does not need a microSD card to work. And the emulation of ROMs from microSD card does not need to be connected to a Wi-Fi network to work.
{: .note }

3. In the ROM selection menu, the user can select the ROM to emulate from the list of ROMs available. Simply press `RETURN` or `ENTER` to select the ROM to emulate, and the Atari ST will load and prepare the ROM to be used. The SidecarT board green led will blink an `E` in Morse code to indicate that the ROM is ready to be used.

4. Gently reset or power cycle the Atari ST to use the ROM. The Atari ST will boot normally and will use the ROM as if it was a physical chip.

### Disable ROM Emulation

Simply press again the `SELECT` button more than one second to enter into the `Configurator` mode and power cycle your computer.

### Set the folder hosting the ROM files

The SidecarT board can be configured to use a folder in the microSD card to host the ROM files. This section explains how to configure the SidecarT board to use a folder in the microSD card. 

1. **Preparation**: Ensure you have a microSD card formatted to FAT16 or exFAT. For instructions, visit [How to format the microSD card](/how_to#format-the-microsd-card).
   
2. **Folder Creation**: On the root directory of the microSD card, create a folder named `roms`. This will serve as the storage for the ROM files. By default, the SidecarT board will scan this directory for ROMs.

3. **ROM Transfers**: Copy your ROM files into the `roms` folder. Supported formats are:
   - Pure binary (Raw binary data of the ROM)
   - STEEM format (Recognized if the file begins with four zeros or has a `.STC` extension)

4. **Activation**:
   - Insert the microSD into the SidecarT board and power it up. The board will auto-recognize the microSD.
   - Access `Configurator` mode by pressing the `SELECT` button, navigate to the ROM selection, and choose your desired ROM. The Atari ST will access this ROM as if it was a physical chip.

{: .note }
If you prefer a different folder name instead of `roms`, you can modify the `ROMS_FOLDER` parameter. Details can be found in the [Configuration Parameters](/parameters) section.
{: .note }


### Set the URL of the ROM files

The SidecarT board can be configured to use a web server to host the ROM files. This section explains how to configure the SidecarT board to use a web server.

1. **URL Configuration**: Point the SidecarT board to your web server's ROM directory by setting the `ROMS_YAML_URL` parameter. The board expects a `roms.json` file at this location. To know more about creating this file, see [Set up your own HTTP server for your ROMs](/how_to#set-up-your-own-http-server-for-your-roms).

2. **HTTPS Limitation**:
{: .warning}
The SidecarT board currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

3. **Finalizing Setup**: After updating the configuration, save your changes and reboot the board in `Configurator` mode.

### Enable ROM delay / Ripper mode

The SidecarT board can be configured to add an extra step when accessing the ROM files. This is useful for example for ROMs tha require a post-activation after another software is loaded from a floppy or hard disk, like ripper-style ROMs did. This section explains how to configure the SidecarT board to enable the ROM delay.

1. **Toggling Delay**: Access the `Configurator` application's main menu and press the `D` key to enable/disable the ROM delay.

{: .note }
Pressing the `D` key switches the `DELAY_ROM_EMULATION` parameter between `false` and `true`. While direct editing is possible, using the `D` key is advised to prevent potential issues.
{: .note}

2. **Usage**: When ROM delay is active, ROM emulation isn't immediate post-power-up. Activation occurs after holding down the `SELECT` button for over a second.

{: .important }
Given the `SELECT` button's dual function, you cannot access the `Configurator` mode using it directly. After enabling the ROM, press `SELECT` again to access the `Configurator` mode.
{: .important}

## Floppies Emulation

{: .warning }
The Floppies Emulation feature is currently in preview. It remains under active development. If you opt to use it in read-write mode, ensure backups are made of your floppy images.
{: .warning}

The Floppies Emulation represents a significant enhancement to the SidecarT board. With this, the Atari ST can interface with floppy images on a microSD card as though they were actual floppy disks. Here's how to get started with Floppies Emulation.

### Pre-requisite: Hosting Floppy Images on microSD

To use the SidecarT board's floppy emulation feature, the floppy images must reside in a specific directory on a FAT16 or exFAT formatted microSD card.

1. **MicroSD Preparation**: The first requirement is a FAT16 or exFAT formatted microSD card. Instructions can be found in the [How to format the microSD card](/how_to#format-the-microsd-card) guide.

{: .note}
If you've already set up ROM Emulation, your microSD is likely formatted appropriately, and you can bypass this step.
{: .note}

2. **Directory Structure**: On the microSD's root, create a `floppies` directory. This is where the board will scan for floppy images.

3. **Transferring Floppy Images**: Move your `.ST` and `.MSA` formatted floppy images into the `floppies` directory. The board recognizes these files automatically.

4. **Initialization**:
   - Insert the microSD into the SidecarT board.
   - Power up the board; it should recognize the microSD card automatically.
   - Enter `Configurator` mode by pressing the `SELECT` button. Navigate to either `Emulate Floppy image` menu option (read-only or read-write) and select the desired floppy image. Upon reboot, the Atari ST will interface with this image as if it were an actual floppy disk.

{: .note }
If `floppies` isn't your desired directory name, it can be changed. Adjust the `FLOPPIES_FOLDER` parameter. Details are available in the [Configuration Parameters](/parameters) section.
{: .note}

### Select a .ST or .MSA Floppy Image to Emulate

{: .note }
Starting from v0.0.11 the Floppy Emulation supports .MSA files.

The steps to select the floppy image to emulate are the same for both read-only and read-write modes. This section explains how to select the floppy image to emulate:

1. Enter into the `Configurator` mode by pressing the `SELECT` button more than one second. Now, power cycle your computer and the `Configurator` boot menu will be displayed. Press LEFT SHIFT to enter into the `Configurator` application, or wait 5 seconds to boot the Atari ST normally, open the `Cartridge` drive and run the `SIDECART.TOS` file.

2. From the main menu, there are two options to emulate floppy images:

```
3. Emulate Floppy image from microSD in Read-Only mode 
4. Emulate Floppy image from microSD in Read-Write mode
```

3. In the floppy image selection menu, the user can select the floppy image to emulate from the list of floppy images available. Simply press `RETURN` or `ENTER` to select the floppy image to emulate, and the Atari ST will load and prepare the floppy image to be used. The SidecarT board green led will blink an `F` in Morse code to indicate that the floppy image is ready to be used.

4. Gently reset or power cycle the Atari ST to use the floppy image. The Atari ST will boot normally and will use the floppy image as if it was a physical floppy disk.

### Read-Write Emulation for Floppy Images

The SidecarT board's ability to emulate floppy images in read-write mode is powerful. It lets the Atari ST write to these images, but this also poses risks.

To mitigate potential data loss, when a floppy image is chosen for read-write emulation, the SidecarT board creates a copy in the `FLOPPIES_FOLDER`. This duplicate has the `.rw` extension, and the Atari ST writes to it, leaving the original image untouched.

If a `.rw` duplicate already exists, the board will prioritize it over the original. It won't spawn another `.rw` file, ensuring consistency between sessions.

{: .warning }
It's important to note that the SidecarT board won't validate the integrity of `.rw` files. If such a file is corrupted, the Atari ST won't be able to interface with it, either for reading or writing.
{: .warning}

### Create an empty writable floppy image

The SidecarT board can be configured to create an empty writable floppy image to create our own content or have a blank floppy image to copy files from the Atari ST.

After selecting the option `Emulate Floppy image from microSD in Read-Write mode`, the first entry in the selection menu will be `< CREATE A BLANK FLOPPY IMAGE >`. Select this option and the SidecarT board will prompt for several parameters:

- `Size [1]-SS/DD (360KB), [2]-DS/DD (720KB), [3]-HD (1.44MB)`: Select the size of the floppy image to create.
- `Volume name (max 8 chars, dot, max 3 chars)`: The volume name of the floppy for the Atari ST computer. Can be empty.
- `Image name (max 255 chars)`: The name of the floppy image file stored in the microSD card. Cannot be empty.

Now the SidecarT will need a few seconds to create the empty floppy image. After that, the Atari ST will report to the user that the new image is ready to be used. The user can now select the new read/write image as any other in the floppy image folder.

### Floppy image formats supported

The default format supported by the SidecarT is the `.ST` format. Starting from version v0.0.11, SidecarT can also read the `.MSA` format, converting it to `.ST` format on the fly. Under the covers, everything is a `.ST` file.

A special mention to read-write images with the extions `.rw`. All `.ST` files are read-only files. The SidecarT board will create a copy of the `.ST` file with the `.rw` extension to emulate a writable floppy image.

## Atari ST database of floppy images

The SidecarT board can read a database of floppy images hosted on a remote web server. This feature is built on top of the Floppies Emulation one. This is an out of the box feature that doesn't require any additional configuration besides the one explained above for the Floppies Emulation. 

### How to download and emulate a floppy image from the database

This section explains how to select the floppy image to emulate from the database:

1. Enter into the `Configurator` mode by pressing the `SELECT` button more than one second. Now, power cycle your computer and the `Configurator` boot menu will be displayed. Press LEFT SHIFT to enter into the `Configurator` application, or wait 5 seconds to boot the Atari ST normally, open the `Cartridge` drive and run the `SIDECART.TOS` file.

2. From the main menu, select the option

```
5. Download from the Floppy Images database
```

3. In the menu, there is a bar with the alphabet and numbers. Selecting the letter or number will display the list of applications starting with that letter in the name. 

4. The user can now select the application to download pressing `RETURN` or `ENTER`. Now, the SidecarT board will find the floppy image in the database that contains the application and download it to the storage folder for floppy images.

5. After the download is finished, the Atari ST will load and prepare the floppy image to be used. The SidecarT board green led will blink an `F` in Morse code to indicate that the floppy image is ready to be used.

4. Gently reset or power cycle the Atari ST to use the floppy image. The Atari ST will boot normally and will use the floppy image as if it was a physical floppy disk.


### Set the URL of the database and images files

{: .warning }
For avanced users only.

The SidecarT board can be configured to use a web server to host both the database and images files. It's not necessary to have both in the same server. 

1. **URL Configuration**: Point the SidecarT board to your web server's Atari ST database by setting the `FLOPPY_DB_URL` parameter. The board expects a folder named `db` and a file for each alphabet letter and number. Each of these files in Comma Separated Values (CSV) format contains the list of disk files urls. See [Set up your own HTTP server for your Atari ST database](/how_to#set-up-your-own-http-server-for-your-atari-st-database).

2. **HTTPS Limitation**:
{: .warning}
The SidecarT board currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

3. **Finalizing Setup**: After updating the configuration, save your changes and reboot the board in `Configurator` mode.


## Real Time Clock (RTC)

Starting from the version v0.0.11 of the firmware, the SidecarT board can be configured to be a Real Time Clock (RTC) for the Atari ST. This section explains how to configure the SidecarT board to be a RTC.

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

[B] - Boot emulator

Press an option key or [ESC] to exit:
```

### Set the NTP parameters

The user can change the NTP server host and port by pressing the `H` and `P` keys respectively. The default values are `pool.ntp.org` for the host and `123` for the port, which are the most common values and should work for most users.

### Set the UTC offset

The user can change the UTC offset by pressing the `U` key. The default value is `0`, which means the UTC offset is null. The NTP time returned by any server does not know about timezones, so the SidecarT board needs to know the UTC offset to be able to convert the UTC time to the local time. The UTC offset is expressed in positive or negative hours.

Also note that the Atari ST does not know about timezones either, so the RTC time will be the local time of the Atari ST.

### Change the RTC type

For the version v0.0.11, there are two RTC types available: `SIDECART` and `DALLAS`. The user can change the RTC type by pressing the `1` or `2` keys. The default value is `SIDECART`. Each type has different characteristics:

- `SIDECART`: This is the default RTC type. To set the date and time it uses a small cartridge firmware at boot time that sets the date and time in the Atari ST computer. This firmware is executed at boot time as an executable cartridge and does not impact in the overall performance or memory usage of the system.

- `DALLAS`: This RTC type emulates a DALLAS 1216 RTC integrated chip. To set the date and time the user must use a program that reads the values provided by the DALLAS 1216 emulator and sets the date and time in the Atari ST computer. There are several programs that can do this, but I strongly recommend the [tools created by Troed Sångberg](https://blog.troed.se/projects/dallas-rtc-sync-tos-y2k-fix/).


{: .note}
Both solutions workaround the Y2K problem, or any problem with dates this century. So far.
{: .note}

### Boot the emulator

To Boot the emulator, press the `B` key. The SidecarT board will reboot and depending on the RTC type chosen the flow will differ:

- `SIDECART`: The SidecarT board will boot the cartridge firmware that will set the date and time in the Atari ST computer. After that, the Atari ST will boot normally. The firmware will report how the process goes in the screen. This is important because the RP2040 must query the NTP server to get the time and set it in the Atari ST computer, and this can take several seconds. The Atari ST will not boot until the date and time are set, or fails. 

- `DALLAS`: The Atari ST will boot normally. As explained above, the user must use a program that reads the values provided by the DALLAS 1216 emulator and sets the date and time in the Atari ST computer. Please keep in mind that DALLAS RTC emulation will only provide a valid date and time once the RP2040 obtains a valid date and time from the NTP server.

{: .warning}
The SidecarT will not return a valid date and time until it obtains a valid date and time from the NTP server. In the SIDECART RTC type, the Atari ST will not boot until the date and time are set, or fails. In the DALLAS RTC type, the Atari ST will boot normally, but the date and time will be invalid until the user sets them with a program.
{: .warning}

## Boot a ROM image from the microSD card in 'Rescue Mode'

The SidecarT can be a very helpful device to troubleshoot damaged computers. A good use case is bypass the configurator and let the SidecarT to run a "default ROM" when plugged. This new feature is called "Rescue Mode", and it will boot a ROM image from the microSD card when the SidecarT is plugged in the Atari ST without interacting with the configurator.

### How to enable the Rescue Mode
To enable the Rescue Mode, the user must create a file named `.romrescue` in the root of the microSD card. The content of the file must be the name of the ROM image to boot as found in the `ROMS_FOLDER` (`roms` by default) configuration parameter. It's important to note that the user does not have to include the full path, just the name of the ROM image.

For example, if the user wants to boot a diagnostic ROM image named `ST Test v4.4.img` located in the `roms` folder, the content of the `.romrescue` file must be `ST Test v4.4.img`.

### First boot after enabling the Rescue Mode
After saving the `.romrescue` file in the microSD card, insert the microSD card in the SidecarT and power on the Atari ST. Now, press the `SELECT` button more than one second to enter into the `Configurator` mode. Now the SidecarT will automatically read the `.romrescue` file and will save its content in the FLASH memory of the RP2040. 

### Next boots
After that, the SidecarT will reboot in `ROM_EMULATION` mode and the Atari ST will boot the ROM image specified. 

### How to disable the Rescue Mode
To disable the Rescue Mode, the user must delete the `.romrescue` file from the microSD card, or rename it. After that, if the user press the `SELECT` button for more than one second, the SidecarT will start in the `Configurator` mode as usual.


## Configurator Application

The Configurator application serves as the central interface for the SidecarT board's configurations. It's alternately known as the `firmware` or the `firmware application`. This guide will walk you through the nuances of the Configurator application.

### Boot Mode Adjustments

Upon the initial power-up of the SidecarT board, or when the `SELECT` button is held for over 1 second, the Configurator is invoked. This application resides in the `Cartridge` drive, which is visible upon starting the Atari ST.

The behavior when pressing `SELECT` for over 1 second is configurable. The SidecarT board can either:

1. Swiftly transition to the `Configurator` mode, or
2. Delay this transition until the Atari ST's next full power cycle (not just a reset).

This behavior is determined by the `SAFE_CONFIG_REBOOT` parameter.

Immediately transitioning can be jarring for ongoing Atari ST applications. Especially for applications or drivers overseeing other storage devices, this abrupt switch can lead to compatibility concerns. As a preventive measure, the SidecarT board can be set to defer this transition until the subsequent power cycle.

By default, `SAFE_CONFIG_REBOOT` is set to `true`. This means the SidecarT will hold off until the next power cycle before transitioning to `Configurator` mode. Altering this behavior involves tweaking the `SAFE_CONFIG_REBOOT` parameter. Further insights can be found in the [Configuration Parameters](/parameters) section.

{: .note}
There are valid scenarios where setting `SAFE_CONFIG_REBOOT` to `false` makes sense. For instance, developers frequently adjusting the SidecarT configuration might find repeatedly waiting for a power cycle tedious. However, exercise this option judiciously.
{: .note}

### Latest release verification

The SidecarT board can be configured to check for the latest release of the firmware available. When the board is connected to the internet, it will check for the latest release and display a blinking exclamation mark at the right side of the current version number at the top bar of the Configurator application. This section explains how to configure the SidecarT board to check for the latest release.

{: .note}
You have to be connected to the internet to check for the latest release.
{: .note}

1. **URL Configuration**: The parameter `LATEST_RELEASE_URL` has to point to a file hosted on a web server. This file has to contain the latest release version number in the first line. The SidecarT board will check this file and compare the version number with the current version number. If the version number is different, the SidecarT board will display a blinking exclamation mark as explained above.

2. **HTTPS Limitation**:
{: .warning}
The SidecarT board currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

### The STABLE and BETA release distribution workflows

The SidecarT board Latest release verification can be configured to check for new releases of type STABLE or BETA. With the growing user base of SidecarT, the need for extensive and stability-focused testing is becoming increasingly important. To address this, we propose introducing two distinct release workflows. This approach aims to balance the needs of our diverse user community, ranging from makers to those seeking more stable and reliable software.

1. **BETA Release Workflow**: This caters to users who are interested in testing the latest features and providing valuable feedback. It allows us to incorporate user experiences into development, ensuring that the software meets a wide range of needs and use cases.

2. **STABLE Release Workflow**: Aimed at users who prioritize stability and reliability. This workflow focuses on delivering a polished and thoroughly tested version of the software, thereby reducing support queries and enhancing user satisfaction.

This is controlled through the `LATEST_RELEASE_URL` parameter in the configuration.

If `LATEST_RELEASE_URL` points to `http://atarist./version.txt`, users will be notified about the availability of a new STABLE (or latest) release.

If `LATEST_RELEASE_URL` points to `http://atarist./beta.txt`, users will be alerted when a new BETA release is available.

In both cases, the SidecarT board will check for the latest release and display a blinking exclamation mark at the right side of the current version number at the top bar of the Configurator application. 

To download the STABLE (latest) or BETA release, navigate to the [Download page](https://sidecartridge.com/downloads) and download the appropriate file. Then, follow the [Update the firmware](/how_to#update-the-firmware) guide.

