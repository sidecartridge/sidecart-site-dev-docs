---
layout: default
title: MIDI-to-IP
nav_order: 7
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/midi-to-ip
  - /microfirmwares/midi-to-ip/
  - /microfirmwares/midi2ip
  - /microfirmwares/midi2ip/
  - /microfirmwares/md-midi2ip
  - /microfirmwares/md-midi2ip/
  - /sidecartridge-multidevice/microfirmwares/midi2ip
  - /sidecartridge-multidevice/microfirmwares/midi2ip/
  - /sidecartridge-multidevice/microfirmwares/md-midi2ip
  - /sidecartridge-multidevice/microfirmwares/md-midi2ip/
---

# MIDI-to-IP
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-MIDI2IP){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-MIDI2IP/releases){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-MIDI2IP/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_MD_MIDI2IP_VERSION }}](){: .label .label-purple }

**MIDI-to-IP** redirects the Atari ST's MIDI IN and OUT traffic to a network endpoint, so games and tools that talk to the ST's MIDI port can run over Wi-Fi / TCP instead of a real MIDI cable. The firmware hooks the BIOS device-3 calls (`Bconstat` / `Bconin` / `Bconout`) and carries every byte over the cartridge bus to a small Python orchestrator that relays them around a virtual ring. The headline target is **MIDI Maze**, the mid-1980s networked first-person shooter for the Atari ST: with one orchestrator on the LAN, up to 16 STs (real or emulated) play together over IP, without a single MIDI cable in the room.

