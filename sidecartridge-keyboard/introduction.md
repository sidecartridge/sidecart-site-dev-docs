---
layout: default
title: Introduction
nav_order: 1
nav_exclude: false
parent: SidecarTridge Keyboard
---

# Introduction
{: .no_toc }

The **SidecarTridge Keyboard Emulator** is a hardware device that emulates the original Atari ST IKBD keyboard controller, allowing modern input devices to be used with Atari ST-family computers while maintaining full compatibility with software that expects standard IKBD behavior.

Unlike simple keyboard adapters that translate key presses, the SidecarTridge Keyboard Emulator reproduces the behavior of the HD6301-based IKBD microcontroller used in the Atari ST, STe, Mega ST, Mega STe, and TT.  
Because the host computer communicates with a real controller implementation, the system behaves as if an original Atari keyboard were connected.

This section introduces the project and explains how the emulator fits into Atari keyboard and input device setups.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## Project overview

The SidecarTridge Keyboard Emulator is designed for Atari computers that use the IKBD keyboard controller architecture, including:

- Atari ST  
- Atari STe  
- Atari Mega ST  
- Atari Mega STe  
- compatible systems using the same IKBD protocol

By emulating the original keyboard microcontroller instead of only translating keystrokes, the device allows modern input methods while preserving compatibility with software that expects the original IKBD behavior.

The SidecarTridge Keyboard Emulator currently exists in two hardware variants.


### SidecarTridge Croissant

SidecarTridge Croissant is an internal adapter for Atari ST and Atari STe computers that use the 7-pin internal keyboard connector.

It works as a middle-man between the motherboard and the keyboard and allows different operating modes, including:

- Bluetooth keyboard, mouse, and gamepad support
- pass-through mode using the original keyboard and mouse

The operating mode can be changed at boot time without opening the computer enclosure.


### SidecarTridge Soufflè

SidecarTridge Soufflè is an external keyboard replacement for Atari Mega ST and Mega STe systems.

It connects to the computer in place of the original keyboard and provides:

- Bluetooth keyboard, mouse, and gamepad support
- USB keyboard, mouse, and gamepad support through an integrated USB hub
- support for original Atari joysticks and mouse together with modern keyboards

Soufflè is intended both as a modernization upgrade and as a replacement for missing or faulty original keyboards.


### Shared firmware

Both Croissant and Soufflè use the same firmware base.  
New firmware versions are expected to support both hardware platforms whenever possible.


## Typical use cases

Common reasons to use the SidecarTridge Keyboard Emulator include:

- using Bluetooth keyboards, mice, or controllers on Atari systems
- using USB keyboards and mice with classic Atari hardware
- preserving compatibility with software that expects standard IKBD behavior
- replacing missing or damaged original keyboards
- combining original Atari input devices with modern peripherals


## Features


### Features common to all models

- full IKBD controller emulation instead of simple key translation
- compatibility-oriented behavior for software that expects normal IKBD responses
- Bluetooth Classic and BLE support for keyboards, mice, and gamepads
- support for many low-cost Bluetooth devices commonly sold online
- USB keyboard and mouse support (Soufflè)
- multiple keyboard layouts
- programmable auto-fire / auto-shoot support
- adjustable mouse speed
- Wi-Fi access point and station modes
- web-based configuration interface
- firmware updates through USB connection
- shared firmware across Croissant and Soufflè hardware variants


### Croissant features

- internal middle-man design for Atari ST / STe
- pass-through mode for original keyboard and mouse
- Bluetooth and pass-through mode selectable at boot


### Soufflè features

- external keyboard replacement for Mega ST / Mega STe
- built-in USB hub for keyboards, mice, and gamepads
- support for original joysticks and mouse together with USB keyboard
- designed for systems without a working original keyboard


## Why full IKBD emulation matters

The Atari keyboard subsystem is not only a key matrix.

In Atari ST-family computers the keyboard contains a microcontroller that communicates with the computer over a serial link and manages:

- keyboard input
- mouse input
- joystick input
- system commands

Because of this design, a reliable replacement must behave like the original IKBD controller.

The SidecarTridge Keyboard Emulator reproduces the behavior of the original controller instead of using a simplified adapter, which improves compatibility with games, demos, and software that rely on normal IKBD operation.


## Documentation structure

Use the next chapters to move from planning to installation and operation:

- [Before You Buy](/sidecartridge-keyboard/before-buy/)
- [Getting Started](/sidecartridge-keyboard/getting-started/)
- [Hardware Installation](/sidecartridge-keyboard/hardware-installation/)
- [User Guide](/sidecartridge-keyboard/user-guide/)
- [Compatibility](/sidecartridge-keyboard/compatibility/)

[Main](/sidecartridge-keyboard/){: .btn .mr-4 }
[Next: Before You Buy](/sidecartridge-keyboard/before-buy/){: .btn }