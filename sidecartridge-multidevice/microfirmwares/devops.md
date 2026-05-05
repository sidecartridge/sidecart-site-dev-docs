---
layout: default
title: SidecarTridge DevOps
nav_order: 5
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/devops/
  - /microfirmwares/devops
  - /microfirmwares/md-devops/
  - /microfirmwares/md-devops
---

# SidecarTridge DevOps
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-devops){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-devops/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-devops/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_DEVOPS_VERSION }}](){: .label .label-purple }


This microfirmware turns the cartridge slot of an Atari ST / STE / Mega ST(E) into a remote development surface for the m68k. While booted, the cartridge emulates a ROM, mounts a microSD subdirectory as a GEMDOS drive (GEMDRIVE), and exposes a Wi-Fi HTTP API plus a Python CLI that lets a workstation upload and download files, launch programs, load and step through them in pieces, switch screen resolution, snapshot ST memory, and stream debug bytes from the running m68k in real time.

If you only need the basic GEMDRIVE experience (folder-as-drive, floppies, ACSI), the sister microfirmware [Drives Emulator](/sidecartridge-multidevice/microfirmwares/drives_emulator/) is what you want. **DevOps** is the developer-focused variant of that surface, with the runner, debug and HTTP management features stitched on top.

{: .important }
For the full reference, more end-to-end examples and the complete API documentation, head to the project's [README on GitHub](https://github.com/sidecartridge/md-devops/blob/main/README.md). The page below is a curated overview; the README is the source of truth and is kept in sync with each release.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ✨ Highlights

- **GEMDRIVE folder-as-drive**: point a microSD subdirectory at a TOS drive letter and it just appears.
- **Runner mode**: the workstation triggers `Pexec` of any TOS / PRG, watches the exit code, can also `cd`, switch resolution and snapshot memory.
- **`Pexec` load / exec / unload split**: load once, re-exec many times, free explicitly. Useful for iterative debugging without re-reading a slow file off SD each cycle.
- **Advanced Runner**: a second command surface running from inside the m68k's VBL ISR, so it keeps working when the foreground program has wedged the system (infinite loops, bombs already painted, traps disabled).
- **Remote HTTP file management**: `curl` plus the `sidecart` Python CLI for `ls / get / put / rm / mv / mkdir / rmdir / mvdir / volume`.
- **Fast debug traces**: single-cartridge-cycle byte emit from the m68k (`*(volatile char *)(0xFBFF00 + c)`), captured RP-side and streamed to either an HTTP `tail -f` endpoint or USB CDC. No framing, no overhead, byte-exact.
- **Live setup menu**: graphical status icons (Wi-Fi / SD / USB CDC / Adv Vector), animated countdown bar, USB CDC attach state refreshed live as you plug or unplug.

{: .warning }
The HTTP API has **no authentication**. Treat the network the device is reachable on as trusted, and do not expose `sidecart.local` past your LAN router.

## 🚀 Installation

To install the DevOps app on your SidecarTridge Multi-device:

1. Launch the **Booster App** on your SidecarTridge Multi-device.
2. Open the Booster web interface.
3. In the **Apps** tab, select **"DevOps"** from the list of available apps.
4. Click **"Download"** to install the app to your SidecarTridge microSD card.
5. Once installed, select the app and click **"Launch"** to activate it.

After launching, the Pico W reboots into DevOps and subsequent power-ons go straight there. You only need to revisit Booster to install another app or to update.

## 🕹️ Boot flow and setup menu

Power-on after install lands on the **Setup menu** for around 20 seconds. You have four top-level commands:

| Key | Action |
| --- | --- |
| `[U]` | **Runner mode** (recommended). GEMDRIVE comes up, plus the Runner control surface for `runner run` / `load` / `exec` and friends. |
| `[G]` | **GEMDRIVE only**. The ST drops straight into the emulated drive but the Runner is not activated. Use this if you only want file emulation and don't need the workstation to drive the ST. |
| `[X]` | Return to the Booster menu (e.g. to install another app). |
| any key | Halt the auto-launch countdown so the menu stays up indefinitely while you read it. |

If you do nothing within ~20 s, the firmware auto-fires `[U]` Runner, the more useful default for unattended boots.

The menu paints into the cartridge framebuffer at `$FAE0C0` so the ST itself shows it. From top to bottom you get a title bar, the **GEMDRIVE** section (folder, drive letter, relocation address, memtop, plus the read-only `_phystop` at `$42E` and `_v_bas_ad` screen base at `$44E`), the **Adv [V]ector** section (which interrupt vector the Advanced Runner installs its hook into), the **API Endpoint** section (mDNS hostname and the IP DHCP leased), and the **USB CDC (Debug serial)** section (`connected` / `disconnected`, live-refreshed as you plug or unplug a USB cable).

