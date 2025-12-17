---
layout: default
title: Troubleshooting
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /troubleshooting_v2
  - /troubleshooting_v2/
---

# Troubleshooting
{: .no_toc }

This section is dedicated to assisting developers in resolving issues encountered while working with the SidecarTridge Multi-device board. It includes common troubleshooting steps, frequently asked questions, and resources for additional support, enabling developers to find solutions and get back to development swiftly.

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
I cannot stress enough how important it is to clean the cartridge connectors on the Atari ST, not only on the Multi-device. The vast majority of issues encountered are related to dirt, flux or poor connectivity due to rust on the connectors.

### Board is detected by the computer but it randomly crashes with different error messages

If your computer randomly crashes with different error messages when the Multi-device is connected, it is likely that the Multi-device is not properly connected to the computer. Please check the following:

- The Multi-device board is properly connected to the Pico W headers.
- The Multi-device board is properly connected to the computer cartridge connector. Please verify that the board is properly inserted and aligned with the cartridge connector.
- The Multi-device board is properly powered. Please verify that the power supply of your computer is working properly. A faulty power supply can cause random crashes and errors.
- The Multi-device board is cartridge connector is clean. Please clean the cartridge connector with isopropyl alcohol.
- The computer cartridge interface is dirty or rusty.

### Board is not detected by the computer

If the Multi-device board is not detected by the computer, please check the following:

1. Connect the Pico WH to your PC/Mac/Linux using a USB data cable. Observe if the green LED blinks during boot-up. If it doesn't, the issue could be with the Pico W.
2. If the LED blinks upon booting, next connect the Pico W to the Multi-device headers and perform the same operation. The green LED should blink in this case too. If it doesn't, there might be a short circuit on the Multi-device board.
3. Lastly, try connecting the Multi-device to the computer. It is highly recommended cleaning the Multi-device cartridge connector with isopropyl alcohol before doing this. If the LED does not blink in this case, there might be a short circuit on the Multi-device board. If the LED blinks, the Multi-device board is working fine and the issue is with the cartridge connector on the computer.


### microSD card not detected

If the microSD card is not detected, please check the following:

1. To use the Multi-device effectively, your microSD card needs to be formatted in FAT32 or exFAT. **We strongly recommend using a high-quality SDHC, SDXC or SDUC microSD from a reputable brand** to ensure optimal performance and reliability. To format the microSD card, you can use the [SD Card Formatter](https://www.sdcard.org/downloads/formatter/) tool available for PC/Mac/Linux.
2. Check that the microSD card is properly inserted in the microSD card slot. The microSD card should be inserted with the label facing up. The microSD card should be inserted until it clicks. 
4. Do not power on the Multi-device until the microSD card is properly inserted. If the microSD card is not properly inserted, the Multi-device will not be able to detect it.
5. In the Booster app, information about the microSD card is displayed at the bottom of the screen with the space available and the number of files in the folders. If the information is not displayed, the Multi-device is not able to detect the microSD card.

## Network issues

### The booster app tries to reconnect to the WiFi network continuously

If the booster app tries to reconnect to the WiFi network continuously, please check the following:

1. You have entered the correct SSID and password in the configurator. Please follow the instructions in the [Initial Factory Configuration](/sidecartridge-multidevice/getting_started_v2/#initial-factory-configuration) section.
2. Your WiFi network does not have any MAC address filtering enabled.
3. Your network is using a 2.4 GHz band. The Multi-device does not support 5 GHz networks.
4. Your WiFi signal is strong enough. If the signal is weak, the Multi-device may have trouble connecting to the network. Try moving the computer closer to the WiFi router or access point.

### Can't connect to the sidecart.local web server

Some networks do not support mDNS, which is used by the Multi-device to resolve the sidecart.local address. If you cannot connect to the sidecart.local web server, please try connecting to the Multi-device using its IP address. You can find the IP address of the Multi-device in the Booster app screen in your Atari ST.

## Restoring factory settings

If you need to restore the factory settings of the Multi-device, you can do it by following these steps:

### Pressing the SELECT button for more than 10 seconds

It does not matter if the Multi-device runs the Booster app or any of the available Microfirmware apps, pressing the SELECT button for more than 10 seconds will restore the factory settings of the Multi-device. 

After powering off and on again, the classic factory settings screen will be displayed, allowing you to reconfigure the Multi-device from scratch as described in the [Initial Factory Configuration](/sidecartridge-multidevice/getting_started_v2/#initial-factory-configuration) section.

If the SELECT button does not work, please try powering on the Atari ST while holding the SELECT button pressed for more than 10 seconds. 

If for any reason the SELECT button does not work, you can reflash the firmware of the Multi-device as described below.

### Reflashing the firmware

If for any reason the above method does not work, you can reflash the firmware of the Multi-device by following the instructions in the [Firmware Update](/sidecartridge-multidevice/getting_started_v2/#firmware-update) section.

### Restore from the Bosster app

In the configuration section of the Booster app, there is an option to restore the factory settings of the Multi-device. After restoring the factory settings, the Multi-device will reboot and the classic factory settings screen will be displayed, allowing you to reconfigure the Multi-device from scratch as described in the [Initial Factory Configuration](/sidecartridge-multidevice/getting_started_v2/#initial-factory-configuration) section.

## Floppy emulation

### Some floppy disk images are not working. Games/applications are crashing

There are mostly two reasons why some floppy disk images are not working:

1. The floppy emulator "traps" the floppy disk access and redirects it to the microSD card. This is done by a combination of hardware and software. The hardware part is done by the Multi-device board and the software part is done by the firmware. The firmware is responsible for reading the floppy disk images from the microSD card and sending them to the Atari ST. Some applications -mostly games- are using a direct access to the floppy disk controller and bypass the operating system. In this case, the firmware is not able to redirect the floppy disk access to the microSD card. This is why some games/applications are not working. The only solution is to use another floppy disk image. As a workaround, I recommend to try a different version of the game/application from another collection or source.

2. The TOS version of your computer is not compatible with the application/game. In this case, you need to use a different TOS version, or find a version of the application/game compatible with your TOS version.

## Hard disk emulation

### Hard Disk Drive Not Visible in GEM

The hard disk drive is assigned to drive letter `C` (or another letter you've chosen), and it must be in uppercase. If the drive isn't appearing, try the following steps: First, click on any 'Floppy Disk' icon. Next, navigate to the 'Options' menu located at the top of the screen and select 'Install Disk Drive...'. Here, choose the letter `C` (or your specific drive letter), ensuring it's in uppercase. For easier identification, change the `Icon label` to `Hard Disk`. After these adjustments, click on `Install`. You should now see the `Drive C:` (or your specified drive) displayed.

### The hard disk drive letter of the GEMdrive collides with the drive letter of other devices

If the hard disk drive letter of the GEMdrive collides with the drive letter of other devices, you can change the drive letter of the GEMdrive in the configurator. To do this, [follow these steps](/sidecartridge-multidevice/userguide/#hard-disk-emulation). Sometimes the drive letter of other devices cannot be changed, so you must change the drive letter of the GEMdrive.

[Previous: Compatibility](/sidecartridge-multidevice/compatibility_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Enclosures](/sidecartridge-multidevice/cases/){: .btn }
