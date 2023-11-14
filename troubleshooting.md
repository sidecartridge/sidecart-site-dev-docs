---
layout: default
title: Troubleshooting
---

# Troubleshooting
{: .no_toc }

This section is dedicated to assisting developers in resolving issues encountered while working with the SidecarT board. It includes common troubleshooting steps, frequently asked questions, and resources for additional support, enabling developers to find solutions and get back to development swiftly.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Common Issues and Resolutions

### I can't see the cartridge drive in Configurator mode

The cartridge drive uses the letter `c` in lowercase. If you can't see the `Drive c:` unit, please be sure you are in `Configurator` mode:

1. Press the `SELECT` button to enter the `Configurator` mode for more than 1 second.
2. Power cycle your computer.
3. After boot, you should see the `Drive c:` unit. If you don't see it, do as follows:
   - Click on any other unit (e.g. `FLOPPY DISK` or `HARD DISK`).
   - Open the `Options` menu at the top of the screen.
   - Click on `Install Disk Drive...`.
   - Change `Drive identifier` to `c` **in lower casee**.
   - You should also rename `Icon label` to `Cartridge` or `Cartridge Drive` to make it easier to identify.
   - Finally, click on `Install`. The `Drive c:` unit should now be visible. Open it and click twice on the application `SIDECART.TOS` to run it.


### I get an error message connecting to the WiFi network
This is a known and random issue with the WiFi module. After version v0.0.10 of the firmware, the SidecarT will try to connect to the WiFi network until it succeeds. If you get an error message, please try again. If the problem persists, press the `BUTTON` of the SidecarT.

