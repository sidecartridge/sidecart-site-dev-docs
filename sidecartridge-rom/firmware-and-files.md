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

_TODO: document exactly what files and folders are present, and what they do._

## Safe eject (important)

Always eject/unmount the ROMEMUL volume after copying files to ensure metadata is flushed correctly.

## FAT12 notes

_TODO: cluster size / size rounding, plus platform-specific notes (macOS hidden files, Windows, Linux)._

## Firmware updates

_TODO: where firmware lives, how to update, how to verify versions (INFO.TXT)._

[Previous: Hardware Integration](/sidecartridge-rom/hardware-integration/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Firmware API](/sidecartridge-rom/firmware-api/){: .btn }
