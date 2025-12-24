---
layout: default
title: Troubleshooting
nav_order: 9
nav_exclude: false
parent: SidecarTridge Kickstart
---

# Troubleshooting
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Hardware issues

### The `ROMEMUL` volume is not recognized by the host computer when the device is connected to a USB power source

First, confirm whether the problem is the USB connection or the SidecarTridge Kickstart board:

#### Check the USB connection

Verify that the cable is correctly connected to the SidecarTridge Kickstart board and the USB power source. Try a different USB port, USB cable, or power brick to rule out bad hardware.

**We cannot stress enough the importance of using a good quality USB <u>data transfering</u> cable.**

#### Enter BOOTSEL mode

If the device still won’t show `ROMEMUL`, force BOOTSEL mode (firmware flashing mode on RP2040/RP2350):

1. Hold down `RESET` on the SidecarTridge Kickstart ROM board.
2. While holding `RESET`, press and hold `BOOT`.
3. Release `RESET`.
4. Release `BOOT`.

Alternative method:

1. Unplug the USB cable.
2. Hold the `BOOT` button.
3. Plug in the USB cable.
4. Release the `BOOT` button.

If the `RP2350` volume does not appear, re-check the USB connection. If it appears, reinstall the firmware following the [Firmware Installation](/sidecartridge-kickstart/getting-started/#firmware-installation) steps.

### The `ROMEMUL` volume is not recognized when the board is powered by the Amiga

When powered from the Amiga, the emulator boots straight into Kickstart emulation and is not exposed as mass storage. Power off the Amiga before connecting the USB cable so the board enters USB mass storage mode.

### Kickstart images copied from the host are not recognized or stored correctly

Host OSes cache writes to removable media. Always **eject the SidecarTridge Kickstart volume after copying** Kickstart or custom ROM images.

### The SidecarTridge Kickstart board does not respond to the RESET button

Verify whether the board enters BOOTSEL mode using the steps above. If it does, try pressing `RESET` again. If not, clean the button with isopropyl alcohol (IPA) and press it repeatedly while wet to clear debris.

### The SidecarTridge Kickstart board does not respond to the BOOT button

If BOOTSEL mode cannot be entered, clean the BOOT button with IPA using the same method as above.

## Amiga issues

### The Amiga does not boot when the SidecarTridge Kickstart emulator is connected

Check these items:

1. Start with a known-good Kickstart 1.3 image (recommended first validation ROM).
2. Set `DEFAULT.TXT` to the exact filename (including extension) of the image you want to boot.
3. Verify the Kickstart image is correctly copied to the device.
4. After any change on the volume, eject it from the host to trigger reindexing.

### The Amiga boots with a black screen or garbage

Some USB cables can assert signals that interfere with the emulator. Fully unplug the USB cable from the SidecarTridge Kickstart board and try again.

## SWITCHER issues

### The SWITCHER program returns an error when reading available images

Ensure the SWITCHER version matches your firmware. SWITCHER is included in the `ROMEMUL` volume; if you updated the firmware, copy the matching SWITCHER from the device.

### The SWITCHER program hangs while loading images

Disconnect the USB cable. Certain USB cables can interfere with the emulator while SWITCHER is running on the Amiga.

### Cannot upload images with names longer than 8.3 characters

SWITCHER supports filenames up to 64 characters, but AmigaDOS limits filenames to 8.3. To upload long filenames, use USB mass storage mode and copy the images directly to `ROMEMUL` from a host computer.

## Kickstart images and volume copying/transferring issues

### Images copied via USB do not appear in SWITCHER

Eject the USB volume after copying. Ejection triggers reindexing so SWITCHER can see the new images.

### Images copied from the Amiga via SWITCHER show old USB-copied entries

SWITCHER refreshes the index after uploads/deletes from the Amiga, including images previously copied over USB and not yet reindexed.

### Manually editing `DEFAULT.TXT` and `RESCUE.TXT` has no effect

After editing, save the files and eject the USB volume to trigger reindexing.

### After editing `DEFAULT.TXT` and `RESCUE.TXT`, the first image is selected instead

Check that filenames (including extension) are correct, ≤64 characters, and exactly match files on the volume.

## Errors ejecting / unmounting the `ROMEMUL` volume

Errors when ejecting or unmounting prevent image changes from being recognized. Common fixes:

### The host returns an error when ejecting/unmounting

Close any programs accessing the volume and try again. Also check:

1. **Third-party tools and drivers**: Antivirus or utilities may create hidden files and metadata. Disable/quit them temporarily.
2. **USB-C cables**: Use a data-capable cable; charge-only cables cause issues.
3. **USB hubs**: Try a direct connection or a different hub/port.

### Can't change the RESCUE or DEFAULT/ACTIVE images from the host computer

The DEFAULT/ACTIVE image can be changed from SWITCHER. The RESCUE image is set in `RESCUE.TXT` to protect against bad images and is not changeable from SWITCHER. To change it, edit `RESCUE.TXT` on `ROMEMUL` (filename only), then:

#### 🛠 How to change the RESCUE image

1. **Connect** the device to your PC via USB.
2. **Edit** `RESCUE.TXT` with the exact filename of the new rescue image (e.g., `KS13.IMG`).
3. **Wait** about a minute so the OS flushes writes (or run `sync` on macOS/Linux).
4. **Unplug** the USB cable directly — do not eject/unmount first. This keeps reindexing from running yet.
5. **Boot your Amiga** and launch SWITCHER.
6. The old RESCUE marker may still show — that is expected.
7. **Select the new image** (matching `RESCUE.TXT`) and **rename it to exactly the same name**. This confirms and activates the RESCUE flag.
8. The new image should now appear with the RESCUE tag assigned.

### The `ROMEMUL` volume is not remounted after ejecting

By default the volume will not auto-remount immediately. Power-cycle the device to mount it again. To auto-remount after eject:

1. Connect the SidecarTridge Kickstart to your computer via USB.
2. Open the `ROMEMUL` volume.
3. Create a file named `REBOOT` in the root of the volume.
4. Eject the `ROMEMUL` volume.

The device will remount the volume automatically after a few seconds.

[Previous: DiagROM Diagnostics](/sidecartridge-kickstart/diagrom/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: FAQ](/sidecartridge-kickstart/faq/){: .btn }
