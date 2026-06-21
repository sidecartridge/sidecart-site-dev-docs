---
layout: default
title: FAQ
nav_order: 9
nav_exclude: false
parent: SidecarTridge Keyboard
---

# FAQ
{: .no_toc }

This page is reserved for frequently asked questions about the SidecarTridge Keyboard Emulator.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Purpose

As the project documentation grows, this page collects the short answers that do not need a full chapter.

## Hardware compatibility

### Why is there no Croissant version for Atari ST computers with an external PSU ("short ST")?

The Croissant version of the SidecarTridge Keyboard Emulator is built for the 7-pin keyboard connector. The "short ST" motherboards (C070115 and C070243) use an 18-pin keyboard connector instead and are easy to recognise because they ship with an external power supply. Supporting them would require a different adapter design, which is not on the short-term roadmap. See [Troubleshooting → Why is there no Croissant version for Atari ST computers with an external PSU](/sidecartridge-keyboard/troubleshooting/#why-is-there-no-croissant-version-for-atari-st-computers-with-an-external-psu-short-st) for more detail.

### What is the difference between Croissant and Soufflè?

Croissant is the internal variant: it installs inside the Atari ST keyboard area, between the motherboard and the original keyboard, so the original case stays closed. Soufflè is the external dongle variant, designed for Atari Mega ST and Mega STE systems, and plugs into the coiled keyboard cable. Both variants share the same firmware base. See the [Introduction](/sidecartridge-keyboard/introduction/) for the full feature breakdown.

[Previous: Troubleshooting](/sidecartridge-keyboard/troubleshooting/){: .btn .mr-4 }
[Main](/sidecartridge-keyboard/){: .btn .mr-4 }
[Next: Changelog](/sidecartridge-keyboard/changelog/){: .btn }
