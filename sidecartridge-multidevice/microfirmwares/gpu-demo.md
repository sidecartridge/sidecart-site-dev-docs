---
layout: default
title: SidecarTridge Multi-device GPU Demo
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/gpu-demo
  - /microfirmwares/gpu-demo/
  - /microfirmwares/sprites-demo
  - /microfirmwares/sprites-demo/
---

# SidecarTridge Multi-device GPU Demo
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-gpu-demo){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-gpu-demo/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-gpu-demo/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_GPU_DEMO_VERSION }}](){: .label .label-purple }

This microfirmware app for the **SidecarTridge Multi-device** is a demoscene-oriented showcase of what the RP2040 in the SidecarT can do when it acts as a graphics co-processor for a real Atari ST, STE, Mega ST or Mega STE. From v2.0.0beta onwards it is no longer a single sprite stress test: it is a small intro / demo playground with an animated boot menu and four worked demos that exercise rotozoom, parallax, filled 3D vectors, sprite swarms and sampled audio.

The whole thing is built on top of the [md-framebuffer-template](https://github.com/sidecartridge/md-framebuffer-template) starter framework, so every effect here is also a working reference you can use as the foundation of your own SidecarT app, including full-blown games that want to squeeze every cycle out of the RP2040.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

<figure class="video_container" style="position: relative; padding-bottom: 140%; height: 0; overflow: hidden; max-width: 420px; margin: 0 auto; background: #000;">
  <iframe
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
    src="https://www.youtube.com/embed/j1Au5puLhb4?iv_load_policy=3&modestbranding=1&playsinline=1&showinfo=0&rel=0&enablejsapi=1"
    loading="lazy"
    allowfullscreen
    allowtransparency>
  </iframe>
</figure>

## ⚠️ Attention

This app is designed **only for low-resolution monitors**. It will **not** work in high-resolution modes.

## 🚀 Installation

To install the GPU Demo app on your SidecarTridge Multi-device:

1. **Launch** the **Booster App** on your SidecarTridge.
2. Open the **Booster web interface** in your browser.
3. Go to the **Apps** tab and select **GPU Demo** from the list.
4. Click **Download** to install the app onto the microSD card.
5. Select the newly installed app and click **Launch**.

After installation, the GPU Demo will start automatically every time your Atari is powered on, dropping you into the demo menu.

## 🕹️ Usage

### Boot menu

On startup the app shows an animated boot menu on top of a rotozooming SidecarTridge backdrop. You can pick a demo with the keyboard, jump directly to a slot with a number key, and toggle the on-screen timing readouts at any time.

Menu controls:

* `Up` / `Down`: move the menu selection.
* `Return`: launch the selected demo.
* `1` / `2` / `3` / `4`: launch the corresponding demo directly.
* `D`: toggle the DRAW / C2P timing readout.
* `Esc`: exit back to GEM (the Atari desktop).

### The four demos

* **Uridium-style parallax**: layered starfields, metal grids, transparent scrolling surfaces and a controllable ship. Cursor keys move the ship vertically.
* **Filled 3D vector object**: fixed-point rotation, projection, backface culling, triangle filling and shaded Atari ST palettes.
* **Multi-sprite stress demo**: many animated sprites with transparent blits and frame-budget tracking, adapted from a Pico VGA demo.
* **Cojorotozoom intro**: fixed-point rotozoom, bitmap scroll-text, palette ramps, transparent texture sampling and sprite overlays.

Inside a demo:

* `Esc`: return to the menu.
* `D`: toggle the timing readouts.

### ⏏️ Exiting to Booster

The GPU Demo replaces the ROM while it is running, so it cannot exit cleanly back to the Booster web UI from the running app. `Esc` only exits the running demo (back to the menu, or back to GEM from the menu).

To return to **Booster**, **power cycle your Atari ST while holding the SELECT button on the SidecarTridge Multi-device**. This is a hardware escape hatch: it jumps straight to Booster before the GPU Demo's configuration or emulation runs, so you can always reach the configurator even if the app misbehaves.

### 🔄 Power cycling

After a power cycle without SELECT held, the GPU Demo auto-launches and you land back on the boot menu.

## 🛠️ Under the hood

The GPU Demo is built on top of the [md-framebuffer-template](https://github.com/sidecartridge/md-framebuffer-template) framework. The RP2040 draws into a 320x200, 16-colour chunky framebuffer in its own RAM; the framework does the chunky-to-planar conversion and the tear-free, VBL-synced hand-off to the ST at 50 Hz. The Atari side also gets keyboard input and sampled audio for free, so each demo can focus on its effect instead of bus timing.

For the implementation details of any individual effect (rotozoom, parallax, vector pipeline, sprite engine, scroll-text), the source code is the reference. The README in the upstream repository links each demo to its file under `rp/src/demo_*.c`.

## 📜 License

This project is released under the **GNU General Public License v3.0**. See the [LICENSE](https://github.com/sidecartridge/md-gpu-demo/blob/main/LICENSE) file for full terms.

## 🤝 Contributing

Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: Debug Cart](/sidecartridge-multidevice/microfirmwares/debug-cart/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Oric Emulator](/sidecartridge-multidevice/microfirmwares/oric-emulator/){: .btn }
