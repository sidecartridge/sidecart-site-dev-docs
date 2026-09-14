---
layout: default
title: Apps Catalog
nav_order: 1
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares
  - /microfirmwares/
  - /apps
  - /apps/
  - /sidecartridge-multidevice/apps
  - /sidecartridge-multidevice/apps/
toc: false
has_toc: false
---

# Apps Catalog
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

![Image showing the terminal-based microfirmware launcher on the Atari ST, with instructions to press ESC to enter the menu and hold SHIFT to boot from GEMDOS](/sidecartridge-multidevice/assets/images/BOOSTER-TERMINAL-SELECTOR.png)

### Available Microfirmware Apps

The full, always up to date catalog of Microfirmware apps lives in the online Apps Store. It reads the same public repository the Booster app uses, so the list you see there matches exactly what you can install on your device, including alpha and beta builds.

<div data-md-store-carousel data-platform="atari-st">
  <a href="https://md-store.sidecartridge.com/#atari-st">Browse all apps in the Store</a>
</div>
<script src="https://md-store.sidecartridge.com/widget/carousel.js" defer></script>

<a href="https://md-store.sidecartridge.com/" class="btn btn-purple fs-5" target="_blank" rel="noopener" style="margin: 1rem 0; display: inline-block;">Browse the Apps Store</a>

Every app in the Store links back to its documentation page here in the docs. You can also open any app page directly from the navigation sidebar on the left.

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

The quickest way in is the [Build a microfirmware](https://md-store.sidecartridge.com/build/) tutorial, a guided walkthrough from an empty template to an app listed in the Store. For the low-level reference, there is a [template repository](https://github.com/sidecartridge/md-microfirmware-template) and the [Programming Guide](/sidecartridge-multidevice/programming/).

Each Microfirmware app should be a self-contained program that can run on the RP2040 or RP235x chip. It should include the necessary code to read the microSD card, communicate with the computer, and provide any additional features you want. 

### Reporting Issues

If you encounter any issues or bugs while using the Microfirmware apps, please report them to help us improve the software. You can find the list of issues and report new ones in the [Issues and Bug Reporting](/sidecartridge-multidevice/issues/) section.


[Previous: User Guide](/sidecartridge-multidevice/userguide_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: ROM Emulator](/sidecartridge-multidevice/microfirmwares/rom_emulator/){: .btn }
