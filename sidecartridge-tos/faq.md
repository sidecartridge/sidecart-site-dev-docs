---
layout: default
title: Frequently Asked Questions
nav_order: 9
nav_exclude: false
parent: SidecarTridge TOS
---

# Frequently Asked Questions

This section compiles a list of frequently asked questions (FAQs) aimed at addressing common inquiries, clarifications, and concerns. Developers are encouraged to consult this section for quick references and insights.

## General Questions

### What is the maximum number of ROMs that the SidecarTridge TOS emulator can support?

Depend on the version of the SidecarTridge TOS emulator you have:
- **SidecarTridge TOS v1 and v2**: The number of ROMs that the device can support depends on the carrier board, not the SidecarTridge ROM emulator itself. The emulator is compatible at the signal level with any ROM, EPROM, or EEPROM with a bus width of 17 or 18 bits (256KBytes of address space), 8 or 16 bits of data bus, and CE and/or OE signals.
- **SidecarTridge TOS v3**: Same as the previous versions, the number of ROMs that the device can support depends on the carrier board, not the SidecarTridge ROM emulator itself. But it can support 512KB ROMs and an extra bit in the address bus. Sadly, the Atari ST/STE/MegaST/MegaSTE motherboards only support 192KB or 256KB ROMs, so the SidecarTridge TOS v3 is limited to 256KB ROMs.

### Why is the SidecarTridge TOS emulator not compatible with certain Atari ST motherboards?

Incompatibility usually arises from the lack of a carrier board that supports the specific number of ROMs required by the motherboard and the layout of the ROM sockets. Eventually, the SidecarTridge TOS emulator aims to be compatible with all Atari ST motherboards with the appropriate carrier board, subject to time and resource constraints.

### Can I use the SidecarTridge TOS emulator with an Atari ST motherboard that is not listed as supported?

Potentially yes, but it is best to inquire first. For unique or unknown motherboards, contact us to discuss compatibility and the possibility of developing a carrier board for it.

### Why is the SidecarTridge TOS emulator limited to 256KB ROMs maximum?

This is a limitation of the RP2040 microcontroller used in the v1 and v2 versions of the SidecarTridge ROM emulator. The RP2040 has a maximum address space of 256KB, which means it can only address up to 256KB of ROM memory.
The v3 version of the SidecarTridge TOS emulator can support 512KB ROMs thanks to the RP2350 microcontroller, but the Atari ST/STE/MegaST/MegaSTE motherboards only support 192KB or 256KB ROMs, so the SidecarTridge TOS v3 is limited to 256KB ROMs.

### Why is the SidecarTridge TOS limited to 16MBytes of Flash storage?

The RP2040 microcontroller in the SidecarTridge ROM Board has a maximum of 16MBytes of addressable SPI Flash memory.

### Will the SidecarTridge TOS emulator support larger Flash storage in the future?

This is a possibility, depending on future hardware developments.

### Why do I need a RESCUE button?

The RESCUE button recovers the SidecarTridge ROM board in case of a failed firmware update or a broken image, allowing you to restore the device to a known good image. This is specially useful for developers and users who want to experiment with custom firmware.

### Why is the RESCUE button not on the SidecarTridge ROM board?

Due to space constraints and the potential for users to access the RESCUE button through a cable or case hole, it is not included directly on the SidecarTridge ROM board.

### Why does the SidecarTridge TOS emulator use a FAT12 filesystem?

The FAT12 filesystem is used to ensure compatibility with all operating systems, including Windows, macOS, and Linux. It is a simple and efficient filesystem that is easy to implement and use.


### Why is the name of the TOS images limited to 64 characters?

The name of the TOS images is limited to 64 characters to ensure it is possible to fit 64 names in 512 bytes of RAM memory. The memory available in the RP2040 and RP2350 microcontroller is limited, so the firmware must be optimized to fit within these constraints.

## Hardware Questions

### There is no power LED on the SidecarTridge TOS emulator. How do I know if it is powered on?

The SidecarTridge TOS emulator board v1 and v2 does not have a power LED. However, the device is powered on when the carrier board is connected to the Atari ST motherboard and the Atari ST is powered on, or when the SidecarTridge TOS emulator is connected to a USB power source.

When the SidecarTridge TOS emulator is powered on and connected to a USB power source, you must press the RESET button during a few seconds to start the device. Then, it will appear as a USB drive on your computer with the name `ROMEMUL`.

Version 3 of the SidecarTridge TOS emulator has a red LED that indicates when the device is powered on.

### Can I use a 256KB ROM image in a ST/STF/STFM motherboard?

You can't use a 256KB ROM image in a ST/STF/STFM motherboard because these motherboards only support 192KB ROMs. 

Also, keep in mind that the TOS for ST/STF/STFM motherboards starts at address `0xFC0000` and ends at `0xFEFFFF`. The STE/MegaSTE TOS starts at `0xE00000` to `0xE3FFFF`.

**If you want to use a 256KB ROM image in a ST/STF/STFM motherboard checkout the [256KB Decoder](/sidecartridge-tos-256kb-decoder/) version of the SidecarTridge TOS emulator.**

## Software Questions

### How do I update the firmware of the SidecarTridge TOS emulator?

The firmware of the SidecarTridge TOS emulator can be updated following the instructions provided in the [Firmware Update](/sidecartridge-tos/getting-startedV2V2/#firmware-installation) section.

### I want to update the firmware of the SidecarTridge TOS emulator but I don't want to lose my TOS images. What should I do?

There are two firmwares available for the SidecarTridge TOS emulator: 
- the standard firmware with a EmuTOS image already flashed. **This firmware will overwrite the existing firmware and TOS images.**
- the update firmware with no EmuTOS image. **This firmware will keep the existing TOS images.**

Follow the instructions provided in the [Firmware Update](/sidecartridge-tos/getting-started/#firmware-installation) section to update the firmware without losing your TOS images.



[Previous: Troubleshooting](/sidecartridge-tos/troubleshooting/){: .btn .mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }
[Next: Changelog](/sidecartridge-tos/changelog/){: .btn }
