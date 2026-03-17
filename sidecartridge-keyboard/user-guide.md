---
layout: default
title: User Guide
nav_order: 5
nav_exclude: false
parent: SidecarTridge Keyboard
---

# User Guide
{: .no_toc }

This chapter is reserved for the normal day-to-day use of the SidecarTridge Keyboard Emulator.

Use this page after the hardware is installed and the initial setup has been completed.

The guide is organized by operating mode and feature area so new procedures can be added later without restructuring the page.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 1. Startup behavior and mode selection

This section explains what happens when the Atari computer is powered on and how the SidecarTridge Keyboard Emulator chooses its operating mode.

### 1.1 Power-on behavior

When the Atari computer is powered on, the SidecarTridge Keyboard Emulator is powered on as well.

The device does not need to be powered separately during normal operation.

### 1.2 First boot behavior

On first boot, the device always starts in configuration mode.

The expected LED pattern is:

* Green LED: blinking
* Orange LED: steady on

This pattern means:

* firmware is running
* device is in configuration mode
* WiFi station is active

From this initial configuration mode, the user can access the web interface and choose the first normal operating mode for the device.

### 1.3 Startup mode after initial configuration

After the first normal operating mode is selected, the device will start in that selected mode every time the computer is powered on.

Depending on the hardware model, the available startup modes are:

* Pass-through mode
* Bluetooth mode
* USB mode (Soufflè only)

The startup mode remains stored until the user changes it.

### 1.4 Entering configuration mode manually

To change the startup operating mode later, the user can return to configuration mode.

Croissant and Soufflè both provide a `CONFIG` button.

Pressing the `CONFIG` button forces the device to enter configuration mode immediately.

Configuration mode exposes the web pages described in this document.

### 1.5 Reset code using the Atari reset button

Applicable hardware:

* Croissant only

Croissant also supports changing the operating mode by using the reset button of the Atari ST during power-on.

Depending on how long the computer reset button is held while powering on the system, the device can switch to a different operating mode.

This reset code allows the user to close the computer enclosure and still change operational features without pressing any button on the board itself.

See the operating mode sections below for the reset code behavior associated with each feature.

## 2. Pass-through mode

Applicable hardware:

* Croissant only

This section covers the operating mode where the internal keyboard path is preserved and the device works inline with the original system hardware.


![SidecarTridge Keyboard Emulator Croissant pass-through mode](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-PASS-THROUGH.png)

### 2.1 Overview

The pass-through mode allows the SidecarTridge Keyboard Emulator to be used without disabling the original Atari keyboard functionality, plus any attached mouse or joystick. In this mode, the HD6301-based IKBD microcontroller used in the 16-bit Atari ST-family computers is not emulated at all, and the original keyboard path is preserved. The device simply passes through the original keyboard, mouse, and joystick signals.

This mode is ideal for users who want to add modern input devices while keeping the original keyboard, joysticks, and mouse fully functional and compatible with software that expects the original hardware behavior.

### 2.2 Enabling or selecting pass-through mode

To enable the pass-through mode, the user can either select it from the web interface or use the reset code on Croissant.

#### Select pass-through mode using the web interface

The pass-through mode can be selected from the configuration page shown below:

![SidecarTridge Keyboard Emulator Croissant pass-through configuration page](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-PASS-THROUGH-CONFIGURATION.png)

1. Choose the pass-through mode option
2. Toggle the `Activate pass-through mode` button in the web interface.
3. Save the configuration settings.

After that, every time the computer is powered on the device will start in Bluetooth mode.

#### Select pass-through mode using the reset code

Sometimes the user may want to enable pass-through mode even though the default active mode is Bluetooth mode. Instead of entering configuration mode, Croissant provides a timing-based reset feature that bypasses the default Bluetooth mode and starts in pass-through mode.

To enable the pass-through mode with the reset code:

1. With the computer powered off, keep the Atari computer reset button pushed and power on the computer.
2. Wait between 5 and 9 seconds.
3. Release the reset button. The computer will then boot normally with pass-through mode enabled.

Note: if the reset button is kept pressed for more than 10 seconds and less than 20 seconds, the device will start in configuration mode.

Warning: the reset code only affects that boot cycle. To permanently change the operating mode of the Croissant device, enter configuration mode and store the new setting there.


### 2.3 Expected behavior in pass-through mode

When pass-through mode is active, the orange LED is steady on and the green LED is off.

The keyboard, joystick, and mouse behave as if the device were not connected.

