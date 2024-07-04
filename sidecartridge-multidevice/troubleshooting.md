---
layout: default
title: Troubleshooting
nav_exclude: false
parent: SidecarTridge Multi-device
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

### CONFIGURATOR mode crashes with two bombs

This is a [known issue](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/issues/55) commonly occurs on computers with less than 1MB of RAM and/or TOS versions prior to 1.62. A simple solution is to upgrade to a firmware version beyond v0.0.11. For optimal results, use the [newest beta firmware version](https://sidecartridge.com/downloads/) available.

### CONFIGURATOR takes very long to start and stops responding or ask me to reboot the computer or show bombs on the screen

If the CONFIGURATOR takes a long time to start and stops responding, ask for a reboot or show bombs on the screen, it is likely that the microSD card folders contain a large number of files. The CONFIGURATOR reads all the files in the microSD card folders on start. To resolve this issue, you can also disable the file count in the microSD card folders by setting the `FILE_COUNT_ENABLED` parameter to `false`.  To do this, remove the microSD card, power off/on the computer and press the `BUTTON` of the SidecarT to enter the CONFIGURATOR mode. After changing the `FILE_COUNT_ENABLED` parameter, power off the computer, insert the microSD card again and power on the computer.

### Cannot enter into the CONFIGURATOR mode

If you cannot enter into the CONFIGURATOR mode, please check the following:

1. Check that the SidecarT is properly connected to the computer cartridge connector and that the SidecarT is properly powered.
2. Press the RESET button on the SidecarT board and keep it pressed.
3. While keeping the RESET button pressed, press the SELECT button for more than 1 second.
4. Release the RESET button.
5. The SidecarT should now be in the CONFIGURATOR mode. The CONFIGURATOR mode is indicated by the green LED blinking a 'C' in Morse code.

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


### microSD card not detected

If the microSD card is not detected, please check the following:

1. The microSD card is formated as Fat16 or exFAT. Please follow the instructions in the [Format de microSD card](https://docs.sidecartridge.com/sidecartridge-multidevice/how_to/#format-the-microsd-card) section.
2. Check that the microSD card has the correct folders created. Please follow the instructions to [set the folder to host ROM files](/sidecartridge-multidevice/userguide/#set-the-folder-hosting-the-rom-files) and [set the folder to host the floppy disk images](/sidecartridge-multidevice/userguide/#pre-requisite-hosting-floppy-images-on-microsd).
3. Check that the microSD card is properly inserted in the microSD card slot. The microSD card should be inserted with the label facing up. The microSD card should be inserted until it clicks. 
4. Do not power on the SidecarT until the microSD card is properly inserted. If the microSD card is not properly inserted, the SidecarT will not be able to detect it.
5. In the CONFIGURATOR mode, information about the microSD card is displayed at the bottom of the screen with the space available and the number of files in the folders. If the information is not displayed, the SidecarT is not able to detect the microSD card.

## Floppy emulation

### Some floppy disk images are not working. Games/applications are crashing

There are mostly two reasons why some floppy disk images are not working:

1. The floppy emulator "traps" the floppy disk access and redirects it to the microSD card. This is done by a combination of hardware and software. The hardware part is done by the SidecarT board and the software part is done by the firmware. The firmware is responsible for reading the floppy disk images from the microSD card and sending them to the Atari ST. Some applications -mostly games- are using a direct access to the floppy disk controller and bypass the operating system. In this case, the firmware is not able to redirect the floppy disk access to the microSD card. This is why some games/applications are not working. The only solution is to use another floppy disk image. As a workaround, I recommend to try a different version of the game/application from another collection or source.

2. The TOS version of your computer is not compatible with the application/game. In this case, you need to use a different TOS version, or find a version of the application/game compatible with your TOS version.

## Hard disk emulation

### Hard Disk Drive Not Visible in GEM

The hard disk drive is assigned to drive letter `C` (or another letter you've chosen), and it must be in uppercase. If the drive isn't appearing, try the following steps: First, click on any 'Floppy Disk' icon. Next, navigate to the 'Options' menu located at the top of the screen and select 'Install Disk Drive...'. Here, choose the letter `C` (or your specific drive letter), ensuring it's in uppercase. For easier identification, change the `Icon label` to `Hard Disk`. After these adjustments, click on `Install`. You should now see the `Drive C:` (or your specified drive) displayed.

### The hard disk drive letter of the GEMdrive collides with the drive letter of other devices

If the hard disk drive letter of the GEMdrive collides with the drive letter of other devices, you can change the drive letter of the GEMdrive in the configurator. To do this, [follow these steps](/sidecartridge-multidevice/userguide/#hard-disk-emulation). Sometimes the drive letter of other devices cannot be changed, so you must change the drive letter of the GEMdrive.