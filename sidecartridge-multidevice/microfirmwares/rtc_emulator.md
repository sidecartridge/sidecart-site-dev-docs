---
layout: default
title: SidecarTridge Multi-device Real Time Clock Emulator V2.0
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/rtc_emulator/
  - /microfirmwares/rtc_emulator
---

# SidecarTridge Multi-device Real Time Clock Emulator
{: .no_toc }

This is a microfirmware application for the **SidecarTridge Multi-device**, designed to emulate a Real Time Clock (RTC) for Atari computers, including the **Atari ST, STe, Mega ST, and Mega STe**.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## 🚀 Installation

To install the RTC Emulator app on your SidecarTridge Multi-device:

1. Launch the **Booster App** on your SidecarTridge  Multi-device..
2. Open the Booster web interface.
3. In the **Apps** tab, select **"Real Time Clock"** from the list of available apps.
4. Click **"Download"** to install the app to your SidecarTridge’s microSD card.
5. Once installed, select the app and click **"Launch"** to activate it.

> **⚠️ WARNING:** Booster Loader is currently in **alpha**. Use at your own risk.

After launching, the app will automatically run every time your Atari computer is powered on.

## 🕹️ Usage

When you boot your Atari ST/STE/Mega ST/Mega STe, the app displays a **setup screen** for 5 seconds.  
If no key is pressed, the emulator will attempt to fetch the current time from the configured NTP server.

> Pressing any key will stop the countdown and keep the setup screen open.

### ⚙️ Setup Screen Commands

| Command | Description |
|---------|-------------|
| **[H]ost NTP** | Set the NTP server hostname (default: `pool.ntp.org`). |
| **[P]ort NTP** | Set the NTP server port (default: `123`). |
| **[U]TC Offset** | Set UTC offset in hours (e.g., `1` for CET, `2` for CEST). |
| **[Y]2K Patch** | Enable or disable the Y2K patch (default: **Enabled**). Disabling it may cause incorrect dates on older TOS versions. |
| **[T]ype** | Select the RTC emulation type: `SIDECART` (native SidecarTridge RTC) or `DS1307` (compatible interface). |
| **[E]xit to Desktop** | Exit setup and start the emulator. Time will be fetched and applied to the Atari clock. |
| **[X] Return to the Booster menu** | Exit setup and return to the Booster Loader main menu. |

### 🔁 System Reset Behavior

The RTC Emulator app is **resistant to system resets**. Pressing the reset button on your Atari will not stop the app — it will continue updating the system clock.

### 🔌 Power Cycling

Every time the Atari is powered on, the setup screen will be shown briefly before the app proceeds to fetch the current time.

### ❌ Time Fetch Failure

If the app cannot fetch a valid time from the NTP server:
- An error message will be displayed.
- The system clock will not be updated.
- You will be returned to the setup screen.

To proceed without a valid time, press **`E`** to exit setup and launch the app manually.

> ⚠️ Please ensure your network connection is properly configured before launching the app.

## 🛠️ Setting Up the Development Environment

This project is based on the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).  
To set up your development environment, please follow the instructions provided in the [official documentation](https://docs.sidecartridge.com/sidecartridge-multidevice/programming/).


## 📄 License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](https://github.com/sidecartridge/md-rtc-emulator/blob/main/LICENSE) file for full terms.

## 🤝 Contributing
Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: ROM Emulator](/sidecartridge-multidevice/microfirmwares/rom_emulator/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Drives Emulator](/sidecartridge-multidevice/microfirmwares/drives_emulator/){: .btn }