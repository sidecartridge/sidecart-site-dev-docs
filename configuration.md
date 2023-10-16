---
layout: default
title: Configuration
nav_order: 7
---

# Configure the SidecarT board

## ROM Emulation configuration

The ROM Emulation is the core feature of the SidecarT board. It allows the Atari ST to access the ROM files stored in the microSD card or an external web server as if they were physical ROM chips. This section explains how to configure the ROM Emulation features.

### Set the folder hosting the ROM files

The SidecarT board can be configured to use a folder in the microSD card to host the ROM files. This section explains how to configure the SidecarT board to use a folder in the microSD card. 

First step is to have a microSD formatted with the supported filesystem, which is FAT32. Please refer to the [How to format the microSD card](/how_to#format-the-microsd-card) section for more information.

Next, create a folder with the name `roms` in the root directory of the microSD card. This folder will be used to host the ROM files. The SidecarT board will only look for ROM files in this folder.

Finally, copy the ROM files to the `roms` folder. The ROM files can be in two formats: pure binary format or STEEM format. The pure binary format is the raw binary data of the ROM file. The STEEM format is a format used by the STEEM emulator. SidecarT detects the format of the ROM file automatically: if the file starts with four zero bytes or the file extension is `.STC`, the file is assumed to be in STEEM format. Otherwise, the file is assumed to be in pure binary format.

The microSD card must be inserted in the SidecarT board and the board must be powered on. The SidecarT board will automatically detect the microSD card and mount it. Enter in the `Configurator` mode pressing `SELECT` button, naviage to the ROM selection menu and select the ROM you want to use. The Atari ST will now be able to access the ROM file as if it was a physical ROM chip.

If you don't want to use the default name `roms`, it's possible to change the name of the folder. The parameter is `ROMS_FOLDER`. Please refer to the [Configuration Parameters](/parameters) section for more information. 

### Set the URL of the ROM files

The SidecarT board can be configured to use a web server to host the ROM files. This section explains how to configure the SidecarT board to use a web server.

The SidecarT board will look for a file named `roms.json` in the URL specified in the `ROMS_YAML_URL` parameter. Please refer to the article [Set up your own HTTP server for your ROMs](/how_to#set-up-your-own-http-server-for-your-roms) for more information on how to create a `roms.json` file. 

{: .note }
Please remember that the SidecarT board does not support HTTPS at the moment. Make sure to disable HTTPS and use HTTP only.
{: .note }

Don't forget after changing the configuration parameters to save the configuration and reboot the board in `Configurator` mode.

### Enable ROM delay / Ripper mode

The SidecarT board can be configured to add an extra step when accessing the ROM files. This is useful for example for ROMs tha require a post-activation after another software is loaded from a floppy or hard disk, like ripper-style ROMs did. This section explains how to configure the SidecarT board to enable the ROM delay.

The ROM delay can be enabled simply clicking on the `D` key of the main menu of the `Configurator` application. The some process can be used to disable the ROM delay.

{: .note }
This key will change the status of the configuration parameter `DELAY_ROM_EMULATION` from `false` to `true` and vice versa. While it's possible to change the value of the parameter directly, it's recommended to use the `D` key to avoid any issue.
{: .note }

When the ROM delay is enabled, the SidecarT board will not activate the ROM emulation immediately when the Atari ST powers on. Instead, the ROM emulation will be activated after the user presses the `SELECT` button for more than one second. 

{: .warning }
Since the `SELECT` now plays a dual role, it's not possible to use the `SELECT` button to enter in the `Configurator` mode. To enter in the `Configurator` mode, press the `SELECT` again after the ROM emulation is activated.
{: .warning }

## Floppies Emulation configuration (PREVIEW)

{: .warning }
This is a preview of the Floppies Emulation feature. This feature is still under development and if you want to use it in read-write mode, please make sure to have a backup of your floppy images.
{: .warning }

The Floppies Emulation is a new feature of the SidecarT board. It allows the Atari ST to access floppy images stored in the microSD card as if they were physical floppy disks. This section explains how to configure the Floppies Emulation features.

### Set the folder hosting the floppy images

The SidecarT board can be configured to use a folder in the microSD card to host the floppy images. This section explains how to configure the SidecarT board to use a folder in the microSD card.

First step is to have a microSD formatted with the supported filesystem, which is FAT32. Please refer to the [How to format the microSD card](/how_to#format-the-microsd-card) section for more information.

{: .note }
If you have already configured the ROM Emulation, the microSD card is already formatted and you can skip the step.
{: .note }

Next, create a folder with the name `floppies` in the root directory of the microSD card. This folder will be used to host the floppy images. The SidecarT board will only look for floppy images in this folder.

Finally, copy the floppy images to the `floppies` folder. At this moment only suppors floppy images in the `.ST` format. The SidecarT board will detect the floppy images automatically.

The microSD card must be inserted in the SidecarT board and the board must be powered on. The SidecarT board will automatically detect the microSD card and mount it. Enter in the `Configurator` mode pressing `SELECT` button, navigate to the `Emulate Floppy image` menus (read-only or read-write) and select the floppy image you want to use. After reboot, the Atari ST will now be able to access the floppy image as if it was a physical floppy disk.

If you don't want to use the default name `floppies`, it's possible to change the name of the folder. The parameter is `FLOPPIES_FOLDER`. Please refer to the [Configuration Parameters](/parameters) section for more information.

### Emulate floppy images in read-write mode

When the SidecarT board emulates the floppy images in read-write mode, the Atari ST will be able to write to the floppy image. As anyone can imagine, this is a feature that can destroy information. 

Hence, when a user selects a floppy image to be emulated in read-write mode, the SidecarT board will do a copy of the floppy image in the folder in `FLOPPIES_FOLDER` with the same name of the floppy image and the extension `.rw`. The Atari ST will write to the `.rw` file, keeping the original floppy image intact.

If the user selects a floppy image that already has a `.rw` file, the SidecarT board will use the `.rw` file instead of the original floppy image, but it will not create a new `.rw` file. This is useful to keep the Atari ST configuration between reboots.

{: .warning }
The SidecarT board will not check if the `.rw` file is a valid floppy image. If the `.rw` file is corrupted, the Atari ST will not be able to read or write to the floppy image.
{: .warning }

