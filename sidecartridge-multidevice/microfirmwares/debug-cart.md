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


This microfirmware repurposes the SidecarTridge Multi-device as a **debug output cartridge** for Atari ST-family computers.

Software running on the Atari can send debug characters through the cartridge address space, which are forwarded to the USB serial port of the Multi-device.

This firmware is useful for low-level development, TOS debugging, driver development, and experiments that require output before normal I/O is available. See the [original project Debug Cart by **Christian Zietz** ](https://github.com/czietz/atari-debug-cart) for the original source and implementation details.

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

Characters are encoded on address lines A8–A1, so each cartridge read generates one output byte.  
This makes the debug channel extremely fast and usable even in timing-critical code.

To receive the debug output, the Raspberry Pi Pico on the SidecarTridge Multi-device exposes a **USB serial port**. On modern operating systems, no special drivers are required. Any terminal program that supports serial ports can be used. Because this is **not a physical UART**, the configured baud rate does not matter.

{: .note }
When using USB debug output, connecting the Pico to a laptop running on battery power may help avoid ground loop issues. This is usually not required, but can improve stability if you see unreliable serial output.

## 🖥️ Using a Serial Terminal

Open any serial terminal program on your host computer and connect to the USB serial port exposed by the SidecarTridge Multi-device.

Once connected, power on or reset the Atari system. Any software using the Debug Cart output method will send its debug messages to the terminal.

## 🧰 Debug Cart in the Wild: EmuTOS

The **[EmuTOS](https://emutos.sourceforge.io/)** operating system includes built-in support for this debug output method.

To enable it, set the `CARTRIDGE_DEBUG_PRINT` macro to `1` in the EmuTOS configuration and rebuild the OS. If you prefer not to compile EmuTOS yourself, you can use the [EmuTOS Building Tool by Thorsten Otto](https://tho-otto.de/emutos/) and enable the same option there. Then open a serial terminal, connect to the USB serial port, and power on the Atari to see the debug output.

## ✨ Benefits

- Very fast output (few CPU cycles per character)
- No initialization required
- Works very early during boot, before screen or serial drivers are initialized
- Does not use MFP or screen output
- Simple host-side setup using USB serial

## 🔁 Runtime Behavior

The firmware starts capturing debug bytes as soon as the app is launched and forwards them to the USB serial connection.

### System Reset Behavior

The debug cart continues running across system resets, so output is still available after pressing the reset button on the Atari.

### Power Cycling

When you power off and on your Atari, the app starts again with the SidecarTridge Multi-device.

### SELECT Button Behavior

* A short press on the **SELECT** button jumps back to the Booster menu.
* A long press resets the device.

## 📟 Example

The following example sends characters to the debug output:
```c
#define CARTRIDGE_ROM3 0xFB0000ul

(void)(((volatile short)(CARTRIDGE_ROM3 + ('H'<<1))));
(void)(((volatile short)(CARTRIDGE_ROM3 + ('i'<<1))));
```

This will print:

Hi

## 🛠️ Setting Up the Development Environment

This project is based on the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).

To set up the development environment, follow the instructions in the [official documentation](https://docs.sidecartridge.com/sidecartridge-multidevice/programming/) and in the [GitHub repository](https://github.com/sidecartridge/md-debug-cart).

## 🙏 Acknowledgements

This project is a direct migration of the [Atari ST Debug Cart by **Christian Zietz**](https://github.com/czietz/atari-debug-cart) and remains closely aligned with the original implementation, with only the changes needed to fit the SidecarTridge Multi-device microfirmware layout. The original code is licensed under **GNU GPL v3.0**, and this project continues under the same terms.

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.
See the [LICENSE](https://github.com/sidecartridge/md-debug-cart/blob/main/LICENSE) file for full terms.

## 🤝 Contributing

Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: File & Download Manager](/sidecartridge-multidevice/microfirmwares/browser/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: GPU Demo](/sidecartridge-multidevice/microfirmwares/gpu-demo/){: .btn }