A `(!)` marker on the Phystop line means TOS' phystop disagrees with the silicon's MMU bank-config nibble at `$FFFF8001`, a sign that a reset-resistant program lowered phystop and survived a warm reset. Only a full power-cycle restores it.

### SELECT button: Pico-side reset and factory reset

The cartridge's physical **SELECT** button is wired so a press on the Pico itself can recover the device without needing the ST's keyboard:

| Press | Action |
| --- | --- |
| Short tap (< 10 s) | **Soft reset** of the Pico. The cartridge boots back into the setup menu. The ST's TOS state is unaffected, but on the next ST cold reset the firmware re-handshakes from scratch. |
| Long press (≥ 10 s, hold steady) | **Factory reset.** The Pico erases its flash-stored aconfig (drive letter, reloc address, hook vector, etc.) and reboots. Use this if a setting got the device into a state where the menu won't come up; power-cycle the ST afterwards so it sees the cleared cartridge. |

The button is the canonical recovery path for any banner the firmware shows on the ST screen (e.g. the `Reloc/stack overlap` warning thrown when a misconfigured relocation address would land on or near the live supervisor stack).

### Picking a hook vector

`[V]` toggles the Advanced Runner ISR between two vectors:

- **`vbl ($70)`** (default): the 68000 hardware vertical-blank exception vector. Sits ahead of TOS' VBL chain, so it keeps firing even if a launched program disables or hijacks TOS' own VBL bookkeeping. Standard m68k exception trap frame on the supervisor stack, so the firmware can reliably rewrite the saved PC. **`runner adv jump` and `runner adv load` only work on this vector.** A program that overwrites `$70.l` with its own raw VBL handler will replace ours on the spot.
- **`etv_timer ($400)`** (opt-in): TOS' documented "extension hook" called from inside TOS' VBL handler chain, after TOS finishes its bookkeeping. Cooperates better with TOS-aware background code and survives a program overwriting `$70.l`. The trap-frame layout when our code runs is past TOS' MFP scratch and not stable across TOS versions, so `runner adv jump` and `runner adv load` refuse with `409 wrong_hook` on this vector. `runner reset` and `runner adv meminfo` still work.

## 🌐 Remote HTTP Management API

Once the device joins Wi-Fi it serves an HTTP/1.1 REST API on port 80 at `http://sidecart.local/`. The API is the **single control surface** for every remote operation in this firmware (file management, program execution, debug streaming).

| Family | HTTP endpoints | CLI prefix |
| --- | --- | --- |
| Health | `GET /api/v1/ping` | `sidecart ping` |
| GEMDRIVE | `GET / PUT / DELETE / POST /api/v1/gemdrive/{volume,files,folders}/…` | `sidecart gemdrive …` |
| Runner | `GET / POST /api/v1/runner/…` | `sidecart runner …` |
| Debug | `GET /api/v1/debug`, `GET /api/v1/debug/log` | `sidecart debug …` |

