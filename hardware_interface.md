---
layout: default
title: Hardware Interface
nav_order: 4
---

# Hardware Interface
This section delves into the hardware interface of the SidecarT board, specifically the way the board and the code in the RP2040 handle the mismatch of the size of the buses between the RP2040 and the Atari ST cartridge port.

## The Atari ST cartridge port

### Overview

The Atari ST, released in the mid-1980s, featured a cartridge port. Against the trend of that time, it was not a very popular expansion port of the computer, especially being an essential feature on many computers and game consoles of that era.

The Atari ST's cartridge port was a direct extension of the system's bus, reflecting the underlying hardware technology and design principles of the time.


{:refdef: style="text-align: center;"}
![ST cartridge pinout](https://sidecart.xyz/assets/blog/images/stcartport.png)](https://sidecart.xyz/assets/blog/images/stcartport.png)
{: refdef}

The cartridge port featured a **double-row 40-pin configuration** designed to directly access the system's bus. This made the addition of external cartridges straightforward, as they could directly interface with the main system without complex adapters or converters.

The Atari ST, like many computers of its era, was primarily based on **TTL (Transistor-Transistor Logic) technology**. This means the logic levels (i.e., what's considered a logical "high" or "low") were defined by typical TTL voltage levels. In practical terms, a high signal would be close to +5V, and a low signal would be close to 0V. This aspect will be key in the design of SidecarT, as we will see. The cartridge port provided a **+5V power pin** to supply power to the cartridges. This was consistent with the TTL logic levels used in the Atari ST. Additionally, ground pins were provided to complete the electrical circuit and ensure proper operation.

The Atari ST featured a CPU clock of 8MHz, but its system clock actually operated at 2MHz—four times slower than the CPU clock. Yes, you read it right. In each system clock cycle, the CPU could place a memory address on the bus to read, receiving a response on the data bus from the device in the cartridge port. This process would take approximately 500ns. You can learn more in [this awesome article](https://pasti.fxatari.com/68kdocs/AtariSTCycleCounting.html).

### Address, Data, & Control Lines: The bus

The design of the cartridge port had a **reduced number of 68000 control lines**. This simplification was crucial to ease the construction of cartridges, making it more feasible for developers to create a range of hardware expansions without dealing with excessive complexity in interfacing with the 68000’s control lines. Interestingly, the designers of the Atari ST made a conscious decision for the cartridge port to be **read-only**. This choice might have stemmed from the simplification of control lines or potentially due to budget constraints; it’s a bit of a mystery. While this read-only nature was a limiting feature for solutions relying on the cartridge, it inevitably sparked the ingenuity to develop smart workarounds.

The Atari ST's cartridge port was an extension of its main system bus. The Motorola 68000 allowed a 32-bit address space (4 gigabytes), but the Atari ST's native address space would use 24 **address lines** (A0-A23), which allows it to address up to 16MB (2^24 bytes) of memory but reduced to 4MB because some of the address space was for ROMs and peripherals. Only 17 address lines (A0=!UDS, A1-A15, A16=!ROM4) were routed to the cartridge port and were used to access the memory range from FA0000 to FBFFFF, addressing effectively 128 Kbytes of ROM memory.

{:refdef: style="text-align: center;"}
![ST Memory map (info-coach.fr)](https://sidecart.xyz/assets/blog/images/stmemorymap_french.jpeg)](https://sidecart.xyz/assets/blog/images/stmemorymap_french.jpeg)
{: refdef}

It had a 16-bit data bus, corresponding to **data lines** D0-D15. This allowed for a 16-bit word to be transferred in a single bus cycle. The UDS and LDS lines addressed either the upper or lower 8 bits of this 16-bit word, allowing for byte-level access. The data lines were read-only.

Beyond address and data lines, several **control lines** were essential for selecting the ROM and the parts of the data lines to read. These would include the ROM select lines ROM3 and ROM4, as well as UDS and LDS (for upper and lower byte selection).

## The Raspberry Pi Pico W GPIOs

## Building a Pure time multiplexing on a multiplexed bus with the RP2040

## How to orchestrate the access to the Atari ST cartridge address and data buses


