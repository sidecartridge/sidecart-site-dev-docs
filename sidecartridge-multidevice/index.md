---
layout: home
title: SidecarTridge Multi-device
nav_order: 0
nav_exclude: false
has_children: true
---


![SidecarTridge Multi-device](/sidecartridge-multidevice/assets/images/BOARD-3.1-PICOW-PERSPECTIVE.png)

# SidecarTridge Multi-device Documentation 
{: .d-inline-block }

STABLE-{{ site.FIRMWARE_VERSION }}
{: .label .label-green }

{{ site.FIRMWARE_ALPHA_VERSION }}
{: .label .label-purple }


Welcome to the SidecarTridge Multi-device Documentation! This comprehensive guide is aimed at providing developers with all the information needed to get started with the SidecarTridge Multi-device board, understand its architecture, and contribute to its development. Please refer to the relevant sections below to explore specific topics.

You can learn about the hardware evolution of the SidecarTridge Multi-device in this video:

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/RvREQNScEzE?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


## 🚀 Latest STABLE Firmware: {{ site.FIRMWARE_VERSION }}
* **💾 [Download STABLE Release {{ site.FIRMWARE_VERSION }}](https://sidecartridge.com/downloads)**
* **📝 [Changelog for STABLE Release {{ site.FIRMWARE_VERSION }}](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/releases/tag/{{ site.FIRMWARE_VERSION }})**
* 🕒 [Older Versions](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/releases)

## 👉 [Do you want to test the new firmware?](#do-you-want-to-test-the-new-alpha-firmware)

## 🐞 Bugs, Issues, and Enhancements
* [Reporting tool](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/issues)

## Other Quick links
* [RP2040 firmware source code](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico)
* [Atari ST Configurator firmware source code](https://github.com/sidecartridge/atarist-sidecart-firmware)
* [Atari ST Floppy Emulator firmware source code](https://github.com/sidecartridge/atarist-sidecart-floppy-emulator)
* [Test ROM](https://github.com/sidecartridge/atarist-sidecart-test-rom)
* [Documentation site (this site)](https://github.com/sidecartridge/sidecart-site-dev-docs)

## Table of Contents

<table style="border-collapse: collapse; border: 0;">
    <tr>
        <td style="border: none;">
            <h3>📘 <a href="/sidecartridge-multidevice/introduction/">Introduction</a></h3>
            <p>An overview of the SidecarTridge Multi-device project, explaining the project's purpose, objectives, and the intended audience.</p>
        </td>
        <td style="border: none;">
            <h3>🚀 <a href="/sidecartridge-multidevice/getting_started/">Getting started</a></h3>
            <p>Guidance on the initial steps including prerequisites, board assembly instructions, setup and configuration.</p>
        </td>
        <td style="border: none;">
            <h3>⚙️ <a href="/sidecartridge-multidevice/userguide/">User Guide</a></h3>
            <p>Learn how to use the SidecarTridge Multi-device.</p>
        </td>
    </tr>
    <tr>
        <td style="border: none;">
            <h3>🏛️ <a href="/sidecartridge-multidevice/architecture_and_design/">Architecture and Design</a></h3>
            <p>Explore the underlying architecture and design principles of the SidecarTridge Multi-device board.</p>
        </td>
        <td style="border: none;">
            <h3>🔌 <a href="/sidecartridge-multidevice/hardware_interface/">Hardware interface</a></h3>
            <p>How the board and the code in the RP2040 handle the mismatch of the buses size between the RP2040 and the Atari ST cartridge.</p>
        </td>
        <td style="border: none;">
            <h3>💻 <a href="/sidecartridge-multidevice/software_development/">Software Development</a></h3>
            <p>Setting up the development environment, compiling the code, debugging, testing and building the firmware.</p>
        </td>
    </tr>
    <tr>
        <td style="border: none;">
            <h3>👨‍💻 <a href="/sidecartridge-multidevice/programming/">Programming SidecarTridge Multi-device</a></h3>
            <p>Learn about the ROM emulation, the asynchronous and synchronous programs, develop the firmware and drivers.</p>
        </td>
        <td style="border: none;">
            <h3>📄 <a href="/sidecartridge-multidevice/parameters/">Parameters</a></h3>
            <p>Description of all the parameters available in the SidecarTridge Multi-device.</p>
        </td>
        <td style="border: none;">
            <h3>🔧 <a href="/sidecartridge-multidevice/how_to/">How to</a></h3>
            <p>Different small tutorials to customize the SidecarTridge Multi-device to your needs.</p>
        </td>
    </tr>
    <tr>
        <td style="border: none;">
            <h3>🤝 <a href="/sidecartridge-multidevice/compatibility_issues/">Compatibility</a></h3>
            <p>Please read this section if you have issues with your SidecarTridge Multi-device.</p>
        </td>
        <td style="border: none;">
            <h3>🛠️ <a href="/sidecartridge-multidevice/troubleshooting/">Troubleshooting</a></h3>
            <p>Check this section if you have issues with your SidecarTridge Multi-device.</p>
        </td>
        <td style="border: none;">
            <h3>❓ <a href="/sidecartridge-multidevice/faq/">FAQ</a></h3>
            <p>Frequently Asked Questions.</p>
        </td>
    </tr>
    <tr>
        <td style="border: none;">
            <h3>📦 <a href="/sidecartridge-multidevice/cases/">Enclosures</a></h3>
            <p>Different enclosures for your board.</p>
        </td>
        <td style="border: none;">
            <h3>🔄 <a href="/sidecartridge-multidevice/revisions/">Board revisions</a></h3>
            <p>Tracing the path of the SidecarTridge Multi-device boards.</p>
         </td>
        <td style="border: none;">
            <h3>🗄️ <a href="/sidecartridge-multidevice/publicfloppydb/">Public Floppy DB</a></h3>
            <p>Contribute to the Floppy Images Database with your own images</p>
        </td>
    </tr>
    <tr>
        <td style="border: none;">
            <h3>🗄️ <a href="/sidecartridge-multidevice/publicromdb/">Public ROM DB</a></h3>
            <p>Contribute to the ROM Images Database with your own images</p>
        </td>
        <td style="border: none;">
            <h3>🗄️ <a href="/sidecartridge-multidevice/unofficial_firmwares/">Unoficial Firmwares</a></h3>
            <p>Smart people out there building incredible stuff with the device</p>
        </td>
        <td style="border: none;">
         </td>
    </tr>
</table>

## Do you want to test the new Alpha firmware?
{: .d-inline-block }

{{ site.FIRMWARE_ALPHA_VERSION }}
{: .label .label-purple }

### 🚀 What’s new in Firmware v2?

Firmware v2 introduces a new architecture for the SidecarTridge Multi-device that brings flexibility, modularity, and a more efficient workflow — especially for power users and developers:

* **🧩 Modular Microfirmwares**
  The core of v2 is the concept of *Microfirmwares*: standalone apps (ROM emulator, floppy emulator, RTC, custom tools, etc.) that you can install and switch between on the same hardware — no need to reflash the entire board.

* **📡 OTA (Over The Air) Downloads & Updates**
  You can now browse and download Microfirmwares directly from official — and even private — Microfirmware repositories, over Wi-Fi. Install or update apps without removing the SD card or using a PC. A simple and secure way to keep your device up to date.

* **⚙️ Per-app Configurations**
  Each Microfirmware stores its own settings in flash memory, isolated from other apps. This allows you to easily switch between functions without losing or reconfiguring settings.

* **🛠️ Optimized Development Workflow & Architecture**
  The v2 architecture separates the core firmware, global settings, and Microfirmwares — making the platform easier to extend and maintain. For developers, this enables a fast test cycle: build ST software on PC/Mac/Linux, test in an emulator, then copy to the device as a microfirmware. Expect faster innovation and more community-contributed Microfirmwares.

Check the following links below:

* **💾 [Download {{ site.FIRMWARE_ALPHA_VERSION }} Release](https://github.com/sidecartridge/rp2-booster-bootloader/releases/download/{{ site.FIRMWARE_ALPHA_VERSION }}/rp-booster-{{ site.FIRMWARE_ALPHA_VERSION }}-full.uf2)**
* Learn to install and configure with the [Getting Started Guide](/sidecartridge-multidevice/getting_started_v2/)
* Learn to download and install the different [microfirmwares](/sidecartridge-multidevice/userguide_v2/)
* Browse the list of available [microfirmwares](/sidecartridge-multidevice/microfirmwares/)
* Are you a brave developer? Check the [Development Guide](/sidecartridge-multidevice/programming/)

Explore, learn, and contribute to the SidecarTridge Multi-device project!