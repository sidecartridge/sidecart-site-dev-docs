---
layout: home
title: SidecarTridge Multi-device
nav_order: 0
nav_exclude: false
has_children: true
---


![SidecarTridge Multi-device](/sidecartridge-multidevice/assets/images/BOARD-3.1-PICOW-PERSPECTIVE.png)

# SidecarTridge Multi-device Documentation 
{: .d-inline-block }

STABLE-{{ site.FIRMWARE_VERSION }}
{: .label .label-green }

{{ site.FIRMWARE_ALPHA_VERSION }}
{: .label .label-purple }


Welcome to the SidecarTridge Multi-device Documentation! This comprehensive guide is aimed at providing developers with all the information needed to get started with the SidecarTridge Multi-device board, understand its architecture, and contribute to its development. Please refer to the relevant sections below to explore specific topics.

You can learn about the hardware evolution of the SidecarTridge Multi-device in this video:

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/RvREQNScEzE?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


## 🚀 Latest STABLE Firmware: {{ site.FIRMWARE_VERSION }}
* **💾 [Download STABLE Release {{ site.FIRMWARE_VERSION }}](https://sidecartridge.com/downloads)**
* **📝 [Changelog for STABLE Release {{ site.FIRMWARE_VERSION }}](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/releases/tag/{{ site.FIRMWARE_VERSION }})**
* 🕒 [Older Versions](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/releases)

## 👉 [Do you want to test the new firmware?](#do-you-want-to-test-the-new-alpha-firmware)

## 🐞 Bugs, Issues, and Enhancements
* [Reporting tool](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/issues)

## Other Quick links
* [RP2040 firmware source code](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico)
* [Atari ST Configurator firmware source code](https://github.com/sidecartridge/atarist-sidecart-firmware)
* [Atari ST Floppy Emulator firmware source code](https://github.com/sidecartridge/atarist-sidecart-floppy-emulator)
* [Test ROM](https://github.com/sidecartridge/atarist-sidecart-test-rom)
* [Documentation site (this site)](https://github.com/sidecartridge/sidecart-site-dev-docs)

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
</style>

<div class="toc-grid">

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📘 <a href="/sidecartridge-multidevice/introduction/">Introduction</a></h3>
    <p>An overview of the SidecarTridge Multi-device project, explaining the project's purpose, objectives, and the intended audience.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🚀 <a href="/sidecartridge-multidevice/getting_started/">Getting started</a></h3>
    <p>Guidance on the initial steps including prerequisites, board assembly instructions, setup and configuration.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>⚙️ <a href="/sidecartridge-multidevice/userguide/">User Guide</a></h3>
    <p>Learn how to use the SidecarTridge Multi-device.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🏛️ <a href="/sidecartridge-multidevice/architecture_and_design/">Architecture and Design</a></h3>
    <p>Explore the underlying architecture and design principles of the SidecarTridge Multi-device board.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🔌 <a href="/sidecartridge-multidevice/hardware_interface/">Hardware interface</a></h3>
    <p>How the board and the code in the RP2040 handle the mismatch of the buses size between the RP2040 and the Atari ST cartridge.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💻 <a href="/sidecartridge-multidevice/software_development/">Software Development</a></h3>
    <p>Setting up the development environment, compiling the code, debugging, testing and building the firmware.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>👨‍💻 <a href="/sidecartridge-multidevice/programming/">Programming SidecarTridge Multi-device</a></h3>
    <p>Learn about the ROM emulation, the asynchronous and synchronous programs, develop the firmware and drivers.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📄 <a href="/sidecartridge-multidevice/parameters/">Parameters</a></h3>
    <p>Description of all the parameters available in the SidecarTridge Multi-device.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🔧 <a href="/sidecartridge-multidevice/how_to/">How to</a></h3>
    <p>Different small tutorials to customize the SidecarTridge Multi-device to your needs.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🤝 <a href="/sidecartridge-multidevice/compatibility_issues/">Compatibility</a></h3>
    <p>Please read this section if you have issues with your SidecarTridge Multi-device.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🛠️ <a href="/sidecartridge-multidevice/troubleshooting/">Troubleshooting</a></h3>
    <p>Check this section if you have issues with your SidecarTridge Multi-device.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>❓ <a href="/sidecartridge-multidevice/faq/">FAQ</a></h3>
    <p>Frequently Asked Questions.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📦 <a href="/sidecartridge-multidevice/cases/">Enclosures</a></h3>
    <p>Different enclosures for your board.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🔄 <a href="/sidecartridge-multidevice/revisions/">Board revisions</a></h3>
    <p>Tracing the path of the SidecarTridge Multi-device boards.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🗄️ <a href="/sidecartridge-multidevice/publicfloppydb/">Public Floppy DB</a></h3>
    <p>Contribute to the Floppy Images Database with your own images</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🗄️ <a href="/sidecartridge-multidevice/publicromdb/">Public ROM DB</a></h3>
    <p>Contribute to the ROM Images Database with your own images</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>🗄️ <a href="/sidecartridge-multidevice/unofficial_firmwares/">Unoficial Firmwares</a></h3>
    <p>Smart people out there building incredible stuff with the device</p>
  </div>

</div>

## 👉 Do you want to test the new firmware?
{: #do-you-want-to-test-the-new-alpha-firmware }

<!-- Scoped styles for the alpha CTA -->
<style>
  .alpha-cta {
    background: linear-gradient(135deg,#5b7cfa 0%, #7c3aed 60%, #b832f6 100%);
    color: #fff;
    border-radius: 16px;
    padding: 1.25rem;
    box-shadow: 0 10px 30px rgba(124,58,237,.25);
    margin: 1rem 0 1.25rem 0;
  }
  .alpha-cta .row {
    display: grid;
    grid-template-columns: 1.2fr .8fr;
    gap: 1.25rem;
    align-items: start;
  }
  @media (max-width: 880px) {
    .alpha-cta .row { grid-template-columns: 1fr; }
  }
  .alpha-chip {
    display:inline-block; font-weight:700; letter-spacing:.02em;
    padding:.28rem .6rem; border-radius:999px; background:rgba(255,255,255,.15);
    border:1px solid rgba(255,255,255,.35); backdrop-filter: blur(6px);
    font-size:.78rem; margin-right:.5rem;
  }
  .alpha-title {
    margin:.2rem 0 .6rem 0; font-size:1.25rem; line-height:1.25;
  }
  .alpha-card {
    background: rgba(255,255,255,.1);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 12px; padding: .9rem .95rem;
  }
  .alpha-actions {
    display:flex; flex-wrap:wrap; gap:.55rem; margin-top:.75rem;
  }
  .alpha-btn {
    display:inline-block; text-decoration:none; font-weight:700;
    padding:.55rem .9rem; border-radius:10px; background:#fff; color:#3b2a7b;
    border:1px solid rgba(0,0,0,.06);
    box-shadow:0 2px 8px rgba(0,0,0,.15);
  }
  .alpha-btn.secondary {
    background: transparent; color:#fff; border:1px solid rgba(255,255,255,.6);
  }
  .alpha-list { margin:.4rem 0 0 1.05rem; }
  .alpha-list li { margin:.25rem 0; }
</style>

<div class="alpha-cta">
  <div class="row">
    <div>
      <span class="alpha-chip">ALPHA {{ site.FIRMWARE_ALPHA_VERSION }}</span>
      <span class="alpha-chip">Firmware v2</span>
      <h3 class="alpha-title">Do you want to test the new firmware?</h3>

      <div class="alpha-card">
        <h4 style="margin:.1rem 0 .35rem 0;">🚀 What’s new in Firmware v2?</h4>
        <ul class="alpha-list">
          <li><strong>🧩 Modular Microfirmwares</strong> — install/switch apps without reflashing.</li>
          <li><strong>📡 OTA downloads & updates</strong> — browse official/private repos over Wi-Fi.</li>
          <li><strong>⚙️ Per-app configurations</strong> — isolated settings in flash.</li>
          <li><strong>🛠️ Optimized dev workflow</strong> — faster build-test via emulator → device.</li>
        </ul>
      </div>

      <div class="alpha-actions">
        <a class="alpha-btn" href="https://github.com/sidecartridge/rp2-booster-bootloader/releases/download/{{ site.FIRMWARE_ALPHA_VERSION }}/rp-booster-{{ site.FIRMWARE_ALPHA_VERSION }}-full.uf2">💾 Download {{ site.FIRMWARE_ALPHA_VERSION }}</a>
        <a class="alpha-btn secondary" href="/sidecartridge-multidevice/getting_started_v2/">Getting Started Guide</a>
        <a class="alpha-btn secondary" href="/sidecartridge-multidevice/userguide_v2/">User Guide</a>
        <a class="alpha-btn secondary" href="/sidecartridge-multidevice/microfirmwares/">Browse Microfirmwares</a>
        <a class="alpha-btn secondary" href="/sidecartridge-multidevice/programming/">Development Guide</a>
      </div>
    </div>

    <div>
      <div class="alpha-card">
        <p style="margin:0 0 .5rem 0;">Check the following links below:</p>
        <ul style="margin:.2rem 0 0 1.05rem;">
          <li><strong>💾 Download {{ site.FIRMWARE_ALPHA_VERSION }} Release</strong></li>
          <li>Learn to install and configure with the <a style="color:#fff;text-decoration:underline;" href="/sidecartridge-multidevice/getting_started_v2/">Getting Started Guide</a></li>
          <li>Learn to download and install the different <a style="color:#fff;text-decoration:underline;" href="/sidecartridge-multidevice/userguide_v2/">microfirmwares</a></li>
          <li>Browse the list of available <a style="color:#fff;text-decoration:underline;" href="/sidecartridge-multidevice/microfirmwares/">microfirmwares</a></li>
          <li>Are you a brave developer? Check the <a style="color:#fff;text-decoration:underline;" href="/sidecartridge-multidevice/programming/">Development Guide</a></li>
        </ul>
      </div>
    </div>
  </div>
</div>

Explore, learn, and contribute to the SidecarTridge Multi-device project!