---
layout: default
title: How to
nav_order: 9
---

# How to
{: .no_toc }

This section showcases a variety of different configurations and parametric setups for the SidecarT board. You don't need to be a developer to follow these guides, but you will need to be familiar with the basics of the Atari ST and the SidecarT board. If you are new to the SidecarT project, please refer to the [Getting Started](/getting_started) section first.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Update the firmware

To install the latest SidecarT firmware on the Raspberry Pi Pico W, connect your PC, Mac, or Linux to the Raspberry Pi Pico W using the USB cable. Now hold down the BOOTSEL button for a few seconds and then hold down the RESET button. Now release the RESET button and gently release the BOOTSEL button afterwards. A new drive named `RPI-RP2` should appear on your PC, Mac, or Linux. Open it.

{:refdef: style="text-align: center;"}
![How enter in BOOTSEL mode](https://sidecartridge.com/assets/images/quickstart/bootsel-mode.gif)
{: refdef}

In this directory, you will need to copy the latest STABLE or BETA Firmware versions, which you can directly get from the [download page](https://sidecartridge.com/downloads).

Once you've copied the file corresponding to your Raspberry Pico W, disconnect the power cable. The new firmware has now been flashed.

## Format the microSD card

To use the SidecarT effectively, your microSD card needs to be formatted in FAT16 or exFAT. Here's how you can format it in FAT16 or exFAT on various platforms:

### Windows:

1. Insert your microSD card into your computer using an SD card reader.
2. Press `Windows + E` to open the File Explorer.
3. Right-click on your microSD card from the list of devices and choose `Format`.
4. In the Format window, from the `File system` dropdown, choose `FAT (Default)` (Note: FAT16 might be referred to as just FAT in some versions of Windows) or `exFAT`.
5. Click `Start` to format the card.
6. Once completed, safely eject the card from your computer.

### macOS:

1. Insert your microSD card into your computer.
2. Open `Disk Utility` (you can use Spotlight with `Command + Space` and then type "Disk Utility").
3. Select your microSD card from the list on the left and then click `Erase`.
4. For the format, choose `MS-DOS (FAT)` which is the macOS term for FAT16, or `ExFAT`.
5. Click `Erase` to format the card.
6. Once the process is complete, safely eject the card from your Mac.

### Linux:

**Using the Terminal:**

1. Insert your microSD card into your computer.
2. Open a terminal.
3. Type `sudo fdisk -l` to list all the storage devices. Identify your microSD card's name (usually `/dev/sdb` or `/dev/mmcblk0` or similar).
4. Type `sudo umount /dev/sdX*` replacing `X` with your microSD card letter.
5. If you want to format it to FAT16, type `sudo mkfs.vfat -F 16 /dev/sdX` again replacing `X` with your microSD card letter to format it to FAT16.
6. If you want to format it to exFAT, type `sudo mkfs.exfat /dev/sdX` instead. Probably you will need to install some packages before, please check what your distribution needs.
6. Once the process completes, you can safely eject the microSD card.

**Using GParted (GUI):**

1. Insert your microSD card into your computer.
2. Open GParted. If you don't have it installed, you can install it using `sudo apt install gparted` on Debian/Ubuntu based distributions.
3. Select your microSD card from the top right dropdown.
4. Right-click on the microSD card partition and select `Format to` -> `fat16` or `exFAT`. Note: probably you will need to install some packages before, please check what your distribution needs
5. Click on the green checkmark to apply the changes.
6. Once the process completes, close GParted and safely eject your microSD card.

{: .note }
Always ensure you've selected the correct device to format, especially when working with disk utilities, to avoid data loss.
{: .note }

## Set up your own HTTP server for your ROMs

### Introduction

The SidecarT board is designed to be used with a web server to host the ROMs. This is the recommended way to use the board if you don't want to store the ROM files in the microSD card, as it allows for a more flexible and user-friendly experience. This guide will show you how to set up a local HTTP server on your computer and configure the SidecarT board to use it.

### Set up a HTTP server

There are many ways to set up a HTTP server and there are plenty of tutorials online. It's also possible to use a storage cloud service like Amazon S3 to host the ROMs. For the purpose of this guide, we will only reference some standard HTTP server setups from the internet.

{: .note }
The SidecarT bord does not support HTTPS at the moment. Make sure to disable HTTPS and use HTTP only.

{: .note }
The SidecarT board also only supports access through port 80 and without proxy. Make sure to configure your server accordingly.

{: .note }



- [Apache](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)



### Create the `roms.json` file

The `roms.json` file is a JSON file that contains the list of ROMs available on the server. The SidecarT board will use this file to display the list of ROMs in the `Configurator` application. The file must be located at any accessible path on the server. For example, if the server is running on `http://yourserver`, the file can be located at `http://yourserver/roms.json`.


The format of the file is as follows:

- The file must be a JSON array of objects.
- Each object must contain the following fields:
  - `url`: The URL of the ROM file. It does not need to be in the same server as the `roms.json` file.
  - `name`: The name of the ROM.
  - `description`: A short description of the ROM.
  - `tags`: An array of tags describing the ROM.
  - `size_kb`: The size of the ROM in kilobytes.

An example of a `roms.json` file is shown below:

```json
[
    {
        "url": "http://roms./Missile%20Command.STC",
        "name": "Missile Command",
        "description": "A classic arcade game where players defend cities from incoming missiles.",
        "tags": [
            "arcade",
            "action"
        ],
        "size_kb": 128
    },
    {
        "url": "http://roms./Buggy%20Boy.img",
        "name": "Buggy Boy",
        "description": "An off-road racing game where players drive a buggy and avoid obstacles.",
        "tags": [
            "racing",
            "arcade"
        ],
        "size_kb": 128
    },
    ...
    ,
    {
        "url": "http://roms./Joust%20and%20Moon%20Patrol.STC",
        "name": "Joust and Moon Patrol",
        "description": "A combo of two arcade classics - Joust, a competitive bird-riding game, and Moon Patrol, a lunar vehicle shooter.",
        "tags": [
            "arcade",
            "action",
            "shooter"
        ],
        "size_kb": 128
    }
]
```

The full content of the sample `roms.json` file can be found [here](http://roms./roms.json). You can use this file as a template to create your own `roms.json` file.

### Upload the ROM images to the server

The ROM images can be uploaded to any accessible path on the server. For example, if the server is running on `http://yourserver`, the ROM images can be located at `http://yourserver/roms/`. 

If the ROM images have a suffix with the name `.STC` and also the first four bytes are zeroed out, the SidecarT board will automatically detect the ROM as a STEEM ROM and will offset the four bytes out. Otherwise, the ROM will be detected as a standard Atari ST ROM. 

{: .warning }
Don't forget to update the `url` field in the `roms.json` file to point to the correct location of the ROM images.


### Change the SidecarT board configuration

The SidecarT board can be configured to use any HTTP server by changing the `ROMS_YAML_URL` parameter in the configuration parameters of the `Configursator`. The default value of this parameter is `http://roms./roms.json`. You should change this value to point to your own `roms.json` file.

{: .note }
The `ROMS_YAML_URL` is not the right name for this parameter. It will be renamed in the future to `ROMS_JSON_URL`.

### Test the configuration

Once the parameter is changed, you can test the configuration by running the `Configurator` application. The application will display the list of ROMs available on the server. You can select a ROM and run it to test it.

## Set up your own HTTP server for your Atari ST database

### Introduction

The SidecarT board is designed to access to a remote Atari ST database of floppy images with hundreds of images and thousands of applications. Thanks to this database, the SidecarT board can easily find and launch software in an easy way. The previous chapter explained how to configure a generic HTTP server, this chapter will explain how to configure the specific files for the Atari ST database.

### The database files

Inside a folder called `db` you will have to place the following files: a file with the alphabet letter or a number of the programs starting with it. For example, if you want to access to the programs starting with the letter `A`, you will have to place the file `a.csv` inside the `db` folder. The file `a.csv` will contain the list of programs starting with the letter `A`. The format of the file is as follows:

The file must be a CSV file with the following fields:
- `application_name`: The name of the program.
- `status`: The status of the program. `0` means OK, any other value means KO.
- `description`: A short description of the program.
- `tags`: An array of tags describing the program.
- `url`: The URL of the floppy image file. If the url does not start with `http://`, it will be considered a relative URI.

For example a excerpt of the file `a.csv`:

```
"A 320";"0";"";"";"";"AUTOMATION/A_093.ST"
"A Mind forever voyaging";"0";"";"";"";"AUTOMATION/A_188.ST"
"A PROTEC DEMO";"0";"";"";"";"MEDWAY/med_068.st"
...
"Anco strip poker1.8 Tos only";"0";"";"";"";"AUTOMATION/A_176.ST"
```
