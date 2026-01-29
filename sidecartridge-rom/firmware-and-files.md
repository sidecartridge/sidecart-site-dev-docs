---
layout: default
title: Firmware & Files (ROMEMUL)
nav_order: 5
nav_exclude: false
parent: SidecarTridge ROM
---

# Firmware & Files (ROMEMUL)
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ROMEMUL volume

The ROM Emulator exposes its on-board flash as a **USB mass-storage volume** (FAT12), typically named **ROMEMUL**.

This is the same core workflow used across SidecarTridge ROM-emulation products (e.g., TOS emulator and Kickstart emulator):

- **When powered from USB-C**, the device starts in **Volume (ROMEMUL) mode** so you can manage files from a computer.
- You copy ROM images and configuration files onto the volume.

### Common files you may see

Depending on firmware/features, you will typically find some of these files in the root of `ROMEMUL`:

- `INDEX.HTM` — opens the device documentation website.
- `INFO.TXT` — shows installed firmware version/date, board details, flash size, etc.
- `CONFIG.TXT` — advanced configuration (timing/speed tuning, and other firmware options).
- `DEFAULT.TXT` — name of the default active ROM image (when supported).
- `RESCUE.TXT` — name of the rescue ROM image (when supported).
- Tool folders (product-specific), for example:
  - `AMIGA/` (Kickstart: SWITCHER app)
  - `SWITCHER.TOS` (TOS: Atari-side switching tool)

You may also see hidden metadata files created by your operating system (names starting with `.`). These are not used by the ROM Emulator.

## Safe eject (important)

As a rule of thumb, **ALWAYS** eject/unmount the `ROMEMUL` volume after making changes.
This ensures the FAT metadata is flushed correctly and the emulator re-indexes images/config reliably.

## FAT12 notes

- The ROMEMUL volume uses **FAT12** and typically a **4 KB cluster size**.
- File sizes may appear rounded up (4 KB steps). This is expected.

### Copying files (macOS / Windows / Linux)

- You can drag & drop files in most cases.
- On macOS, Finder may create temporary hidden files; if you run into issues, prefer copying from Terminal:

```bash
cp -R /path/to/ROM\ Images/* /Volumes/ROMEMUL/
```

On Linux, the mount point varies by distro:

```bash
cp -R /path/to/ROM\ Images/* /media/username/ROMEMUL/
```

## Magic file and folder names

Some SidecarTridge ROM-emulation firmwares support **"magic" file/folder names** that trigger actions when the `ROMEMUL` volume is ejected.

Common examples:

- `REBOOT` — after eject, the device attempts to mount the volume again.
- `RESET` — after eject, the device enters BOOTSEL mode and exposes a `RPI-RP2` or `RP2350` volume so you can flash firmware.

{: .note }
Magic files/folders are typically deleted after the action is triggered.

## Firmware updates

The ROM Emulator ships with firmware installed, but you may want to update it.

- The installed firmware version can be checked in `INFO.TXT`.
- Firmware update procedures are product/board specific.
- If your firmware supports the `RESET` magic name, it can be used to enter BOOTSEL mode.

{: .warning }
Some firmware updates (especially major upgrades) may erase stored images. Back up your `ROMEMUL` contents before updating.

[Previous: Hardware Integration](/sidecartridge-rom/hardware-integration/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Firmware API](/sidecartridge-rom/firmware-api/){: .btn }
