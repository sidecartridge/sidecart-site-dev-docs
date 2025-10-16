---
layout: default
title: Compatibility Issues
nav_order: 8
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /compatibility_issues
  - /compatibility_issues/
---

# Compatibility Issues

## Warning to all users
SidecarTridge Multi-device has undergone extensive testing on various Atari ST, STE, MegaST, and MegaSTE computers featuring diverse TOS versions. However, it's important to note that this version does not support Atari TT, Falcon computers, and their clones. While heavily modified and customized computers are likely compatible, it’s up to you to decide to use the Multi-device.

No Atari ST computers were harmed during the development of Multi-device. It’s a homebrew product designed for hobbyists with a keen interest in experimenting with their computers. If you seek a seamless, Apple-like experience, Multi-device may not meet your expectations.

I am more than willing to issue refunds to users who encounter compatibility issues, but I am also open to collaborating with them to resolve any problems and understand the underlying causes.

## Incompatibility issues and severity

| Severity | Device | Computer | Issue | Description | Fix |
|----------|--------|----------|-------|-------------|-----|
| CRITICAL | CosmoseX | MegaSTE | Corrupt storage in CosmoseX | Combining Multi-device with CosmoseX corrupts the content of the storage devices connected. | Not yet (UPDATE 30-Oct-2023: The adjustments we made in v0.0.10, specifically setting the parameter SAFE_CONFIG_REBOOT to TRUE, appear to have effectively prevented the issue from recurring.  |
| HIGH | >8Mhz CPU | All | Multi-device not detected | It seems that Multi-device cannot talk with computers with CPUs faster than 8Mhz. Future versions will eventually support higher CPU speed after appropiate testing period. | Change the CPU speed to 8Mhz without cache for compatibility. Note: starting in beta-v0.0.14 Multi-device supports MegaSTE in 16Mhz and cache enabled.|
| LOW | Very low quality microSD cards | All | microSD cards not detected | Some very low cost Aliexpress microSD cards (less than €1) can't be detected. Please don't use ultra low cost microSD cards. I bought a good bunch of them from AliExpress and all worked except one. But please don't play the roulette with yout data | Won't fix |
