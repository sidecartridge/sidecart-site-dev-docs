---
layout: default
title: Board revisions
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /revisions
  - /revisions/
---

# Board revisions
{: .no_toc }
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

This page documents every hardware revision of the SidecarTridge Multi-device board. The revision number for your unit is printed on the silkscreen on the underside of the PCB.

Prefer video? Start here:

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
        src="https://www.youtube-nocookie.com/embed/RvREQNScEzE?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


## Revision 0: The original

{:refdef: style="text-align: center;"}
![Multi-device revision 0](https://sidecartridge.com/assets/blog/images/sidecart-rev0.png)
{: refdef}

Owners of Multi-device boards purchased before February 2024 have Revision 0, the original model. It evolved from the launch prototype with only minor tweaks in order to manufacture a first batch of 25–30 boards. Demand quickly outpaced that plan. To keep the product affordable we stayed with a two-layer PCB, optimized trace widths for reliability, and stuck to a footprint defined by the cartridge connector, the Pico W dimensions, and straightforward panelization so shipping and production stayed economical.

## Revision 1: The Hidden Failure

{:refdef: style="text-align: center;"}
![Multi-device revision 1](https://sidecartridge.com/assets/blog/images/sidecart-rev1.png)
{: refdef}

Revision 1 shrank the board to roughly 70 % of the original and moved to a four-layer PCB, repositioning the Pico W headers, SELECT button, and several passives to improve signal stability and mechanical rigidity. Those changes exposed new issues: some Atari ST models became finicky, the slimmer mounting holes were easier to crack, and existing Revision 0 cases no longer fit. The takeaway was clear—preserve backward compatibility whenever possible. **Revision 1 never shipped commercially; only a few prototypes exist.**

## Revision 2: The Hybrid

{:refdef: style="text-align: center;"}
![Multi-device revision 2](https://sidecartridge.com/assets/blog/images/sidecart-rev2.png)
{: refdef}

### Revision 2.0

Shipping since February 2024, Revision 2.0 keeps the four-layer stack-up while returning to the original footprint so existing cases still fit. It adds larger case mounting holes, refines button placement, introduces a power LED, and supports a castellated Pico W option for lower-profile installs. The goal: blend the best of Revisions 0 and 1 without breaking anything owners already built.

### Revision 2.1

Revision 2.1 makes two small tweaks to 2.0:
- The power LED resistor moves to 6.8 kΩ to reduce brightness.
- The Ground and UART headers return to their original configuration so JLPCB no longer charges the SMT pins as though they were through-hole components.

### Revision 2.2.0

Revision 2.2.0 brings two notable upgrades:
- Dual USB-A power-only ports. Their rails are fused and protected with Schottky diodes to keep your Atari ST, the SidecarTridge, and connected USB devices safe.
- Dual JST-SH 2× male, 1.0 mm pitch connectors for the RESET and SELECT buttons, making it easier to add or remove front-panel controls inside enclosures.

### Revision 2.2.1

Revision 2.2.1 adds a single JST-SH 3× male, 1.0 mm pitch connector for UART and GND, simplifying hookups to the Raspberry Pi Debug Probe.

### Revision 2.3.0

Revision 2.3.0 refines the 2.2.x family to improve Pico W RF performance:
- Rerouted traces beneath the Pico W module.
- A larger keep-out (no-copper) area under the antenna window.

### Revision 3.1

{:refdef: style="text-align: center;"}
![Multi-device revision 3.1](/sidecartridge-multidevice/assets/images/BOARD-3.1-KIT-TOP.png)
{: refdef}

Revision 3.1 is a broad quality-of-life refresh:
- **Smaller & more compact** – Slimmer geometry makes installation easier without dropping features.
- **Enhanced performance & stability** – ENIG PCBs plus an optimized track layout improve signal integrity and reduce noise, especially in aging systems.
- **Better power efficiency** – Updated power distribution lowers consumption without compromising performance.
- **Stronger Wi‑Fi** – A larger copper window for the Pico W antenna delivers more reliable wireless links.
- **Flexible Pico W integration** – Supports both direct soldering and reflow assembly for the Pico W.
- **Expanded maker connectivity** – Offers JST and classic two-pin headers for RESET/SELECT, UART access, and full DEBUG connectivity.

### Revision 3.2

Revision 3.2 focuses on power resilience for tired or marginal power supplies. It replaces the previous input protection circuit with a dual-voltage input switcher paired with an LM66200 ideal-diode controller. The new design automatically balances both power inputs, minimizes voltage drop, and shields the Multi-device from brown-outs when a computer’s PSU can no longer deliver a healthy 5 V rail.


## Want to contribute?

You can contribute to this page. Please scroll to the bottom of the page and click on the "Edit this page on GitHub" link. You can then submit a pull request with your changes.

[Previous: Enclosures](/sidecartridge-multidevice/cases/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Public Floppy Database](/sidecartridge-multidevice/publicfloppydb/){: .btn }