{: .important }
The README on the [md-MIDI2IP repository](https://github.com/sidecartridge/md-MIDI2IP) is the source of truth for the orchestrator CLI, the wire protocol, and every flag. The page below is a curated overview of the user-facing flow. For deep integration details head to the project's [README on GitHub](https://github.com/sidecartridge/md-MIDI2IP/blob/main/README.md).

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 🕹️ What MIDI-to-IP does

**MIDI Maze** chains up to 16 Atari STs by wiring each machine's MIDI OUT into the next machine's MIDI IN, and the last machine back into the first. The game data circulates around that ring.

```
Physical MIDI Maze ring, up to 16 machines:

   ST 1 ─▶ ST 2 ─▶ ST 3 ─▶ ... ─▶ ST 16
    ▲                              │
    └──────────────────────────────┘
```

MIDI-to-IP recreates that ring **over the network**. Each node's MIDI traffic is carried over Wi-Fi / TCP to a small **orchestrator** that relays it to the next node in the ring. A "node" is either a **real Atari ST + SidecarTridge Multi-device**, or a **Hatari emulator + the bundled gateway script**. Mix them freely, up to 16 in a single ring.

```
MIDI-to-IP: the ring relayed over Wi-Fi / TCP through one orchestrator.

      node ──┐        ┌── node       A "node" is a real Atari ST + SidecarTridge,
             ▼        ▼              or the Hatari emulator + gateway.
           ┌──────────────┐
           │ orchestrator │          It relays each node's MIDI OUT
           └──────────────┘          into the next node's MIDI IN.
             ▲        ▲              (Mix freely, up to 16 in one ring.)
      node ──┘        └── node
```

## 📦 What ships in the repository

| Component | Role | Path | How you run it |
| --- | --- | --- | --- |
| **MIDI-to-IP microfirmware** | RP2040 firmware that hooks BIOS device 3 on the ST and bridges MIDI to the orchestrator | `rp/`, `target/atarist/` | Install from the **Booster** app (below) |
| **Orchestrator** | Python server that relays the ring and serves a live ring view | `orchestrator/orchestrator.py` | `python3 orchestrator/orchestrator.py` |
| **Hatari gateway** | Bridges Hatari's file-based MIDI FIFOs to the orchestrator, so a software node joins the same ring | `hatari-gateway/gateway.py` | `python3 hatari-gateway/gateway.py` |

Both the orchestrator and the Hatari gateway are **Python 3 standard-library** scripts: no `pip install`, no dependencies.

## 🚀 Installation

You can install MIDI-to-IP the same way as any other microfirmware in the catalog.

1. **Launch the Booster App** on your SidecarTridge Multi-device.
2. Open the **Booster web interface** in your browser.
3. Go to the **Apps** tab and select **MIDI-to-IP** from the list.
4. Click **Download** to install the app onto the microSD card.
5. Select the newly installed app and click **Launch**.

If you prefer the manual route (for example, when testing a release that is not yet in the catalog):

1. Download the latest `.uf2` and `.json` files from the [releases page](https://github.com/sidecartridge/md-MIDI2IP/releases).
2. Copy both files to the `/apps` folder of your SidecarTridge microSD card.
3. From the Booster screen press **ESC** to open the app list and select **MIDI-to-IP**.

After launching, MIDI-to-IP boots automatically every time the Atari is powered on, until you switch back to a different microfirmware from the Booster.

## 🛰️ Start the orchestrator

The orchestrator is the relay every node connects to. Run it on any machine that the STs can reach over the LAN (a laptop, a Raspberry Pi, a small VM):

```sh
python3 orchestrator/orchestrator.py
# defaults: TCP game on 0.0.0.0:5005, HTTP status on :8080

# common options
#   --ws [--ws-port 5006]   also accept WebSocket nodes (see "WebSocket transport")
#   --admin-key <key>       enable the rooms REST API (see "Private rooms")
#   --rooms-file <path>     persist provisioned rooms across restarts
#   --host H  --port P  --http-port P  --inspect  --no-http
```

Open `http://<orchestrator-ip>:8080/` in any browser for the live **ring view**: every connected node is drawn around the ring with its host / IP, transport, and bytes in/out, refreshing every 2 s. A room dropdown picks which ring to watch, and `/lobby` lists every room. `--inspect` logs the decoded MIDI Maze protocol as it passes. `--no-http` drops the status page (which rules out any status-poll jitter on the lock-step ring).

## 🕹️ Bring up a real Atari ST node

1. Install and launch MIDI-to-IP from the Booster (see [Installation](#-installation)). Make sure Wi-Fi is already configured for the device (via the Booster / global config — see the [Multi-device getting started](/sidecartridge-multidevice/getting_started_v2/) guide).
2. On boot, the MIDI-to-IP menu shows a countdown plus the current Wi-Fi link status, the local IP, and the orchestrator status.
3. Set the endpoint:
    - Press **`[H]ost`** and type the orchestrator's IP address or hostname.
    - Press **`[P]ort`** and type its port (default `5005`). It edits the port for the **currently selected transport**, so the TCP port and the WebSocket port are remembered separately.
    - Press **`[T]ransport`** to cycle between `tcp` and `ws`. See [WebSocket transport](#-websocket-transport) for when to pick `ws`.
    - Press **`[R]oom`** to set a private room key. Leave it empty to join the default ring. See [Private rooms](#-private-rooms).
    - The host, port, transport, and room are written to the app's local config and **persist across reboots**. Once it is set, the cartridge boots straight into the ring.
4. Press **`[E]xit to GEM`** to launch the MIDI firmware now, or let the countdown finish and it auto-launches. **`[X] Booster`** returns to the Booster.
5. From GEM, run **MIDI Maze** as usual. The cartridge's BIOS device-3 hook now carries the ST's MIDI traffic over the network instead of through the MIDI ports.

## 🖥️ Bring up a Hatari node

A Hatari emulator can join the same ring as a real ST. The bundled gateway script bridges Hatari's file-based MIDI FIFOs to the orchestrator.

```sh
# default: orchestrator on 127.0.0.1:5005, FIFOs in /tmp/hatari-midi
python3 hatari-gateway/gateway.py --host <orchestrator-ip> --port 5005

# WebSocket instead of TCP:
python3 hatari-gateway/gateway.py --host <orchestrator-ip> --port 5006 --transport ws

# join a private room:
python3 hatari-gateway/gateway.py --host <orchestrator-ip> --port 5006 --transport ws --room DIEGOROOM
```

The gateway prints the exact Hatari command to run. Launch Hatari with the two MIDI FIFOs:

```sh
hatari --midi-out /tmp/hatari-midi/midi_out.fifo \
       --midi-in  /tmp/hatari-midi/midi_in.fifo  <midimaze program or disk>
```

Start the orchestrator first; the gateway and Hatari can start in either order.

## 🎮 Play a match

MIDI Maze supports **up to 16 players** in one ring. To put a session together:

1. Start the orchestrator on a machine the others can reach over the LAN.
2. Bring up each participant pointed at that orchestrator's IP. Mix **real ST + SidecarTridge** nodes and **Hatari + gateway** nodes freely in the same ring.
3. To play in a private group, give every participant the **same room key** (see [Private rooms](#-private-rooms)). Otherwise they all share the default ring.
4. Open `http://<orchestrator-ip>:8080/` and pick the room from the dropdown. Every node should appear around the ring.
5. In MIDI Maze, run the master-election / count-players flow as usual and start the match. All nodes now play over IP.

## 🌐 WebSocket transport

By default a node reaches the orchestrator over a plain **TCP** socket on port 5005. A node can instead use **WebSocket**, which rides a standard HTTP port and an Upgrade handshake, so it can pass an HTTP reverse proxy (nginx, Cloudflare, a PaaS load balancer) or a firewall that only allows web ports. The MIDI bytes are identical; WebSocket only wraps the carrier. TCP and WebSocket nodes share the same ring, so you can mix them.

Enable it on each side:

- **Orchestrator:** add `--ws` (and optionally `--ws-port`, default 5006). Both listeners run at once.
  ```sh
  python3 orchestrator/orchestrator.py --ws
  # TCP :5005, WebSocket :5006, HTTP :8080
  ```
- **Real Atari ST node:** in the boot menu press **`[T]ransport`** to cycle `tcp` / `ws`. Each carrier keeps its own port, so **`[P]ort`** edits the port for the selected transport. The choice persists across reboots.
- **Hatari gateway:** add `--transport ws` and point `--port` at the WebSocket port.
  ```sh
  python3 hatari-gateway/gateway.py --host <orchestrator-ip> --port 5006 --transport ws
  ```

There is **no TLS yet**: `wss` is not supported on the RP2040, so the WebSocket carries clear text. For an exposed deployment, put a TLS-terminating reverse proxy in front of the orchestrator and speak `ws` to it on the internal network.

## 🔒 Private rooms

One orchestrator can host **many independent rings** at once. A **room key** is a short word that selects a private ring: every node that enters the same key plays together, isolated from the other rooms. A node with no key joins a shared **default room** (the original single-ring behavior). Rooms ride the WebSocket carrier (the key travels in the handshake), so a room node uses the `ws` transport.

### Operator: provision the rooms

Start the orchestrator with an admin key, then create rooms over a small REST API on the HTTP port. A join to a room that was not provisioned is refused, so only the rooms you create exist.

```sh
python3 orchestrator/orchestrator.py --ws --admin-key secret --rooms-file rooms.json

# create a named room
curl -X POST http://<orchestrator-ip>:8080/rooms -H "X-Admin-Key: secret" -d '{"key":"DIEGOROOM"}'

# or mint a short auto-generated code
curl -X POST http://<orchestrator-ip>:8080/rooms -H "X-Admin-Key: secret"

# list rooms / delete a room
curl http://<orchestrator-ip>:8080/rooms
curl -X DELETE http://<orchestrator-ip>:8080/rooms/DIEGOROOM -H "X-Admin-Key: secret"
```

`--rooms-file` keeps the provisioned rooms across restarts. An empty room is reclaimed after `--room-ttl` seconds (default 600); the default room is never reclaimed. Each ring caps at the MIDI Maze limit of 16 players.

### Player: enter the room key

- **Real Atari ST node:** set `[T]ransport` to `ws`, then press **`[R]oom`** and type the key (for example `DIEGOROOM`). It persists across reboots; leave it empty for the default room.
- **Hatari gateway:** add `--transport ws --room DIEGOROOM` to the gateway command.
  ```sh
  python3 hatari-gateway/gateway.py --host <orchestrator-ip> --port 5006 --transport ws --room DIEGOROOM
  ```

### Watch a room

The ring view at `http://<orchestrator-ip>:8080/` has a room dropdown and highlights the master node. `http://<orchestrator-ip>:8080/lobby` lists every room with its player count and game phase, each link jumping into that room's ring. `http://<orchestrator-ip>:8080/?room=DIEGOROOM` opens straight into a room.

A room key gates a ring; it is not a password for the traffic. Without TLS it travels in clear text, so use a reverse proxy for TLS and to guard the admin REST API on an exposed deployment.

## 🧠 Reference project for AI-assisted firmware development

MIDI-to-IP is also a **public reference for AI-assisted SidecarTridge microfirmware development**. Unlike the other microfirmwares in this catalog, its planning backlog lives in the repo at [`docs/epics/`](https://github.com/sidecartridge/md-MIDI2IP/tree/main/docs/epics) and is committed to git as the planning source of truth alongside the code:

- **`STATUS.md`** is a generated cockpit: epics grouped by iteration, with progress percentages driven by the task checkboxes inside each story.
- **`ITERATIONS.md`** carries the per-iteration narrative (goal + outcome).
- **`DECISIONS.md`** records cross-cutting decisions (`D-NN`) and non-functional constraints (`C-NN`) so stories reference them by ID instead of re-arguing the point.
- **`ORCHESTRATOR-CONTRACT.md`** specifies the wire format and ring semantics between the firmware and the orchestrator, the shared interface between the RP2040 side and the Python side.
- **`EPIC-NN-<slug>/`** folders hold an `epic.md` plus its `STORY-NN-<slug>.md` files. Tasks are GitHub-style `- [ ]` / `- [x]` checkboxes inside each story.

If you are building your own microfirmware with an AI coding agent (or want to read how this one was built), the `docs/epics/` folder is a working example of an iteration-driven backlog that an agent can read, update, and ship from end to end.

## 🙏 Acknowledgements

- **Jesús Ángel González Gorrado**: his *Trabajo Fin de Grado* reverse-engineering the MIDI Maze protocol is what made the MIDI-to-IP microfirmware look doable in the first place. [TAZ-TFG-2022-4616.pdf](https://zaguan.unizar.es/record/146840/files/TAZ-TFG-2022-4616.pdf)
- **Markus Fritze ([@sarnau](https://github.com/sarnau))**: author of MIDI Maze II and the [`AtariST-MIDIMaze-Source`](https://github.com/sarnau/AtariST-MIDIMaze-Source) reference, an expert in the MIDI Maze internals and a long-time supporter of the Atari ST scene.

## 📄 License

The source code of MIDI-to-IP is licensed under the GNU General Public License v3.0. The full license is in the [LICENSE](https://github.com/sidecartridge/md-MIDI2IP/blob/main/LICENSE) file in the repository.

[Previous: MD/JS](/sidecartridge-multidevice/microfirmwares/md-js/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Architecture and Design](/sidecartridge-multidevice/architecture_and_design/){: .btn }
