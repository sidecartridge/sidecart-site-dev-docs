---
layout: home
title: SidecarTridge Multi-device
nav_order: 0
nav_exclude: false
has_children: true
---


![SidecarTridge Multi-device](/sidecartridge-multidevice/assets/images/BOARD-3.1-PICOW-PERSPECTIVE.png)

# SidecarTridge Multi-device Documentation 
{: .no_toc }
{: .d-inline-block }

{{ site.FIRMWARE_VERSION }}
{: .label .label-purple }


Welcome to the SidecarTridge Multi-device Documentation! This comprehensive guide is aimed at providing developers with all the information needed to get started with the SidecarTridge Multi-device board, understand its architecture, and contribute to its development. Please refer to the relevant sections below to explore specific topics.

You can learn about the new features and improvements in the latest firmware release by watching the video below:

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/S1IZKrRRqhw?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


## 🚀 Latest STABLE Firmware: {{ site.FIRMWARE_VERSION }}
* **💾 [Download STABLE Release {{ site.FIRMWARE_VERSION }}](https://sidecartridge.com/downloads)**
* **📝 [Changelog for STABLE Release {{ site.FIRMWARE_VERSION }}](https://github.com/sidecartridge/rp2-booster-bootloader/releases/tag/{{ site.FIRMWARE_VERSION }})**
* 🕒 [Older Versions](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/releases)

## 🐞 Bugs, Issues, and Enhancements
* [Project management tool](https://github.com/orgs/sidecartridge/projects/2)

## Other Quick links
* [SidecarTridge source code repositories](https://github.com/sidecartridge/)


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
    <h3>🚀 <a href="/sidecartridge-multidevice/getting_started_v2/">Getting started</a></h3>
    <p>Guidance on the initial steps including prerequisites, board assembly instructions, setup and configuration.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>⚙️ <a href="/sidecartridge-multidevice/userguide_v2/">User Guide</a></h3>
    <p>Learn how to use the SidecarTridge Multi-device.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🔧 <a href="/sidecartridge-multidevice/microfirmwares/">Microfirmwares</a></h3>
    <p>The self-contained program that runs standalone providing the features of the device.</p>
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

  <!-- <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💻 <a href="/sidecartridge-multidevice/software_development/">Software Development</a></h3>
    <p>Setting up the development environment, compiling the code, debugging, testing and building the firmware.</p>
  </div> -->

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
    <h3>🔧 <a href="/sidecartridge-multidevice/how_to_v2/">How to</a></h3>
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
    <h3>❓ <a href="/sidecartridge-multidevice/faq_v2/">FAQ</a></h3>
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


Explore, learn, and contribute to the SidecarTridge Multi-device project!