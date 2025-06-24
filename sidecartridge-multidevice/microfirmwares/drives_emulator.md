---
layout: default
title: SidecarTridge Multi-device Drives Emulator V2.0
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/drives_emulator/
  - /microfirmwares/drives_emulator
---

# SidecarTridge Multi-device Drives Emulator
{: .no_toc }
{: .d-inline-block }

{{ site.FIRMWARE_ALPHA_VERSION }}
{: .label .label-purple }

This is a microfirmware application for the **SidecarTridge Multi-device**, designed to emulate hard disks and floppy drives for Atari computers, including the **Atari ST, STe, Mega ST, and Mega STe**.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## 🚀 Installation

To install the Drives Emulator app on your SidecarTridge Multi-device:

1. Launch the **Booster App** on your SidecarTridge  Multi-device..
2. Open the Booster web interface.
3. In the **Apps** tab, select **"Drives Emulator"** from the list of available apps.
4. Click **"Download"** to install the app to your SidecarTridge’s microSD card.
5. Once installed, select the app and click **"Launch"** to activate it.

> **⚠️ WARNING:** Booster Loader is currently in **alpha**. Use at your own risk.

After launching, the app will automatically run every time your Atari computer is powered on.

## 🕹️ Usage

When you boot your Atari ST/STE/Mega ST/Mega STe, the app displays a **setup screen** for 5 seconds.  
If no key is pressed, the emulator will start emulating the floppy and hard disk drives configured in the setup screen.

This menu will pop up every time you power on your Atari computer, but not when you reset it. If you want to enter into this menu without powering off your Atari, you can press the **`SELECT`** button on your Multi-device and press the reset button on your Atari.

## ⚙️ Setup Screen

### Information on the Setup Screen

The setup screen displays the following information:
- **Emulator Version**: The version of the Drives Emulator app.
- **Network Status**: Indicates whether the app is connected to the network and the local IP address of the SidecarTridge Multi-device.
- **USB Mass Storage Status**: Indicates whether the SidecarTridge Multi-device is connected to the computer via USB and the current status of the USB mass storage device connected. 

### GEMDrive Hard Disk Emulation

#### What is GEMDrive?

The Multi-device introduces a hard disk emulation feature for the Atari ST, offering a significant storage solution without the necessity for an actual hard disk. Distinct from other methods, the Multi-device uniquely facilitates hard disk emulation by integrating the Atari ST's file system with that of a microSD card, managed by the RP2040 microcontroller. This method presents several benefits and drawbacks:

- **Advantages**:
  - Unlimited hard disk size, allowing the use of the full capacity of the microSD card.
  - Not affected by the infamous Bad-DMA issue, as the Multi-device doesn't rely on the Atari ST's DMA controller.
  - Compatibility across TOS versions 1.00 to 2.06 and EmuTOS.
  - Enables organizing files into folders on the microSD card, simulating multiple hard disks on a single card.
  - Facilitates easy file transfer between the microSD card and computers (PC/Mac/Linux).
  - Requires less or no memory compared to other emulation drivers.
  
- **Disadvantages**:
  - Writing operations to the hard disk are slower than reading due to the slower protocol communication with the RP2040 during write operations.
  - Not all software is compatible, particularly those making direct hardware calls to the hard disk, as the Multi-device emulates hard disk functions by intercepting GEMDOS calls.
  - The emulation driver is less mature, potentially leading to bugs or issues during use.

Despite these challenges, the benefits of Hard Disk Emulation often surpass the drawbacks, providing a reliable storage solution. Moreover, with ongoing development, the Multi-device is poised for further enhancements, promising an even more robust and user-friendly experience in the future.

The concept for the GEMdrive hard disk emulation originated with the GEMDOS component of the Hatari emulator, though it's worth noting that there exists a GemDrive for the ACSI2STM project, which serves a different purpose. Initially, the plan was to borrow the GEMDOS implementation from Hatari and adapt it for use with the Multi-device. However, this strategy proved unfeasible due to the Hatari emulator's capability for extensive interaction with both the Atari ST's internals and the host computer—capabilities that the Multi-device, as a peripheral, cannot match due to its need to adhere to the Atari ST's hardware constraints. The GEMDOS code from Hatari was ultimately deemed too intricate and too intertwined with the emulator itself for direct application in the Multi-device environment. Nevertheless, the exploration of Hatari's GEMDOS code was highly informative, leading to the development of a bespoke GEMdrive code specifically tailored for the Multi-device.

#### GEMDrive Related Setup Screen Commands

| Command | Description |
|---------|-------------|
| **[G]EMDRIVE** | Enable or disable GEMDrive emulation. |
| **F[o]lder** | Select the folder for the GEMDrive. It allows to navigate through the microSD card's directory structure. |
| **[D]rive** | Choose the drive letter for the GEMDrive (e.g., `C:`). Change it if there is a conflict with other hard disk drivers. |

### Floppy Drive Emulation

