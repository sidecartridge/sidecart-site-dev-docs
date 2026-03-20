---
layout: default
title: Troubleshooting
nav_order: 8
nav_exclude: false
parent: SidecarTridge Keyboard
---

# Troubleshooting
{: .no_toc }

Use this chapter to collect the most common problems, diagnostic checks, and recovery steps for the SidecarTridge Keyboard Emulator.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Typical checks

When something does not work as expected, this page should help verify:

- power and connection state
- cable orientation
- firmware version, if applicable
- host compatibility limits
- recovery or reset procedures

## Croissant & Souffle

General troubleshooting topics shared by both hardware variants belong in this section.

### Where is the RESET button?

The RESET button was removed from the latest PCB revisions of both devices because it is rarely used once the board is installed in its enclosure. Power-cycle the computer instead.

## Croissant

### Why is there no Croissant version for Atari ST computers with an external PSU ("short ST")?

The Croissant version of the SidecarTridge Keyboard Emulator is designed for computers with the 7-pin keyboard connector. The well-known "short ST" motherboards C070115 and C070243 use an 18-pin keyboard connector instead and are easy to recognize because they use an external power supply. Supporting those machines would require a different adapter, which makes the design significantly more complex and expensive to develop and manufacture. It is probably possible to support them, but there are no plans to do so in the near future.

## Souffle

### The power LED is unstable in Configuration mode and the orange and green LEDs are dim

This usually means the computer power supply cannot handle Configuration mode with Wi-Fi and Bluetooth enabled at the same time.

Before replacing the power supply, try the following:

1. Remove USB devices from the hub. They also consume power and are not needed for configuration.
2. If it still fails, disconnect the device from the computer's coiled cable and power it from the Pico 2W micro USB port instead. This should always work.

Then configure the USB parameters or pair the Bluetooth devices. Do not forget to save the settings.

Finally, unplug the micro USB power cable if used, reconnect any USB devices, and plug the coiled cable back into the device.

Power on the computer again. The device should now work as expected.

[Previous: Compatibility](/sidecartridge-keyboard/compatibility/){: .btn .mr-4 }
[Main](/sidecartridge-keyboard/){: .btn .mr-4 }
[Next: FAQ](/sidecartridge-keyboard/faq/){: .btn }
