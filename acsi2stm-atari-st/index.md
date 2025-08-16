---
layout: home
title: ACSI2STM Hard Disk for Atari ST
nav_order: 0
nav_exclude: false
has_children: true
---


![ACSI2STM Hard Disk](/acsi2stm-atari-st/assets/images/ACSI2STM2-TOP.png)

# ACSI2STM Hard Disk for Atari ST

The ACSI2STM is an open-source hard drive emulator designed for Atari ST computers, enabling the use of SD cards as storage devices. Powered by an STM32 microcontroller, it bridges the Atari’s ACSI port with modern SD cards, providing a cost-effective, reliable, and versatile solution for expanding storage on vintage Atari systems.

After extensive testing of the original ACSI2STM device, SidecarTridge has introduced an enhanced version with several key improvements:

- **Upgraded 4-Layer PCB Design:** This new design ensures optimal performance, even in older and noisier computer systems, by reducing issues like crosstalk and electrical interference.

- **Premium microSD Card Slots:** Utilizing the same high-quality slots as the SidecarTridge Multi-device, these are more robust and feature a built-in eject mechanism, facilitating easy insertion and removal of microSD cards.

- **Optimized Crystal Oscillator Circuit:** Adjustments in the capacitors of the crystal oscillator circuit have been made to enhance performance and stability. This modification addresses a flaw in the original design that could cause operational failures or prolonged boot times. For detailed information on recalibrating the capacitors in the crystal oscillator circuit, please refer to the [GitHub issue discussion](https://github.com/retro16/acsi2stm/issues/58).

- **External LED connector:** The new design includes a connector for an external LED, allowing users to display the activity of the ACSI2STM device. This feature is particularly useful for those who prefer to place the ACSI2STM inside their Atari Mega ST or Mega STE, as it provides a visual indication of the device’s status without needing to open the case. 

**The new board design is slightly larger than the original ACSI2STM with this very distintictive castile shape, and that is why it is called the "Castillian" ACSI2STM board. The new design is fully compatible with the original ACSI2STM firmware and retains all the features and functionality of the original device.**

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
    <h3>📘 <a href="/acsi2stm-atari-st/introduction/">Introduction</a></h3>
    <p>An overview of the ACSI2STM device and its features and benefits</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>💲 <a href="/acsi2stm-atari-st/before-buy/">Before You Buy</a></h3>
    <p>What you need to know before you buy</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-guide">Guide</span>
    <h3>🤝 <a href="/acsi2stm-atari-st/user-guide/">User Guide</a></h3>
    <p>Please read this section to know about open issues and compatibility.</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🛠️ <a href="/acsi2stm-atari-st/external-led/">External Activity LED</a></h3>
    <p>How to connect an external activity LED to the ACSI2STM</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-howto">How-to</span>
    <h3>🔧 <a href="/acsi2stm-atari-st/troubleshooting/">Troubleshooting</a></h3>
    <p>Common issues and how to solve them</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>? <a href="/acsi2stm-atari-st/faq/">Frequently Asked Questions</a></h3>
    <p>Answers to common questions about the ACSI2STM</p>
  </div>

  <div class="toc-card">
    <span class="toc-chip chip-ref">Reference</span>
    <h3>📦 <a href="/acsi2stm-atari-st/cases/">Enclosures/Cases</a></h3>
    <p>List of enclosures and cases available for the ACSI2STM</p>
  </div>

</div>


{: .warning}
The ACSI2STM is an Open Source project, and you can find the source code and schematics in the [GitHub repository](https://github.com/retro16/acsi2stm/). The repository contains more in depth information about the project, and you can also contribute to the project by submitting issues or pull requests.