You can drive the API from any HTTP client (`curl`, `wget`, `httpie`, a browser, a shell script). The full per-endpoint reference (URLs, JSON envelope shapes, status codes, error vocabulary, `curl` examples) lives in the [API documentation](https://github.com/sidecartridge/md-devops/blob/main/docs/api.md) inside the source repo.

### `cli/sidecart.py`, the Python CLI

A single-file Python script in the repo. **Requirements**: Python 3.10 or later, no third-party packages (stdlib-only). Clone the repo (or download the one file) and call it directly:

```sh
git clone https://github.com/sidecartridge/md-devops.git
cd md-devops
python3 cli/sidecart.py ping
```

Drop a symlink on your `PATH` to use it as `sidecart`:

```sh
chmod +x cli/sidecart.py
ln -s "$(pwd)/cli/sidecart.py" /usr/local/bin/sidecart
sidecart ping
```

The CLI talks to `sidecart.local` by default. Override per-invocation with `--host`, or for the whole shell session with `SIDECART_HOST`. Precedence: `--host` > `$SIDECART_HOST` > `sidecart.local`.

## 💾 GEMDRIVE: manage files and folders remotely

The Atari ST sees a microSD subdirectory as a TOS drive (default `C:`, configurable from the setup menu). The `gemdrive` subcommand on the workstation gives you full read / write access to that same directory tree without ejecting the SD card.

```sh
$ sidecart gemdrive volume                    # disk capacity
$ sidecart gemdrive ls /                      # list a folder
$ sidecart gemdrive get GAME.TOS              # download a file
$ sidecart gemdrive put GAME.TOS -f           # upload (overwrite)
$ sidecart gemdrive rm STALE.TXT              # delete a file
$ sidecart gemdrive mv OLD.TXT NEW.TXT        # rename / move
$ sidecart gemdrive mkdir /GAMES              # create a folder
$ sidecart gemdrive rmdir /GAMES/EMPTY        # delete an empty folder
$ sidecart gemdrive mvdir /TMP/STAGE /GAMES/  # rename / move a folder
```

All paths are jailed under the `GEMDRIVE_FOLDER` parameter (default `/devops`). FAT 8.3 names are enforced (stem ≤ 8 chars, extension ≤ 3 chars, ASCII, no `*?/\:<>"|+,;=[]`). Per-request upload cap is 4 MB; `Content-Length` is required and chunked uploads are rejected.

A typical edit-build-test loop on the workstation:

```sh
make game.tos
sidecart gemdrive put game.tos /GAMES/ -f
sidecart runner run /GAMES/game.tos
sidecart runner status        # check exit code
```

## 🏃 Runner mode

Runner mode is the foreground execution path. The user picks `[U]` at the setup menu to launch it. The m68k Runner stays in a poll loop waiting for commands from the RP, while GEMDRIVE keeps servicing TOS file I/O so launched programs can use the emulated drive normally.

The Runner surface splits into three behavioural buckets:

- **Status reads** (`runner status`, `runner adv status`): pure RP-side state, always succeed (200 OK), never block, never error.
- **Foreground commands** (`runner cd` / `res` / `meminfo` / `run` / `load` / `exec` / `unload`): speak to the m68k Runner poll loop. Return `409 runner_inactive` if `[U]` was not picked, and `503 busy` if another foreground command is already in flight. Cannot reach a wedged ST.
- **VBL-driven commands** (`runner reset` and the `runner adv` family): ride the m68k VBL ISR (`$70`, or `$400` if you switched `ADV_HOOK_VECTOR` to `etv_timer`), so they keep working even when the foreground poll loop is wedged. None gate on the busy lock.

Common verbs:

| Verb | Purpose |
| --- | --- |
| `runner status` | Show Runner state (active flag, busy lock, cwd, last command, last exit code, loaded basepage). |
| `runner reset` | Cold-reset the Atari ST through the VBL ISR. Works against wedged programs the foreground commands cannot reach. |
| `runner cd PATH` | Change the Runner's cwd (GEMDOS `Dsetpath`). |
| `runner res low\|med` | Switch ST screen resolution (XBIOS `Setscreen`). |
| `runner meminfo` | System memory snapshot (`membottom`, `memtop`, `phystop`, `screenmem`, `basepage`, bank sizes). |
| `runner run REMOTE [args…]` | `Pexec(0)` load + go + free, identical to typing the program name on the GEMDOS prompt. |
| `runner load` / `exec` / `unload` | `Pexec(3)` / `Pexec(4)` lifecycle: load once, re-exec many times, free explicitly. Useful for iterative debugging without re-reading a slow file off SD each cycle. |

The `runner adv` family mirrors the foreground verbs through the VBL ISR: `runner adv status`, `runner adv meminfo`, `runner adv jump ADDR`, `runner adv load REMOTE`. The two `jump` / `load` advanced verbs require the default `vbl ($70)` hook because they rewrite the saved PC on the supervisor stack.

## 🐞 Debug traces

The m68k emits debug bytes through indexed memory reads at `0xFBFF00`–`0xFBFFFF`. The cartridge address bus carries the byte value, the firmware captures it and streams it to either an HTTP chunked transfer endpoint or USB CDC simultaneously. There is no framing and no overhead, just byte-exact transport.

```c
// Send the character 'A' through the debug channel.
#define CARTRIDGE_DEBUG 0xFBFF00ul
*((volatile char *)(CARTRIDGE_DEBUG + 'A'));
```

The ring buffer tracks dropped bytes when consumers drain too slowly. Two consumers can read the same stream at the same time:

```sh
$ sidecart debug log         # HTTP long-poll, tail -f style
```

Or open the USB CDC serial port that the Pico W exposes when you plug it into your workstation. No drivers needed on macOS; Linux usually picks it up as `/dev/ttyACM0`; Windows installs a CDC driver automatically.

## 🛠️ Setting up the development environment

This project is based on the [SidecarTridge Multi-device Microfirmware App Template](https://github.com/sidecartridge/md-microfirmware-template).

To set up the development environment, follow the instructions in the [Programming Guide](/sidecartridge-multidevice/programming/) and in the [GitHub repository](https://github.com/sidecartridge/md-devops).

Building requires the ARM GNU 14.2 toolchain plus Docker-based m68k compilation; standalone m68k builds run via `target/atarist/build.sh`.

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.
See the [LICENSE](https://github.com/sidecartridge/md-devops/blob/main/LICENSE) file for full terms.

## 🤝 Contributing

Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: Oric Emulator](/sidecartridge-multidevice/microfirmwares/oric-emulator/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Architecture and Design](/sidecartridge-multidevice/architecture_and_design/){: .btn }
