---
layout: default
title: SidecarTridge USB-C PD Multi-Rail Power Supply Units
nav_order: 0
nav_exclude: true
toc: false
has_toc: false
---


![SidecarTridge USB-C PD Multi-Rail board](/sidecartridge-usb-c-pd-psu/assets/images/USB-C-PD-BOARD.png)

# SidecarTridge USB-C PD Multi-Rail Power Supply Unit board

## The USB-C PD Multi-Rail Power Supply Unit board

This USB-C Power Delivery multi-rail converter board is designed to generate clean, regulated +5 V, +12 V, and −12 V inside the machine. The output rails can deliver up to 3 A on +5 V, 3 A on +12 V, and 0.3 A on −12 V. It is intended for use in retro computing applications, such as powering vintage computers like the Atari ST/STE/MegaST or Amiga 500 or other electronics projects that require multiple voltage rails.

The board is powered by a USB-C PD charger that must provide either 15 V or 20 V input voltage. It includes overcurrent and thermal protection features to ensure safe operation. The board is compact and easy to integrate into existing systems, making it a convenient solution for powering retro computing devices.

## USB-C PD charger requirements

**It is important to note that this board is not a standalone power supply and requires an external USB-C PD charger to function.**

* Minimum output: 60 W
* Required PD profiles: 15 V and 20 V
* Recommended capability: 15 V 3 A and 20 V 3 A or higher
* Cable: certified USB-C rated 60 W or 100 W
* Multiport chargers must deliver the full 60 W on the chosen port
* PD is required; QC-only or PPS-only chargers are not supported

## List of charger models tested

> **Warning:** Power adapters must be PD 3.0 compliant. Some chargers with PD 3.1 may not work properly -specifically with support for Extended Power Range (EPR), although they announce backwards compatibility with PD 3.0.

| Brand         | Model                          | Output Power | Notes|
|---------------|--------------------------------|--------------|--------------------------------------------|
| Anker       | A2039 (523-Series) Power Adapter | 47 W         | OK. A user reported ghosting issues. |
| Apple       | A2166 USB-C Power Adapter      | 96 W         | OK |
| Apple       | A2743 USB-C Power Adapter      | 70 W         | OK |
| Baseus       | GaN PD Power Adapter        | 65 W         | OK. With STE computers fails to deliver enough power. |
| Baseus       | GaN PD Power Adapter        | 100 W         | OK |
| BIOnd       | BGG-GRS-65W Power Adapter    | 65 W         | OK. Low cost device in GAME stores. It says it has 65W but I doubt (45W?) |
| Dell     | LA60NM200 Power Adapter         | 60 W         | OK |
| Essager      | GaN PD Power Adapter        | 100 W         | OK. Reported ghosting issues. |
| Lenovo      | ADLX65YLC3D Power Adapter    | 65 W         | OK |
| Raspberry Pi | P4123 - 27W USB-C Power Adapter      | 27 W         | OK with 15V. With STE computers fails to deliver enough power. |
| Raspberry Pi | P5224 - 45W USB-C Power Adapter      | 45 W         | OK. Cheapest option with remarkable quality. |



## List of SidecarTridge products using the USB-C PD Multi-Rail board

### USB-C PD Multi-Rail PSU Drop-In Replacement Kit for Atari ST/STE/MegaST

![SidecarTridge USB-C PD Multi-Rail PSU Drop-In](/sidecartridge-usb-c-pd-psu/assets/images/USB-C-PD-INTERNAL-KIT-ATARI-ST.png)

- [Product page](https://sidecartridge.com/products/usb-c-pd-psu-atari-st/)
- [Shopify store](https://store.sidecartridge.com/products/usb-c-pd-multi-rail-power-supply-unit-for-atari-st-e-and-megast)
- [Quickstart installation guide](https://sidecartridge.com/quickstart/usb-c-pd-psu-atari-st/)

### External USB-C PD Multi-Rail PSU + Enclosure + Cable Harness for Atari “short model” ST

![External USB-C PD PSU with printed enclosure](/sidecartridge-usb-c-pd-psu/assets/images/USB-C-PD-external-kit.jpg)

Our external kit is aimed at the earliest “short model” Atari ST units that originally relied on an internal linear PSU. It ships fully assembled: the USB-C PD multi-rail board is pre-mounted inside a printed ABS enclosure, the harness terminates in the correct 7-pin power connector, and the cable exit already includes strain relief. Add any 60 W (or higher) USB-C PD charger that supports 15 V/20 V profiles and you can power an ST without re-opening the case.

Key points:

- Single USB-C PD input, regulated +5 V/+12 V/−12 V output for the short-model ST mainboard
- Harness length matched to fit directly into the rear power inlet of a bare chassis
- Includes printed enclosure, fasteners, and internal wiring loom — just plug into a PD brick and your Atari
- Ideal for labs/repairs when you need an immediately swappable supply for case-less boards

### External USB-C PD Multi-Rail PSU + Cable Harness Kit for Atari “short model” ST

Prefer to print your own shell? This version bundles the populated USB-C PD board plus the short-model ST harness and strain-relief hardware, letting you reuse an enclosure of your choice.

- Ships with the same wiring loom and rubber grommet as the pre-built external unit
- Download the enclosure STL from the product page (or remix your own); the design uses standard M3 machine screws and nuts to clamp the two halves together
- Recommended hardware: four M3 × 12 mm pan-head screws with matching M3 hex nuts for the enclosure, plus two M2.5 × 10 mm self-tapping screws for the cable clamp
- Perfect if you already have a 3D printer or want to match a custom color/finish

Both external options rely on the same USB-C PD charger requirements listed above, so you can share a single high-quality PD brick across multiple Atari systems.
