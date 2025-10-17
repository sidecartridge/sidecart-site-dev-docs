---
layout: default
title: Hardware Installation
nav_order: 3
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
- Multimeter
- Blue tack (optional)


### Safety Precautions
1. **Power Off and Unplug:** Ensure the Atari ST is powered off and unplugged from any power source before beginning the disassembly.
2. **Ground Yourself:** Wear an anti-static wrist strap to prevent static electricity from damaging internal components. Alternatively, touch a grounded metal object periodically to discharge static electricity.
3. **Work on a Clean Surface:** Use a clean, static-free workspace to prevent any debris or static discharge from interfering with the components.

## Locate the Motorola 68000 CPU pins

### Alignment and Orientation of the Decoder

The SidecarTridge TOS 256KB Decoder board is designed to be soldered directly onto the Motorola 68000 CPU. The board has a specific alignment and orientation to ensure proper functionality. The decoder board should be aligned with the CPU pins and soldered in place according to the following guidelines:

1. **Orientation**: The decoder board should be oriented with the components facing up, the solder pins facing down sitting on the CPU pins, and the connector facing towards the opposite side of the CPU orientation notch.

![Motorola 68000 orientation](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-BOARD-SOLDERING-1.png)

2. **Alignment**: The decoder board must sit on top of the CPU pins with the same numbers displayed on the CPU and the decoder board. The pins should align correctly to ensure a proper connection. The motherboards have the pins numbered from 1 to 64, but if the numbers are blurred or missing, you can use the CPU orientation notch as a reference: the pin at the top left corner is pin 1, and the pin at the top right corner is pin 64.

The left side of the decoder has the following signals printed, with the pin numbers in parentheses:

- AS (6) 
- RW (9)
- DTACK (10)
- BGACK (12) (V2.0 only with Blitter Patch enabled)
- CLK (15) (V2.0 only with Blitter Patch enabled)
- RESET (18) (V2.0 only with Blitter Patch enabled)

and the right side has the following signals printed, with the pin numbers in parentheses:

- A16 (44)
- A17 (45)
- A20 (48)
- +5V (49)
- A21 (50)
- A22 (51)
- A23 (52)
- GND (53)

![256KB Decoder orientation top](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-BOARD-SOLDERING-2.png)

![256KB Decoder orientation right](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-BOARD-SOLDERING-3.png)

![256KB Decoder orientation left](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-BOARD-SOLDERING-4.png)

Before starting with the soldering process, ensure that the decoder board is correctly aligned and oriented with the Motorola 68000 CPU.

{: .note}
A little bit of blue tack can be used to hold the decoder board in place while soldering. This will help to keep the board aligned with the CPU pins and prevent it from moving during the soldering process.

### Soldering the Decoder to the CPU with Low-Temperature Solder

Given the age and heat sensitivity of these computers, it’s recommended to use low-temperature solder when attaching the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU. This type of solder melts at a lower temperature than standard solder, minimizing the risk of damage to the CPU and other components on the motherboard.

1. **Apply Flux**: Begin by applying a small amount of flux to the CPU pins to help the solder flow smoothly and ensure a strong bond.
2. **Align the Decoder**: Carefully position the SidecarTridge TOS 256KB Decoder board on top of the Motorola 68000 CPU, making sure the pins are properly aligned.
3. **Solder the Pins**: With a soldering iron, solder each pin of the decoder board to the corresponding pin on the CPU. Take care to avoid creating solder bridges between adjacent pins.
4. **Inspect the Solder Joints**: Once all pins are soldered, inspect each connection to ensure secure soldering with no solder bridges or cold joints.
5. **Clean the Board**: Use isopropyl alcohol to clean the board and remove any flux residue.

### Soldering the Decoder to the CPU with Solder Paste

Alternatively, solder paste can be used to attach the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU. Solder paste is a blend of flux and solder particles applied to the CPU pins and decoder board, then reflowed to create a strong bond.

1. **Apply Solder Paste**: Using a fine-tipped applicator or syringe, apply a small amount of solder paste to the CPU pins.
2. **Align the Decoder**: Position the SidecarTridge TOS 256KB Decoder board carefully on top of the Motorola 68000 CPU, ensuring proper pin alignment.
3. **Reflow the Solder**: Use a hot air rework station or reflow oven to heat the solder paste, bonding the decoder board and CPU pins. If a reflow station isn’t available, you can use a soldering iron to heat the solder paste, taking care not to overheat the components.
4. **Inspect the Solder Joints**: After reflowing, inspect each connection to confirm secure soldering with no solder bridges or cold joints.
5. **Clean the Board**: Clean the board with isopropyl alcohol to remove any remaining flux residue.

