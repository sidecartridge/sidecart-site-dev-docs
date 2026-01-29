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

The SidecarTridge ROM Emulator is a developer-oriented module that emulates parallel ROM devices (e.g., 27C/28C families) at the signal level, letting you load, select, and switch between multiple binary images without physically swapping chips. It’s the same core technology used in products like the [SidecarTridge TOS](/sidecartridge-tos/) emulator (Atari ST family) and the [SidecarTridge Kickstart](/sidecartridge-kickstart/) emulator (Classic Amiga), presented here as a general-purpose building block you can integrate into your own projects.

The ROM Emulator combines solid hardware (RP2350 + PIO) with a simple host workflow: the on-board flash is exposed as a USB mass-storage volume, you copy images to it, and then select which image is active. Tools and firmware features include FAT12 handling and self-hosted image management (yes, it's possible to upload images directly from the computer running the emulator).

## What you can do with it

- Boot different firmware/OS ROMs on a target system for development, diagnostics, or preservation.
- Keep a library of ROM images (up to 64 within 16 MB) and switch without opening the machine.
- Script image selection and management from the self-hosted environment, or the host API.
- Reuse the proven approach from the TOS product to run official and custom ROMs on real hardware for different computer systems.

## Where it fits in the SidecarTridge ecosystem

The ROM Emulator exists to **bring the same benefits proven in the SidecarTridge TOS Emulator to other computers and embedded targets**—without being tied to Atari ST specifics. In practice, it gives you **multi-image ROM libraries**, **hot/image switching without chip swaps**, and **host-driven, scriptable workflows** for build/test—now applicable to any platform that expects a parallel ROM/EPROM/Flash device.

## How it works (high level)

At runtime, RP2350 PIO state machines present address, data, and control timings compatible with standard ROM/EEPROM/Flash parts (CS#, OE# behavior), while the active image is fetched from on-board flash. The device enumerates as a FAT12 USB mass-storage volume for easy image management; self-contained tools can also upload and switch images programmatically.

## Who is this for?

- **Developers & hardware hackers** who need repeatable ROM testing without burning chips.  
- **Retrocomputing enthusiasts** who want to run official or community ROMs on original hardware.  
- **Integrators/OEMs** who need a compact, embeddable ROM solution in custom projects.

## Capabilities and limits (at a glance)

- Supports common parallel ROM pinouts in **8- or 16-bit** data widths and sizes from **4 KB to 512 KB** per image (within the device’s **16 MB** storage).  
- Stores up to **64 images** and can switch the active image without a power-cycle (by host command or mapped triggers, depending on firmware setup).  
- Supports bus speed from **1 MHz to 24 MHz** (depending on firmware configuration and target hardware).  
- Designed as a **module** to integrate; it is **not** a standalone consumer product.

## Prerequisites & related docs

If you’re evaluating this module because you’ve seen other SidecarTridge ROM-emulation products, these docs offer helpful patterns for installation, operation, and recovery flows that translate well to other targets:

- SidecarTridge **TOS Emulator** (Atari ST / STE / Mega ST / Mega STE): https://docs.sidecartridge.com/sidecartridge-tos/
- SidecarTridge **Kickstart Emulator** (Classic Amiga): https://docs.sidecartridge.com/sidecartridge-kickstart/


[Previous: Index](/sidecartridge-rom/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Getting Started](/sidecartridge-rom/getting-started/){: .btn }
