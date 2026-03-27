---
layout: default
title: Microfirmwares for the Firmware V2.0 
nav_order: 3
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares
  - /microfirmwares/
toc: false
has_toc: false
---

# Microfirmwares for the Firmware V2.0 
{: .no_toc }
{: .d-inline-block }

{{ site.FIRMWARE_VERSION }}
{: .label .label-purple }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Microfirmwares

### What is a microfirmware?

A Microfirmware app is a small, self-contained program that runs on a standalone RP2040 or RP235x chip, along with a companion firmware on your computer that talks to it. Together, they provide the features of the device.

### Launching microfirmwares from the Atari ST terminal
Starting with Booster v2.1.0 you can launch any microfirmware that is already downloaded even when Wi-Fi is unavailable. When the Manager screen appears on the Atari ST:

- Press `ESC` to enter the terminal-driven apps workflow. Use the keyboard to pick the microfirmware you want to boot.
- Hold any `SHIFT` key if you simply want to keep booting from GEMDOS without touching the web UI.

This offline-safe launcher is useful when the access point is down, the router blocks the device, or you just prefer not to open the web interface.

### Available Microfirmware Apps

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; margin-top: 1rem;">

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>📀 <a href="/sidecartridge-multidevice/microfirmwares/rom_emulator/">ROM Emulator</a></h3>
<p>An emulator for ROM files. Run games and apps from microSD or a remote server.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>⏰ <a href="/sidecartridge-multidevice/microfirmwares/rtc_emulator/">Real Time Clock Emulator</a></h3>
<p>Provides RTC functionality, syncs with NTP servers, and emulates a DS1307 chip.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>💾 <a href="/sidecartridge-multidevice/microfirmwares/drives_emulator/">Drives Emulator</a></h3>
<p>Emulates hard and floppy drives with microSD-stored images. Includes RTC emulator.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>🎵 <a href="/sidecartridge-multidevice/microfirmwares/mv16-emulator/">MV16 Emulator</a></h3>
<p>Emulates the MV-16 audio device and routes its output to Bluetooth audio streaming.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>🧪 <a href="/sidecartridge-multidevice/microfirmwares/multidevice-test/">Multi-device Test ROM</a></h3>
<p>A diagnostic tool to validate functionality and performance of your device.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>🌐 <a href="/sidecartridge-multidevice/microfirmwares/browser/">File & Download Manager</a></h3>
<p>Browse and download from the public floppy DB. Manage files on your microSD card.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>🐞 <a href="/sidecartridge-multidevice/microfirmwares/debug-cart/">Debug Cart</a></h3>
<p>Expose debug output from Atari ST-family software through the cartridge port over USB serial.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>🎨 <a href="/sidecartridge-multidevice/microfirmwares/gpu-demo/">GPU Demo</a></h3>
<p>Showcases RP2040 graphics: real-time sprites and tiles in Atari ST/STE modes.</p>
</div>

<div style="background:#f8f9fa; border-radius:12px; padding:1rem; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
<h3>🕹️ <a href="/sidecartridge-multidevice/microfirmwares/oric-emulator/">Oric Emulator</a></h3>
<p>Emulates an Oric computer on Atari ST-class machines via the Multi-device.</p>
</div>

</div>

### How it works:

### Microfirmware App Core
This is the main program running on the RP2040 chip. It manages things like reading the microSD card, talking to the computer, and (if needed) providing a web interface.

#### Global Settings
These are settings for the whole device, stored in flash memory. The Microfirmware app reads them to know how the device is configured, but does not change them.

#### Local Settings
Each Microfirmware app can have its own settings, also stored in flash. These are used just by that app, so one app’s settings won’t affect another.

#### Computer Firmware
On the computer side, there is a small program (called the Booster app) that acts as a terminal and communicates with the Microfirmware app. Because this runs in the computer’s ROM, it’s harder to update and debug. Most testing and debugging happens on the Microfirmware app side.

The Booster App is designed to manage the Microfirmware apps on the device, allowing users to download, install, update, and launch them easily. It also provides a web interface for managing the apps.

The available Microfirmware apps are listed in a public repository, which the Booster app connects to. Users can browse and install apps from this repository, or upload their own apps to the device. They can also install their own repository for themselves or others to use.

### Developing Microfirmware Apps

To develop your own Microfirmware apps, there is a  [template repository](https://github.com/sidecartridge/md-microfirmware-template) and follow the instructions in the [Programming Guide](/sidecartridge-multidevice/programming/).

Each Microfirmware app should be a self-contained program that can run on the RP2040 or RP235x chip. It should include the necessary code to read the microSD card, communicate with the computer, and provide any additional features you want. 

### Reporting Issues

If you encounter any issues or bugs while using the Microfirmware apps, please report them to help us improve the software. You can find the list of issues and report new ones in the [Issues and Bug Reporting](/sidecartridge-multidevice/issues/) section.


[Previous: User Guide](/sidecartridge-multidevice/userguide_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: ROM Emulator](/sidecartridge-multidevice/microfirmwares/rom_emulator/){: .btn }
