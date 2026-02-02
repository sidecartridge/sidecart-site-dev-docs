---
layout: home
title: SidecarTridge TOS
nav_order: 0
nav_exclude: false
has_children: true
toc: false
has_toc: false
---


![SidecarTridge TOS](/sidecartridge-tos/assets/images/sidecartridge-tos-boards-versions.png)

# SidecarTridge TOS Emulator 
{: .d-inline-block }

The SidecarTridge TOS emulator is a compact board that emulates Atari ST internal ROMs, enabling users to run any TOS version or custom ROM without physically swapping chips.

This guide offers comprehensive information about the SidecarTridge TOS emulator for the Atari ST family of computers. Explore the relevant sections below to find specific details.

There are two main versions of the SidecarTridge TOS emulator:

- **SidecarTridge TOS v1 and v2**: Designed for the Atari ST, STE, Mega ST, and Mega STE, this version uses the Raspberry Pi RP2040 microcontroller and mounts directly onto the computer’s carrier board via a short pin header. It features a slimmer profile, and when powered via USB or the computer, there is no red LED indicator. In the image above, this board appears on the left.

- **SidecarTridge TOS v3**: This version also supports the Atari ST, STE, Mega ST, and Mega STE, with additional versions in development for other systems. It is based on the more advanced Raspberry Pi RP2350 microcontroller and is surface-mounted with a soldered castellated board. The v3 board is wider, and features a red LED for power, a green LED to show the firmware is running, and an orange LED to indicate the internal USB drive is mounted. In the image above, you’ll find this board on the right.

**ALL BOARDS SHIPPED AFTER MID JUNE 2025 ARE v3 BOARDS.**

## 🚀 Latest Firmware and applications
There are two different firmware versions available for the SidecarTridge TOS emulator, depending on the version of the board you have:
- **Firmware v2.x**: This firmware is designed for the SidecarTridge TOS v1 and v2 boards. The current firmware version is STABLE-{{ site.SIDECARTRIDGE_TOS_FIRMWARE_VERSION }}.
- **Firmware v3.x**: This firmware is designed for the SidecarTridge TOS v3 boards. The current firmware version is STABLE-{{ site.SIDECARTRIDGE_TOS_FIRMWARE_V3_VERSION }}.

Visit the official [downloads](https://sidecartridge.com/downloads/) page to get the latest firmware and applications.

## Table of Contents

<!-- Card grid + chips (scoped to this section) -->
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
  .chip-depr    { background: #eceff1; color: #37474f; border: 1px solid #cfd8dc; }
</style>

<div class="toc-grid">

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📘 <a href="/sidecartridge-tos/introduction/">Introduction</a></h3>
    <p>An overview of the SidecarTridge TOS emulator project, explaining the project's purpose, objectives, and the intended audience.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💲 <a href="/sidecartridge-tos/before-buy/">Before You Buy</a></h3>
    <p>What you need to know before buying a kit</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🚀 <a href="/sidecartridge-tos/getting-startedV2/">Getting started</a></h3>
    <p>Guidance on the initial steps including prerequisites, setup and configuration.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>⚙️ <a href="/sidecartridge-tos/hardware-installation/">Hardware Installation</a></h3>
    <p>Learn how to install the device in your computers.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>😊 <a href="/sidecartridge-tos/user-guideV2/">User Guide</a></h3>
    <p>Learn how to use the device day in day out</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Reference</span>
    <h3>😊 <a href="/sidecartridge-tos/advanced-settings/">Advanced Settings</a></h3>
    <p>Explore advanced configuration options for power users.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🤝 <a href="/sidecartridge-tos/compatibility/">Compatibility</a></h3>
    <p>Please read this section to know about open issues and compatibility.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🛠️ <a href="/sidecartridge-tos/troubleshooting/">Troubleshooting</a></h3>
    <p>Check this section if you have issues with your SidecarTridge.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>❓ <a href="/sidecartridge-tos/faq/">FAQ</a></h3>
    <p>Frequently Asked Questions.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📝 <a href="/sidecartridge-tos/changelog/">Changelog</a></h3>
    <p>The latest changes in the firmware, applications and hardware.</p>
  </div>

</div>

<h3>Previous Deprecated Firmware Versions</h3>

<div class="toc-grid">
  <div class="toc-card">
    <span class="toc-chip chip-depr">Deprecated</span>
    <h3><a href="/sidecartridge-tos/getting-started/">Firmware v1.0: Getting started</a></h3>
  </div>
  <div class="toc-card">
    <span class="toc-chip chip-depr">Deprecated</span>
    <h3><a href="/sidecartridge-tos/user-guide/">Firmware V1.0: User Guide</a></h3>
  </div>
</div>
