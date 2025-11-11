---
layout: home
title: SidecarTridge Documentation Site
nav_exclude: true
redirect_from: 
  - /sidecartridge-v2-user-guide/
  - /sidecartridge-v2-user-guide
  - /sidecartridge-v2-programming-guide/
  - /sidecartridge-v2-programming-guide
  - /downloads
  - /downloads/
  - /sidecartridge-v2-microfirmwares/
  - /sidecartridge-v2-microfirmwares

---

![SidecarTridge TOS](/assets/images/SIDECARTRIDGE_TEXT_1920x416_BLACK.png)

# SidecarTridge Documentation Site

![Discord](https://img.shields.io/discord/1160868666162823218?style=flat&label=Discord&link=https%3A%2F%2Fdiscord.com%2Finvite%2Fu73QP9MEYC)

<!-- Project list – single column with left thumbnail -->
<style>
  .proj-list {
    display: grid;
    grid-template-columns: 1fr;      /* always one per row */
    gap: 1rem;
    margin-top: 0.75rem;
  }
  .proj-card {
    background: #f8f9fa;
    border-radius: 14px;
    padding: 1rem 1.1rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    transition: transform .12s ease, box-shadow .12s ease;
  }
  .proj-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(0,0,0,0.12);
  }
  .proj-inner {
    display: grid;
    grid-template-columns: 112px 1fr; /* thumbnail left, content right */
    gap: .9rem;
    align-items: center;
  }
  @media (max-width: 520px) {
    .proj-inner { grid-template-columns: 1fr; } /* stack on very small screens */
  }
  .proj-thumb {
    width: 100%;
    max-height: 96px;
    object-fit: contain;
    border-radius: 10px;
    background: #fff;
    padding: .25rem;
    border: 1px solid #e9ecef;
  }
  .proj-card h2 {
    margin: 0 0 .25rem 0;
    font-size: 1.15rem;
    line-height: 1.25;
  }
  .proj-card h2 a { text-decoration: none; }
  .proj-card p {
    margin: 0;
    font-size: .95rem;
    color: #333;
  }
  .support-note {
    margin-top: 2rem;
    padding: 1rem;
    background: #f1f3f5;
    border-radius: 10px;
    text-align: center;
    font-size: 1rem;
    color: #222;
  }
</style>

<div class="proj-list">

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-multidevice/assets/images/BOARD-3.1-PICOW-PERSPECTIVE.png" alt="SidecarTridge multi-device thumbnail">
      <div>
        <h2><a href="/sidecartridge-multidevice/">SidecarTridge Multi-device for Atari ST/MegaST/STE/MegaSTE</a></h2>
        <p>State-of-the-art multi-device emulator crafted for the Atari ST, STE, and Mega series.</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-psu/assets/images/psu_kit_top-thumbnail.png" alt="SidecarTridge PSU thumbnail">
      <div>
        <h2><a href="/sidecartridge-psu/">SidecarTridge PSU for Atari ST/MegaST/STE</a></h2>
        <p>A modern, solderless replacement power supply unit designed for Atari ST, STE and MegaST computers.</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-usb-c-pd-psu/assets/images/USB-C-PD-BOARD.png" alt="SidecarTridge USB-C PD Multi-Rail Power Supply Unit thumbnail">
      <div>
        <h2><a href="/sidecartridge-usb-c-pd-psu/">SidecarTridge USB-C PD Multi-Rail Power Supply</a></h2>
        <p>A modern USB-C PD Multi-Rail PSU drop-in replacement for Atari ST/STE/MegaST and Amiga computers</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-tos/assets/images/sidecartridge-tos-boards-versions-thumbnail.png" alt="SidecarTridge TOS thumbnail">
      <div>
        <h2><a href="/sidecartridge-tos/">SidecarTridge TOS emulator for Atari ST/MegaST/STE/MegaSTE</a></h2>
        <p>A compact board designed to emulate Atari ST internal ROMs, allowing users to access any TOS version without swapping chips.</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-BOXED-KIT-BOARD-V3-THUMBNAIL.png" alt="SidecarTridge 256KB Decoder thumbnail">
      <div>
        <h2><a href="/sidecartridge-tos-256kb-decoder/">SidecarTridge TOS 256KB Decoder for Atari ST/MegaST</a></h2>
        <p>A Decoder board that enables 256KB ROM decoding for Atari ST and MegaST series with the TOS emulator.</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/acsi2stm-atari-st/assets/images/ACSI2STM2-TOP-CONNECTOR.png" alt="ACSI2STM HD thumbnail">
      <div>
        <h2><a href="/acsi2stm-atari-st/">ACSI2STM Hard Disk for ST/MegaST/STE/MegaSTE</a></h2>
        <p>A modern hard disk device for Atari ST/MegaST/STE/MegaSTE.</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-rom/assets/images/PINOUT_DIAGRAM_V2_1280px.png" alt="SidecarTridge ROM thumbnail">
      <div>
        <h2><a href="/sidecartridge-rom/">SidecarTridge ROM emulator board</a></h2>
        <p>Programmable 512 KB ROM emulator for 8/16-bit data buses with dynamic speed selection. The core custom board inside the TOS emulator.</p>
      </div>
    </div>
  </div>

  <div class="proj-card">
    <div class="proj-inner">
      <img class="proj-thumb" src="/sidecartridge-kickstart/assets/images/KICKSTART-A500-TOP.png" alt="SidecarTridge Kickstart thumbnail">
      <div>
        <h2><a href="/sidecartridge-kickstart/">SidecarTridge Kickstart emulator</a></h2>
        <p>A compact board designed to emulate Amiga internal ROMs, allowing users to access any Kickstart version without swapping chips.</p>
      </div>
    </div>
  </div>

</div>

<div class="support-note">
  Looking for support? <a href="https://discord.com/invite/u73QP9MEYC">Join our Discord server</a> or <a href="mailto:sidecart+support@gooddatalabs.com">drop us an email</a>!
</div>

