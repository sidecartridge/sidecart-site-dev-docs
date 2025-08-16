---
layout: default
title: Introduction
nav_order: 1
nav_exclude: false
parent: SidecarTridge ROM
---

# Introduction
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

The SidecarTridge ROM Emulator is a developer-oriented module that emulates parallel ROM devices (e.g., 27C/28C families) at the signal level, letting you load, select, and switch between multiple binary images without physically swapping chips. It’s the same core technology used in the SidecarTridge TOS product to boot different Atari ST TOS versions and custom ROMs, presented here as a general-purpose building block you can integrate into your own projects.

The ROM Emulator combines solid hardware (RP2350 + PIO) with a simple host workflow: the on-board flash is exposed as a USB mass-storage volume, you copy images to it, and then select which image is active. Tools and firmware features include FAT12 handling and host-initiated uploads and switching.

---

## What you can do with it

- Boot different firmware/OS ROMs on a target system for development, diagnostics, or preservation.
- Keep a library of ROM images (up to 64 within 16 MB) and switch without opening the machine.
- Script image selection and management from the host, integrating with build/test pipelines.
- Reuse the proven approach from the TOS product to run official and custom ROMs on real hardware.

---

## Where it fits in the SidecarTridge ecosystem

The ROM Emulator underpins the SidecarTridge TOS Emulator by presenting multiple TOS versions on Atari ST-family machines—no chip swaps required. In TOS-style use cases that need 256 KB mapping, it can be paired with the 256 KB Decoder. For standalone use, embed the module in your own designs and control it from a host PC or target firmware.

---

## How it works (high level)

At runtime, RP2350 PIO state machines present address, data, and control timings compatible with standard ROM/EEPROM/Flash parts (CS#, OE#, WE# behavior), while the active image is fetched from on-board flash. The device enumerates as a FAT12 USB mass-storage volume for easy image management; host tools can also upload and switch images programmatically.

---

## Who is this for?

- **Developers & hardware hackers** who need repeatable ROM testing without burning chips.  
- **Retrocomputing enthusiasts** who want to run official or community ROMs on original hardware.  
- **Integrators/OEMs** who need a compact, embeddable ROM solution in custom projects.

---

## Capabilities and limits (at a glance)

- Supports common parallel ROM pinouts in **8- or 16-bit** data widths and sizes from **4 KB to 512 KB** per image (within the device’s **16 MB** storage).  
- Stores up to **64 images** and can switch the active image without a power-cycle (by host command or mapped triggers, depending on firmware setup).  
- Designed as a **module** to integrate; it is **not** a standalone consumer product.

---

## Prerequisites & related docs

If you’re evaluating this module because you’ve seen the TOS product, the TOS documentation offers helpful patterns for installation, operation, and recovery flows that translate well to other targets:  
- https://docs.sidecartridge.com/sidecartridge-tos/

---

## What’s next

- **Getting Started** — connect, mount storage, copy your first images, and select an active ROM.  
- **Hardware Overview** — physical layout, power, connectors, pinout, and electrical notes.  
- **Host API & Tools** — list, upload, and switch images from your development machine.  
- **Bus Timing & Performance** — the signal-level view and how to tune wait-states.  
- **Troubleshooting & FAQ** — common pitfalls and quick checks.

[Previous: Index](/sidecartridge-rom/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Getting Started](/sidecartridge-rom/getting-started/){: .btn }
