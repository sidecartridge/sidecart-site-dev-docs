---
layout: default
title: Upgrading an older Mega ST carrier board
nav_order: 5
nav_exclude: false
parent: SidecarTridge TOS 256KB Decoder
---

# Upgrading an older Mega ST carrier board for the 256KB Decoder
{: .no_toc }

This guide describes how to upgrade an older SidecarTridge TOS Emulator Mega ST carrier board that ships without the components required to drive the external SidecarTridge TOS 256KB Decoder. Once the components are added, the carrier board behaves like a current revision 4.0.0 or higher board and can be connected to the decoder using the standard 6-pin flat cable.

{: .warning}
This upgrade involves soldering on a small carrier PCB. You should have **solid soldering skills**, the **right tools** (temperature-controlled iron, fine tip, flux, solder wick or desoldering pump, magnification), and the **right materials** for the package you are working with (SMD or through-hole). If you are not comfortable with this kind of work, please ask an experienced technician to do it for you. Damaging the carrier board during the upgrade is not covered by warranty.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Step 1 - Identify the carrier board revision

Flip the Mega ST carrier board over and read the revision number printed on the back side of the PCB silkscreen.

## Step 2 - If the revision is 4.0.0 or higher, you are done

Carrier boards from revision 4.0.0 onward already ship with the multiplexer, decoupling capacitor, pull-up resistor and 2x3 pin header populated. You can connect the SidecarTridge TOS 256KB Decoder directly using the 6-pin flat cable and follow the standard [Hardware Installation](/sidecartridge-tos-256kb-decoder/hardware-installation/) guide. No upgrade is required.

## Step 3 - If the revision is below 4.0.0, identify SMD or through-hole

Older carrier boards come in two flavours depending on the manufacturing run:

- **SMD**: the multiplexer footprint is a surface-mount SOP-16 pad cluster and the passives are 0805 pads.
- **Through-hole**: you will see drilled holes for the multiplexer IC pins, plus separate holes for a resistor and a capacitor with 5.08 mm pin pitch.

A quick visual inspection of the back side of the carrier board is enough to tell which version you have.

## Step 4 - Bill of materials

### SMD variant

| Reference | Part | Package |
|-----------|------|---------|
| MUX | 74LS157 | SOP-16 |
| Capacitor | 100 nF | 0805 |
| Resistor | 10 kΩ | 0805 |
| Connector | IDC pin header 2x3, 2 mm pitch, right angle | Through-hole |

### Through-hole variant

| Reference | Part | Package |
|-----------|------|---------|
| MUX | 74LS157 | DIP-16 |
| Capacitor | 100 nF | Lead pitch 5.08 mm |
| Resistor | 10 kΩ | Lead pitch 5.08 mm |
| Connector | IDC pin header 2x3, 2 mm pitch, right angle | Through-hole |

{: .note}
The 2x3 right-angle IDC pin header is the same part for both variants. It is the connector where the 6-pin flat cable from the decoder board plugs in.

## Step 5 - Solder the components

Solder each component onto its footprint:

1. Start with the multiplexer (74LS157), respecting pin 1 orientation as marked on the silkscreen.
2. Solder the 100 nF decoupling capacitor.
3. Solder the 10 kΩ pull-up resistor.
4. Solder the 2x3 right-angle pin header, with the pins facing outward so the flat cable can reach the decoder board.

Inspect each joint under magnification. Look for bridges between adjacent pins on the multiplexer and on the pin header.

## Step 6 - Clear the solder jumpers SJ4, SJ5 and SJ6

The carrier board has three solder jumpers labelled **SJ4**, **SJ5** and **SJ6** that act as a bypass around the multiplexer. On older boards that shipped without the multiplexer populated, these jumpers may have been bridged with solder to keep the signal path closed.

If any of SJ4, SJ5 or SJ6 are bridged with solder, remove the solder from them using solder wick or a desoldering pump so the jumpers are left open. Leaving them bridged will keep the multiplexer shorted out and the decoder will not work correctly.

## Verify the upgrade

After soldering and clearing the jumpers, double-check the work before installing the carrier board back into the Atari Mega ST:

- All four components are firmly in place.
- No solder bridges between adjacent pins, especially on the multiplexer.
- SJ4, SJ5 and SJ6 are open (no solder bridge).
- Pin 1 of the multiplexer matches the silkscreen marking.

Once the inspection passes, the carrier board is ready to be connected to the SidecarTridge TOS 256KB Decoder. Continue with the standard [Hardware Installation](/sidecartridge-tos-256kb-decoder/hardware-installation/) guide.

[Previous: Compatibility](/sidecartridge-tos-256kb-decoder/compatibility/){: .btn .mr-4 }
[Main](/sidecartridge-tos-256kb-decoder/){: .btn .mr-4 }
