---
layout: default
title: SidecarTridge Multi-device ROM Emulator V2.0
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/rom_emulator/
  - /microfirmwares/rom_emulator
---

# SidecarTridge Multi-device ROM Emulator
{: .no_toc }

This is a microfirmware application for the **SidecarTridge Multi-device**, designed to emulate a ROM cartridge for Atari computers, including the **Atari ST, STe, Mega ST, and Mega STe**.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## 🚀 Installation

To install the ROM Emulator app on your SidecarTridge Multi-device:

1. Launch the **Booster App** on your SidecarTridge  Multi-device..
2. Open the Booster web interface.
3. In the **Apps** tab, select **"ROM Emulator"** from the list of available apps.
4. Click **"Download"** to install the app to your SidecarTridge’s microSD card.
5. Once installed, select the app and click **"Launch"** to activate it.

> **⚠️ WARNING:** Booster Loader is currently in **alpha**. Use at your own risk.

After launching, the app will automatically run every time your Atari computer is powered on.

## 🕹️ Usage

If there is no ROM binary file loaded, the app will display a **setup screen**. If there is already a ROM loaded, the app will attempt to run it immediately after powering on your Atari. To return to the setup screen, press **`SELECT`** on your Multi-device and reboot.

### ⚙️ Setup Screen Commands

| Command | Description |
|---------|-------------|
| **[B]rowse** | Browse the ROM files on the microSD card. |
| **[D]ownload** | Download a ROM file from the internet. |
| **[S]ettings** | Configure the low level settings for the ROM emulator. |
| **[R]Ripper** | Enable or Disable the Delay/Ripper mode. It does not load the ROM file until the **`SELECT`** button is pressed. |
| **[L]aunch** | Launch the selected ROM file, if available. |
| **[E]xit to Desktop** | Exit to desktop without loading the ROM. |
| **[X] Return to the Booster menu** | Exit setup and return to the Booster Loader main menu. |

### ⬇️ Browsing or Downloading ROM Files

When you select the **[B]rowse** option, the app will display a list of available ROM files on the microSD card. You can navigate through the list using the keyboard and select a ROM file to load it.
When you select the **[D]ownload** option, the app will show you the list of available ROM files from the internet. You can select a ROM file to download it to your microSD card.

### 🚀 Launching a ROM

When you select the **[L]aunch** option, the app will attempt to run the selected ROM file. If the ROM is valid and compatible, it will be loaded into memory and executed. The computer will then behave as if the ROM was loaded from a physical cartridge, even after a power cycle or reset.

To return to the setup screen, press **`SELECT`** on your Multi-device and reboot.

### 🔁 System Reset Behavior

The ROM Emulator app is **resistant to system resets**. Pressing the reset button on your Atari will load again the ROM file, if available, or return to the setup screen if no ROM is loaded. 

### 🔌 Power Cycling

The ROM Emulator app is designed to be **persistent across power cycles**. When you power off and on your Atari, the app will automatically load the last selected ROM file, if available, or return to the setup screen if no ROM is loaded.

### ❌ Delay/Ripper Mode

The ROM Emulator app includes a **Delay/Ripper mode** that allows you to load the ROM file only when you press the **`SELECT`** button on your Multi-device. This is useful for debugging or testing purposes, as it prevents the ROM from being loaded automatically when the app starts.
To enable or disable the Delay/Ripper mode, select the **[R]Ripper** option in the setup screen. When enabled, the app will not load the ROM file until you press the **`SELECT`** button.

The Ripper mode was useful combined with tools like [Ultimate Ripper](https://www.atarimania.com/utility-atari-st-ultimate-ripper_s20034.html). To use it, follow these steps:
1. Download the Ultimate Ripper ROM file from the internet repository (option `D`).
2. Enable the Ripper mode in the setup screen (option `R`).
3. Launch the Ultimate Ripper ROM file (option `L`).
4. Now reset or power cycle your Atari computer and load your own application or game.
5. When you want to rip the ROM, press the **`SELECT`** button on your Multi-device. The game or application should continue running.
6. Reset (not power cycle) your Atari computer. The screen will look like it is frozen. Now, you have can press F1 (move memory to allocate the ripper program) or F2 (use memory available to allocate the ripper program) to enter the Ultimate Ripper menu.

## 🛠️ Setting Up the Development Environment

This project is based on an early version of the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).  
To set up your development environment, please follow the instructions provided in the [official documentation](https://docs.sidecartridge.com/sidecartridge-multidevice/programming/).


## 📄 License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](https://github.com/sidecartridge/md-rom-emulator/blob/main/LICENSE) file for full terms.

## 🤝 Contributing
Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: Microfirmwares](/sidecartridge-multidevice/microfirmwares/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: RTC Emulator](/sidecartridge-multidevice/microfirmwares/rtc_emulator/){: .btn }