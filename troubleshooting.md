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

{: .warning }
I cannot stress enough how important it is to clean the cartridge connectors on the Atari ST, not only on the SidecarT. The vast majority of issues encountered are related to dirt, flux or poor connectivity due to rust on the connectors.

### Board is detected by the computer but it randomly crashes with different error messages

If your computer randomly crashes with different error messages when the SidecarT is connected, it is likely that the SidecarT is not properly connected to the computer. Please check the following:

- The SidecarT board is properly connected to the Pico W headers.
- The SidecarT board is properly connected to the computer cartridge connector. Please verify that the board is properly inserted and aligned with the cartridge connector.
- The SidecarT board is properly powered. Please verify that the power supply of your computer is working properly. A faulty power supply can cause random crashes and errors.
- The SidecarT board is cartridge connector is clean. Please clean the cartridge connector with isopropyl alcohol.
- The computer cartridge interface is dirty or rusty.

### Board is not detected by the computer

If the SidecarT board is not detected by the computer, please check the following:

1. Connect the Pico WH to your PC/Mac/Linux using a USB data cable. Observe if the green LED blinks during boot-up. If it doesn't, the issue could be with the Pico W.
2. If the LED blinks upon booting, next connect the Pico W to the SidecarT headers and perform the same operation. The green LED should blink in this case too. If it doesn't, there might be a short circuit on the SidecarT board.
3. Lastly, try connecting the SidecarT to the computer. It is highly recommended cleaning the SidecarT cartridge connector with isopropyl alcohol before doing this. If the LED does not blink in this case, there might be a short circuit on the SidecarT board. If the LED blinks, the SidecarT board is working fine and the issue is with the cartridge connector on the computer.

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
