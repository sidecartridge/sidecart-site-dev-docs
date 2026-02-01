---
layout: default
title: Firmware API
nav_order: 6
nav_exclude: false
parent: SidecarTridge ROM
---

# Firmware API
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Overview

This section documents the API used by host software to control the ROM Emulator:

- Query device info (firmware version, capabilities)
- List images
- Upload/install images
- Select the active image
- Configure timing/switching behavior

_TODO: fill in transport details (how commands are sent/received) and provide canonical examples._

## Concepts

- Images, slots, and the "active" image
- Persistence rules

## Endpoints / commands

_TODO: list actual commands and parameters once we confirm the implementation._

## Error handling

_TODO: return codes, typical failure modes._

[Previous: Firmware & Files](/sidecartridge-rom/firmware-and-files/){: .btn .mr-4 }
[Main](/sidecartridge-rom/){: .btn .mr-4 }
[Next: Compatibility](/sidecartridge-rom/compatibility/){: .btn }