The Floppies Emulation represents a significant enhancement to the Multi-device. With this, the Atari ST can interface with floppy images on a microSD card as though they were actual floppy disks. Here's how to get started with Floppies Emulation.

#### Floppy Drive Related Setup Screen Commands

| Command | Description |
|---------|-------------|
| **[F]loppy** | Enable or disable Floppy emulation. |
| **Fo[l]der** | Select the base folder for the Floppy images. It allows to navigate through the microSD card's directory structure. |
| **[A] Drive** | Select the .ST (Read only) or .ST.RW  (Read/Write) image file to use as the floppy disk. It  allows to navigate through the microSD card's directory structure. |
| **[B] Drive** | Select the .ST (Read only) or .ST.RW  (Read/Write) image file to use as the second floppy disk. It allows to navigate through the microSD card's directory structure. |
| **[SHIFT+A] Drive** | Unmount the floppy disk image from the A: drive. |
| **[SHIFT+B] Drive** | Unmount the floppy disk image from the B: drive. |
| **Boo[t] enabled** | Enable or disable the boot sector emulation. When enabled, the emulator will attempt to boot from the floppy disk image. |
| **XBIO[S] trap** | Enable or disable the XBIOS trap for floppy disk operations. When enabled, the emulator will intercept XBIOS calls related to floppy disk operations. |
| **Format [I]mage** | Format a new floppy disk image. It can format image sizes of 360KB (DS), 720KB (DD), 1.44MB (HD), and 2.88MB (ED). The image will be created in the selected folder with a given name plus the extension `.ST.RW`. It will be created empty. |
| **[C]onvert MSA to ST** | Convert a floppy disk image from MSA format to ST format. The converted image will be created in the selected folder with the same name plus the extension `.ST`. |

### Real Time Clock Emulation

Temporarily disabled.

### Other Setup Screen Commands

| **[E]xit to Desktop** | Exit to desktop and start the emulation |
| **[X] Return to the Booster menu** | Exit setup and return to the Booster Loader main menu. |

### ⬇️ Browsing the microSD Card

The internal browser allows you to navigate through the microSD card's directory structure. You can select folders and files using the keyboard:
| Key | Action |
|-----|--------|
| **`UP`** | Move up in the directory structure |
| **`DOWN`** | Move down in the directory structure |
| **`LEFT`** | Move to the previous page of the directory structure |
| **`RIGHT`** | Move to the next page of the directory structure |
| **`ENTER`** | Enter into a folder, or go to the partent folder if you are not in the root folder |
| **`SPACE`** | Select a file or folder, and then exit with the newly selected item. |

As a rule of thumb, **`SPACE`** will select the current item. So, if you want to choose a new folder, navigate to it, press **`ENTER`** to enter it, and then press **`SPACE`** to select it. If you want to select a file, navigate to it, and then press **`SPACE`** to select it.

### 💾 Concurrent USB Mass Storage

The Multi-device supports **simultaneous USB mass storage access**, allowing you to read and write to the microSD card *while the emulator is running*. You can copy files to and from the card without pausing or interrupting the emulator.

For example, if you are developing an application, you can compile it on your computer, test it in an Atari ST emulator (such as Hatari or STEEM), and then simply copy the finished binary to the mounted USB drive. **GEMDRIVE** will automatically detect the new file and make it available to the Atari ST—no need to restart the emulator or the Atari itself.

This provides a fast, seamless workflow for development and testing.

It's recommened to connect the Multi-device to your computer via USB before launching the emulator. 

### 🚀 Exiting to Desktop

Pressing **`E`** on the setup screen will exit the emulator and return to the Atari desktop enabling the hard or floppy drives emulation. 

To return to the setup screen, press **`SELECT`** on your Multi-device and reboot. Or simply power off your Atari and power it on again.

### 🔁 System Reset Behavior

The Drives Emulator app is **resistant to system resets**. Pressing the reset button on your Atari will continue emulating the hard disk and floppy drives, maintaining the current state of the emulator.

### 🔌 Power Cycling

The Drives Emulator app is designed to return to the setup screen after a power cycle. When you power off and on your Atari, the app will display the setup screen again, allowing you to configure the emulator or launch it with the last used settings.


## 🛠️ Setting Up the Development Environment

This project is based on an early version of the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).  
To set up your development environment, please follow the instructions provided in the [official documentation](https://docs.sidecartridge.com/sidecartridge-multidevice/programming/).

## Missing features in ALPHA version

- [ ] Support for Disk Swapping (changing floppy disk images on the fly).
- [ ] Support for Downloading images from the internet repository.
- [ ] Support for Read-Only GEMDRIVE (currently, it is read/write).
- [ ] Support for Real Time Clock emulation (currently, it is disabled).


## 📄 License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](https://github.com/sidecartridge/md-drives-emulator/blob/main/LICENSE) file for full terms.

## 🤝 Contributing
Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: RTC Emulator](/sidecartridge-multidevice/microfirmwares/rtc_emulator/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Multidevice Test](/sidecartridge-multidevice/microfirmwares/multidevice-test/){: .btn }