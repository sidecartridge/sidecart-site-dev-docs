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
- TOC
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
This is a known and random issue with the WiFi module. As a workaround, while you are in the `Configurator` mode and running the `SIDECART.TOS` application, you can try to reset the SidecarT board by pressing the `RESET` button on the board surface. This will reboot the SidecarT, restarting the WiFi module and allowing you to connect to the WiFi network. If this doesn't work, you can try to power off the Atari ST, wait for a few seconds, and power it on again.

