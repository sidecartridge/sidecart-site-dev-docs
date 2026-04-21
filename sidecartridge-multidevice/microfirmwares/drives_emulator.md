---
layout: default
title: SidecarTridge Multi-device Drives Emulator
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

[Source code](https://github.com/sidecartridge/md-drives-emulator){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-drives-emulator/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-drives-emulator/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_DRIVES_EMULATOR_VERSION }}](){: .label .label-purple }

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

After launching, the app will automatically run every time your Atari computer is powered on.

## 🕹️ Usage

When you boot your Atari ST/STE/Mega ST/Mega STe, the app displays a **setup screen** for 5 seconds.  
If no key is pressed, the emulator will start emulating the floppy and hard disk drives configured in the setup screen.

This menu will pop up every time you power on your Atari computer, but not when you reset it. If you want to enter into this menu without powering off your Atari, you can press the **`SELECT`** button on your Multi-device and press the reset button on your Atari.

During normal runtime, a short press on **`SELECT`** can also cycle floppy **A:** to the next configured image if you have configured multiple images for drive A.

On first use, the microfirmware automatically creates the default folders it needs on the microSD card if they do not already exist:
- `/hd` for GEMDrive hard disk emulation
- `/floppies` for floppy image emulation

You can change both folders later from the setup screen.

## ⚙️ Setup Screen

### Information on the Setup Screen

The setup screen displays the following information:
- **Emulator Version**: The version of the Drives Emulator app.
- **Boot information line**: The bottom line shows the setup countdown, `Countdown stopped. Press [E] or [X] to continue.`, or `USB Mass Storage Connected` when the device is mounted over USB.

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
| **F[o]lder** | Select the folder for the GEMDrive. By default, the emulator uses `/hd` and creates it automatically on first use if needed. You can change it at boot time by navigating through the microSD card's directory structure. |
| **[D]rive** | Choose the drive letter for the GEMDrive (e.g., `C:`). Change it if there is a conflict with other hard disk drivers. |

### ACSI Hard Disk Emulation (Experimental)

#### What is ACSI Emulation?

In addition to GEMDrive, the Multi-device can emulate **ACSI** hard disks at the block-device level, driven by a raw disk image file on the microSD card. Unlike GEMDrive, which intercepts GEMDOS calls and presents a folder as a drive, the ACSI path emulates the disk at the BIOS level and hands TOS a real partition table plus BPBs.

This feature is currently marked **EXPERIMENTAL** and is disabled by default.

- **Advantages**:
  - Works with software that talks to the hard disk at the BIOS level rather than through GEMDOS.
  - Announces a real partition table with up to 14 FAT16 partitions (`C:`..`P:`).
  - A single image file can be mounted instead of using one folder per partition on the microSD card.

- **Disadvantages**:
  - Maximum partition and image size is bounded by the FAT16 limits of the image format.
  - Moving files in and out of the image requires either USB Mass Storage from the setup screen or a host-side image editor.
  - This path is less battle-tested than GEMDrive and should still be considered experimental.

This release has been tested from **TOS 1.04 through TOS 2.06**. It does **not** currently work under **EmuTOS**.

The ACSI bus ID and the starting drive letter are configured independently. This lets the emulator coexist with a real ACSI device if you give the emulated unit a free ACSI ID and choose a drive-letter range that does not conflict with other hard disk drivers.

#### ACSI Related Setup Screen Commands

| Command | Description |
|---------|-------------|
| **A[C]SI Enabled** | Enable or disable ACSI block-device emulation. Toggling this setting may trigger a warm reset so the required RAM pool can be reserved or released. |
| **[I]mage** | Select the hard disk image file on the microSD card to mount. |
| **U[n]it (ACSI ID)** | Choose the ACSI bus ID reported to TOS (`0` to `7`). Default is `7`. |
| **Dri[v]e** | Choose the starting drive letter for the first announced partition (`C:` to `P:`). Subsequent partitions take consecutive letters. |

### Floppy Drive Emulation

The Floppies Emulation represents a significant enhancement to the Multi-device. With this, the Atari ST can interface with floppy images on a microSD card as though they were actual floppy disks. Here's how to get started with Floppies Emulation.

#### Floppy Drive Related Setup Screen Commands

| Command | Description |
|---------|-------------|
| **[F]loppy** | Enable or disable Floppy emulation. |
| **Fo[l]der** | Select the base folder for the Floppy images. By default, the emulator uses `/floppies` and creates it automatically on first use if needed. You can change it at boot time by navigating through the microSD card's directory structure. |
| **[A] Drive** | Select the .ST (Read only) or .ST.RW (Read/Write) image file to use as the floppy disk. |
| **[CTRL+A] Configure multiple images** | Configure up to 10 persistent images for floppy drive A. Slot 1 is the main **[A] Drive** image; slots 2..10 are optional extra images. |
| **[B] Drive** | Select the .ST (Read only) or .ST.RW (Read/Write) image file to use as the second floppy disk. |
| **[SHIFT+A] Drive** | Unmount the floppy disk image from the A: drive. |
| **[SHIFT+B] Drive** | Unmount the floppy disk image from the B: drive. |
| **Boo[t] enabled** | Enable or disable the boot sector emulation. When enabled, the emulator will attempt to boot from the floppy disk image. |
| **XBIO[S] trap** | Enable or disable the XBIOS trap for floppy disk operations. When enabled, the emulator will intercept XBIOS calls related to floppy disk operations. |

Formatting floppy images and converting `.MSA` images to `.ST` are no longer done from the Drives Emulator setup menu. Use the [File & Download Manager](/sidecartridge-multidevice/microfirmwares/browser/) microfirmware for those maintenance tasks.

#### Runtime floppy A image cycling

Floppy drive **A:** can keep a persistent list of up to **10 images**:

- **Slot 1** is always the normal **[A] Drive** image.
- **Slots 2..10** are configured through **[CTRL+A] Configure multiple images** in the setup menu.
- The slot list is stored in flash and survives power cycles.

When the emulator is already running:

- A short press on **`SELECT`** cycles floppy **A:** to the next configured slot.
- Empty slots are skipped automatically.
- After the last configured slot, cycling wraps back to slot 1.
- The Pico W LED flashes the active slot number so you can see which image was selected.

If only slot 1 is configured, a short **`SELECT`** press does nothing during runtime.

### Real Time Clock Emulation

The Real Time Clock (RTC) emulation allows the Multi-device to emulate RTC functionality for Atari ST computers, enabling accurate timekeeping and date management.

When RTC is enabled, the emulator can also synchronize the internal RP2040 clock with an NTP server during boot. The WiFi STA stack is started only on demand for this RTC/NTP flow and is shut down again immediately afterward.

If WiFi is not configured in STA mode, or if the NTP sync fails, the emulator still continues into normal emulation.

Please refer to the [RTC Emulator documentation](/sidecartridge-multidevice/microfirmwares/rtc_emulator/) for more details on how to use this feature.

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

### 💾 USB Mass Storage

USB mass storage is currently available only while you are in the **setup menu**.

You can read and write the microSD card from your computer during setup without interrupting the setup screen.

The USB device is exposed as a pure **MSC** device. The old composite CDC + MSC configuration is no longer used.

When USB mass storage is mounted, the Pico W green LED stays on. During active USB read/write traffic, the LED turns off and then returns on again when the transfer finishes.

It is recommended to connect the Multi-device to your computer via USB before launching the emulator.

### 🚀 Exiting to Desktop

Pressing **`E`** on the setup screen will exit the emulator and return to the Atari desktop enabling the hard or floppy drives emulation.

If RTC is enabled, the emulator may briefly initialize WiFi at this point to obtain the NTP time before continuing.

To return to the setup screen, press **`SELECT`** on your Multi-device and reboot. Or simply power off your Atari and power it on again.

### 🔁 System Reset Behavior

The Drives Emulator app is **resistant to system resets**. Pressing the reset button on your Atari will continue emulating the hard disk and floppy drives, maintaining the current state of the emulator.

### 🔌 Power Cycling

The Drives Emulator app is designed to return to the setup screen after a power cycle. When you power off and on your Atari, the app will display the setup screen again, allowing you to configure the emulator or launch it with the last used settings.

### ⚙️ Advanced Features

#### Changing the speed of the microSD card 

The speed of the microSD is measured in the megahertzs (MHz) of the Serial Peripheral Interface (SPI) bus that connects the RP2040 microcontroller to the microSD card. The range of speeds supported by the Multi-device is from 1 MHz to 24 MHz. The default speed is set to 12.5 MHz, which is a good balance between performance and stability.

The microSD card speed is a global setting that applies not only to the GEMDRIVE and Floppy emulation, but also to all the other microfirmwares that use the microSD card. Hence, this paremeter is set in the **Booster App** and not in the Drives Emulator app.

To modify the microSD card speed, follow these steps:
1. Launch the **Booster App** on your SidecarTridge Multi-device. If you are not already in the Booster App, press the **`X`** button on your Multi-device to return to the Booster menu.
2. Open the Booster web interface.
3. In the **"Config"** tab, locate the **"SD card bus speed (KHz)"** setting and adjust it to your desired value. The value is in kilohertz (KHz), so for example, if you want to set the speed to 24 MHz, enter `24000`.
4. Click **"Save"** to apply the changes.
5. Go back to the **"Apps"** tab and launch the **"Drives Emulator"** app again.

{: .warning}
Any value below 1Mhz will be discarded and the speed will be set to 1 MHz. Same for values above 24 MHz, which will be set to 24 MHz.

**It's relatively safe to set the speed to 24 MHz**, but if you experience issues with the emulator, try lowering the speed to 12.5 MHz or even 6 MHz. Any modern microSD card should be able to handle these speeds without issue.

## What changed in v1.1.0

Highlights of version **v1.1.0**:

- experimental **ACSI block-level hard disk emulation** was added
- floppy **A:** now supports **multiple persistent image slots** and runtime cycling with **`SELECT`**
- RTC / NTP networking now starts **only on demand** instead of on every boot
- USB Mass Storage was simplified to a pure **MSC** device
- floppy image formatting and `.MSA` to `.ST` conversion were removed from this setup menu and are now expected to be handled through the File & Download Manager microfirmware
- several stability, performance, FAT16, and write-path fixes were introduced in the emulator core


## 📄 License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](https://github.com/sidecartridge/md-drives-emulator/blob/main/LICENSE) file for full terms.

## 🤝 Contributing
Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: RTC Emulator](/sidecartridge-multidevice/microfirmwares/rtc_emulator/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Multidevice Test](/sidecartridge-multidevice/microfirmwares/multidevice-test/){: .btn }
