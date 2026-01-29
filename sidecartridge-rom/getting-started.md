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

This guide walks you through a first successful end-to-end workflow:

1. Verify hardware integration (carrier board + soldering + power).
2. Mount the ROMEMUL USB mass-storage volume.
3. Copy a ROM image.
4. Select the active image.
5. Validate on target hardware.

## Prerequisites

- ROM Emulator module integrated into your carrier board (soldered, inspected).
- A target system designed to accept the emulated ROM device.
- A USB-C cable (for ROMEMUL access).

## Step 1 — Power + enumerate

_TODO: document expected LEDs, USB enumeration behavior, and what “normal” looks like._

## Step 2 — Open ROMEMUL volume

_TODO: describe volume contents (INFO.TXT, CONFIG.TXT, folders) and safe eject requirements._

## Step 3 — Copy a ROM image

_TODO: document supported ROM image sizes/widths and recommended naming conventions._

## Step 4 — Select the active image

_TODO: describe how selection works (via API, triggers, or configuration files)._

## Step 5 — Validate on target

_TODO: what signals/boot success look like, and what to check if it fails._

## Next steps

- [Firmware & Files (ROMEMUL)](/sidecartridge-rom/firmware-and-files/)
- [Firmware API](/sidecartridge-rom/firmware-api/)
- [Troubleshooting](/sidecartridge-rom/troubleshooting/)

[Previous: Introduction](/sidecartridge-rom/introduction/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Hardware Integration](/sidecartridge-rom/hardware-integration/){: .btn }
