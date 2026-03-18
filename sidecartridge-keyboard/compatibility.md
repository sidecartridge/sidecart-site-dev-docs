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

Status legend:

* <span class="label label-green">OK</span> works
* <span class="label label-yellow">OK WITH CAVEATS</span> works, but requires some extra action by the user
* <span class="label label-red">KO</span> does not work

### Bluetooth keyboards

Bluepad32 reports these tested keyboards and keyboard-like devices:

| Device name | Status | Notes |
| --- | --- | --- |
| 8BitDo Retro Mechanical Keyboard | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Air Mouse with Touchpad Keyboard | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Apple Magic Keyboard 2 model A1644 | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Apple Magic Keyboard model A1314 | <span class="label label-yellow">OK WITH CAVEATS</span> | Tested by SidecarTridge. Needs to enter '0000' + ENTER for pairing. |
| Esynic Bluetooth Keyboard | <span class="label label-green">OK</span> | Tested by SidecarTridge |
| Handlebar Media Controller | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Microsoft Designer Bluetooth Keyboard | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Tik Tok Remote Controller | <span class="label label-green">OK</span> | Tested by Bluepad32 |

General compatibility notes for Bluetooth keyboards:

* BLE keyboards should generally work
* BR/EDR keyboards should generally work
* dual-mode keyboards might work, but can be less predictable

Keyboard support in Bluepad32 is still considered beta, so occasional issues should be expected even with otherwise supported devices.

### Bluetooth mice

Bluepad32 reports these tested mice and pointer devices:

| Device name | Status | Notes |
| --- | --- | --- |
| Adesso iMouse M300 | <span class="label label-green">OK</span> | Noticeable lag when resuming from resting mode |
| Apple Magic Mouse A1296 (1st gen) | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Apple Magic Mouse A1657 (2nd gen) | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Apple Magic Trackpad A1339 (1st gen) | <span class="label label-green">OK</span> | Right and middle click are not working |
| ASUS BX700 | <span class="label label-green">OK</span> | Tested by SidecarTridge |
| Bornd C170B | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| BT5.4 Mouse | <span class="label label-green">OK</span> | Tested by SidecarTridge. Generic low cost mouse with Bluetooth 5.4 support but lacking DIS. |
| HP Z5000 | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| HXSJ Bluetooth 3.0 Wireless Mouse | <span class="label label-green">OK</span> | Known assert issue upstream |
| Kensington SureTrack K75351WW | <span class="label label-green">OK</span> | Known assert issue upstream |
| LogiLink ID0078A | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Logitech M336 / M337 / M535 | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Logitech M-RCL124 (MX Revolution) | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| SteelSeries Rival 3 Wireless | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Tank Mouse | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| TECKNET 2600DPI | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| TECKNET Three modes | <span class="label label-green">OK</span> | Known assert issue upstream |

General compatibility notes for Bluetooth mice:

* BLE mice should generally work
* BR/EDR mice should generally work
* dual-mode mice might work, but can be less predictable
* Some low cost Bluetooth mice may lack the Device Information Service (DIS), which can cause compatibility issues. The Bluepad32 version used in the SidecarTridge Keyboard Emulator includes a workaround for this issue, but it may not be perfect.

Mouse support in Bluepad32 is also still considered beta.

### Bluetooth gamepads

Bluepad32 reports support for these gamepad families and tested controllers:

| Device name | Status | Notes |
| --- | --- | --- |
| 8BitDo family, including Ultimate, SN30 Pro, Pro 2, Lite, Lite 2, M30, Arcade Stick, Zero 2, and NES30 | <span class="label label-green">OK</span> | Supported family in Bluepad32 |
| Amazon Fire TV Remote 1st gen | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Android gamepads, including ASUS, Moga Pro 2, Amazon Fire TV gamepads, SteelSeries Status Duo, and DIY ESP32 gamepads | <span class="label label-green">OK</span> | Supported family in Bluepad32 |
| AOLION Bluetooth Gamepad | <span class="label label-green">OK</span> | Tested by SidecarTridge |
| Atari VCS Joystick | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| iCade 8-bitty | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| iCade Cabinet | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Miscellaneous controllers such as DATA FROG P02, DATA FROG S80, Gamesir T3s, Gamesir Nova Lite, HS-SW510, and Terios T3 / ShanWan BM-769 | <span class="label label-green">OK</span> | Mixed tested devices |
| Nintendo Switch JoyCon | <span class="label label-green">OK</span> | Supported individually, not as one combined controller |
| Nintendo Switch Pro | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Nintendo Wii Balance Board | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Nintendo Wii Remote | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Nintendo Wii Remote + Classic Controller / Classic Controller Pro | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Nintendo Wii Remote + Nunchuk | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Nintendo Wii U Pro Controller | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| OUYA 1st gen | <span class="label label-green">OK</span> | Only 1st generation supported |
| Shanwan Q36 | <span class="label label-green">OK</span> | Tested by SidecarTridge |
| Sony DualSense (PS5) | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Sony DualShock 3 (PS3) | <span class="label label-green">OK</span> | Requires manual pairing |
| Sony DualShock 4 (PS4) | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Sony Motion Controller | <span class="label label-green">OK</span> | Requires manual pairing |
| Stadia Controller | <span class="label label-green">OK</span> | Requires Bluetooth firmware |
| Steam Controller | <span class="label label-green">OK</span> | Requires Bluetooth firmware |
| SteelSeries Nimbus | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Xbox Adaptive Controller | <span class="label label-green">OK</span> | Tested by Bluepad32 |
| Xbox Wireless model 1708 | <span class="label label-green">OK</span> | Support depends on firmware version for BR/EDR versus BLE |
| Xbox Wireless model 1914 | <span class="label label-green">OK</span> | Support depends on firmware version for BR/EDR versus BLE |

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
