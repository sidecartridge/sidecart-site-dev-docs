---
layout: default
title: Introduction
nav_order: 1
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /introduction
  - /introduction/
---

# Introduction
{: .no_toc }

The first chapter provides an overview of the SidecarTridge Multi-device project, explaining the project's purpose, objectives, and the intended audience. The goal is to give readers a concise understanding of what the project entails and what it seeks to achieve.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Project Overview

Welcome to Multi-device, your gateway to a harmonious blend of nostalgic computing with modern technological enhancements. This device is a cartridge ROM emulator meticulously designed for the Atari ST, STE, and Mega series. It's built to ride the robust capabilities of the RP2040 microcontroller found in the Raspberry Pi Pico, offering a comprehensive and versatile emulation experience. Whether you’re looking to dive back into the authentic experience of using retro machines or a developer eager to explore the vast possibilities of retro computing, Multi-device is your companion.

Key Highlights:
- **Versatile ROM Emulation:** Multi-device provides a seamless experience in emulating both 64Kbyte and 128Kbyte ROMs, loaded effortlessly from a microSD card or via a Wi-Fi connection.
- **Real-time Interaction:** It offers unparalleled real-time interaction with the cartridge bus, allowing users to read and write data on-the-fly, enhancing the emulation of various devices like hard disks, floppy disks, keyboards, and more.
- **Open Architecture:** The open-source nature of Multi-device fosters innovation and creativity, letting the community expand its functionalities and explore new horizons in retro computing.
- **Evolving Capabilities:** As a bridge between the past and the present, Multi-device is ever-evolving, ensuring that enthusiasts stay at the cutting edge of emulation technology.

## Objective and Purpose

The inception of Multi-device is deeply rooted in the passion and desire to develop software for obsolete machines purely for the joy and the challenge it presents. This journey, reminiscent of teenage years spent with the beloved Atari 1040STFM, was rekindled by a midlife reconnection with the old creations and the community from the Atari ST retro world.

The concept of Multi-device stemmed from the longing for the original experience of using machines from the bygone era but supercharged with the modern-day luxuries and capabilities. It’s not about just using an emulator on contemporary operating systems; it’s about experiencing the speed, ease of access, and abundance of resources on the original hardware, bringing the authentic tactile experience of retro computing to the present day.

The Multi-device venture was met with several challenges, like developing a protocol to overcome the read-only constraint of the Atari ST's cartridge interface and finding a suitable microcontroller that could meet the stringent response time requirements for emulating the ROMs of an Atari ST cartridge. The breakthrough came with the discovery of the Raspberry Pi Pico and its RP2040 microcontroller, which, with its Programmable Input/Output blocks, provided the precise and deterministic manner of managing I/O needed for this project.

## Target Audience

Multi-device is more than just an emulator; it’s a canvas for tech enthusiasts, developers, and retro computing aficionados to paint their innovations. It’s a contribution to the community, a piece of technology open for modifications, expansions, and enhancements, aiming to keep the spirit of Atari ST alive and evolving, allowing users to relive the past with a touch of the present.

Whether you are reminiscing about the golden days of computing or exploring the infinite possibilities of emulation technology, Multi-device is your conduit to a world where the past meets the future, where nostalgia intertwines with innovation. It's not just a journey back in time; it's a journey forward in exploration and discovery.

## Contribution Guidelines

Below are some quick guidelines to ensure smooth contributions to our project.

### 📜 Licensing

- **Software**: Contributed code must adhere to the [GNU General Public License v3.0](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/main/LICENSE).
- **Hardware**: The design and schematics of the hardware are licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### 🐞 Reporting Bugs

- Check for existing reports to avoid duplicates in the [Issues](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/issues) section. Please tag as `bug`.
- Provide clear details and steps to reproduce.

### 💡 Feature Requests

- Describe the feature and its advantages in the [Issues](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/issues) section. Please tag as `enhancement`.
- Suggest possible solutions or alternatives.

### 💻 Code Contributions

- Ensure adherence to GPL and current coding standards.
- Submit through a pull request and describe the changes.

### 🛠 Hardware Contributions

- Submit designs and assembly instructions via pull request.
- Ensure all designs are non-commercial and safe to replicate.

### 📚 Documentation

- Focus on clarity and accuracy.
- Follow existing documentation styles.

### 👀 Review Process

- Contributions will be reviewed and feedback will be provided.
- Once approved, your contributions will be merged.

### 🙌 Thank You!

Thank you for your interest in contributing to SidecarTridge Multi-device! Your contributions are valuable to us. Let's build something great together!

