---
layout: default
title: How to
nav_order: 9
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /how_to
  - /how_to/
---

# How to
{: .no_toc }

This section showcases a variety of different configurations and parametric setups for the SidecarTridge Multi-device board. You don't need to be a developer to follow these guides, but you will need to be familiar with the basics of the Atari ST and the Multi-device board. If you are new to the Multi-device project, please refer to the [Getting Started](/sidecartridge-multidevice/getting_started/) section first.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Update the firmware

To install the latest Multi-device firmware on the Raspberry Pi Pico W, connect your PC, Mac, or Linux to the Raspberry Pi Pico W using the USB cable. Now hold down the BOOTSEL button for a few seconds and then hold down the RESET button. Now release the RESET button and gently release the BOOTSEL button afterwards. A new drive named `RPI-RP2` should appear on your PC, Mac, or Linux. Open it.

{:refdef: style="text-align: center;"}
![How enter in BOOTSEL mode](https://sidecartridge.com/assets/images/quickstart/bootsel-mode.gif)
{: refdef}

In this directory, you will need to copy the latest STABLE Firmware versions, which you can directly get from the [download page](https://sidecartridge.com/downloads/).

Once you've copied the file corresponding to your Raspberry Pico W, disconnect the power cable. The new firmware has now been flashed.

## Format the microSD card

To use the Multi-device effectively, your microSD card needs to be formatted in FAT16 or exFAT. Here's how you can format it in FAT16 or exFAT on various platforms:

### Windows:

1. Insert your microSD card into your computer using an SD card reader.
2. Press `Windows + E` to open the File Explorer.
3. Right-click on your microSD card from the list of devices and choose `Format`.
4. In the Format window, from the `File system` dropdown, choose `FAT (Default)` (Note: FAT16 might be referred to as just FAT in some versions of Windows) or `exFAT`.
5. Click `Start` to format the card.
6. Once completed, safely eject the card from your computer.

### macOS:

1. Insert your microSD card into your computer.
2. Open `Terminal` (you can use Spotlight with `Command + Space` and then type "Terminal").
3. Type 'diskutil list' to get a list of all dtives. Identify your SD Card. Example: disk8s1, where 8 is the Disk and s1 the Volume. It also shows you filesystem, name and size. Doublecheck and make sure to pick the right Disk!
4. Type `diskutil eraseDisk exFAT <NAME> disk<X>` NAME=Name for the disk. X=Disk.
5. Once the process completes, you can safely eject the microSD card.

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

The Multi-device board is designed to be used with a web server to host the ROMs. This is the recommended way to use the board if you don't want to store the ROM files in the microSD card, as it allows for a more flexible and user-friendly experience. This guide will show you how to set up a local HTTP server on your computer and configure the Multi-device board to use it.

### Set up a HTTP server

There are many ways to set up a HTTP server and there are plenty of tutorials online. It's also possible to use a storage cloud service like Amazon S3 to host the ROMs. For the purpose of this guide, we will only reference some standard HTTP server setups from the internet.

{: .note }
The Multi-device bord does not support HTTPS at the moment. Make sure to disable HTTPS and use HTTP only.

{: .note }
The Multi-device board also only supports access through port 80 and without proxy. Make sure to configure your server accordingly.

{: .note }



- [Apache](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)



### Create the `roms.json` file

{: .warning }
The JSON file has been deprecated starting in version v0.0.18 of the firmware due to performance reasons. Please see the `roms.csv` format instead.

The `roms.json` file is a JSON file that contains the list of ROMs available on the server. The Multi-device board will use this file to display the list of ROMs in the `Configurator` application. The file must be located at any accessible path on the server. For example, if the server is running on `http://yourserver`, the file can be located at `http://yourserver/roms.json`.


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

The full content of the sample `roms.json` file can be found [here](http://roms.sidecartridge.com/roms.json). You can use this file as a template to create your own `roms.json` file.


### Create the `roms.csv` file

The `roms.csv` file is comma separated values file that comes to replace the `roms.json` file due to performance and memory reasons. It contains the same values but in a different format. The device will use this file to display the list of ROMs in the `Configurator` application. The file must be located at any accessible path on the server. For example, if the server is running on `http://yourserver`, the file can be located at `http://yourserver/roms.csv`.


The format of the file is as follows:

- The file must be a CSV file separated by commas.
- Each field value must be enclosed in double quotes.
- Each line must contain the following fields:
  1. `url`: The URL of the ROM file. If only contains a name, it will assume is in the same path as the `roms.csv` file.
  - `name`: The name of the ROM.
  - `description`: A short description of the ROM.
  - `tags`: An array of tags describing the ROM.
  - `size_kb`: The size of the ROM in kilobytes.

The first line of the file must contain the field names. An example of a `roms.csv` file is shown below:

```csv
"URL","Name","Description","Tags","Size (KB)"
"1st%20address%20v1.01-D.bin","1st address v1.01-D","1st address is a file management assistant.","tools; office","16"
"backpack.stc","Backpack","Utility software for file management.","utility; management","128"
"Buggy%20Boy.img","Buggy Boy","An off-road racing game where players drive a buggy and avoid obstacles.","racing; arcade","128"
"cumana%20OS-9.stc","Cumana OS-9","A popular operating system.","os","128"
```

The full content of the sample `roms.csv` file can be found [here](http://roms.sidecartridge.com/roms.csv). You can use this file as a template to create your own `roms.csv` file.

### Upload the ROM images to the server

The ROM images can be uploaded to any accessible path on the server. For example, if the server is running on `http://yourserver`, the ROM images can be located at `http://yourserver/roms/`. 

If the ROM images have a suffix with the name `.STC` and also the first four bytes are zeroed out, the Multi-device board will automatically detect the ROM as a STEEM ROM and will offset the four bytes out. Otherwise, the ROM will be detected as a standard Atari ST ROM. 

{: .warning }
Don't forget to update the `url` field in the `roms.csv` file to point to the correct location of the ROM images.



### Change the Multi-device board configuration

The Multi-device board can be configured to use any HTTP server by changing the `ROMS_YAML_URL` parameter in the configuration parameters of the `Configursator`. The default value of this parameter is `http://roms.sidecartridge.com/roms.csv`. You should change this value to point to your own `roms.csv` file.

{: .note }
The `ROMS_YAML_URL` is not the right name for this parameter. It will be renamed in the future to `ROMS_JSON_URL`.

### Test the configuration

Once the parameter is changed, you can test the configuration by running the `Configurator` application. The application will display the list of ROMs available on the server. You can select a ROM and run it to test it.

## Set up your own HTTP server for your Atari ST database

### Introduction

The Multi-device board is designed to access to a remote Atari ST database of floppy images with hundreds of images and thousands of applications. Thanks to this database, the Multi-device board can easily find and launch software in an easy way. The previous chapter explained how to configure a generic HTTP server, this chapter will explain how to configure the specific files for the Atari ST database.

### The database files

Inside a folder called `db` you will have to place the following files: a file with the alphabet letter or a number of the programs starting with it. For example, if you want to access to the programs starting with the letter `A`, you will have to place the file `a.csv` inside the `db` folder. The file `a.csv` will contain the list of programs starting with the letter `A`. The format of the file is as follows:

The file must be a CSV file with the following fields:
- `application_name`: The name of the program.
- `status`: The status of the program. `0` means OK, any other value means KO.
- `description`: A short description of the program.
- `tags`: An array of tags describing the program.
- `PLACEHOLDER`: Reserved for future use.
- `url`: The URL of the floppy image file. If the url does not start with `http://`, it will be considered a relative URI.

For example a excerpt of the file `a.csv`:

```
"A 320";"0";"";"";"";"AUTOMATION/A_093.ST"
"A Mind forever voyaging";"0";"";"";"";"AUTOMATION/A_188.ST"
"A PROTEC DEMO";"0";"";"";"";"MEDWAY/med_068.st"
...
"Anco strip poker1.8 Tos only";"0";"";"";"";"AUTOMATION/A_176.ST"
```

## Configure the WiFi password in a file in the microSD card

### Introduction

The Multi-device board can be configured to connect to a WiFi network by configuring the WiFi SSID and password in the `Configurator`. Sometimes entering the WiFi password using the `Configurator` can be cumbersome, especially if the password is long. This how-to will explain how to configure the WiFi password in a file in the microSD card so that the Multi-device board can automatically connect to the WiFi network.

### Create the `.wifipass` file

The `.wifipass` file is a text file that contains the WiFi password. The file must be located at the root of the microSD card. The Multi-device board will automatically read the file and connect to the WiFi network, overriding the WiFi password configured in the `Configurator`.

To create the file, open a text editor in your PC/Mac/Linux computer and type the WiFi password. Save the file as `.wifipass` and insert the microSD card into the Multi-device board. The Multi-device board will automatically read the file and connect to the WiFi network after a reboot or power cycle of the Multi-device board.

{: .note }
The maximum length of the WiFi password is 63 characters.

[Previous: Parameters](/sidecartridge-multidevice/parameters_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: How to](/sidecartridge-multidevice/how_to/){: .btn }
