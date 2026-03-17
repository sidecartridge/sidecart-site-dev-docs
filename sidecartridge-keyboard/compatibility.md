---
layout: default
title: Compatibility
nav_order: 7
nav_exclude: false
parent: SidecarTridge Keyboard
---

# Compatibility
{: .no_toc }

Use this chapter to track input-device compatibility for the SidecarTridge Keyboard Emulator.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## USB compatibility

Applicable hardware:

* Soufflè only

USB compatibility is generally very broad. In practice, most standard USB keyboards, mice, and gamepads should work.

Instead of maintaining a list of all working USB devices, this section focuses on the cases that are more likely to create trouble.

### USB devices that can create trouble

These categories are more likely to cause problems:

* USB hubs
* keyboards with RGB lighting or other high power requirements
* gaming mice with many extra features
* unusual composite USB devices that do not behave like simple HID peripherals

### USB power-related caveats

Soufflè powers USB devices from its own USB port, so power draw matters.

Devices may fail to initialize correctly if:

* the Atari computer is powered off
* the computer power supply is weak or unstable
* the connected USB device requires more power than Soufflè can comfortably provide

For the best compatibility, prefer simple wired USB keyboards, basic mice, and standard gamepads.

## Bluetooth compatibility

Applicable hardware:

* Croissant
* Soufflè

Bluetooth compatibility in the SidecarTridge Keyboard Emulator follows the device support available in Bluepad32. The lists below are adapted from the official Bluepad32 compatibility pages for keyboards, mice, and gamepads.

### Bluetooth keyboards

Bluepad32 reports these tested keyboards and keyboard-like devices:

| Device name | Notes |
| --- | --- |
| 8BitDo Retro Mechanical Keyboard | Tested by Bluepad32 |
| Air Mouse with Touchpad Keyboard | Tested by Bluepad32 |
| Apple Magic Keyboard 2 model A1644 | Tested by Bluepad32 |
| Apple Magic Keyboard model A1314 | Tested by SidecarTridge. Needs to enter '0000' + ENTER for pairing. |
| Esynic Bluetooth Keyboard | Tested by SidecarTridge |
| Handlebar Media Controller | Tested by Bluepad32 |
| Microsoft Designer Bluetooth Keyboard | Tested by Bluepad32 |
| Tik Tok Remote Controller | Tested by Bluepad32 |

General compatibility notes for Bluetooth keyboards:

* BLE keyboards should generally work
* BR/EDR keyboards should generally work
* dual-mode keyboards might work, but can be less predictable

Keyboard support in Bluepad32 is still considered beta, so occasional issues should be expected even with otherwise supported devices.

### Bluetooth mice

Bluepad32 reports these tested mice and pointer devices:

| Device name | Notes |
| --- | --- |
| Adesso iMouse M300 | Noticeable lag when resuming from resting mode |
| Apple Magic Mouse A1296 (1st gen) | Tested by Bluepad32 |
| Apple Magic Mouse A1657 (2nd gen) | Tested by Bluepad32 |
| Apple Magic Trackpad A1339 (1st gen) | Right and middle click are not working |
| ASUS BX700 | Tested by SidecarTridge |
| Bornd C170B | Tested by Bluepad32 |
| BT5.4 Mouse | Tested by SidecarTridge. Generic low cost mouse with Bluetooth 5.4 support but lacking DIS. |
| HP Z5000 | Tested by Bluepad32 |
| HXSJ Bluetooth 3.0 Wireless Mouse | Known assert issue upstream |
| Kensington SureTrack K75351WW | Known assert issue upstream |
| LogiLink ID0078A | Tested by Bluepad32 |
| Logitech M336 / M337 / M535 | Tested by Bluepad32 |
| Logitech M-RCL124 (MX Revolution) | Tested by Bluepad32 |
| SteelSeries Rival 3 Wireless | Tested by Bluepad32 |
| Tank Mouse | Tested by Bluepad32 |
| TECKNET 2600DPI | Tested by Bluepad32 |
| TECKNET Three modes | Known assert issue upstream |

General compatibility notes for Bluetooth mice:

* BLE mice should generally work
* BR/EDR mice should generally work
* dual-mode mice might work, but can be less predictable
* Some low cost Bluetooth mice may lack the Device Information Service (DIS), which can cause compatibility issues. The Bluepad32 version used in the SidecarTridge Keyboard Emulator includes a workaround for this issue, but it may not be perfect.

Mouse support in Bluepad32 is also still considered beta.

### Bluetooth gamepads

Bluepad32 reports support for these gamepad families and tested controllers:

| Device name | Notes |
| --- | --- |
| 8BitDo family, including Ultimate, SN30 Pro, Pro 2, Lite, Lite 2, M30, Arcade Stick, Zero 2, and NES30 | Supported family in Bluepad32 |
| Amazon Fire TV Remote 1st gen | Tested by Bluepad32 |
| Android gamepads, including ASUS, Moga Pro 2, Amazon Fire TV gamepads, SteelSeries Status Duo, and DIY ESP32 gamepads | Supported family in Bluepad32 |
| AOLION Bluetooth Gamepad | Tested by SidecarTridge |
| Atari VCS Joystick | Tested by Bluepad32 |
| iCade 8-bitty | Tested by Bluepad32 |
| iCade Cabinet | Tested by Bluepad32 |
| Miscellaneous controllers such as DATA FROG P02, DATA FROG S80, Gamesir T3s, Gamesir Nova Lite, HS-SW510, and Terios T3 / ShanWan BM-769 | Mixed tested devices |
| Nintendo Switch JoyCon | Supported individually, not as one combined controller |
| Nintendo Switch Pro | Tested by Bluepad32 |
| Nintendo Wii Balance Board | Tested by Bluepad32 |
| Nintendo Wii Remote | Tested by Bluepad32 |
| Nintendo Wii Remote + Classic Controller / Classic Controller Pro | Tested by Bluepad32 |
| Nintendo Wii Remote + Nunchuk | Tested by Bluepad32 |
| Nintendo Wii U Pro Controller | Tested by Bluepad32 |
| OUYA 1st gen | Only 1st generation supported |
| Shanwan Q36 | Tested by SidecarTridge |
| Sony DualSense (PS5) | Tested by Bluepad32 |
| Sony DualShock 3 (PS3) | Requires manual pairing |
| Sony DualShock 4 (PS4) | Tested by Bluepad32 |
| Sony Motion Controller | Requires manual pairing |
| Stadia Controller | Requires Bluetooth firmware |
| Steam Controller | Requires Bluetooth firmware |
| SteelSeries Nimbus | Tested by Bluepad32 |
| Xbox Adaptive Controller | Tested by Bluepad32 |
| Xbox Wireless model 1708 | Support depends on firmware version for BR/EDR versus BLE |
| Xbox Wireless model 1914 | Support depends on firmware version for BR/EDR versus BLE |

### Bluetooth protocol notes

Most modern Bluetooth gamepads still use BR/EDR, while some use BLE.

For keyboards and mice, Bluepad32 reports this general behavior:

* BLE-only devices should generally work
* BR/EDR-only devices should generally work
* dual-mode devices might work, but are the least predictable category

If a Bluetooth device is not listed above, it may still work, but it should be treated as unconfirmed until tested.

[Previous: Firmware Update](/sidecartridge-keyboard/firmware-update/){: .btn .mr-4 }
[Main](/sidecartridge-keyboard/){: .btn .mr-4 }
[Next: Troubleshooting](/sidecartridge-keyboard/troubleshooting/){: .btn }
