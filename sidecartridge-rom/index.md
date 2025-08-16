---
layout: default
title: SidecarTridge ROM Emulator
nav_order: 0
nav_exclude: true
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
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🧱 <a href="/sidecartridge-rom/hardware-overview/">Bus Protocol &amp; Timing Diagrams</a></h3>
    <p>Signal-level emulation explained with WaveDrom: CS#, OE#, WE#, address/data timing, and wait-states.</p>
  </div>



<!--

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🧩 <a href="/sidecartridge-rom/host-api-and-tools/">Host API &amp; Tools</a></h3>
    <p>Use the host API/CLI to list, upload, select, and switch images.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🗂️ <a href="/sidecartridge-rom/image-management/">Image Management</a></h3>
    <p>Flash layout, FAT12 volume, naming, and organizing up to 64 images.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🔀 <a href="/sidecartridge-rom/switching-mechanisms/">Switching Mechanisms</a></h3>
    <p>Address-triggered switching, safety notes, and best practices.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>⚡ <a href="/sidecartridge-rom/bus-timing-and-performance/">Bus Timing &amp; Performance</a></h3>
    <p>Dynamic speed selection, wait states, and tuning for stability.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🧱 <a href="/sidecartridge-rom/hardware-overview/">Hardware Overview</a></h3>
    <p>Board layout, power options, connectors, and physical specs.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📌 <a href="/sidecartridge-rom/pinout-and-electrical/">Pinout &amp; Electrical Specs</a></h3>
    <p>Pin mapping, logic levels (5 V &amp; TTL), and interfacing notes.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>💾 <a href="/sidecartridge-rom/supported-roms/">Supported ROM Types &amp; Sizes</a></h3>
    <p>27C/28C series, 8/16-bit width, supported size range (4 KB–512 KB).</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🧪 <a href="/sidecartridge-rom/examples-and-designs/">Examples &amp; Reference Designs</a></h3>
    <p>Minimal wiring, adapters, and integration patterns.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🔧 <a href="/sidecartridge-rom/troubleshooting/">Troubleshooting</a></h3>
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
    <p>Latest firmware, tooling, and documentation updates.</p>
  </div>

-->

</div>
