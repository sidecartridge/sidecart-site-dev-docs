---
layout: default
title: Compatibility Issues
nav_order: 8
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /compatibility_v2
  - /compatibility_v2/
---

# Compatibility Issues with Firmware v2

## Warning to all users
SidecarTridge Multi-device has undergone extensive testing on various Atari ST, STE, MegaST, and MegaSTE computers featuring diverse TOS versions. However, it's important to note that this version partially support Atari TT, Falcon computers, and their clones. While heavily modified and customized computers are likely compatible, it’s up to you to decide to use the Multi-device.

No Atari ST computers were harmed during the development of Multi-device. It’s a homebrew product designed for hobbyists with a keen interest in experimenting with their computers. **If you seek a seamless, Apple-like experience, Multi-device may not meet your expectations.**

I am more than willing to issue refunds to users who encounter compatibility issues, but I am also open to collaborating with them to resolve any problems and understand the underlying causes.

## Incompatibility issues and severity

| Severity | Device | Computer | Issue | Description | Fix |
|----------|--------|----------|-------|-------------|-----|
| MEDIUM | All | Atari TT and Falcon | Multi-drive not working | The Multi-device board may not be fully compatible with Atari TT and Falcon computers, leading to issues with multi-drive setups. | Not yet |
| LOW | All | All | microSD cards not detected | Only microSDHC, microSDXC and microSDUC supported. The device can read most of the existing microSD cards. Even the cheapest crap from AliExpress can work, but only microSDHC, microSDXC and microSDUC cards are supported. | Won't fix |
| LOW | All | All | 5Ghz WiFi not working | The Multi-device board supports only 2.4GHz WiFi networks. 5GHz networks are not supported. | Won't fix |

[Previous: Parameters](/sidecartridge-multidevice/parameters_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Troubleshooting](/sidecartridge-multidevice/troubleshooting_v2/){: .btn }
