---
layout: default
title: SidecarTridge Debug Cart
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/debug-cart/
  - /microfirmwares/debug-cart
  - /microfirmwares/debug_cart/
  - /microfirmwares/debug_cart

---

# SidecarTridge Debug Cart
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-debug-cart){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-debug-cart/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-debug-cart/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_DEBUG_CART_VERSION }}](){: .label .label-purple }


This is a microfirmware application for the **SidecarTridge Multi-device**, designed to provide **debug output for Atari ST-family software** through the cartridge port.

It repurposes the SidecarTridge Multi-device as a debug-output device for **Atari ST, STe, Mega ST, and Mega STe** software. Debug output is captured by reading from the cartridge address space and forwarded to a **USB serial connection**. See the [original project Debug Cart by **Christian Zietz** ](https://github.com/sidecartridge/md-debug-cart) for the original source and implementation details.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 🚀 Installation

To install the Debug Cart app on your SidecarTridge Multi-device:

1. Launch the **Booster App** on your SidecarTridge Multi-device.
2. Open the Booster web interface.
3. In the **Apps** tab, select **"Debug Cart"** from the list of available apps.
4. Click **"Download"** to install the app to your SidecarTridge microSD card.
5. Once installed, select the app and click **"Launch"** to activate it.

After launching, the app will automatically run every time your Atari computer is powered on.

## 🧪 How It Works

Debug output is transmitted by reading from the cartridge address space at `0xFBxxxx`. Characters are encoded on address lines `A8-A1`. For example, the following code sends the character `A`:

```c
#define CARTRIDGE_ROM3 0xFB0000ul
(void)(*((volatile short*)(CARTRIDGE_ROM3 + ('A'<<1))));
```

To receive the debug output, the Raspberry Pi Pico on the SidecarTridge Multi-device exposes a **USB serial port**. On modern operating systems, no special drivers are required. Any terminal program that supports serial ports can be used. Because this is **not a physical UART**, the configured baud rate does not matter.

{: .note }
To reduce the risk of ground current loops, it is recommended, but not mandatory, to connect the Pico USB port to a battery-powered computer such as a laptop running on battery while the SidecarTridge Multi-device is plugged into the Atari.

## 🖥️ Using a Serial Terminal

Open any serial terminal program on your host computer and connect to the USB serial port exposed by the SidecarTridge Multi-device.

Once connected, power on or reset the Atari system. Any software using the Debug Cart output method will send its debug messages to the terminal.

## 🧰 Debug Cart in the Wild: EmuTOS

The **[EmuTOS](https://emutos.sourceforge.io/)** operating system includes built-in support for this debug output method.

To enable it, set the `CARTRIDGE_DEBUG_PRINT` macro to `1` in the EmuTOS configuration and rebuild the OS. If you prefer not to compile EmuTOS yourself, you can use the [EmuTOS Building Tool by Thorsten Otto](https://tho-otto.de/emutos/) and enable the same option there. Then open a serial terminal, connect to the USB serial port, and power on the Atari to see the debug output.

## ✨ Benefits

* **Fast output**: cartridge-port access takes only a few CPU cycles, so the timing impact is much lower than with MFP serial output or on-screen debug output.
* **No hardware initialization required**: cartridge-port access is available immediately.
* **Useful for early boot debugging**: output can be produced very early in software startup.
* **Simple host-side setup**: only a USB serial terminal is needed.

## 🔁 Runtime Behavior

The firmware starts capturing debug bytes as soon as the app is launched and forwards them to the USB serial connection.

### System Reset Behavior

The app is resistant to Atari system resets. Pressing the reset button on the Atari does not stop the firmware.

### Power Cycling

When you power off and on your Atari, the app starts again with the SidecarTridge Multi-device.

### SELECT Button Behavior

* A short press on the **SELECT** button jumps back to the Booster menu.
* A long press resets the device.

## 🛠️ Setting Up the Development Environment

This project is based on the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).

To set up the development environment, follow the instructions in the [official documentation](https://docs.sidecartridge.com/sidecartridge-multidevice/programming/) and in the [GitHub repository](https://github.com/sidecartridge/md-debug-cart).

## 🙏 Acknowledgements

This project is a direct migration of the Atari ST Debug Cart by **Christian Zietz** and remains closely aligned with the original implementation, with only the changes needed to fit the SidecarTridge Multi-device microfirmware layout. The original code is licensed under **GNU GPL v3.0**, and this project continues under the same terms.

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.
See the [LICENSE](https://github.com/sidecartridge/md-debug-cart/blob/main/LICENSE) file for full terms.

## 🤝 Contributing

Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: File & Download Manager](/sidecartridge-multidevice/microfirmwares/browser/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: GPU Demo](/sidecartridge-multidevice/microfirmwares/gpu-demo/){: .btn }