### 2.4 Limitations or mode-specific notes

There are no known restrictions in pass-through mode.

## 3. Bluetooth mode

Applicable hardware:

* Croissant
* Soufflè

This section covers Bluetooth operation for keyboards, mice, and other supported wireless input devices.

Example select Bluetooth mode page on Croissant (same on Soufflè):

![SidecarTridge Keyboard Emulator Croissant Bluetooth mode](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-BLUETOOTH.png)

### 3.1 Overview

The Bluetooth mode allows the SidecarTridge Keyboard Emulator to connect to modern wireless input devices, such as keyboards, mice and gamepads supported Bluetooth peripherals. In this mode, the device emulates the original Atari keyboard, mouse or joystick functionality while adding support for Bluetooth input.

This mode is ideal for users who want to use modern wireless input devices with their Atari computer, providing flexibility and convenience without sacrificing compatibility with software that expects the original hardware behavior.

The Bluetooth mode supports Classic and BLE Bluetooth devices. There is not an exact list of supported devices, but the current implementation uses a superset of the devices supported by the [Bluepad32 library](https://bluepad32.readthedocs.io/en/latest/), which includes a wide range of popular Bluetooth keyboards, mice, and gamepads. We will keep updating the supported device list as we test more peripherals, but users can also try pairing their own Bluetooth devices to see if they are compatible with the emulator.

The Bluetooth chip in the Raspberry Pi Pico 2W  and the Pico-SDK BTstack supports a wide range of features, but don't expect support for every Bluetooth device on the market, or for the features you can find in a full-fledged Operating System Bluetooth stack. If you are expecting an iPhone-like experience, go and buy an iPhone; this is not for you.

Also the Croissant device runs between the motherboard and the original keyboard, so the Bluetooth range is not going to be the same as a Bluetooth adapter connected to your computer. Expect the range to be around 5-10 meters in an open space, and don't expect to be able to connect from another room or through  walls. The Bluetooth performance will depend on the environment and the specific devices you are trying to connect, so your mileage may vary. These limitations are not in the Souffle device, which has a more open design.

### 3.1 LED behavior in Bluetooth mode

When Bluetooth mode is active, the orange LED is off and the green LED is steady on.

### 3.2 Configure Bluetooth mode

To enable Bluetooth mode, open the Bluetooth configuration page in the web interface. The same configuration workflow is used on both Croissant and Soufflè.

![SidecarTridge Keyboard Emulator Bluetooth configuration page](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-BLUETOOTH-CONFIG.png)

The Bluetooth configuration page provides these controls:

* `Activate Bluetooth mode` enables Bluetooth input mode.
* `Current pairings` shows the pairing status for keyboard, mouse, and gamepad.
* `Open pairing page` opens the pairing workflow for new Bluetooth devices.
* `Keyboard layout` selects the keyboard layout used by Bluetooth keyboards.
* `Mouse speed` adjusts pointer sensitivity for Bluetooth mice.
* `Gamepad auto-shoot` sets the auto-shoot speed used by supported Bluetooth gamepads.

To configure Bluetooth mode:

1. Enable `Activate Bluetooth mode`.
2. Review the `Current pairings` status shown for keyboard, mouse, and gamepad. `Not paired` means no device is currently paired for that category, while `Paired` means a device is already paired and connected. The user must open the `Open pairing page` to modify the current pairing status.
3. Click `Open pairing page` if you want to add or replace a Bluetooth device.
4. Select the required `Keyboard layout`.
5. Adjust `Mouse speed` and `Gamepad auto-shoot` as needed.
6. Click `Save settings` to store the configuration.

If you made changes that you do not want to keep, click `Reset` before saving.

After that, every time the computer is powered on the device will start in Bluetooth mode.


### 3.3 Keyboard layout

The `Keyboard layout` setting allows the user to select the keyboard layout used by Bluetooth keyboards connected to the device. This setting is important for ensuring that the keys on the Bluetooth keyboard correspond correctly to the expected key codes sent to the Atari computer.

In the latest firmware version, the following keyboard layouts are supported:
- United States ANSI
- France ISO (FR)
- Germany ISO (DE)
- United Kingdom ISO (GB)
- Spain ISO (ES)
- Italy ISO (IT)

Expect more layouts to be added in the future, but if you need a specific layout that is not currently supported, please open an issue in the GitHub repository and we will prioritize it based on demand.

Note: the usual way to use this is the user has to match the TOS keyboard layout with the Bluetooth keyboard layout. For example, if the user has a TOS in French, they should select the France ISO (FR) layout for their Bluetooth keyboard. This ensures that the keys on the Bluetooth keyboard produce the correct characters and key codes when used with the Atari computer.

### 3.4 Mouse speed

The `Mouse speed` setting allows the user to adjust the pointer sensitivity for Bluetooth mice connected to the device. This setting controls how fast the mouse pointer moves on the screen in response to physical movement of the Bluetooth mouse.

`1` is the slowest speed, while `10` is the fastest. The default value is `5`, which provides a balanced sensitivity for most users. Adjusting this setting can help improve the user experience when using a Bluetooth mouse with the Atari computer, especially if the default sensitivity feels too slow or too fast.

### 3.5 Gamepad auto-shoot

The `Gamepad auto-shoot` setting allows the user to adjust the auto-shoot speed for supported Bluetooth gamepads connected to the device. This setting controls how quickly the gamepad will repeatedly send the shoot command when the shoot button is held down.

`0` means no auto-shoot, while `10` is the fastest auto-shoot speed. The default value is `0`, which means that auto-shoot is disabled by default. Adjusting this setting can help improve the gaming experience when using a Bluetooth gamepad with the Atari computer, especially for games that require rapid firing. The auto-shoot feature is triggered when the user holds down the shoot button on the gamepad for more than two seconds.

### 3.6 Saving Bluetooth configuration

After adjusting the Bluetooth settings, click the `Save settings` button to store the configuration. This will ensure that the selected Bluetooth mode and settings are applied every time the computer is powered on.

### 3.7 Pairing procedure

While the Bluetooth mode does not stricly needs to have pre-paired devices to work, it is strongly recommened to pair them in advance to ensure a smoother experience, as the pairing process can be a bit tricky and may require multiple attempts to get right.

It is very important to note that the Raspberry Pi Pico 2W uses the wireless chipset CYW43439 to serve a web page through 2.4Ghz WiFi and pairing Bluetooth devices at the same time. How can this happen?

![SidecarTridge Keyboard Emulator Bluetooth pairing animation](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-BLUETOOTH-PAIRING.gif)

The CYW43439 is a combo chip that supports both WiFi and Bluetooth, but it can only use one of the two wireless technologies at a time. So we do some magic. Sadly, the magic is not perfect and sometimes the Bluetooth pairing process can be a bit unstable. But keep in mind that once the devices are paired, only the Bluetooth connection is used at runtime.

When pressing the `Open pairing page` button, the device will show a new page with instructions to complete the pairing process. 

Example of the Bluetooth pairing page before pairing has started:

![SidecarTridge Keyboard Emulator Bluetooth pairing page before scan start](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-BLUETOOTH-PAIRING-PAGE.png)

To complete the pairing process:

1. Click `Start pairing` to begin scanning for nearby Bluetooth devices.

![SidecarTridge Keyboard Emulator Bluetooth pairing scan running](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-BLUETOOTH-PAIRING-RUNNING.png)

2. When a compatible device appears in the lower device list, click that device to pair it.
3. If the pairing succeeds, the device is moved into the `Current pairings` section and an `Unpair` button becomes available for that category.

![SidecarTridge Keyboard Emulator Bluetooth pairing complete](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-BLUETOOTH-PAIRING-COMPLETE.png)

4. Once you are done, click `Stop pairing` to stop the scan.
5. Return to the Bluetooth configuration page by clicking `Bluetooth` in the navigation bar.
6. Verify that the paired devices are listed and click `Save settings` so they are stored for the next power-on.

![SidecarTridge Keyboard Emulator Bluetooth configuration with paired devices](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-BLUETOOTH-CONFIG-PAIRED-DEVICES.png)


### 3.8 Powering on with paired Bluetooth devices

When powering on the computer with Bluetooth mode active and paired devices, the device will attempt to connect to the paired Bluetooth devices when they are in range and in use. The expected behavior is:

1. Power on the computer. The device starts in Bluetooth mode.
2. The device listens for any paired Bluetooth devices that are trying to connect.
3. When a paired Bluetooth device tries to connect, the device will establish a connection.
4. The connected Bluetooth device can then be used as an input device for the Atari computer, emulating the original keyboard, mouse, or joystick functionality.

It can take a few seconds for the Bluetooth devices to connect after power-on, so be patient. If the devices do not connect, make sure they are powered on, in range, and that Bluetooth mode is active on the device.

### 3.9 Powering on without paired Bluetooth devices

If the computer is powered on with Bluetooth mode active but no paired Bluetooth devices, the device will simply wait for Bluetooth devices to connect. The expected behavior is:

1. Power on the computer. The device starts in Bluetooth mode.
2. The device listens for any Bluetooth devices that are trying to connect.
3. Since there are no paired devices, the device will not establish any connections and will remain idle until a Bluetooth device tries to connect.
4. If a Bluetooth device is powered on and tries to connect while the computer is running, the device will establish a connection and allow the Bluetooth device to be used as an input device for the Atari computer.

It can take longer for Bluetooth devices to connect after power-on if there are no paired devices, so be patient. If you want to use Bluetooth input devices, it is recommended to pair them in advance through the web interface.

### 3.10 Keyboard behavior in Bluetooth mode

When Bluetooth mode is active and a Bluetooth keyboard is connected, the device emulates the original Atari keyboard functionality while allowing the use of the Bluetooth keyboard, but with a few differences to keep in mind. The main differences have to do with the use of a keyboard layout without a numerical and function keys. While it is possible to avoid the numerical keyboard, the combination of `ALTERNATE + INSERT` is a very important key combination that mimics the left button of the mouse. If the user is using a keyboard layout without a numerical keyboard, they can still access the `ALTERNATE + INSERT` combination by pressing `ALTERNATE + BACKSPACE` instead.

### 3.11 Mouse behavior in Bluetooth mode

When Bluetooth mode is active and a Bluetooth mouse is connected, the device emulates the original Atari mouse functionality while allowing the use of the Bluetooth mouse.

Some cheap and dirty mice has a stripped version of the bluetooth stack, making it incompatible with the device. If you are having trouble connecting a Bluetooth mouse, try using a different model or brand to see if it works better.

### 3.12 Gamepad behavior in Bluetooth mode

When Bluetooth mode is active and a supported Bluetooth gamepad is connected, the device emulates the original Atari joystick functionality while allowing the use of the Bluetooth gamepad. The gamepad is mapped to the joystick port as follows:

-  D-pad: mapped to the joystick directional inputs (up, down, left, right)
-  A, B, X, Y buttons: mapped to the joystick fire button


## 4. USB mode

Applicable hardware:

* Soufflè only

This section covers the use of USB input devices connected to the Soufflè hardware.

### 4.1 Overview

Example USB mode page on Soufflè:

![SidecarTridge Keyboard Emulator Soufflè USB mode](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-SOUFFLE-USB.png)

The USB mode allows the SidecarTridge Keyboard Emulator to use modern wired USB input devices, such as keyboards, mice, and joystick or gamepad devices connected to Soufflè.

In this mode, the device emulates the original Atari keyboard, mouse, or joystick functionality while taking input from supported USB peripherals.

This mode is ideal for users who want a simple wired setup without Bluetooth pairing, wireless range limits, or radio interference.

The current implementation is intended for standard USB input peripherals. Support will depend on the behavior of the USB device connected to Soufflè, so some devices may work better than others.

A very special feature of the USB mode is that it supports native Atari input devices like mouse and joysticks that use the original 9-pin connector, combined with modern USB input devices. This allows users to have the best of both worlds: the original hardware experience with the convenience of modern peripherals.

### 4.2 Configure USB mode

To enable USB mode, open the USB configuration page in the web interface on Soufflè.

![SidecarTridge Keyboard Emulator Soufflè USB configuration page](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-SOUFFLE-USB-CONFIG.png)

The USB configuration page provides these controls:

* `Activate USB mode` enables USB input mode.
* `Keyboard layout` selects the keyboard layout used by USB keyboards.
* `Use original mouse (Experimental)` keeps the original ST mouse active instead of using a USB mouse.
* `USB joystick/gamepad` enables USB joystick and gamepad input.
* `Preferred joystick port` selects which Atari ST joystick port the USB joystick maps to.
* `Gamepad auto-shoot` sets the auto-shoot speed used by supported USB gamepads.
* `Mouse speed` adjusts pointer sensitivity for USB mice.

To configure USB mode:

1. Enable `Activate USB mode`.
2. Select the required `Keyboard layout`.
3. Enable `Use original mouse (Experimental)` if you want to keep using the original ST mouse instead of a USB mouse.
4. Enable `USB joystick/gamepad` if you want to use a USB joystick or gamepad.
5. Select the `Preferred joystick port` for the USB joystick or gamepad.
6. Adjust `Gamepad auto-shoot` and `Mouse speed` as needed.
7. Click `Save settings` to store the configuration.

If you made changes that you do not want to keep, click `Reset` before saving.

After that, every time the computer is powered on the device will start in USB mode.

### 4.3 Keyboard layout

The `Keyboard layout` setting allows the user to select the keyboard layout used by USB keyboards connected to the device. This setting is important for ensuring that the keys on the USB keyboard correspond correctly to the expected key codes sent to the Atari computer.

In the latest firmware version, the following keyboard layouts are supported:
- United States ANSI
- France ISO (FR)
- Germany ISO (DE)
- United Kingdom ISO (GB)
- Spain ISO (ES)
- Italy ISO (IT)

Expect more layouts to be added in the future, but if you need a specific layout that is not currently supported, please open an issue in the GitHub repository and we will prioritize it based on demand.

Note: the usual way to use this is the user has to match the TOS keyboard layout with the USB keyboard layout. For example, if the user has a TOS in French, they should select the France ISO (FR) layout for their USB keyboard. This ensures that the keys on the USB keyboard produce the correct characters and key codes when used with the Atari computer.

### 4.4 Mouse speed

The `Mouse speed` setting allows the user to adjust the pointer sensitivity for native and USB mice connected to the device. This setting controls how fast the mouse pointer moves on the screen in response to physical movement of the mouse.

`1` is the slowest speed, while `10` is the fastest. The default value is `5`, which provides a balanced sensitivity for most users. Adjusting this setting can help improve the user experience when using a mouse with the Atari computer, especially if the default sensitivity feels too slow or too fast.

### 4.5 Gamepad auto-shoot

The `Gamepad auto-shoot` setting allows the user to adjust the auto-shoot speed for supported USB gamepads connected to the device. This setting controls how quickly the gamepad will repeatedly send the shoot command when the shoot button is held down.

`0` means no auto-shoot, while `10` is the fastest auto-shoot speed. The default value is `0`, which means that auto-shoot is disabled by default. Adjusting this setting can help improve the gaming experience when using a USB gamepad with the Atari computer, especially for games that require rapid firing. The auto-shoot feature is triggered when the user holds down the shoot button on the gamepad for more than two seconds.

### 4.6 Use original mouse (Experimental)

The `Use original mouse (Experimental)` setting allows the user to keep using the original ST mouse instead of using a USB mouse. When this option is enabled, the device will not emulate the original Atari mouse functionality for Bluetooth mice, and instead will pass through the signals from the original ST mouse.

### 4.7 USB joystick/gamepad

The `USB joystick/gamepad` setting allows the user to enable USB joystick and gamepad input. When this option is enabled, the device will emulate the original Atari joystick functionality for supported USB gamepads connected to the device. The gamepad is mapped to the joystick port selected in the `Preferred joystick port` setting.

### 4.8 Saving USB configuration

After adjusting the USB settings, click the `Save settings` button to store the configuration. This will ensure that the selected USB mode and settings are applied every time the computer is powered on.

### 4.9 Powering on with connected USB devices

When the computer is powered on with USB mode active and supported USB devices already connected, the expected behavior is:

1. Power on the computer. The device starts in USB mode.
2. Soufflè initializes the connected USB devices.
3. Once initialization is complete, the USB devices can be used as Atari input devices.

This mode is generally more direct than Bluetooth mode because it does not require wireless reconnection.

### 4.10 Powering on without connected USB devices

If the computer is powered on with USB mode active but no USB devices connected, the device simply starts in USB mode and waits for compatible USB peripherals to be attached.

Supported USB devices can then be connected later and used once they are detected by the emulator.

### 4.11 Keyboard behavior in USB mode

When USB mode is active and a USB keyboard is connected, the device emulates the original Atari keyboard while taking input from the USB keyboard.

The goal is to preserve the normal Atari keyboard behavior while allowing the use of a modern wired keyboard, but with a few differences to keep in mind. The main differences have to do with the use of a keyboard layout without a numerical and function keys. While it is possible to avoid the numerical keyboard, the combination of `ALTERNATE + INSERT` is a very important key combination that mimics the left button of the mouse. If the user is using a keyboard layout without a numerical keyboard, they can still access the `ALTERNATE + INSERT` combination by pressing `ALTERNATE + BACKSPACE` instead.

### 4.12 Mouse behavior in USB mode

When USB mode is active and a USB mouse is connected, the device emulates the original Atari mouse while taking movement and button input from the USB mouse.

If mouse behavior does not feel correct, try a different USB mouse model to rule out device-specific compatibility issues.

### 4.13 Gamepad behavior in USB mode

When USB mode is active and a supported USB joystick or gamepad is connected, the device emulates the original Atari joystick behavior while allowing the use of the USB gamepad. The gamepad is mapped to the joystick port selected in the `Preferred joystick port` setting as follows:

* D-pad: mapped to the joystick directional inputs (up, down, left, right)
* A, B, X, Y buttons: mapped to the joystick fire button

Support will depend on the USB device and the way it exposes its input controls to the emulator.

### 4.14 USB power caveats or limitations

USB mode is only available on Soufflè.

The USB devices take the power from the USB port of the Soufflè device, so they are not going to work if the computer is powered off. This means that USB devices will only work when the computer is on and the computer has a healthy power supply. Poor power supply or power issues can cause USB devices to disconnect or not work properly.

Also, as a rule of thumb, do not use power-hungry USB devices like USB hubs, keyboard with RGB lighting, or gaming mice with lots of features. The USB mode is intended for simple input devices like basic keyboards, mice, and gamepads. If you want to use more complex USB devices, consider using Bluetooth mode instead.

## 5. Advanced network configuration

Applicable hardware:

* Croissant
* Soufflè

This section is reserved for network-related configuration beyond the first-time setup described in Getting Started.

### 5.1 Overview

Example advanced networking page used by Croissant and Soufflè:

![SidecarTridge Keyboard Emulator advanced networking page](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-ADVANCED-NETWORKING.png)

The advanced network settings control how the manager web interface connects to Wi-Fi.

The two available connection modes are:

* `Access Point`: the device creates its own Wi-Fi network for direct access
* `Station`: the device joins an existing Wi-Fi network

Both modes share these common settings:

* `Host name`: hostname used by mDNS and local network naming
* `Password`: Wi-Fi password used by the selected mode
* `Auth mode`: Wi-Fi authentication mode used by the selected mode

Any changes on this page must be stored with `Save settings`.

### 5.2 Access Point settings

In `Access Point` mode, the device creates its own Wi-Fi network so a computer, tablet, or phone can connect directly to it.

Example of the advanced network page in Access Point mode:

![SidecarTridge Keyboard Emulator advanced network Access Point mode](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-ADVANCED-NETWORK-ACCESS-POINT.png)

When `Connection mode` is set to `Access Point`, the page exposes these settings:

* `Host name`: base name used for the device network identity
* `Password`: password required to join the device network
* `Auth mode`: authentication mode for the device network

In Access Point mode, the device is intended to be reached directly by joining its own Wi-Fi network.

Use `Save settings` to store the configuration, or `Reset` to discard unsaved changes.

### 5.3 Station settings

In `Station` mode, the device connects to an existing Wi-Fi network instead of creating its own.

Example of the advanced network page in Station mode:

![SidecarTridge Keyboard Emulator advanced network Station mode](/sidecartridge-keyboard/assets/images/KEYBOARD-EMULATOR-CROISSANT-SOUFFLE-ADVANCED-NETWORK-STATION.png)

When `Connection mode` is set to `Station`, the page provides these settings:

* `Host name`: hostname used by mDNS and local network naming
* `SSID`: Wi-Fi network name to join, or a BSSID for more advanced setups
* `Password`: password of the Wi-Fi network to join
* `Auth mode`: authentication mode used by that Wi-Fi network

In Station mode, the device requests an IP address by DHCP and should be reachable as `hostname.local` on the local network.

If Station mode setup fails, the device automatically falls back after 90 seconds to Access Point mode using default network settings.

Use `Save settings` to store the configuration, or `Reset` to discard unsaved changes.

### 5.4 Why use each configuration

Use `Access Point` mode when:

* you want to keep using the default network mode of the device
* you want a direct connection to the device without depending on an existing Wi-Fi network
* you are performing first-time setup or recovery
* you want the simplest possible way to reach the web interface

Use `Station` mode when:

* you want the device to join your normal Wi-Fi network
* you want to reach the web interface from another device already connected to that network
* you have several devices and want to rename each one with a host name that is easier to remember
* you prefer to access the device through `hostname.local` without switching to a dedicated device network

[Previous: Hardware Installation](/sidecartridge-keyboard/hardware-installation/){: .btn .mr-4 }
[Main](/sidecartridge-keyboard/){: .btn .mr-4 }
[Next: Compatibility](/sidecartridge-keyboard/compatibility/){: .btn }
