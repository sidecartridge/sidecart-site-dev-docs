---
layout: default
title: Configuration
nav_order: 7
---

# Configure the SidecarT board

## ROM Emulation Configuration

ROM Emulation is a pivotal feature of the SidecarT board, enabling the Atari ST to treat ROM files from a microSD card or an external web server as native ROM chips. This guide covers how to set up the ROM Emulation.

### Set the folder hosting the ROM files

The SidecarT board can be configured to use a folder in the microSD card to host the ROM files. This section explains how to configure the SidecarT board to use a folder in the microSD card. 

1. **Preparation**: Ensure you have a microSD card formatted to FAT32. For instructions, visit [How to format the microSD card](/how_to#format-the-microsd-card).
   
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
**Attention**: The SidecarT board currently doesn't support HTTPS. Ensure that your server uses HTTP only.
{: .warning}

3. **Finalizing Setup**: After updating the configuration, save your changes and reboot the board in `Configurator` mode.

### Enable ROM delay / Ripper mode

The SidecarT board can be configured to add an extra step when accessing the ROM files. This is useful for example for ROMs tha require a post-activation after another software is loaded from a floppy or hard disk, like ripper-style ROMs did. This section explains how to configure the SidecarT board to enable the ROM delay.

1. **Toggling Delay**: Access the `Configurator` application's main menu and press the `D` key to enable/disable the ROM delay.

{: .note }
Pressing the `D` key switches the `DELAY_ROM_EMULATION` parameter between `false` and `true`. While direct editing is possible, using the `D` key is advised to prevent potential issues.
{: .note}

2. **Usage**: When ROM delay is active, ROM emulation isn't immediate post-power-up. Activation occurs after holding down the `SELECT` button for over a second.

{: .warning }
**Important**: Given the `SELECT` button's dual function, you cannot access the `Configurator` mode using it directly. After enabling the ROM, press `SELECT` again to access the `Configurator` mode.
{: .warning}

## Floppies Emulation configuration (PREVIEW)

{: .warning }
**Preview Notice**: The Floppies Emulation feature is currently in preview. It remains under active development. If you opt to use it in read-write mode, ensure backups are made of your floppy images.
{: .warning}

The Floppies Emulation represents a significant enhancement to the SidecarT board. With this, the Atari ST can interface with floppy images on a microSD card as though they were actual floppy disks. Here's how to get started with Floppies Emulation.

### Hosting Floppy Images on microSD

To use the SidecarT board's floppy emulation feature, the floppy images must reside in a specific directory on a FAT32-formatted microSD card.

1. **MicroSD Preparation**: The first requirement is a FAT32-formatted microSD card. Instructions can be found in the [How to format the microSD card](/how_to#format-the-microsd-card) guide.

{: .note}
If you've already set up ROM Emulation, your microSD is likely formatted appropriately, and you can bypass this step.
{: .note}

2. **Directory Structure**: On the microSD's root, create a `floppies` directory. This is where the board will scan for floppy images.

3. **Transferring Floppy Images**: Move your `.ST` formatted floppy images into the `floppies` directory. The board recognizes these files automatically.

4. **Initialization**:
   - Insert the microSD into the SidecarT board.
   - Power up the board; it should recognize the microSD card automatically.
   - Enter `Configurator` mode by pressing the `SELECT` button. Navigate to either `Emulate Floppy image` menu option (read-only or read-write) and select the desired floppy image. Upon reboot, the Atari ST will interface with this image as if it were an actual floppy disk.

{: .hint }
If `floppies` isn't your desired directory name, it can be changed. Adjust the `FLOPPIES_FOLDER` parameter. Details are available in the [Configuration Parameters](/parameters) section.
{: .hint}

### Read-Write Emulation for Floppy Images

The SidecarT board's ability to emulate floppy images in read-write mode is powerful. It lets the Atari ST write to these images, but this also poses risks.

To mitigate potential data loss, when a floppy image is chosen for read-write emulation, the SidecarT board creates a copy in the `FLOPPIES_FOLDER`. This duplicate has the `.rw` extension, and the Atari ST writes to it, leaving the original image untouched.

If a `.rw` duplicate already exists, the board will prioritize it over the original. It won't spawn another `.rw` file, ensuring consistency between sessions.

{: .warning }
It's important to note that the SidecarT board won't validate the integrity of `.rw` files. If such a file is corrupted, the Atari ST won't be able to interface with it, either for reading or writing.
{: .warning}