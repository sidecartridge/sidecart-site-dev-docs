---
layout: default
title: USB devices on Croissant (experimental)
nav_order: 12
nav_exclude: false
parent: SidecarTridge Keyboard
---

# USB devices on Croissant (experimental)
{: .no_toc }

This page documents an unsupported way to add USB keyboard input (and optionally a USB mouse or gamepad) to a Croissant install on an Atari ST or STE that uses the 7-pin internal keyboard connector. It is aimed at owners who are happy to keep the computer case open (or to cut a slot for a small hub) and who accept that we will not provide support for this configuration.

{: .warning }
This is an experimental setup. It is not validated in production, no specific USB device is guaranteed to work, and we cannot offer support for problems caused by it. Use at your own risk.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Who this is for

Owners of an Atari **ST** or **STE** with the **7-pin internal keyboard connector** (the Croissant target) who want USB input on their machine and are happy with the trade-offs listed under [Limitations](#limitations) below.

If your machine is a **Mega ST** or **Mega STe**, you do not need this workaround. The dedicated product for those is **Soufflè**, which ships with a built-in USB hub. See the [Introduction](introduction.md) for the variant breakdown.

## How it works

Croissant and Soufflè share the same firmware base and the same Raspberry Pi Pico 2W microcontroller. What differs is the carrier board around the Pico:

- **Soufflè** routes a built-in USB hub to the Pico's USB host port. Plugging USB devices is plug-and-play.
- **Croissant** has no built-in hub. The Pico's USB port is exposed as the micro-USB port normally used for power and flashing.

The workaround leverages that shared base. By flashing the **Soufflè firmware** onto a Croissant board, its micro-USB port behaves as a USB host. Hanging a small USB hub off that port then gives you somewhere to plug USB input devices.

## What you need

- A working Croissant install on your ST or STE. The Bluetooth path should already pair successfully before you try this workaround.
- A **4-port micro-USB OTG hub**. The reference part we have tested costs around €3 on AliExpress: [example listing](https://a.aliexpress.com/_Eu4fzSA).
- The USB input devices you want to use. A USB keyboard is the typical case; a USB mouse or gamepad can be added on the same hub.
- The standard [firmware flashing flow](firmware-update.md) ready on a host computer.

## Steps

1. **Flash the Soufflè firmware onto your Croissant.** Use the regular [firmware update flow](firmware-update.md), but pick the **Soufflè** firmware image instead of the Croissant one. The same flasher works for both.
2. **Power off your Atari** and open the case far enough to access the Croissant board.
3. **Plug the OTG hub into the Croissant's Pico 2W micro-USB port.** The hub will hang loose unless you secure it. Double-sided tape or a 3D-printed clip both work; a slot cut in the case is the cleanest end state if you do not mind the modification.
4. **Connect your USB devices to the hub.** A USB keyboard is the typical setup. A USB mouse or gamepad can be added on the same hub.
5. **Power the Atari back on.** Devices are scanned at boot, exactly as on a standard Soufflè install.

## Limitations

- **The case stays open or modified.** The hub dangles off the Pico's micro-USB connector. There is no enclosure plan for this configuration. Either leave the cover off or cut a slot for the hub.
- **No guaranteed power budget.** Every USB device on the hub draws power from the Atari 5V rail through the Pico. Avoid power-hungry devices like RGB-lit gaming keyboards or USB-powered storage.
- **Some hubs will not enumerate.** If yours does not, try another passive 4-port micro-USB OTG hub. Active or self-powered hubs are not required and may not behave consistently.
- **Mechanical fragility.** The Pico's micro-USB connector was not designed to carry a hanging hub long-term. Avoid pulling on the hub once it is in place.
- **Device compatibility is not exhaustive.** The same caveats that apply to Soufflè around USB device behaviour and power draw apply here.

## Reverting to Bluetooth

If you decide to go back to the supported Bluetooth path, re-flash the **Croissant** firmware over the Soufflè firmware using the same [firmware update flow](firmware-update.md). The Croissant hardware itself is not modified by the workaround, so the rollback is just a firmware re-flash.

## What we will not help with

This configuration is on the user. We will not provide support for:

- USB devices that fail to enumerate on the hub.
- Power instability with several USB devices plugged in at once.
- Mechanical problems caused by the hub hanging off the Pico.
- Keyboard mapping or device quirks that are not present on the supported Croissant Bluetooth path.

If you hit any of those, please re-flash the Croissant firmware first and confirm the supported Bluetooth path works. Then raise a support ticket from a known-good baseline so we can reproduce the issue.
