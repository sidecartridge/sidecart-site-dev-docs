---
layout: default
title: SidecarTridge USB-C PD Multi-Rail Power Supply Units
nav_order: 0
nav_exclude: true
toc: false
has_toc: false
---


![SidecarTridge USB-C PD Multi-Rail board](/sidecartridge-usb-c-pd-psu/assets/images/USB-C-PD-BOARD.png)

<div class="hero-highlights">
  <h1>Internal USB-C PD PSU for Atari ST/STE/Mega ST</h1>
  <ul>
    <li>Drop-in USB-C PD multi-rail board – regulated +5V / +12V / −12V</li>
    <li>Compatible with C070115 / C070243 ST/STE/Mega mainboards</li>
    <li>Solderless harness, USB-C panel mount, USB-A auxiliary output</li>
    <li>Works with SidecarTridge Multi-Device, ACSI2STM, and modern expansions</li>
  </ul>
</div>

## Why upgrade to USB-C PD inside the Atari ST

This USB-C Power Delivery multi-rail converter board replaces the original internal PSU and generates clean, regulated +5 V, +12 V, and −12 V rails inside the machine. Ageing stock PSUs develop drifting voltages, noisy 12 V rails, and sudden shutdowns that can kill SidecarTridge expansions. Dropping in the USB-C PD board eliminates the mains transformer, keeps only low-voltage DC inside the chassis, and ensures all rails stay within spec even under modern loads.

### Quick comparison

|                   | Original PSU (1980s) | Mean Well RPD-60 kit | USB-C PD Multi-Rail kit |
|-------------------|----------------------|----------------------|-------------------------|
| Input             | 230 V / 120 V AC     | 230 V / 120 V AC     | USB-C PD 15 V / 20 V    |
| Rails             | +5 V, +12 V, −12 V   | +5 V, +12 V, −12 V   | +5 V, +12 V, −12 V (+5 V USB-A) |
| Installation      | Stock                | Solderless drop-in   | Solderless drop-in + USB-C panel |
| Safety            | Full AC inside ST    | AC inside ST         | Low-voltage DC only     |
| Expansion headroom| Limited              | Good                 | Excellent (SidecarTridge-ready) |

> Want to keep an external brick instead? See [External USB-C PD PSU →](/products/external-usb-c-pd-psu-atari-st/)

## USB-C PD charger requirements

**This board is not a standalone power supply; it requires an external USB-C PD charger.**

- Minimum output: 45 W (60 W recommended)
- Required PD profiles: 15 V and 20 V
- Recommended capability: 15 V 3 A and 20 V 3 A or higher
- Cable: certified USB-C rated 60 W or 100 W
- Multiport chargers must deliver the full wattage on the chosen port
- PD 3.0 is required; QC-only or PPS-only chargers are not supported
- PD 3.1 / EPR bricks may mis-negotiate; check the [tested adapter list](https://docs.sidecartridge.com/sidecartridge-usb-c-pd-psu/)

## Kit contents

- Riser PSU PCB matching the original mounting points
- SidecarTridge USB-C PD Multi-Rail power board
- Solderless harness (JST-VH 3.96 mm to TE 171822-6)
- USB-C panel + JST-PH 2.0 cable
- 3D-printed covers for AC inlet and power switch
- M3 screws/nuts and rubber feet
- +5 V USB-A auxiliary output for ACSI2STM, Gotek, etc.

## Installation overview

1. Remove the vintage PSU and shield (ST/STE/Mega instructions on the [Quickstart](https://sidecartridge.com/quickstart/usb-c-pd-psu-atari-st/)).
2. Mount the USB-C PD board and riser using the supplied screws.
3. Install the USB-C panel where the original AC inlet lived.
4. Plug in the JST harness to the motherboard header.
5. Connect a compliant USB-C PD charger.

Opening the Atari ST requires only a screwdriver. STF/STE systems let you lift the metal shield without full removal; Mega ST variants need complete shield removal.

## Frequently asked questions

### What USB-C PD power adapter do I need?
Use a PD 3.0 charger rated for at least 60 W (20 V/3 A). Laptop-class chargers from reputable brands work best. For a budget EU option, the [Raspberry Pi 45 W USB-C supply](https://www.raspberrypi.com/products/45w-power-supply/) is tested and stable.

### Can I choose 15 V or 20 V?
Yes. A hardware slider selects the PD profile (15 V or 20 V). Pick 20 V for more headroom if your charger supports it. The status LED confirms negotiation.

### Does it work on Mega STE, TT, or Falcon?
No—use the dedicated Mega STE or TT/Falcon solutions. For short 520ST machines with external bricks, buy the [external USB-C PD PSU](https://sidecartridge.com/products/external-usb-c-pd-psu-atari-st/).

### Do I need to open the Atari ST?
Yes, but the kit is fully solderless. Remove the original PSU, install the board, and close the machine. No mains voltages remain inside once the USB-C panel is installed.

### Can the PSU harm my computer?
It meets the power requirements of ST/STE/Mega ST boards and adds overcurrent/thermal protection. Follow the Quickstart instructions and use a compliant USB-C PD charger.

### Is this product for me?
This is a homebrew upgrade for hobbyists comfortable opening their Atari ST. If you prefer a drop-in external brick for short models, use the external kit.

### Why can’t I access the store or Discord even though you ship to my country?
We require basic respect in all community channels; abusive behavior leads to revoked access. We build for tinkerers who enjoy experimentation.

## Documentation and links

- [Product page (Shopify)](https://store.sidecartridge.com/products/usb-c-pd-multi-rail-power-supply-unit-for-atari-st-e-and-megast)
- [Quickstart installation guide](https://sidecartridge.com/quickstart/usb-c-pd-psu-atari-st/)
- [SidecarTridge USB-C PD documentation](https://docs.sidecartridge.com/sidecartridge-usb-c-pd-psu/)
- [KB: microSD card not detected](../SIDECARTRIDGE-KB/products/sidecartridge-multidevice/topics/microsd-not-detected.md)
- [KB: Improving SIDECART Wi-Fi reliability](../SIDECARTRIDGE-KB/products/sidecartridge-multidevice/topics/improving-wifi-signal.md)

