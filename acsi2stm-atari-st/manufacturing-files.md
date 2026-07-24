---
layout: default
title: Manufacturing files and open hardware
nav_order: 9
nav_exclude: false
parent: ACSI2STM Hard Disk for Atari ST
---

# Manufacturing files and open hardware
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

The SidecarTridge ACSI2STM boards are derivatives of the open-source [ACSI2STM project](https://github.com/retro16/acsi2stm) by retro16, released under its open-source [GNU license](https://github.com/retro16/acsi2stm/blob/stable/LICENSE). Building on that work, SidecarTridge produced improved variants such as the ACSI2STM Compact and the ACSI2STM Mini, with a 4-layer PCB and premium microSD slots among other refinements.

In the spirit of the original project, the hardware design and manufacturing files for these variants are published openly. You do not have to buy an assembled device: if you prefer to build your own, you can download the full manufacturing package from the SidecarTridge GitHub organization and have the boards produced at any PCB manufacturer.

{: .warning }
Building your own units from these files is done entirely at your own risk. This is open hardware, so by downloading and using these files you accept full responsibility for fabrication, assembly and the outcome, and you take on everything that using open hardware implies. The files are provided as is, with no warranty of any kind.

## What the package contains

Each board's manufacturing package typically includes:

- **Gerber files**: the PCB fabrication data (copper layers, soldermask, silkscreen and drill files).
- **Bill of Materials (BOM)**: the list of components with their references and part numbers.
- **Pick and place file (CPL / centroid)**: the position and orientation of each component for automated assembly.
- **Fabrication notes**: the board specification for the PCB manufacturer, such as layer stackup, board thickness or surface finish.

## Where to find them

The manufacturing files live in the [SidecarTridge GitHub organization](https://github.com/sidecartridge), next to the source and documentation of each device. Open the repository for the board you want and look for its hardware or manufacturing folder.

## Files per device

The per-device packages are listed below. This section grows as files are published for each board.

### ACSI2STM Compact

The full manufacturing package for the ACSI2STM Compact lives in the [`pcb/Compact` folder of the acsi2stm repository](https://github.com/sidecartridge/acsi2stm/tree/sidecartridge-castillian-realdb19/pcb/Compact), on the `sidecartridge-castillian-realdb19` branch.

Direct downloads:

- [Gerber files (ZIP)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-castillian-realdb19/pcb/Compact/Gerber%20-%20ACSI2STM%20Compact.zip)
- [Bill of Materials (CSV)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-castillian-realdb19/pcb/Compact/BOM%20-%20ACSI2STM%20Compact.csv)
- [Pick and place / CPL (CSV)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-castillian-realdb19/pcb/Compact/PickAndPlace%20-%20ACSI2STM%20Compact.csv)

Fabrication notes for the PCB manufacturer:

- Layers: 4
- PCB thickness: 1.6 mm
- Surface finish: lead-free HASL
- Specify layer sequence: yes

### ACSI2STM Mini

The full manufacturing package for the ACSI2STM Mini lives in the [`pcb/Mini` folder of the acsi2stm repository](https://github.com/sidecartridge/acsi2stm/tree/sidecartridge-mini-realdb19/pcb/Mini), on the `sidecartridge-mini-realdb19` branch.

Direct downloads:

- [Gerber files (ZIP)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-mini-realdb19/pcb/Mini/Gerber_ACSI2STM-MINI_PCB-ACSI2STM-MINI_2026-07-24.zip)
- [Bill of Materials (CSV)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-mini-realdb19/pcb/Mini/BOM_ACSI2STM-MINI_2026-07-24.csv)
- [Pick and place / CPL (CSV)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-mini-realdb19/pcb/Mini/PickAndPlace_PCB-ACSI2STM-MINI_2026-07-24.csv)
- [Schematic (PDF)](https://github.com/sidecartridge/acsi2stm/blob/sidecartridge-mini-realdb19/pcb/Mini/Schematic_ACSI2STM-MINI_2026-07-24.pdf)

Fabrication notes for the PCB manufacturer:

- Layers: 4
- PCB thickness: 1.2 mm
- Surface finish: lead-free HASL
- Specify layer sequence: yes

### DB19-to-IDC20 adapter

The [DB19-to-IDC20 adapter](/acsi2stm-atari-st/riser-boards/#db19-to-idc20-adapter-external-connection) is a passive board that exposes the ACSI2STM Compact IDC-20 header on an external DB-19 connector. Because it carries no active components, its package is a single Gerber file with no BOM or pick and place.

Direct download:

- [Gerber files (ZIP)](/acsi2stm-atari-st/assets/schematics/Gerber_DB19-IDC20-ADAPTER_2026-07-03.zip)

Fabrication notes for the PCB manufacturer:

- Layers: 2
- PCB thickness: 1.6 mm
- Surface finish: lead-free HASL

[Previous: Internal riser boards](/acsi2stm-atari-st/riser-boards/){: .btn .mr-4 }
[Main](/acsi2stm-atari-st/){: .btn }
