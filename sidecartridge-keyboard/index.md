---
layout: home
title: SidecarTridge Keyboard
nav_order: 0
nav_exclude: false
has_children: true
toc: false
has_toc: false
---

![SidecarTridge Keyboard Emulator hardware variants](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-PERSPECTIVE.png)

# SidecarTridge Keyboard Emulator
{: .d-inline-block }

{{ site.SIDECARTRIDGE_IKBD_VERSION }}
{: .label .label-purple }

The **SidecarTridge Keyboard Emulator** is a hardware device that emulates the original Atari ST IKBD keyboard controller, allowing modern keyboards, mice, and game controllers to be used on Atari ST-family computers while preserving full compatibility with software that expects the original IKBD behavior.

Unlike simple keyboard adapters that only translate keystrokes, the SidecarTridge Keyboard Emulator reproduces the behavior of the HD6301-based IKBD microcontroller used in the Atari ST, STe, Mega ST, Mega STe, and TT.  
Because the host computer communicates with a real controller implementation, the system behaves as if an original Atari keyboard were connected.

The project currently exists in two hardware variants that share the same firmware base.


## Hardware variants

- **SidecarTridge Croissant**  
  Internal adapter for Atari ST and Atari STe computers with the internal 7-pin keyboard connector.  
  Works as a middle-man between the motherboard and the original keyboard path, allowing Bluetooth, and mixed input configurations while preserving compatibility with original devices.

![SidecarTridge Croissant internal keyboard emulator](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSSANT-TOP.png)

- **SidecarTridge Soufflè**  
  External keyboard replacement for Atari Mega ST and Mega STe systems.  
  Connects in place of the original keyboard and adds Bluetooth and USB input support while maintaining normal IKBD behavior.

![SidecarTridge Soufflè external keyboard emulator](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-SOUFFLE-PERSPECTIVE.png)

Both hardware variants use the same firmware architecture, so firmware updates are expected to support both platforms whenever possible.


## Latest Stable Firmware: {{ site.SIDECARTRIDGE_IKBD_VERSION }}

- [Download Stable Release {{ site.SIDECARTRIDGE_IKBD_VERSION }}](https://sidecartridge.com/downloads/)
- [Firmware Update Guide](/sidecartridge-keyboard/firmware-update/)
- [Keyboard Changelog](/sidecartridge-keyboard/changelog/)


## Source Code Repositories

- [SidecarTridge Keyboard firmware](https://github.com/sidecartridge/rp2-atarist-rpikb)
- [SidecarTridge Keyboard booster](https://github.com/sidecartridge/rp2-atarist-rpikb-booster)


## What this project provides

Typical use cases for the SidecarTridge Keyboard Emulator include:

- using Bluetooth keyboards, mice, and gamepads on Atari ST systems
- using USB keyboards and mice on classic Atari hardware
- replacing missing or faulty original keyboards
- preserving compatibility with software that depends on normal IKBD behavior
- combining modern input devices with original Atari joysticks and mouse
- modernizing Atari ST, STe, Mega ST, Mega STe, and TT setups


## Table of Contents

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

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📘 <a href="/sidecartridge-keyboard/introduction/">Introduction</a></h3>
    <p>An overview of the IKBD-emulation approach, supported systems, and the Croissant and Soufflè hardware variants.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💲 <a href="/sidecartridge-keyboard/before-buy/">Before You Buy</a></h3>
    <p>What to review before buying or integrating the device.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🚀 <a href="/sidecartridge-keyboard/getting-started/">Getting Started</a></h3>
    <p>Initial setup, prerequisites, and first-use workflow.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>⚙️ <a href="/sidecartridge-keyboard/hardware-installation/">Hardware Installation</a></h3>
    <p>Physical installation notes and integration guidance.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>😊 <a href="/sidecartridge-keyboard/user-guide/">User Guide</a></h3>
    <p>Daily operation, expected workflows, and common tasks.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🔄 <a href="/sidecartridge-keyboard/firmware-update/">Firmware Update</a></h3>
    <p>How to place the device in BOOTSEL mode and install a newer firmware release.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🤝 <a href="/sidecartridge-keyboard/compatibility/">Compatibility</a></h3>
    <p>Supported hardware, firmware, and known integration limits.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🛠️ <a href="/sidecartridge-keyboard/troubleshooting/">Troubleshooting</a></h3>
    <p>Common issues, checks, and recovery steps.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>❓ <a href="/sidecartridge-keyboard/faq/">FAQ</a></h3>
    <p>Answers to frequently asked questions.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📝 <a href="/sidecartridge-keyboard/changelog/">Changelog</a></h3>
    <p>Documentation, firmware, and hardware changes over time.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📐 <a href="/sidecartridge-keyboard/croissant-open-hardware/">Croissant Open Hardware</a></h3>
    <p>Diagram, schematics, manufacturing files, and license for the Croissant hardware release.</p>
  </div>

</div>
