---
layout: default
title: SidecarTridge Multi-device File & Download Manager
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/browser
  - /microfirmwares/browser/
---

# SidecarTridge Multi-device GPU Demo
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-sprites-demo){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-sprites-demo/blob/main/CHANGELOG.md){: .label .label-green }
[{{ site.MICROFIRMWARE_GPU_DEMO_VERSION }}](){: .label .label-purple }

This micro-firmware app for the **SidecarTridge Multi-device** showcases the RP2040’s capabilities in the Raspberry Pi Pico W acting as a graphics co-processor.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

<figure class="video_container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
  <iframe 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
    src="https://www.youtube.com/embed/NPjklKdaaVs?iv_load_policy=3&modestbranding=1&playsinline=1&showinfo=0&rel=0&enablejsapi=1"
    loading="lazy"
    allowfullscreen
    allowtransparency>
  </iframe>
</figure>

## ⚠️ Attention

This demo is designed **only for low-resolution monitors**.
It will **not** work in high-resolution modes.

## 🚀 Installation

To install the GPU Demo app on your SidecarTridge Multi-device:

1. **Launch** the **Booster App** on your SidecarTridge.
2. Open the **Booster web interface** in your browser.
3. Go to the **Apps** tab and select **GPU Demo** from the list.
4. Click **Download** to install the app to your SidecarTridge’s microSD card.
5. Once installed, select the app and click **Launch**.

> **⚠️ WARNING:** The Booster Loader is currently in **alpha** — use at your own risk.

After installation, the GPU Demo will start automatically every time your Atari is powered on.

## 🕹️ Usage

On startup, the app shows a brown wall and torches. Then:

* The demo begins rendering **48×48 sprites** with a **16-color palette** over a background of **64×64 tiles** (also 16 colors).
* Every 3 seconds, a new sprite appears — up to \~37–38 sprites (limited by time needed to maintain 50 FPS).

**Controls:**

* **Any other key** - exits the emulator and boots into the Atari GEM desktop.
* **ESC** — return to the Booster App.


### ⏏️ Exiting to GEMDOS or Booster

* **ESC** → Launch Booster app.
* **Any other key** → Exit emulator, boot Atari GEM desktop.
* **SELECT button** on Multi-device → Reboot demo (Atari ST reset must be done manually).
* **Hold SELECT for 10 seconds** → Factory reset the Multi-device.


### ♻️ Reset Behavior

* Pressing the Atari reset button **alone** will **not restart the demo**.
  To restart: press **SELECT** first, then reset the computer.


### 🔄 Power Cycling

After a power cycle, the demo auto-launches.


## 🛠️  Under the hood

This demo is a re-imagining of the [RP2040 VGA 6-bit demo](https://github.com/moefh/pico-vga-6bit-demo) for the Atari ST world. Instead of producing VGA signals, the RP2040 fills Atari-friendly framebuffers in its own memory — the same memory used by the ROM emulation logic in the SidecarTridge.

The framebuffers follow the classic Atari ST low-res layout: 32 KB of contiguous memory, four bitplanes. The RP2040 keeps them updated with whatever’s happening in the scene, and the Atari just reads and displays them.


## Tiles, sprites, and color conversion

In the original VGA demo, tiles and sprites are stored in **RGB6** format: 6 bits per pixel, two bits each for red, green, and blue, allowing 64 colors. The Atari ST can only show 16 colors at a time, so conversion is necessary. A “smart” approach would be to pre-convert all data to the ST’s planar format. This demo takes the opposite route: it converts on-the-fly.

Why? Because the goal isn’t raw performance — it’s to explore strategies for live conversion from chunky RGB6 to the ST’s planar format, which might be useful for future work. Converting a whole screen of background tiles takes around 8 ms, which would be too slow for some uses but serves fine here.


## Transparency

Sprites use a simple color-key transparency: one palette color is treated as invisible, and any pixel matching it isn’t drawn. This, too, is handled live during conversion. 

## Text

Text rendering works the same way — a small 6×8 bitmap font is stored in the RP2040, converted to planar format as needed, and blended into the scene.

## ST vs. STE

The core loop is tuned differently for the two machines. On a plain ST, it’s raw 68000 speed, using self-generated `MOVEM.L` sequences to blast the framebuffer to screen memory in under 20 ms:

```
MOVEM.L $FA0600, D0-D7/A0-A7
MOVEM.L D0-D7/A0-A7, $70000
...
```

On an STE, the blitter takes over, copying large chunks in one go and finishing much faster. In the ST version you’ll see a red timing bar at the bottom showing how much copy time is used; on the STE, that bar turns blue and is shorter, thanks to the blitter’s speed.

## Double buffering

Two framebuffers live in the RP2040’s RAM and two more in the Atari’s. This is overkill but makes tearing impossible: while one buffer is displayed, the other is being drawn. It could be made leaner, but again, performance tuning wasn’t the main goal here.

## What’s next

I don’t plan to push this much further — it’s a proof of concept and a learning project before tackling something far bigger, like getting DOOM running on the Multi-device.

If you want to take it further, you could pre-convert all assets to planar format, shrink the number of framebuffers, or cut down on redundant OR operations when drawing tiles.

## 📜 License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](https://github.com/sidecartridge/md-sprites-demo/blob/main/LICENSE) file for full terms.

## 🤝 Contributing
Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: Browser](/sidecartridge-multidevice/microfirmwares/browser/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
