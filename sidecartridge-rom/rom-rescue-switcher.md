---
layout: default
title: ROM Rescue Switcher
nav_order: 5.5
nav_exclude: false
parent: SidecarTridge ROM
---

# ROM Rescue Switcher
{: .no_toc }

The ROM Rescue Switcher is a bare-metal rescue ROM for the SidecarTridge ROM Emulator family. It boots directly from the rescue image and lets you choose another ROM image already stored on `ROMEMUL`, without depending on TOS, GEMDOS, BIOS, XBIOS, Kickstart, or AmigaOS.

Project links:

- [GitHub project](https://github.com/sidecartridge/romemul-switcher-rom)
- [Releases](https://github.com/sidecartridge/romemul-switcher-rom/releases)

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## What it is

The ROM Rescue Switcher is intended as a recovery tool for ROM-emulator integrations that support a rescue image.

When the target system enters rescue mode, the switcher boots and presents a ROM chooser menu. From there, you can select another ROM image already available on the device and continue booting with that image instead of editing files from a host computer.

## Supported platforms

Current builds are published for:

- Atari ST / Mega ST
- Atari STE / Mega STE
- Amiga 500 / Amiga 2000

## Available images

Download the image that matches your target machine and ROM size:

| Target system | ROM size | Rescue image file |
|---------------|----------|-------------------|
| Atari ST / Mega ST | 192 KB | `RESCUE_SWITCHER_vX.Y.Z_192KB.img` |
| Atari STE / Mega STE | 256 KB | `RESCUE_SWITCHER_vX.Y.Z_256KB.img` |
| Amiga 500 / Amiga 2000 | 512 KB | `RESCUE_SWITCHER_vX.Y.Z_512KB.img` |

{: .note }
Replace `vX.Y.Z` with the actual release version you downloaded.

## Installing the rescue image

1. Download the correct rescue image from the [project releases page](https://github.com/sidecartridge/romemul-switcher-rom/releases).
2. Connect the device to your computer so the `ROMEMUL` volume appears.
3. Copy the rescue image file to the root of `ROMEMUL`.
4. Edit `RESCUE.TXT` so it contains exactly the rescue image file name.
5. Eject the `ROMEMUL` volume safely.
6. Enter rescue mode on the target system or product integration.

{: .warning }
Always eject or unmount `ROMEMUL` after copying files or changing `RESCUE.TXT`, so the device reindexes the file list correctly.

## What happens at boot

At rescue boot, the switcher:

- starts directly from ROM without host operating system services
- verifies its own ROM contents before entering the chooser
- scans the images already stored on the device
- shows a text-based selection menu
- boots the ROM image you select

## Notes for SidecarTridge products

If you are using a product built on the ROM Emulator family, the rescue-mode procedure is product-specific:

- [SidecarTridge TOS rescue mode](/sidecartridge-tos/user-guideV2/#rescue-mode)
- [SidecarTridge Kickstart rescue mode](/sidecartridge-kickstart/user-guide/#rescue-mode)

For custom carrier-board integrations, rescue-mode activation depends on your board design and firmware setup.

## Development status

The current project publishes active rescue-switcher builds for Atari ST, Atari STE, and Amiga Kickstart-replacement ROM setups.

[Previous: Firmware & Files (ROMEMUL)](/sidecartridge-rom/firmware-and-files/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Firmware API](/sidecartridge-rom/firmware-api/){: .btn }
