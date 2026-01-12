---
layout: default
title: SidecarTridge Multi-device Oric Computer Emulator
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/oric-emulator
  - /microfirmwares/oric-emulator/
  - /microfirmwares/oric_emulator
  - /microfirmwares/oric_emulator/
---

# SidecarTridge Multi-device Oric Computer Emulator
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-oric){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-oric/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-oric/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_ORIC_EMULATOR_VERSION }}](){: .label .label-purple }

This microfirmware app for the **SidecarTridge Multi-device platform** emulates an
**Oric** computer in the Atari ST class of machines. 

This emulator is based on the [Reload Emulator](https://github.com/vsladkov/reload-emulator)
project by Veselin Sladkov. **Huge thanks** for his great work!

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ⚠️ Attention

This emulator is designed **only for low-resolution monitors**.
It will **not** work in high-resolution modes.

## 🚀 Installation

To install the Emulator app on your SidecarTridge Multi-device:

1. **Launch** the **Booster App** on your SidecarTridge.
2. Open the **Booster web interface** in your browser.
3. Go to the **Apps** tab and select **Oric Emulator** from the list.
4. Click **Download** to install the app to your SidecarTridge’s microSD card.
5. Once installed, select the app and click **Launch**.

After installation, the Oric Emulator will start automatically every time your Atari is powered on.

## 🕹️ Usage

### Configuration

The emulator requires an image file with the Oric ROM to function. There are
plenty of Oric ROM images available online, try searching for "orica.zip" or
similar. Once you have the ROM image, rename it to `rom.img` and copy it to the
directory `/oric` on the SidecarTridge microSD card.

This should be enough to get started, but if you want to load applications and games, copy `.TAP` or `.WAV` files to the same `/oric` directory with the following structure:

- `f1.tap` or `f1.wav` - second tape file, loaded when pressing the F1 key.
- `f2.tap` or `f2.wav` - third tape file, loaded when pressing the F2 key.
- and so on...

Once the files are in place, launch the Oric Emulator app from the Booster interface or by rebooting your Atari with the Multi-device set to auto-launch the app.

### Emulator Controls

The emulator currently only supports file loading from tape or wave images. Use the
following keys to load the corresponding tape files:

* **F1** → Load `f1.tap` or `f1.wav` in the virtual cassette drive.
* **F2** → Load `f2.tap` or `f2.wav` in the virtual cassette drive.
* **F3** → Load `f3.tap` or `f3.wav` in the virtual cassette drive.
* and so on...

If the file is of TAP format, it will convert it to WAV format and will save a copy
as `fX.wav` in the same directory for future use.

After loading the tape file, use the command `CLOAD""` in the Oric BASIC prompt to load the program from the virtual tape.

You can find plenty of Oric software online in places like [Oric.org](http://www.oric.org/).

The `HELP` button will perform a soft reset of the Oric machine. The `UNDO` button will pause the emulation.

### ⏏️ Exiting to Booster

The emulator cannot exit back to GEM or the Booster interface directly. To exit
the emulator and return to the Booster app, you need to **power cycle** your
Atari ST and at the same time hold down the **SELECT** button on the
SidecarTridge. This will interrupt the normal boot process and launch the
Booster app instead of the Oric Emulator.

### 🔄 Power Cycling

After a power cycle, the emulator auto-launches.

## 🛠️ Under the hood

The Oric Emulator is built using the Reload Emulator core, adapted to run on the
SidecarTridge Multi-device platform.

## What’s next

Maintaining and improving this emulator is a hobby project for me. If you have
any suggestions or find any issues, please feel free to open an issue on the
GitHub repository.

### Missing features, future roadmap

This is a solid first release and a fun experiment, but there is plenty of room
to improve.

- [ ] Better framebuffer. It refreshes at 50 Hz, but shows the previous frame
  instead of the latest one.
- [ ] Joystick/gamepad support.
- [ ] Floppy disk support. I removed it to save CPU cycles, but that is not the
  right place to cut.
- [ ] TAP file load menu. The function key solution is functional, but clunky.
- [ ] Faster framebuffer build. Creating the Atari ST framebuffer from the Oric
  screen needs to be more efficient.
- [ ] Performance improvements.
- [ ] Direct TAP file load. The current code converts to WAV; it works, but is
  not ideal.

## License

This project is released under the GNU General Public License v3.0. See the [LICENSE](https://github.com/sidecartridge/md-sprites-demo/blob/main/LICENSE) file for details.

Note: the original Reload Emulator repository does not display a license, so I
do not know what license to attribute for that upstream code.

## 🤝 Contributing
Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: GPU Demo](/sidecartridge-multidevice/microfirmwares/gpu-demo/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Architecture and Design](/sidecartridge-multidevice/architecture_and_design/){: .btn }
