---
layout: default
title: Frequently Asked Questions
nav_order: 9
nav_exclude: false
parent: SidecarTridge Kickstart
---

# Frequently Asked Questions

This section compiles a list of frequently asked questions (FAQs) aimed at addressing common inquiries, clarifications, and concerns. Developers are encouraged to consult this section for quick references and insights.

## General Questions

### What is the maximum number of ROMs that the SidecarTridge Kickstart emulator can support?

Across Kickstart hardware revisions, the limit is driven by flash size, not the number of selectable entries. With 16MB of flash you can typically store dozens of 256–512KB images; SWITCHER will list the stored images and let you pick the active one.

### Which Amiga motherboards are supported?

The A500 family revisions (rev3/rev5/rev6a) and the A2000 Kickstart socket are supported using the matching carrier board. See the [Compatibility](/sidecartridge-kickstart/compatibility/) page for details.

### Can I use the SidecarTridge Kickstart emulator with an Amiga that is not listed?

Potentially, if a carrier board exists for that ROM socket and the board uses a 68000-compatible 512KB Kickstart layout. If your model is unlisted, contact us before purchase.

### Which Kickstart sizes are supported?

Classic 256KB Kickstart 1.x/early 2.x images and 512KB Kickstart 2.04/2.05/3.x images are supported. Custom ROMs like DiagROM/EmuTOS that use the same pinout and size also work.

### Why is the SidecarTridge Kickstart limited to 16MB of flash storage?

The current ROM board uses 16MB of addressable SPI flash on the RP2350 platform.

### Will the SidecarTridge Kickstart emulator support larger flash storage in the future?

This is a possibility, depending on future hardware developments.

### Why do I need a RESCUE button?

The RESCUE button recovers the SidecarTridge ROM board in case of a failed firmware update or a broken image, allowing you to restore the device to a known good image. This is especially useful for developers and users who want to experiment with custom firmware.

### Why is the RESCUE button not on the SidecarTridge ROM board?

Due to space constraints and the potential for users to access the RESCUE button through a cable or case hole, it is not included directly on the SidecarTridge ROM board.

### Why does the SidecarTridge Kickstart emulator use a FAT12 filesystem?

The FAT12 filesystem is used to ensure compatibility with all operating systems, including Windows, macOS, and Linux. It is a simple and efficient filesystem that is easy to implement and use.


### Why is the name of the Kickstart/ROM images limited to 64 characters?

The name of the images is limited to 64 characters to ensure it is possible to fit 64 names in 512 bytes of RAM memory. The memory available in the RP2350 microcontroller is limited, so the firmware must be optimized to fit within these constraints.

## Hardware Questions

### How do I know the SidecarTridge Kickstart board is powered on?

A red LED lights when powered.

### Can I use the board in an A500 if the Kickstart ROM is soldered?

No. You need a socketed ROM position. If your ROM is soldered, have a technician install a socket first (see [Before You Buy](/sidecartridge-kickstart/before-buy/)).

### Which carrier board should I order?

Match the carrier to your motherboard revision: A500 rev3/rev5/rev6a each have their own kit; the A2000 Kickstart socket uses the A500-family carrier. See [Compatibility](/sidecartridge-kickstart/compatibility/).

## Software Questions

### How do I update the firmware of the SidecarTridge Kickstart emulator?

Follow the steps in [Getting Started](/sidecartridge-kickstart/getting-started/#firmware-installation) to enter BOOTSEL mode and copy the firmware UF2.

### Will firmware updates erase my Kickstart images?

Standard updates do not overwrite your stored images. As a best practice, keep a backup of your ROM images on your PC before flashing new firmware.

### How do I switch between Kickstart versions?

Use the SWITCHER application from the `ROMEMUL` volume on your Amiga, or edit `DEFAULT.TXT`/`RESCUE.TXT` over USB and eject to reindex. See the [User Guide](/sidecartridge-kickstart/user-guide/) for details.

[Previous: Troubleshooting](/sidecartridge-kickstart/troubleshooting/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Changelog](/sidecartridge-kickstart/changelog/){: .btn }
