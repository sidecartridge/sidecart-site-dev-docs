---
layout: default
title: Croissant Open Hardware
nav_order: 11
nav_exclude: false
parent: SidecarTridge Keyboard
---

# Croissant Open Hardware
{: .no_toc }

This page collects the released hardware design files for **SidecarTridge Croissant**, including the diagram, schematics, PCB manufacturing data, assembly files, and licensing information.

The material published here applies to the **Croissant** internal Atari ST / Atari STe keyboard emulator board.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Why This Design Is Being Released

The Croissant hardware design is intentionally very simple. The real value and “magic” of the project lives in the firmware and software, which are also open source.

This hardware is being published to:

* document the design for long-term preservation
* support repair and maintenance of existing boards
* enable learning and understanding of how the system works
* allow anyone to reproduce the board for personal use

If you want to build your own Croissant board, you are absolutely welcome to do so.

However:

* **commercial use is not allowed**
* **professional selling of assembled boards is not permitted**

This follows the same non-commercial philosophy as the rest of the project. If you are interested in commercial use, please contact the author for separate permission.

Publishing the design also makes it easier to understand how the board interfaces with the Atari keyboard path and what is required to manufacture or assemble it.

## Hardware Diagram

The Croissant schematic export is also available as a PNG preview:

- [Schematic preview PNG](/sidecartridge-keyboard/assets/schematics/Schematic_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.png)

![Croissant schematic preview](/sidecartridge-keyboard/assets/schematics/Schematic_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.png)

## Schematics

The schematic PDF documents the electrical design of the Croissant board.

- [Schematic PDF](/sidecartridge-keyboard/assets/schematics/Schematic_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.pdf)
- [Schematic preview PNG](/sidecartridge-keyboard/assets/schematics/Schematic_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.png)

## Manufacturing Files

### Gerber Files

The PCB fabrication package for board production:

- [Gerber ZIP](/sidecartridge-keyboard/assets/schematics/Gerber_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.zip)

These manufacturing files are prepared to work directly with common PCB fabrication services that accept standard Gerber, BOM, and Pick and Place inputs.

Croissant is a simple 2-layer board, so the default low-complexity 2-layer PCB option is the correct starting point for fabrication.

### Bill of Materials

The BOM used to source the required components:

- [BOM CSV](/sidecartridge-keyboard/assets/schematics/BOM_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.csv)

### Pick and Place

The assembly placement file for automated board assembly:

- [Pick and Place CSV](/sidecartridge-keyboard/assets/schematics/PickAndPlace_PCB_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.csv)

Together with the BOM and Gerbers, the assembly files are intended to be usable as-is for a straightforward 2-layer PCB assembly order.

## Release Files

The current Croissant hardware release includes:

- [Schematic PDF](/sidecartridge-keyboard/assets/schematics/Schematic_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.pdf)
- [Schematic preview PNG](/sidecartridge-keyboard/assets/schematics/Schematic_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.png)
- [Gerber ZIP](/sidecartridge-keyboard/assets/schematics/Gerber_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.zip)
- [BOM CSV](/sidecartridge-keyboard/assets/schematics/BOM_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.csv)
- [Pick and Place CSV](/sidecartridge-keyboard/assets/schematics/PickAndPlace_PCB_CROISSANT-KEYBOARD-Emulator_REV-1.2.0.csv)
- [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

If you later publish source design files, they can be linked from this same section.

## Related Repositories

The Croissant hardware relies on the SidecarTridge Keyboard firmware and booster software repositories:

- [SidecarTridge Keyboard firmware](https://github.com/sidecartridge/rp2-atarist-rpikb)
- [SidecarTridge Keyboard booster](https://github.com/sidecartridge/rp2-atarist-rpikb-booster)

## License

The SidecarTridge Croissant hardware design files are licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

In practical terms, this means:

- attribution is required
- commercial use is not allowed without separate permission
- derivative works must be shared under the same license

## Notes for Builders

These files are provided to help document and reproduce the board, but builders should review all data before ordering PCBs or assembly.

Before manufacturing, verify:

- board revision
- connector orientation
- component availability
- assembly origin, rotation, and layer conventions

{: .warning}
Hardware files are provided as-is. Anyone building the board is responsible for validating the manufacturing data before production or installation.

[Previous: Changelog](/sidecartridge-keyboard/changelog/){: .btn .mr-4 }
[Main](/sidecartridge-keyboard/){: .btn }
