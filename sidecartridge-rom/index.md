---
layout: default
title: SidecarTridge ROM Emulator
nav_order: 0
nav_exclude: false
has_children: true
---

![SidecarTridge ROM Emulator pinout diagram](/sidecartridge-rom/assets/images/PINOUT_DIAGRAM_V2_1280px.png)

# SidecarTridge ROM Emulator
{: .d-inline-block }

## Programmable 512 KB ROM emulator for 8/16-bit data buses with dynamic speed selection

The SidecarTridge ROM Emulator is a versatile tool for developers and hobbyists who need to emulate ROMs across different systems. Compatible with the 27C/28C EPROM and EEPROM series, it lets you load binary images and switch between ROMs effortlessly.

**The SidecarTridge ROM Emulator is a module intended for developers, builders, and hardware makers to integrate into their projects. It is not a standalone consumer product and requires host hardware to function.**

### Why choose SidecarTridge ROM Emulator?

- **Versatile ROM emulation** – Load binary images from 4 KB to 512 KB, in 8- or 16-bit width, with selectable bus-speed grades.
- **Compact design** – Fits common enclosures and integrates easily.
- **USB connectivity** – Transfer images on Windows, macOS, and Linux.
- **API support** – Control the emulator from the host via a simple API.

### Key features

- **Bit-banged emulation** – Uses RP2350 PIO to emulate ROMs at the signal level.
- **Multi-image storage** – Up to 64 images in 16 MB flash; no physical swaps.
- **Simple management** – Manage images via API calls from the host.

### How it works

- **Signal-accurate PIO** – Drives address, data, and control lines to mimic ROM/EEPROM/Flash devices.
- **Flash storage as USB MSC** – 16 MB non-volatile flash exposed as a FAT12 USB mass-storage volume.
- **Hot swapping** – Image switching can be triggered by reads to specific addresses; no power-cycle required.

### Perfect for makers

Ideal for makers, developers, and hobbyists—especially when emulating ROMs for vintage computers.

### At a glance (hardware)

- **55 mm × 25 mm** compact PCB
- **Single-side PCB**
- **Castellated edges + mounting holes**
- **USB-C connector**
- **DEBUG/UART JST (optional)**
- **Dual power inputs (USB or external)**
- **5 V supply**
- **5 V & TTL logic levels**

---

## Table of Contents

<!-- Card grid + chips (scoped to this page) -->
<style>
  .toc-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.2rem;
    margin-top: 0.75rem;
  }
  .toc-card {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 1rem 1.1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    transition: transform .12s ease, box-shadow .12s ease;
  }
  .toc-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
  }
  .toc-card h3 {
    margin: .25rem 0 .35rem 0;
    font-size: 1.05rem;
    line-height: 1.25;
  }
  .toc-card h3 a { text-decoration: none; }
  .toc-card p {
    margin: 0;
    font-size: .95rem;
    color: #333;
  }
  .toc-chip {
    display: inline-block;
    font-size: .72rem;
    font-weight: 600;
    letter-spacing: .02em;
    padding: .22rem .5rem;
    border-radius: 999px;
    margin-bottom: .25rem;
    user-select: none;
  }
  .chip-guide   { background: #e8f5e9; color: #1b5e20; border: 1px solid #c8e6c9; }
  .chip-ref     { background: #e3f2fd; color: #0d47a1; border: 1px solid #bbdefb; }
  .chip-howto   { background: #fff3e0; color: #e65100; border: 1px solid #ffe0b2; }
</style>

<div class="toc-grid">

  <!-- Guides -->
  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>📘 <a href="/sidecartridge-rom/introduction/">Introduction</a></h3>
    <p>Overview, capabilities, and when to use the ROM Emulator.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🚀 <a href="/sidecartridge-rom/getting-started/">Getting Started</a></h3>
    <p>Connect, power, mount USB storage, and load your first ROM image.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💲 <a href="/sidecartridge-rom/before-buy/">Before You Buy</a></h3>
    <p>What you need to know before integrating the ROM Emulator module into a project.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🧷 <a href="/sidecartridge-rom/hardware-integration/">Hardware Integration (Carrier Board)</a></h3>
    <p>Carrier board requirements, soldering notes, and power considerations.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💾 <a href="/sidecartridge-rom/firmware-and-files/">Firmware &amp; Files (ROMEMUL)</a></h3>
    <p>USB mass-storage workflow, volume layout, and safe-eject rules.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🧩 <a href="/sidecartridge-rom/firmware-api/">Firmware API</a></h3>
    <p>Host control API: list/upload/select images and configure behavior.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🤝 <a href="/sidecartridge-rom/compatibility/">Compatibility</a></h3>
    <p>Known-good integrations, supported sizes/widths, and known issues.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🛠️ <a href="/sidecartridge-rom/troubleshooting/">Troubleshooting</a></h3>
    <p>Common issues, diagnostics, and quick fixes.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>❓ <a href="/sidecartridge-rom/faq/">FAQ</a></h3>
    <p>Answers to frequently asked questions.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📝 <a href="/sidecartridge-rom/changelog/">Changelog</a></h3>
    <p>Firmware, hardware, and documentation changes over time.</p>
  </div>

</div>
