---
layout: default
title: Hardware Interface
nav_order: 4
---

# Hardware Interface
This section delves into the hardware interface of the SidecarT board, specifically the way the board and the code in the RP2040 handle the mismatch of the size of the buses between the RP2040 and the Atari ST cartridge port.

## The Atari ST Cartridge Port

### Overview

The Atari ST, unveiled in the mid-1980s, boasted a cartridge port that, paradoxically, was not immensely popular, defying the widespread trend of cartridge utilization in computers and gaming consoles of that period.

The cartridge port of the Atari ST served as a direct extension of the system's bus, reflecting the era's prevailing hardware technology and design ideologies.

{:refdef: style="text-align: center;"}
![ST Cartridge Pinout](https://sidecart.xyz/assets/blog/images/stcartport.png)
{: refdef}

The port adopted a **double-row 40-pin configuration**, engineered to gain direct access to the system's bus. This allowed external cartridges to interface seamlessly with the main system without the necessity for intricate adapters or converters.

Typical of many computers from its epoch, the Atari ST was grounded in **TTL (Transistor-Transistor Logic) technology**, defining logical levels (high or low) through standard TTL voltage levels. Furthermore, the cartridge port offered a **+5V power pin** to energize the cartridges, aligning with the TTL logic levels utilized in the Atari ST. Ground pins were also furnished to form the electrical circuit and ascertain stable operation.

Despite the Atari ST's CPU clock functioning at 8MHz, its system clock operated at a mere 2MHz—quadruple the speed of the CPU clock. During each system clock cycle, the CPU could delegate a memory address on the bus to read, obtaining a response on the data bus from the device in the cartridge port within approximately 500ns. More can be learned from [this article](https://pasti.fxatari.com/68kdocs/AtariSTCycleCounting.html).

### Address, Data, & Control Lines

The cartridge port was designed with a **limited number of 68000 control lines** to simplify cartridge construction, thereby enabling developers to forge various hardware expansions without confronting the multifaceted intricacies of interfacing with the 68000’s control lines. The Atari ST's designers deliberately engineered the cartridge port to be **read-only**. This decision was due to a desire to simplify control lines or potentially due to financial constraints. Although this read-only characteristic limited certain solutions dependent on the cartridge, it inadvertently catalyzed the development of ingenious alternatives.

Serving as an extension of its primary system bus, the Atari ST's cartridge port utilized 24 **address lines** (A0-A23), enabling it to address up to 16MB (2^24 bytes) of memory, which was limited to 4MB due to some address space being allocated to ROMs and peripherals. A mere 17 address lines (A0=!UDS, A1-A15, A16=!ROM4) were routed to the cartridge port, used to access the memory range from FA0000 to FBFFFF, thereby addressing a substantial 128 Kbytes of ROM memory effectively.

{:refdef: style="text-align: center;"}
![ST Memory Map (info-coach.fr)](https://sidecart.xyz/assets/blog/images/stmemorymap_french.jpeg)
{: refdef}

The Atari ST incorporated a 16-bit data bus, correlating with **data lines** D0-D15. This allowed a 16-bit word to be transmitted in a single bus cycle. The UDS and LDS lines addressed either the upper or lower 8 bits of this 16-bit word, thus permitting byte-level access. The data lines were read-only.

In addition to the address and data lines, several **control lines** were crucial for selecting the ROM and determining which parts of the data lines to read. These encompassed the ROM select lines ROM3 and ROM4, as well as UDS and LDS, which were integral for upper and lower byte selection.

## The Raspberry Pi Pico W GPIOs

## Building a Pure time multiplexing on a multiplexed bus with the RP2040

## How to orchestrate the access to the Atari ST cartridge address and data buses


