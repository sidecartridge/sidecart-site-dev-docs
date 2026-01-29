---
layout: default
title: Getting Started
nav_order: 2
nav_exclude: false
parent: SidecarTridge ROM
---

# Getting Started
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Quick summary

The SidecarTridge ROM Emulator is a **module** that must be **integrated into host hardware** (typically by soldering it onto a custom carrier board).

A first end-to-end workflow looks like this:

1. Verify hardware integration (carrier board + soldering + power).
2. Boot into **Volume (ROMEMUL) mode** from USB‑C and copy ROM images.
3. Select which image should be active (exact method depends on firmware).
4. Boot the target system in **Emulation mode**.

## Prerequisites

- ROM Emulator module integrated into your carrier board.
- A target system designed to accept the emulated ROM/EPROM/EEPROM device.
- USB‑C cable (to access `ROMEMUL`).

## Step 1 — Understand the two power/mode options

The ROM Emulator can be powered in two ways (and the power source determines the startup mode):

- **Carrier +5V** → starts in **EMULATION mode** (ready to run inside the target motherboard).
- **USB‑C +5V** → starts in **Volume (ROMEMUL) mode** (ready to manage files from a computer).

{: .note }
It is safe to power both at the same time. If USB‑C power is detected, **Volume (ROMEMUL) mode prevails**.

## Step 2 — Connect to your computer (Volume / ROMEMUL mode)

1. Connect the ROM Emulator to your computer using USB‑C.
2. The `ROMEMUL` volume should appear.

If `ROMEMUL` does not appear, check your cable and power, and see:
- [Troubleshooting](/sidecartridge-rom/troubleshooting/)

## Step 3 — Inspect ROMEMUL contents

Typical files you may see in the root of `ROMEMUL`:

- `INDEX.HTM` — opens documentation.
- `INFO.TXT` — firmware version/date and board info.
- `CONFIG.TXT` — advanced configuration.
- `DEFAULT.TXT` / `RESCUE.TXT` — default/rescue image selection (when supported).

## Step 4 — Copy ROM images

Copy your ROM images onto `ROMEMUL`.

{: .warning }
As a rule of thumb, **ALWAYS** eject/unmount `ROMEMUL` after making changes.

### macOS

Drag & drop works, but if you hit issues with hidden/temp files, use Terminal:

```bash
cp -R /path/to/ROM\ Images/* /Volumes/ROMEMUL/
```

### Windows

Drag & drop usually works.

### Linux

Mount point varies by distro:

```bash
cp -R /path/to/ROM\ Images/* /media/username/ROMEMUL/
```

## Step 5 — Select the active image

How you select the active ROM image depends on the firmware and the integration:

- **File-based selection** (when supported): edit `DEFAULT.TXT`.
- **Host-side tooling** (product specific): e.g. switcher applications.
- **Firmware API**: select the active image programmatically.

See:
- [Firmware API](/sidecartridge-rom/firmware-api/)

## Step 6 — Boot the target system (Emulation mode)

Power the ROM Emulator from the **carrier +5V** (or power the target motherboard normally, if that is how the carrier supplies +5V).
In EMULATION mode, the emulator starts immediately and should behave like the target ROM/EPROM/EEPROM device.

If the target does not boot, see:
- [Hardware Integration](/sidecartridge-rom/hardware-integration/)
- [Troubleshooting](/sidecartridge-rom/troubleshooting/)

## Next steps

- [Firmware & Files (ROMEMUL)](/sidecartridge-rom/firmware-and-files/)
- [Firmware API](/sidecartridge-rom/firmware-api/)
- [Hardware Integration](/sidecartridge-rom/hardware-integration/)

[Previous: Introduction](/sidecartridge-rom/introduction/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Hardware Integration](/sidecartridge-rom/hardware-integration/){: .btn }
