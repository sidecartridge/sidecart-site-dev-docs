---
layout: default
title: SidecarTridge Multi-device MV16 Emulator V2.0
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/mv16-emulator/
  - /microfirmwares/mv16-emulator
---

# SidecarTridge Multi-device MV16 Emulator
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-mv16-emulator){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-mv16-emulator/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-mv16-emulator/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_MV16_EMULATOR_VERSION }}](){: .label .label-purple }

This is a microfirmware application for the **SidecarTridge Multi-device**, designed to emulate the **MV-16 audio device** for Atari computers, including the **Atari ST, STe, Mega ST, and Mega STe**.

The original **MV-16** was a small expansion cartridge bundled with the game **B.A.T.** and capable of playing sampled sounds with up to **16 voices**. This microfirmware recreates that hardware behavior and routes the resulting audio to a **Bluetooth audio stream**.

{: .warning }
This microfirmware is currently an **experiment**. Audio quality, compatibility, and overall behavior can still be improved. It is also a good starter project for new developers who want to learn how to build software for the **SidecarTridge Multi-device**.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 🚀 Installation

To install the MV16 Emulator app on your SidecarTridge Multi-device:

1. Launch the **Booster App** on your SidecarTridge Multi-device.
2. Open the Booster web interface.
3. In the **Apps** tab, select **"MV16 Emulator"** from the list of available apps.
4. Click **"Download"** to install the app to your SidecarTridge's microSD card.
5. Once installed, select the app and click **"Launch"** to activate it.

After launching, the app will automatically run every time your Atari computer is powered on.

## 🕹️ Usage

When the application starts, it opens a simple terminal menu on the Atari ST.

From there, the default action is to start scanning for nearby Bluetooth audio devices. Once a device is found and selected, the firmware connects to it and starts the **A2DP audio path**.

After the connection is established, you can:

- return to the desktop while keeping the Bluetooth side active
- scan again for another device
- jump to the Booster application
- exit the application completely

The intended workflow is simple: launch the app, connect audio, and continue using the computer.

### ⚙️ Setup Screen Commands

| Command | Description |
|---------|-------------|
| **[S]can** | Start scanning for nearby Bluetooth audio devices. |
| **[E]xit to Desktop** | Exit to the desktop while keeping the Bluetooth side active. |
| **[X] Return to the Booster menu** | Exit setup and return to the Booster Loader main menu. |

### 🔁 System Reset Behavior

The app is **resistant to system resets**. Pressing the reset button on your Atari does not make the app exit or lose its state. It continues running and keeps the Bluetooth audio connection active, so you can reset the Atari without interrupting audio playback.

### 🔌 Power Cycling

When you power off and on your Atari, the app starts again and attempts to reconnect to the last paired Bluetooth audio device. This reduces the amount of setup needed between sessions.

### ❌ SELECT Button Behavior

Pressing the **SELECT** button on your SidecarTridge Multi-device returns the app to its main menu. From there, you can scan again, leave to the desktop, or jump back to the Booster Loader.

## 🛠️ Setting Up the Development Environment

This project is based on the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).

To set up your development environment, follow the instructions in the [official programming documentation](https://docs.sidecartridge.com/sidecartridge-multidevice/programming/).

The repository also includes additional build notes for contributors. In its current setup, local builds expect the **Arm GNU Toolchain**, **Pico SDK**, and **Pico Extras** to be configured before running the build script.

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

See the [LICENSE](https://github.com/sidecartridge/md-mv16-emulator/blob/main/LICENSE) file for full terms.

## 🤝 Contributing

Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: Microfirmwares](/sidecartridge-multidevice/microfirmwares/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: ROM Emulator](/sidecartridge-multidevice/microfirmwares/rom_emulator/){: .btn }
