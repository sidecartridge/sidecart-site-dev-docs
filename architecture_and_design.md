---
layout: default
title: Architecture and Design
nav_order: 3
---

# Architecture and Design
This section explores the underlying architecture and design principles of the SidecarT board. Understanding the architecture and design is crucial for developers to effectively interact with the board and develop robust and efficient applications.

{: .important }
The SidecarT board is a hardware solution that provides an environment for the execution of applications in a RP2040 Microcontroller -manufactured by the Raspberry foundation- that can share a range of its RAM memory with the host computer, an Atari ST computer series.

## The SidecarT board from the Atari ST perspective

For the Atari ST, the SidecarT board simplistically emerges as a ROM memory expansion. The incorporation of the RP2040 microcontroller into the Atari ST's cartridge port enables it to share a spectrum of its RAM memory with the Atari ST computer, which perceptively reads the shared RAM memory as if it were a ROM memory expansion. The swift processing capabilities of the RP2040 mask its true nature, providing the Atari ST with a seamless memory interaction without realizing it's interacting with a microcontroller sharing its RAM memory instead of a conventional ROM memory. This nuance fosters a crucial benefit: the Atari ST doesn’t require any software driver to interact with the SidecarT board, blissfully unaware of its existence and perceives it purely as a ROM memory expansion.

There are two basic **functional modes**:

### Full ROM Emulation Mode

In what we denote as the **Full ROM Emulation Mode**, the Atari ST effortlessly reads the shared RAM memory as if perusing through a full address range of the ROM memory expansion, void of any perceptible differences.

### Hybrid Emulation Mode

However, the capabilities of the RP2040 microcontroller extend far beyond merely sharing its RAM memory. Especially, considering the selected variant of the RP2040 Raspberry Pi Pico W comes embellished with WiFi and Bluetooth capabilities, coupled with the integration of a microSD card reader on the SidecarT board, it amplifies its utility. This ushers in the **Hybrid Emulation Mode**, where the Atari ST accesses the shared RAM memory but only a specific subrange of addresses of the ROM memory expansion. The other subranges are allocated to implement a command protocol between the host and the microcontroller, fostering an interactive session with applications running on the RP2040.

In this mode, awareness of the SidecarT board is mandatory for the Atari ST, necessitating a software driver to establish interaction. Nevertheless, this driver can reside in the ROM address subrange, maintaining a nearly transparent operation from the perspective of the Atari ST computer.

In the expansive realm of the **Hybrid Emulation Mode**, the SidecarT can mimic various functionalities like emulating Floppy disks, hard disks, network interfaces, Real Time Clocks, and peripheral devices such as printers and keyboards. Furthermore, it can serve as a computational delegate to shoulder intensive processes (hi there Demoscene developers!).


## The SidecarT board from the RP2040 microcontroller perspective

Contrary to the perceptual experience from the Atari ST, the RP2040 doesn’t literally share a range of its RAM memory. Given that from the RP2040's viewpoint, sharing its address and data memory bus isn't possible due to its embedded nature in the chip. Nonetheless, utilizing the RP2040’s capabilities, it successfully simulates memory sharing via its GPIO pins. Its adept speed allows it to respond to requests from the Atari ST computer, emulating the memory bus, which is why the Atari ST can read the shared RAM memory as though it’s a ROM memory expansion.

The RP2040 doesn’t merely stand as a passive memory-sharing entity. It’s a comprehensive microcontroller, embracing a wide spectrum of capabilities, enabling the implementation of a vast array of functionalities—executing swiftly enough to be almost imperceptible to the Atari ST computer.

### Full ROM Emulation Mode

In the **Full ROM Emulation Mode**, the RP2040 maximizes its hardware, employing Programmable Input Output (PIO) features and DMA channels to emulate the memory bus, responding to requests from the Atari ST computer. While straightforward in explanation, realizing this was no easy feat. However, this section of the code might not necessitate modification by developers, albeit being amongst the most intriguing ones. The functionality is implemented within the [`romemul.c`](https://github.com/diegoparrilla/atarist-sidecart-raspberry-pico/blob/main/romemul/romemul.c) and [`romemul.pio`](https://github.com/diegoparrilla/atarist-sidecart-raspberry-pico/blob/main/romemul/romemul.pio) files.

### Hybrid Emulation Mode

Transitioning to **Hybrid Emulation Mode**, the RP2040 extends beyond utilizing PIO and DMA. It reads incoming information from the Atari ST computer, interpreting it to materialize the desired functionality. **This code segment will demand modifications from developers to implement specific functionalities.** Refer to [Programming SidecarT](/programming_sidecart) for guidance on execution. An exemplification of this would be the implementation of the [Configurator](https://github.com/diegoparrilla/atarist-sidecart-firmware) application (or 'The Firmware'), a tool for configuring the SidecarT board. Implementational code for this functionality on the RP2040's end is housed within the [`romloader.c`](https://github.com/diegoparrilla/atarist-sidecart-raspberry-pico/blob/main/romemul/ronmloader.c) file.

## Board Components
   
## System Architecture

## Design Principles
   
## Design Considerations
