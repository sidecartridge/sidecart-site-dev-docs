---
layout: default
title: Compatibility
nav_order: 7
nav_exclude: false
parent: SidecarTridge Kickstart

---

# Compatibility
{: .no_toc }

Use this section to confirm that your Amiga model, motherboard revision, and Kickstart images will work with the SidecarTridge Kickstart emulator. Start by checking your motherboard revision inside the case and matching it with the tables below. If you have any doubts, please reach out before powering on the board.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Supported Amiga motherboards and carrier boards

{: .info}
Carrier boards for additional Amiga models are in active development. Check the SidecarTridge website for the latest updates.
{: .warning}

### Amiga 500 family

- Make sure your Kickstart ROM is socketed; if it is soldered you must add a socket before using the emulator (see [Before You Buy](/sidecartridge-kickstart/before-buy/)).
- All rows below refer to Classic Amiga 512KB ROM layouts used by the A500 family.

| Motherboard revision | ROM socket layout | Carrier board / kit | Status |
|----------------------|-------------------|---------------------|--------|
| A500 rev3            | Single 512KB Kickstart socket | A500 carrier rev5 and earlier | Supported |
| A500 rev5            | Single 512KB Kickstart socket | A500 carrier rev5 and earlier | Supported |
| A500 rev6a           | Single 512KB Kickstart socket | A500 carrier rev6 and later | Supported |

### Amiga 2000 family

- Make sure your Kickstart ROM is socketed; if it is soldered you must add a socket before using the emulator (see [Before You Buy](/sidecartridge-kickstart/before-buy/)).
- All rows below refer to Classic Amiga 512KB Kickstart sockets used by the A2000 family.

| Motherboard revision | ROM socket layout | Carrier board / kit | Status |
|----------------------|-------------------|---------------------|--------|
| A2000 rev4.2 and earlier | Single 512KB Kickstart socket | A2000 carrier rev4.2 and earlier | Supported |
| A2000 rev4.3 and later   | Single 512KB Kickstart socket | A2000 carrier rev4.3 and later | Supported |

{: .warning}
If your motherboard revision is not listed, or if you are unsure whether the ROM is socketed, please contact us before purchasing or installing the emulator.

## Kickstart and custom ROM compatibility

The SidecarTridge Kickstart emulator targets the classic Amiga 512KB Kickstart ROM socket and also runs custom ROMs such as DiagROM or EmuTOS. If you use Cloanto/Amiga Forever images, convert them with the [Kickstart ROM conversion guide](/sidecartridge-kickstart/kickstart-conversion/).

### ROM image size requirements

The emulator presents a single 512KB ROM image to the Amiga. Every file copied to `ROMEMUL` and selected via `DEFAULT.TXT`/`RESCUE.TXT` (or SWITCHER) must therefore be **exactly 524288 bytes (512KB)**.

Original Kickstart 1.x and early 2.x images are 256KB on real hardware because the original Amiga motherboards mirror those 256KB into the 512KB address space natively. The SidecarTridge Kickstart emulator does not perform that mirror in firmware, so 256KB Kickstart images must be doubled (mirrored to 512KB) in software before they can be used. This is by design and will not change in future firmware releases.

There are two ways to obtain a 512KB image from a 256KB Kickstart source:

- **Encrypted Amiga Forever image (AMIROMTYPE1)**: use the [web converter](/sidecartridge-kickstart/kickstart-conversion/). When the decoded payload is 256KB or smaller, the converter automatically pads it to 256KB and duplicates the block, returning a ready-to-use 512KB file.
- **Already-decoded plain 256KB ROM dump**: the converter does not accept this kind of file. Duplicate the ROM manually before copying it to `ROMEMUL`. See [Already-decoded Kickstart ROMs](/sidecartridge-kickstart/kickstart-conversion/#already-decoded-kickstart-roms) for the exact `cat` and PowerShell snippets.

Files that are not exactly 512KB on `ROMEMUL` will either be ignored by the device or boot to a hang/black screen on the Amiga, depending on the actual size. If you see that behaviour, check the byte count of the file first.

### Tested ROM images

| ROM image | Native size (KB) | Tested | Works | Notes |
|-----------|------------------|--------|-------|-------|
| Kickstart 0.7 | 256 | Yes | No | Fails to boot properly on the emulator |
| Kickstart 1.0 | 256 | Yes | No | Fails to boot properly on the emulator |
| Kickstart 1.1 | 256 | Yes | Yes | Must be mirrored to 512KB before use |
| Kickstart 1.2 (33.180) | 256 | Yes | Yes | Must be mirrored to 512KB before use |
| Kickstart 1.3 (34.5) | 256 | Yes | Yes | Must be mirrored to 512KB before use |
| Kickstart 2.04 (37.175) | 512 | Yes | Yes | OK |
| Kickstart 2.05 | 512 | Yes | Yes | OK |
| Kickstart 3.0 | 512 | Yes | Yes | OK |
| Kickstart 3.1 (40.63) | 512 | Yes | Yes | OK |
| DiagROM 1.x | 512 | Yes | Yes | OK |
| DiagROM 2.x beta | 512 | Yes | Yes | OK |
| Logica Diagnostics 2.0 | 512 | Yes | Yes | OK |
| EmuTOS 68K 1.x | 512 | Yes | Yes | OK |

{: .info}
There are other custom ROMs available. The table above lists the most common ones that have been tested. If you find any other versions that work or do not work, please let us know so we can update the compatibility list. Or update it yourself by submitting a pull request on the link at the bottom of the documentation pages.


{: .warning}
If you plan to use a ROM image that is not listed, ensure it is built for the 68000-based Amiga 512KB layout and test it with the [rescue mode setup](/sidecartridge-kickstart/getting-started/#setting-the-default-and-rescue-rom-images) so you can recover easily.

[Previous: Advanced Settings](/sidecartridge-kickstart/advanced-settings/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Kickstart ROM Conversion](/sidecartridge-kickstart/kickstart-conversion/){: .btn }
