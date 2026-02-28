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

* Minimum output: 45 W (laptop-class USB-C PD supply)
* Required PD profiles: 15 V and 20 V
* Recommended capability: 15 V 3 A and 20 V 3 A or higher
* Cable: certified USB-C rated 60 W or 100 W
* Multiport chargers must deliver the full wattage on the chosen port
* PD 3.0 is required; QC-only or PPS-only chargers are not supported

## List of charger models tested

> **Warning:** Power adapters must be PD 3.0 compliant. Some chargers with PD 3.1 may not work properly—specifically those advertising Extended Power Range (EPR)—even if they claim backwards compatibility with PD 3.0.

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

This fully assembled external PSU directly replaces the original 7-pin Atari ST power brick used by the earliest “short” 520ST units. The SidecarTridge USB-C PD multi-rail board is pre-mounted inside a resin enclosure, the harness is professionally crimped with the correct JST-VH and 7-pin DIN connectors, and strain relief is already in place. Plug in a compliant USB-C PD charger, connect the DIN plug to the ST, and power up—no need to open the computer or touch mains voltages.

Key points:

- Single USB-C PD input with independently regulated +5 V/+12 V/−12 V rails sized for SidecarTridge add-ons
- Harness length matched to the short-model ST rear inlet; keeps wiring tidy even on bare chassis
- Includes printed enclosure, internal wiring loom, fasteners, and pre-installed rubber feet—ready out of the box
- Integrated +5 V USB-A auxiliary output for devices such as ACSI2STM, SatanDisk, or Gotek
- Ideal for labs/repairs when you need a safe, swappable supply without reassembling the computer

#### Charger requirements for the external PSU

- USB-C Power Delivery 3.0 charger supporting **both 15 V and 20 V** profiles
- **45 W minimum output** (60 W+ recommended if you share the brick with other hardware)
- Certified USB-C cable rated for 60 W or 100 W
- Multi-port chargers must be able to deliver the full wattage on the selected port
- QC-only, PPS-only, or proprietary fast-charge standards are **not** supported
- Some PD 3.1 / EPR chargers can mis-negotiate; stick to the [tested adapter list](https://docs.sidecartridge.com/sidecartridge-usb-c-pd-psu/) when in doubt

#### Compatibility

Designed for short 520ST units that shipped with the external 7-pin PSU brick, including motherboards:

- C070115
- C070243

If your ST has an internal PSU (later STF/STE/Mega variants), use the internal drop-in kit instead.

#### Contents

Each **External USB-C PD PSU for Atari ST** box includes:

- White resin enclosure with pre-installed rubber feet
- SidecarTridge USB-C PD multi-rail board, mounted and wired
- Professionally built 1 m harness (JST-VH 3.96 mm + 7-pin DIN)
- Four M2 × 8 mm screws and hardware for the enclosure
- Cable strain relief + grommet assembly

Fully assembled and ready to use—no soldering or internal modifications required.

#### FAQ

**Do I need to open the Atari ST?**  
No. Unplug the old brick, connect the USB-C PD charger to the new PSU, and plug the DIN connector into the ST.

**What is the weight of the PSU unit?**  
Approximately 250 g.

**Can it harm my computer?**  
The PSU is designed specifically around the ST’s power requirements with independent regulation on each rail. Just follow the installation steps and use a compliant charger.

**Can it power other devices like ACSI2STM, SatanDisk, or Gotek?**  
Yes. Use the integrated +5 V USB-A output for storage peripherals that cannot draw power from the ST motherboard.

**Which USB-C PD charger do you recommend?**  
Any reputable laptop-class PD 3.0 charger that meets the requirements works. A proven budget option is the Raspberry Pi 45 W USB-C Power Supply. See the [tested adapter list](https://docs.sidecartridge.com/sidecartridge-usb-c-pd-psu/) for more models.

### External USB-C PD Multi-Rail PSU + Cable Harness Kit for Atari “short model” ST

Prefer to print your own shell? This version bundles the populated USB-C PD board plus the short-model ST harness and strain-relief hardware, letting you reuse an enclosure of your choice.

- Ships with the same wiring loom and rubber grommet as the pre-built external unit
- Download the enclosure STL from the product page (or remix your own); the design uses standard M3 machine screws and nuts to clamp the two halves together
- Recommended hardware: four M3 × 12 mm pan-head screws with matching M3 hex nuts for the enclosure, plus two M2.5 × 10 mm self-tapping screws for the cable clamp
- Perfect if you already have a 3D printer or want to match a custom color/finish

Both external options rely on the same USB-C PD charger requirements listed above, so you can share a single high-quality PD brick across multiple Atari systems.