{: .warning}
If you’re not confident in your soldering skills or don’t have the proper tools, it’s advisable to seek professional assistance for installing the SidecarTridge TOS 256KB Decoder. Improper soldering could damage the CPU or other motherboard components.


### A note to Mega ST owners 

#### 256KB Decoder V1.0

Some Mega ST models already have a board soldered on top of the CPU. This board is called the 'Blitter Fix' or 'Blitter Patch' and must be removed and placed on top of the SidecarTridge TOS 256KB Decoder. It is a small PCB that corrects a design flaw in the Mega ST motherboard related to the Blitter chip. The soldering of both boards is a bit tricky, but it can be done with care and precision as shown in the following image:

![256KB Decoder to Blitter Fix to Mega ST CPU](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-MEGAST-BLITTER.png)

#### 256KB Decoder V2.0

The SidecarTridge TOS 256KB Decoder V2.0 already has the Blitter patch integrated into the design. This means that you can use the SidecarTridge TOS 256KB Decoder V2.0 and removing the Blitter patch.

To install the SidecarTridge TOS 256KB Decoder V2.0, follow the same steps as described above for the V1.0 version and also:

1. Disconnect the cable from the motherboard to the Blitter patch and connect it to the SidecarTridge TOS 256KB Decoder V2.0 `WIRE` pad as shown in the following image below.
2. Solder the Blitter Patch specific pins `BGACK`, `CLK`, and `RESET` to the Motorola 68000 CPU. These pins are easy to identify because they have white silkscreen on the board.

![256KB Decoder V2.0 to Mega ST CPU](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-MEGAST-BLITTER-V2.png)


### Verify the Installation

After soldering the SidecarTridge TOS 256KB Decoder to the Motorola 68000 CPU, it’s essential to verify the installation to ensure all connections are secure. Before powering on your Atari ST or Mega ST, use a multimeter to check continuity between the decoder board pins and the CPU pins to confirm proper connections. Also, check continuity between adjacent pins to ensure there are no unintended solder bridges.

If the original ROMs are still installed on the motherboard, you can power on the computer to verify that it boots correctly. A successful installation of the decoder board will not affect the computer’s operation until the SidecarTridge TOS Emulator is added.

{: .warning}
Do not proceed to the next step until you have confirmed that the SidecarTridge TOS 256KB Decoder does not interfere with the normal operation of the Atari ST or Mega ST with the original ROMs installed.

## Continue with the SidecarTridge TOS Emulator Installation

Once the SidecarTridge TOS 256KB Decoder is installed on the Motorola 68000 CPU, you can proceed with the installation of the SidecarTridge TOS Emulator as described in the [hardware installation guide](/sidecartridge-tos/hardware-installation/). The decoder board will work in conjunction with the emulator to provide access to 256KB ROMs on your Atari ST or Mega ST computer.

## Connect the Decoder to the Carrier Board

Once the SidecarTridge TOS 256KB Decoder is soldered to the Motorola 68000 CPU and the TOS Emulator installed, connect the decoder board to the SidecarTridge TOS emulator carrier board using the 6-pin flat cable. The connector should be securely attached to both boards to ensure a proper connection.

This is how it should look like in an Atari ST:
![256KB Decoder to TOS Emulator for Atari ST](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-STDUAL-MOTHERBOARD.png)

And this is how it should look like in a Mega ST:
![256KB Decoder to TOS Emulator for Mega ST](/sidecartridge-tos-256kb-decoder/assets/images/256KB-DECODER-MEGAST-MOTHERBOARD.png)

## Power On and Test

After completing the installation of the SidecarTridge TOS 256KB Decoder and the TOS Emulator, power on the Atari ST or Mega ST computer to test the functionality of the decoder board. If the installation was successful, you should be able to access and run different TOS versions and custom ROMs on your Atari ST or Mega ST computer.

[Previous: Before you buy](/sidecartridge-tos-256kb-decoder/before-buy/){: .btn .mr-4 }
[Main](/sidecartridge-tos-256kb-decoder/){: .btn .mr-4 }
[Next: Compatibility](/sidecartridge-tos-256kb-decoder/compatibility/){: .btn }

