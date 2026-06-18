---
layout: default
title: SidecarTridge MD/JS JavaScript Worker
nav_order: 6
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/md-js
  - /microfirmwares/md-js/
  - /microfirmwares/mdjs
  - /microfirmwares/mdjs/
  - /sidecartridge-multidevice/microfirmwares/mdjs
  - /sidecartridge-multidevice/microfirmwares/mdjs/
---

# SidecarTridge MD/JS JavaScript Worker
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-js){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-js/releases){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-js/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_MDJS_VERSION }}](){: .label .label-purple }

**MD/JS** turns your SidecarTridge Multi-device into a persistent JavaScript worker for the Atari ST family. Upload JavaScript source from your ST, call named functions with JSON arguments, parse JSON results, and use `fetch()` to load text or JSON files over HTTP. A full [JerryScript](https://jerryscript.net) ES.next runtime runs on the RP2040, so your ST can drive modern scripting without leaving its native ROM.

This microfirmware is the work of [**Neil Rackett**](https://github.com/neilrackett) ([@neilrackett](https://x.com/neilrackett) on X), maintained in his upstream repository at [github.com/neilrackett/md-js](https://github.com/neilrackett/md-js). The SidecarTridge organisation hosts a fork at [github.com/sidecartridge/md-js](https://github.com/sidecartridge/md-js) with Neil's explicit permission, so it can be distributed through the Booster app catalog alongside the other official microfirmwares. **Huge thanks to Neil** for the work, the collaboration, and for letting us bring MD/JS to every SidecarTridge user.

{: .important }
The README on Neil's repo is the source of truth for the JavaScript API, build instructions, and the full protocol description. The page below is a curated overview of the user-facing flow. For integration details head to the project's [README on GitHub](https://github.com/sidecartridge/md-js/blob/main/README.md).

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ✨ What MD/JS does

- Uploads JavaScript source from the ST to the RP2040 over the cartridge bus.
- Runs a persistent JerryScript ES.next runtime with ES5.1, ES6 / 2015, and most ES2020 features.
- Calls named JavaScript functions with JSON arguments and returns JSON results.
- Loads text or JSON files via `fetch()` (HTTP GET).
- Exposes a clean C API so ST programs can embed `mdjs_*` calls directly.

Within these limits:

- 32 KB JavaScript heap (48 KB when compiled without `fetch`).
- 2 KB result buffer.
- `fetch()` is HTTP GET only.

## 🚀 Installation

You can install MD/JS the same way as any other microfirmware in the catalog.

1. **Launch the Booster App** on your SidecarTridge Multi-device.
2. Open the **Booster web interface** in your browser.
3. Go to the **Apps** tab and select **MD/JS** from the list.
4. Click **Download** to install the app onto the microSD card.
5. Select the newly installed app and click **Launch**.

If you prefer the manual route (for example, when testing a release that is not yet in the catalog):

1. Download the latest `.uf2` and `.json` files from the [releases page](https://github.com/sidecartridge/md-js/releases).
2. Copy both files to the `/apps` folder of your SidecarTridge microSD card.
3. From the Booster screen press **ESC** to open the app list and select **MD/JS**.

After launching, MD/JS will run automatically every time your Atari is powered on.

## 🕹️ Usage

### First boot

When MD/JS starts, your ST shows the message:

```
MD/JS: JavaScript Worker is ready
```

That is your signal that the JerryScript runtime is alive on the RP2040 and that the ST-side API is reachable.

### Try the demo

The microfirmware ships with a quick demo so you can see MD/JS in action without writing any code:

1. Open the cartridge icon on your ST's desktop (the lower case `c` drive).
2. Run `MDJSDEMO.PRG`.

The demo uploads a small JavaScript program, calls a couple of functions, and prints the results on the ST.

### MD/JS Code (GEM editor)

[**MD/JS Code**](https://github.com/sidecartridge/md-js/releases) is an example GEM application maintained by Neil that lets you edit and run JavaScript source code directly on the Atari ST. Download it from the releases page if you want a ready-made workbench instead of building your own ST front-end.

### Writing your own ST programs

To integrate MD/JS into a native ST application, include `mdjs.h` and link against `mdjs.c` and `sidecart_stubs.S`:

```c
#include "mdjs.h"

/* Check the worker is present */
if (mdjs_ping() != 0) {
  /* No SidecarTridge / worker not running */
}

/* Upload JavaScript source (evaluated immediately) */
mdjs_upload("function greet(name) { return 'Hello, ' + name + '!'; }");

/* Call a function: args as a JSON array, result as a JSON value */
char result[256];
mdjs_call("greet", "[\"World\"]", result, sizeof(result));
/* result == "\"Hello, World!\"" */

/* Clear the JS context and start fresh */
mdjs_reset();
```

All functions return `0` on success, non-zero on timeout or error. `mdjs_upload` handles chunking automatically, so just pass the full source string. For long-running scripts there is also an async API (`mdjs_call_async` / `mdjs_status` / `mdjs_result`) that does not block the 68000 while the JS runs on the RP2040.

### API limits

| Parameter              | Limit / address                              |
| ---------------------- | -------------------------------------------- |
| JS source per upload   | Up to ~16 KB (8 chunks × 2096 bytes)         |
| Function name          | 63 characters                                |
| Result JSON            | 2048 bytes                                   |
| Args JSON              | 2031 bytes (max, with 63-char function name) |
| JerryScript heap       | 48 KB                                        |
| Result buffer (ST)     | `$FAF100` (ROM4 + 0xF100)                    |
| Async status byte (ST) | `$FAF008` (ROM4 + 0xF008)                    |

### ⏏️ Exiting to Booster

MD/JS replaces the ROM while it is running, so it cannot exit cleanly back to GEM or to the Booster web UI from the running app.

To return to **Booster**, **power cycle your Atari ST while holding the SELECT button on the SidecarTridge Multi-device**. This interrupts the normal boot path and launches the Booster app instead of MD/JS.

### 🔄 Power Cycling

After a power cycle without SELECT held, MD/JS auto-launches and the worker is ready again as soon as the ST shows the "ready" message.

## 🛠️ Under the hood

MD/JS uses both cores of the RP2040 so the cartridge bus is never blocked:

- **Core 0** handles the cartridge bus and the MD/JS protocol decode.
- **Core 1** runs the JerryScript runtime (`jerry_parse` / `jerry_run` / `jerry_call`).
- Calls cross between cores through the RP2040 multicore FIFO.
- Results are written into the ST's ROM4 address space at `$FAF100` and the async status byte lives at `$FAF008`, so the ST can poll without a bus transaction.

```
Atari ST (68000)                     RP2040
----------------                     ------
mdjs_ping()           --CMD 0x10--   Core 0: tprotocol decode
mdjs_upload(src)      --CMD 0x11--        v  multicore FIFO
mdjs_call(f, a, r)    --CMD 0x12--   Core 1: JerryScript runtime
mdjs_reset()          --CMD 0x13--        v  jerry_parse / jerry_run / jerry_call
mdjs_call_async(f, a) --CMD 0x14--        v  result -> ROM-in-RAM @ $FAF100
mdjs_poll()           --CMD 0x15--   Core 0: writes random token (unblocks ST)

mdjs_result(r)        <-------       Status byte @ $FAF008 (no bus transaction)
```

For the full protocol description, build targets, and the JavaScript / C API reference, see the upstream README at [github.com/sidecartridge/md-js](https://github.com/sidecartridge/md-js/blob/main/README.md).

## 🙏 Credits

- **Author and maintainer:** [Neil Rackett](https://github.com/neilrackett) ([@neilrackett on X](https://x.com/neilrackett)).
- **Upstream repository:** [github.com/neilrackett/md-js](https://github.com/neilrackett/md-js).
- **SidecarTridge fork (catalog distribution):** [github.com/sidecartridge/md-js](https://github.com/sidecartridge/md-js).
- **Runtime:** [JerryScript](https://jerryscript.net), the lightweight JavaScript engine that does the heavy lifting on the RP2040.

If you build something with MD/JS or hit an issue, please report it on Neil's upstream repository so the wider ecosystem benefits.

## 📜 License

The source code is released under the **GNU General Public License v3.0**. See the [LICENSE](https://github.com/sidecartridge/md-js/blob/main/LICENSE) file for the full text.

## 🤝 Contributing

MD/JS is **made with care by [Neil Rackett](https://github.com/neilrackett)**, distributed through the SidecarTridge Multi-device catalog with his permission. Issues and pull requests are welcome upstream.

[Previous: DevOps](/sidecartridge-multidevice/microfirmwares/devops/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: MIDI-to-IP](/sidecartridge-multidevice/microfirmwares/midi-to-ip/){: .btn }
