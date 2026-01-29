---
layout: default
title: Hardware Integration (Carrier Board)
nav_order: 4
nav_exclude: false
parent: SidecarTridge ROM
---

# Hardware Integration (Carrier Board)
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Overview

The ROM Emulator module must be integrated into host hardware.
In most real-world builds, that means the ROM Emulator is **soldered onto a custom carrier board** that adapts it to the target system’s ROM socket/pinout and mechanical constraints.

## Carrier board requirements

A ROM Emulator carrier board typically has **two functional sections**:

1. **Castellated section (ROM Emulator module footprint)**
   - This section is used to **solder the ROM Emulator PCB** onto the carrier.
   - The carrier can provide a **solder mask / footprint variants** for different ROM Emulator module models.
   - The carrier-side footprint can be implemented as **through-hole or SMD**, depending on the module and assembly preference.

2. **ROM/EPROM/EEPROM “chip” section (target pinout adapter)**
   - This section must **mimic the pinout** of the device you want to emulate.
   - In practice, this is usually implemented as a **through-hole DIP footprint** (or equivalent), matching the target socket/package.

### Layers, routing, and signal integrity

- The carrier PCB can be **2-layer or 4-layer**.
- Prefer **non-crossing routes** for critical address/data/control lines.
- If signal lines must cross, route them so there is a **solid GND and/or +5V region** between them (this is a key reason why **4 layers** can be a better option).

### Trace width guidance

- Recommended **minimum trace width** for signal lines: **1.27 mm**.
- For bus speeds **below ~16 MHz**, thinner traces can still be safe depending on the target system.
- Typical widths we use: **2.5 mm down to 1.27 mm**.

### Power and ground

- The carrier must provide **+5V power** and a **good ground connection** to the ROM Emulator.
- Additional local decoupling capacitors on the carrier are **not strictly necessary**: we assume the target motherboard already has decoupling in the ROM/EPROM/EEPROM area.

### Optional indicators

- It can be useful to add LEDs to observe **line activity** on the carrier.
- However, the ROM Emulator board already provides LEDs for **Power**, **Emulation**, and **Volume (ROMEMUL)**, so extra LEDs are optional.

## Soldering & inspection

There are two common ways to mount/solder the ROM Emulator module to the carrier board:

1. **Through-hole headers (stacked)**
   - Use **two interleaved 2.54 mm headers**, typically **2× 20 pins**.
   - This is a robust and very build-friendly option.

2. **Direct castellated soldering (recommended for tight builds)**
   - Solder the ROM Emulator directly via its **castellated edges** onto the carrier footprint.
   - This is generally the **best option when vertical clearance/space is restricted**.

Both approaches are perfectly valid; choose based on mechanical constraints and the target enclosure.

## Powering

The ROM Emulator can be powered in two ways:

### 1) Power from the carrier board (+5V)

- If the ROM Emulator is fed with **+5V from the carrier board**, the firmware assumes it must start in **EMULATION mode**.
- In this mode, the **green LED is on** and ROM emulation starts immediately, ready to work inside the target motherboard.

### 2) Power from USB-C (+5V)

- If the ROM Emulator is fed with **+5V via the USB‑C connector**, it starts in **Volume (ROMEMUL) mode**.
- This is the expected mode when connecting the device to a computer to manage ROM images on the ROMEMUL mass-storage volume.

### Powering both at the same time

- It is **safe** to feed both power sources at the same time.
- When USB‑C power is detected, **Volume (ROMEMUL) mode prevails**.

[Previous: Getting Started](/sidecartridge-rom/getting-started/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Firmware & Files](/sidecartridge-rom/firmware-and-files/){: .btn }
