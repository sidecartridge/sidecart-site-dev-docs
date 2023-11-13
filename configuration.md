---
layout: default
title: Configuration
nav_order: 7
---

# Configure the SidecarT board
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## ROM Emulation Configuration

ROM Emulation is a pivotal feature of the SidecarT board, enabling the Atari ST to treat ROM files from a microSD card or an external web server as native ROM chips. This guide covers how to set up the ROM Emulation.

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

## Floppies Emulation configuration (PREVIEW)

{: .warning }
The Floppies Emulation feature is currently in preview. It remains under active development. If you opt to use it in read-write mode, ensure backups are made of your floppy images.
{: .warning}

The Floppies Emulation represents a significant enhancement to the SidecarT board. With this, the Atari ST can interface with floppy images on a microSD card as though they were actual floppy disks. Here's how to get started with Floppies Emulation.

### Hosting Floppy Images on microSD

To use the SidecarT board's floppy emulation feature, the floppy images must reside in a specific directory on a FAT16 or exFAT formatted microSD card.

1. **MicroSD Preparation**: The first requirement is a FAT16 or exFAT formatted microSD card. Instructions can be found in the [How to format the microSD card](/how_to#format-the-microsd-card) guide.

{: .note}
If you've already set up ROM Emulation, your microSD is likely formatted appropriately, and you can bypass this step.
{: .note}

2. **Directory Structure**: On the microSD's root, create a `floppies` directory. This is where the board will scan for floppy images.

3. **Transferring Floppy Images**: Move your `.ST` formatted floppy images into the `floppies` directory. The board recognizes these files automatically.

4. **Initialization**:
   - Insert the microSD into the SidecarT board.
   - Power up the board; it should recognize the microSD card automatically.
   - Enter `Configurator` mode by pressing the `SELECT` button. Navigate to either `Emulate Floppy image` menu option (read-only or read-write) and select the desired floppy image. Upon reboot, the Atari ST will interface with this image as if it were an actual floppy disk.

{: .note }
If `floppies` isn't your desired directory name, it can be changed. Adjust the `FLOPPIES_FOLDER` parameter. Details are available in the [Configuration Parameters](/parameters) section.
{: .note}

### Read-Write Emulation for Floppy Images

The SidecarT board's ability to emulate floppy images in read-write mode is powerful. It lets the Atari ST write to these images, but this also poses risks.

To mitigate potential data loss, when a floppy image is chosen for read-write emulation, the SidecarT board creates a copy in the `FLOPPIES_FOLDER`. This duplicate has the `.rw` extension, and the Atari ST writes to it, leaving the original image untouched.

If a `.rw` duplicate already exists, the board will prioritize it over the original. It won't spawn another `.rw` file, ensuring consistency between sessions.

{: .warning }
It's important to note that the SidecarT board won't validate the integrity of `.rw` files. If such a file is corrupted, the Atari ST won't be able to interface with it, either for reading or writing.
{: .warning}

## Atari ST database of floppy images

The SidecarT board can read a database of floppy images hosted on a remote web server. This feature is built on top of the Floppies Emulation one. This is an out of the box feature that doesn't require any additional configuration besides the one explained above for the Floppies Emulation. 

The SidecarT board will read the database and display the list of floppy images available in the `Download from the Floppy Images database` menu option of the `Configurator` application. Simply navigate through the list and select the application you want to download. The SidecarT board will find the floppy image in the database that contains the application and download it to the storage folder for floppy images.

If you want to host your own database of floppy images, please continue reading. 

### Set the URL of the database and images files

The SidecarT board can be configured to use a web server to host both the database and images files. It's not necessary to have both in the same server. 

1. **URL Configuration**: Point the SidecarT board to your web server's Atari ST database by setting the `FLOPPY_DB_URL` parameter. The board expects a folder named `db` and a file for each alphabet letter and number. Each of these files in Comma Separated Values (CSV) format contains the list of disk files urls. See [Set up your own HTTP server for your Atari ST database](/how_to#set-up-your-own-http-server-for-your-atari-st-database).

2. **HTTPS Limitation**:
{: .warning}
The SidecarT board currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

3. **Finalizing Setup**: After updating the configuration, save your changes and reboot the board in `Configurator` mode.


## Configuring the Configurator Application

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

2. **STABLE (or Latest) Release Workflow**: Aimed at users who prioritize stability and reliability. This workflow focuses on delivering a polished and thoroughly tested version of the software, thereby reducing support queries and enhancing user satisfaction.

This is controlled through the `LATEST_RELEASE_URL` parameter in the configuration.

If `LATEST_RELEASE_URL` points to http://atarist.sidecart.xyz/version.txt, users will be notified about the availability of a new STABLE (or latest) release.

If `LATEST_RELEASE_URL` points to http://atarist.sidecart.xyz/beta.txt, users will be alerted when a new BETA release is available.

In both cases, the SidecarT board will check for the latest release and display a blinking exclamation mark at the right side of the current version number at the top bar of the Configurator application. 

To download the STABLE (latest) or BETA release, navigate to the [Download page](https://sidecart.xyz/downloads) and download the appropriate file. Then, follow the [Update the firmware](/how_to#update-the-firmware) guide.

{: .note}

{: .note}



{: .note}