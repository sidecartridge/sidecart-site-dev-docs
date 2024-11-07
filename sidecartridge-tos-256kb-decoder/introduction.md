---
layout: default
title: Introduction
nav_order: 1
nav_exclude: false
parent: SidecarTridge TOS 256KB Decoder
---

# Introduction
{: .no_toc }

This chapter provides a concise overview of the SidecarTridge TOS 256KB Decoder, explaining its purpose, features, and benefits for Atari ST and Mega ST computers.


<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/xYn6r8SssYQ?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>

## Overview

The **256KB Decoder** is an add-on board for the SidecarTridge TOS emulator that enables decoding of 256KB ROMs used in the Atari STe and Mega STe computers, bringing this functionality to the Atari ST and Mega ST series. **Soldered onto the Motorola 68000 CPU**, it performs two key functions:

- **Provides necessary address signals** to the SidecarTridge TOS emulator for reading the ROMs.
- **Generates a synthetic Chip Enable (CE) signal** to activate the ROMs only when accessed by the CPU in the address range starting at $E00000 for the 256KB ROMs.

The SidecarTridge TOS emulator is an innovative solution that enhances the functionality and flexibility of the Atari ST series. Utilizing bit-banged emulation, it replicates the internal ROMs of the Atari ST, allowing users to access and run any version of TOS (The Operating System) without physically swapping ROM chips. This capability extends to custom ROMs, including EmuTOS—an open-source TOS replacement.

Combined with a custom version of the SidecarTridge TOS emulator hardware, an Atari ST or Mega ST computer can transparently decode both 192KB and 256KB ROMs.

## Purpose and Objectives

Historically, Atari ST and Mega ST users have been limited to the 192KB TOS versions installed on their computers. After 1989, Atari ceased releasing new 192KB TOS ROMs but continued developing TOS versions up to 1993. The SidecarTridge TOS emulator, along with the 256KB Decoder, addresses this limitation by providing a flexible and user-friendly solution. It allows users to access any TOS version or custom ROMs without the need for physical ROM chip swaps.

## Features and Benefits

By combining the SidecarTridge TOS emulator and the 256KB Decoder, you can enjoy a wide range of TOS versions on an Atari ST or Mega ST computer:

- **TOS 1.00**
- **TOS 1.02**
- **TOS 1.04**
- **KAOS TOS 1.4**
- **TOS 2.06**
- **SuperTOS 2.06**
- **Custom TOS 2.16**
- **EmuTOS 192KB**
- **EmuTOS 256KB**

{: .warning }
The 256KB TOS versions 1.06, 1.62, and 2.05 are not compatible with Atari ST and Mega ST computers. While the SidecarTridge TOS emulator with the 256KB Decoder can decode them, these versions do not function on these models.

## Intended Audience

The SidecarTridge TOS emulator and the 256KB Decoder are designed for Atari ST and Mega ST enthusiasts, hobbyists, and developers who wish to explore and experiment with different TOS versions and custom ROMs. It's suitable for users with a basic understanding of electronics and soldering skills, as the add-on board must be soldered onto the Motorola 68000 CPU. Proper installation requires a certain level of expertise to ensure functionality.

## Project Background

The SidecarTridge TOS 256KB Decoder is an extension of the [SidecarTridge TOS emulator](/sidecartridge-tos/) project. It requires a special version of the SidecarTridge TOS emulator carrier board to function, which connects to the 256KB Decoder board.

## Key Hardware Components

The SidecarTridge TOS 256KB Decoder kit includes several essential components, each contributing to its functionality and ease of use. It can be considered a superset of the SidecarTridge TOS Emulator. The main components are:

1. **SidecarTridge ROM Emulator Board**: The core of the SidecarTridge TOS emulator, it leverages the Programmable Input/Output (PIO) features of the Raspberry Pi RP2040 microcontroller to emulate a ROM chip at the signal level. This board contains the necessary circuitry and flash memory to store multiple custom ROMs, provides a USB interface for connectivity, and communicates with the Atari ST bus through bus level shifters converting TTL (5 volts) to CMOS (3.3 volts).

2. **SidecarTridge Atari ST or Mega ST Models Carrier Board for 256KB Decoder**: Designed to fit seamlessly into various models the carrier board for the Atari ST and Mega ST series includes a multiplexer. This allows the SidecarTridge TOS emulator to select between 192KB and 256KB ROMs, enabling transparent decoding of both.

3. **256KB Decoder Board**: Soldered onto the Motorola 68000 CPU, this add-on board decodes the 256KB ROMs used in the Atari STe and Mega STe computers when installed in the Atari ST and Mega ST series. It supplies the necessary signals to the SidecarTridge TOS emulator.

4. **6-Pin Connector**: This connector links the 256KB Decoder board to the SidecarTridge TOS emulator carrier board.

---

[Previous: Index](/sidecartridge-tos-256kb-decoder/){: .btn .mr-4 }
[Main](/sidecartridge-tos-256kb-decoder/){: .btn .mr-4 }
[Next: Before You Buy](/sidecartridge-tos-256kb-decoder/before-buy/){: .btn .mr-4 }
