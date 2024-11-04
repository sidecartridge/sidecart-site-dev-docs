---
layout: default
title: Hardware Installation
nav_order: 4
nav_exclude: false
parent: SidecarTridge TOS 256KB Decoder

---

# Hardware Installation
{: .no_toc }

This chapter will guide you through the process of installing the SidecarTridge TOS 256KB Decoder in your Atari ST or Mega ST series computer, specifically how to solder the decoder to the Motorola 68000 CPU. Once the decoder is installed, you can continue with the installation of the SidecarTridge TOS Emulator as described in the [hardware installation guide](/sidecartridge-tos/hardware-installation/).

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Accessing the Motorola 68000 CPU

### Overview

In order to install the SidecarTridge TOS 256KB Decoder, you will need to access the Motorola 68000 CPU on the Atari ST or Mega ST motherboard. The decoder board must be soldered directly onto the CPU to function correctly. This process requires precision and care to avoid damaging the CPU or other components on the motherboard.

{: .warning}
Soldering the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU requires soldering skills and knowledge of electronics. If you are not experienced with soldering, it is recommended to seek professional assistance to avoid damaging your Atari ST or Mega ST motherboard.

### Tools Required
- Soldering iron
- Low temperature solder or solder paste
- Flux
- Isopropyl alcohol

### Safety Precautions
1. **Power Off and Unplug:** Ensure the Atari ST is powered off and unplugged from any power source before beginning the disassembly.
2. **Ground Yourself:** Wear an anti-static wrist strap to prevent static electricity from damaging internal components. Alternatively, touch a grounded metal object periodically to discharge static electricity.
3. **Work on a Clean Surface:** Use a clean, static-free workspace to prevent any debris or static discharge from interfering with the components.

## Locate the Motorola 68000 CPU pins

### Alignment and Orientation of the Decoder

The SidecarTridge TOS 256KB Decoder board is designed to be soldered directly onto the Motorola 68000 CPU. The board has a specific alignment and orientation to ensure proper functionality. The decoder board should be aligned with the CPU pins and soldered in place according to the following guidelines:

1. **Orientation**: The decoder board should be oriented with the components facing up, the solder pins facing down sitting on the CPU pins, and the connector facing towards the opposite side of the CPU orientation notch.
2. **Alignment**: The decoder board must sit on top of the CPU pins with the same numbers displayed on the CPU and the decoder board. The pins should align correctly to ensure a proper connection. The motherboards have the pins numbered from 1 to 64, but if the numbers are blurred or missing, you can use the CPU orientation notch as a reference: the pin at the top left corner is pin 1, and the pin at the top right corner is pin 64.

Before starting with the soldering process, ensure that the decoder board is correctly aligned and oriented with the Motorola 68000 CPU.

### Soldering the Decoder to the CPU with low-temperature solder

Since the computers are old and the components are sensitive to heat, it is recommended to use low-temperature solder to solder the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU. Low-temperature solder melts at a lower temperature than standard solder, reducing the risk of damaging the CPU or other components on the motherboard.

1. **Apply Flux**: Apply a small amount of flux to the CPU pins to help the solder flow and create a strong bond.
2. **Align the Decoder**: Carefully place the SidecarTridge TOS 256KB Decoder board on top of the Motorola 68000 CPU, aligning the pins correctly.
3. **Solder the Pins**: Using a soldering iron, solder each pin of the decoder board to the corresponding pin on the CPU. Be careful not to create solder bridges between adjacent pins.
4. **Inspect the Solder Joints**: After soldering all the pins, inspect the connections to ensure that each pin is securely soldered and there are no solder bridges or cold joints.
5. **Clean the Board**: Use isopropyl alcohol to clean the board and remove any flux residue.

### Soldering the Decoder to the CPU with solder paste

Alternatively, you can use solder paste to solder the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU. Solder paste is a mixture of flux and solder particles that can be applied to the CPU pins and the decoder board before reflowing the solder to create a strong bond.

1. **Apply Solder Paste**: Apply a small amount of solder paste to the CPU pins using a fine-tipped applicator or syringe.
2. **Align the Decoder**: Carefully place the SidecarTridge TOS 256KB Decoder board on top of the Motorola 68000 CPU, aligning the pins correctly.
3. **Reflow the Solder**: Use a hot air rework station or a reflow oven to heat the solder paste and create a strong bond between the decoder board and the CPU pins. If you don't have a reflow station, you can use a soldering iron to heat the solder paste, but be careful not to overheat the components.
4. **Inspect the Solder Joints**: After reflowing the solder, inspect the connections to ensure that each pin is securely soldered and there are no solder bridges or cold joints.
5. **Clean the Board**: Use isopropyl alcohol to clean the board and remove any flux residue.

{: .warning}
If you are not comfortable with soldering or do not have the necessary tools and skills, it is recommended to seek professional assistance to install the SidecarTridge TOS 256KB Decoder. Incorrect soldering can damage the CPU or other components on the motherboard.

### Verify the Installation

After soldering the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU, verify the installation by checking the connections and ensuring that the decoder board is securely attached to the CPU. Before powering on the Atari ST or Mega ST computer use a multimeter to check for continuity between the decoder board pins and the CPU pins to confirm a proper connection. It is also a good idea to check continuity between adjacent pins to ensure there are no solder bridges.

If you have not removed the old ROMs from the motherboard, you can power on the computer to verify that the computer boots correctly. If the installation was successful, the decoder board should not have any impact on the computer's operation until the SidecarTridge TOS Emulator is installed.

{: .warning}
Do not pass to the next step until you have verified that the SidecarTridge TOS 256KB Decoder does not interfere with the normal operation of the Atari ST or Mega ST computer with the old ROMs installed.


## Continue with the SidecarTridge TOS Emulator Installation

Once the SidecarTridge TOS 256KB Decoder is installed on the Motorola 68000 CPU, you can proceed with the installation of the SidecarTridge TOS Emulator as described in the [hardware installation guide](/sidecartridge-tos/hardware-installation/). The decoder board will work in conjunction with the emulator to provide access to 256KB ROMs on your Atari ST or Mega ST computer.

## Connect the Decoder to the Carrier Board

Once the SidecarTridge TOS 256KB Decoder is soldered to the Motorola 68000 CPU and the TOS Emulator installed, connect the decoder board to the SidecarTridge TOS emulator carrier board using the 6-pin connector. The connector should be securely attached to both boards to ensure a proper connection.

## Power On and Test

After completing the installation of the SidecarTridge TOS 256KB Decoder and the TOS Emulator, power on the Atari ST or Mega ST computer to test the functionality of the decoder board. If the installation was successful, you should be able to access and run different TOS versions and custom ROMs on your Atari ST or Mega ST computer.

[Previous: Getting Started](/sidecartridge-tos/getting-startedV2/){: .btn .mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }
[Next: User Guide](/sidecartridge-tos/user-guideV2/){: .btn }

