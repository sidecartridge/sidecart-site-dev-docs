---
layout: minimal
title: Frequently Asked Questions
nav_order: 9
nav_exclude: true
parent: SidecarTridge TOS
---

# Frequently Asked Questions

This section compiles a list of frequently asked questions (FAQs) aimed at addressing common inquiries, clarifications, and concerns. Developers are encouraged to consult this section for quick references and insights.

## General Questions

### What is the maximum number of ROMs that the SidecarTridge TOS emulator can support?

The number of ROMs that the device can support depends on the carrier board, not the SidecarTridge ROM emulator itself. The emulator is compatible at the signal level with any ROM, EPROM, or EEPROM with a bus width of 17 or 18 bits (256KBytes of address space), 8 or 16 bits of data bus, and CE and/or OE signals.

### Why is the SidecarTridge TOS emulator not compatible with certain Atari ST motherboards?

Incompatibility usually arises from the lack of a carrier board that supports the specific number of ROMs required by the motherboard and the layout of the ROM sockets. Eventually, the SidecarTridge TOS emulator aims to be compatible with all Atari ST motherboards with the appropriate carrier board, subject to time and resource constraints.

### Can I use the SidecarTridge TOS emulator with an Atari ST motherboard that is not listed as supported?

Potentially yes, but it is best to inquire first. For unique or unknown motherboards, contact us to discuss compatibility and the possibility of developing a carrier board for it.

### Why is the SidecarTridge TOS emulator limited to 256KB ROMs maximum?

It uses the RP2040 microcontroller in the SidecarTridge ROM emulator, which has a maximum of 264KB of RAM memory. With 8KB reserved for the program, the maximum ROM size is 256KB.

### Will the SidecarTridge TOS emulator support larger ROMs in the future?

Potentially, but it cannot be promised. There are rumors of a new RP2040 microcontroller with more memory and features, but it is not yet available.

### Why is the SidecarTridge TOS limited to 16MBytes of Flash storage?

The RP2040 microcontroller in the SidecarTridge ROM Board has a maximum of 16MBytes of addressable SPI Flash memory.

### Will the SidecarTridge TOS emulator support larger Flash storage in the future?

This is a possibility, depending on future hardware developments.

### Why do I need a RESCUE button?

The RESCUE button recovers the SidecarTridge ROM board in case of a failed firmware update or a broken image, allowing you to restore the device to a known good image. This is specially useful for developers and users who want to experiment with custom firmware.

### Why is the RESCUE button not on the SidecarTridge ROM board?

Due to space constraints and the potential for users to access the RESCUE button through a cable or case hole, it is not included directly on the SidecarTridge ROM board.

### Why is the FAT16 filesystem used in the SidecarTridge ROM board not fully implemented?

The FAT16 filesystem is used for storing TOS images. For performance reasons, it is implemented simply to store and read images sequentially, avoiding fragmentation issues.

### Why is the number of available TOS images limited to 64?

It's a design choice to keep the firmware simple and efficient. The number of available TOS images is limited to 64 to ensure that the firmware remains responsive and reliable. Future firmware updates may increase this limit.

### Why is the name of the TOS images limited to 56 characters?

The name of the TOS images is limited to 56 characters to ensure it is possible to fit 64 names in 512 bytes of RAM memory. The memory available in the RP2040 microcontroller is limited, so the firmware must be optimized to fit within these constraints.

## Hardware Questions

## Software Questions

## Troubleshooting Questions
