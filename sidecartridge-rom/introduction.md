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

The SidecarTridge ROM Emulator is a developer-oriented module that emulates parallel ROM devices (e.g., 27C/28C families) at the signal level, letting you load, select, and switch between multiple binary images without physically swapping chips. It’s the same core technology used inside the SidecarTridge **TOS Emulator** to boot different Atari ST TOS versions and custom ROMs, but presented here as a general-purpose building block you can integrate into your own projects. :contentReference[oaicite:0]{index=0}

The ROM Emulator pairs solid hardware (RP2350 + PIO) with a simple host-side workflow: expose flash as a USB mass-storage volume, copy images, and select which image is active. Firmware and tools evolved from the TOS work now support quality-of-life features such as FAT12 storage handling and host-initiated uploads. :contentReference[oaicite:1]{index=1}

## What you can do with it

- Boot different firmware/OS ROMs on a target system (development, diagnostics, or preservation use-cases).  
- Maintain a library of ROM images (up to 64, within 16 MB) and switch without opening the machine or removing media.  
- Script image selection and management from the host, integrating with your own build/test pipelines.  
- Reuse the approach proven in the TOS Emulator to explore official and custom ROMs safely on real hardware. :contentReference[oaicite:2]{index=2}

## Where it fits in the SidecarTridge ecosystem

The ROM Emulator is the core that enables the SidecarTridge **TOS Emulator** to present multiple TOS versions on Atari ST-family machines—no chip swaps required. On those systems, it works alongside optional accessories (e.g., the **256 KB Decoder** for STe/Mega STe-class ROM layouts). For standalone use, you can embed the ROM Emulator into your own designs and drive it from a host PC or target system firmware. :contentReference[oaicite:3]{index=3}

## How it works (high level)

At runtime, the RP2350’s PIO state machines present address/data/control timing compatible with standard ROM/EEPROM/Flash parts (e.g., CS#, OE#, WE# behavior), while the active image is fetched from on-board flash. The device enumerates as a USB mass-storage volume (FAT12) for easy image management; host tools can also upload/switch images programmatically. This is the same pattern documented and shipped with the TOS product line, adapted here for general ROM workloads. :contentReference[oaicite:4]{index=4}

## Who is this for?

- **Developers & hardware hackers** who need repeatable ROM testing without burning chips.  
- **Retrocomputing enthusiasts** who want to run official or community ROMs on original hardware.  
- **Integrators/OEMs** who need a compact, embeddable ROM solution in custom projects. :contentReference[oaicite:5]{index=5}

## Capabilities and limits (at a glance)

- Supports common parallel ROM pinouts in **8- or 16-bit data widths** and sizes from **4 KB up to 512 KB** per image (within the device’s 16 MB storage).  
- Stores up to **64 images** and can switch the active image without power-cycling (by host command or mapped triggers, depending on firmware setup).  
- Designed as a **module** to integrate; it is **not** a consumer standalone product. For certain Atari ST models requiring 256 KB ROM mapping, pair with the **256 KB Decoder** when replicating TOS use-cases. :contentReference[oaicite:6]{index=6}

## Prerequisites & related docs

If you’re evaluating this module because you’ve seen the TOS product:  
- The TOS docs provide good context on installation considerations across Atari ST models, daily operation (e.g., selecting a TOS), and rescue/boot flows—useful patterns even if your target is different. :contentReference[oaicite:7]{index=7}

## What’s next

- **Getting Started** — connect, mount storage, copy your first images, and select an active ROM.  
- **Hardware Overview** — physical layout, power, connectors, pinout, and electrical notes.  
- **Host API & Tools** — list, upload, and switch images from your development machine.  
- **Bus Timing & Performance** — the signal-level view and how to tune wait-states.  
- **Troubleshooting & FAQ** — common pitfalls and quick checks.

[Previous: Index](/sidecartridge-rom/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Getting Started](/sidecartridge-rom/getting-started/){: .btn }
