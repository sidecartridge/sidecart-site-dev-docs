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
| A500 rev3            | Single 512KB Kickstart socket | A500 rev3 kit | Supported |
| A500 rev5            | Single 512KB Kickstart socket | A500 rev5 kit | Supported |
| A500 rev6a           | Single 512KB Kickstart socket | A500 rev6a kit | Supported |
| A2000 (Kickstart socket) | Single 512KB Kickstart socket | A500-family carrier board | Supported |

{: .warning}
If your motherboard revision is not listed, or if you are unsure whether the ROM is socketed, please contact us before purchasing or installing the emulator.

## Kickstart and custom ROM compatibility

The SidecarTridge Kickstart emulator targets the classic Amiga 512KB Kickstart ROM series and also runs custom ROMs such as DiagROM or EmuTOS. If you use Cloanto/Amiga Forever images, convert them with the [Kickstart ROM conversion guide](/sidecartridge-kickstart/kickstart-conversion/).

| ROM image | Size (KB) | Tested | Works | Notes |
|-----------|-----------|--------|-------|-------|
| Kickstart 0.7 | 256 | Yes | No | Fails to boot properly on the emulator |
| Kickstart 1.0 | 256 | Yes | No | Fails to boot properly on the emulator |
| Kickstart 1.1 | 256 | Yes | Yes | OK |
| Kickstart 1.2 (33.180) | 256 | Yes | Yes | OK |
| Kickstart 1.3 (34.5) | 256 | Yes | Yes | OK |
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
