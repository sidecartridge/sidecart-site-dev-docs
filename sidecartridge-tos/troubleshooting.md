---
layout: default
title: Troubleshooting
nav_exclude: true
parent: SidecarTridge TOS
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

## Common Issues and Resolutions

{: .warning}
The top issue is the fragmentation of the filesystem. Please read [The Mini-FAT16 Filesystem](/sidecartridge-tos/getting-started/#the-mini-fat16-file-system) first to save headaches later.

### Some of the TOS images are not recognized by the Atari ST

It is possible that the TOS image is not correctly flashed on the SidecarTridge TOS due to fragmentation issues. To solve this issue:

1. copy the TOS images in small batches
2. use the `DEFRAG` command in the SidecarTridge TOS to defragment the filesystem as described in the [Copying TOS image files section](/sidecartridge-tos/getting-started/#copying-tos-image-files) section.
3. verify that the TOS image is correctly flashed on the SidecarTridge TOS. Check the information in the file `INFO.TXT` to see if the TOS image is correctly flashed.
4. Repeat the process until all the TOS images are correctly recognized by the Atari ST.

### The `Sidecartrdg` volume is not recognized by the host computer when the device is connected to a USB power source

Depending on the host computer's operating system and USB port manufacturer it can take more than 10 miliseconds to set the power signals in the USB port. This can cause the device to not be recognized by the host computer. To solve this issue, press the RESET button on the TOS emulator board for a few seconds until the `Sidecartrdg` volume appears on the host computer.

### The `Sidecartrdg` volume is not recognized by the host computer when the device is connected to the Atari ST

If the SidecarTridge TOS takes the power from the Atari ST it will not be recognized by the host computer and the device will start working in the TOS emulator mode and not in the mass storage mode. To solve this issue, double check that your Atari ST is powered off when you connect the SidecarTridge TOS to the Atari ST.

### The Atari ST does not boot when the SidecarTridge TOS is connected

Ensure that the TOS images are correctly flashed on the SidecarTridge TOS:

1. Try first with the default firmware version that comes with the EmuTOS image. It should work out of the box.
2. Open the file 'INFO.TXT' and check if the default TOS image is the one you want to use. Othwerwise, modify the file `DEFAULT.TXT` with the name of the TOS image you want to use.
3. Verify that the TOS image size is correct for your Atari ST model. As a rule of thumb, the TOS image size should be 192KB for ST/STF/STFM models and 256KB for STE/MegaSTE models.
4. Verify that the TOS image is correctly flashed on the SidecarTridge TOS. Check the information in the file `INFO.TXT` to see if the TOS image is correctly flashed.
5. Copy multiple TOS images in a single batch. This will help to avoid fragmentation issues.

Explore the capabilities and limits of the board copying and flashing images in small batches first. This will help you to understand the limitations of the board and the filesystem.

### When I copy a TOS image to the SidecarTridge TOS, the file is not recognized or stored correctly

The host computers implement in the external storage devices a cache mechanism that can cause the file to be stored incorrectly. To solve this issue, eject the SidecarTridge TOS volume ALWAYS from the host computer when you finish copying the TOS images.



[Previous: Compatibility](/sidecartridge-tos/compatibility/){: .btn .mr-4 }
[Main](/sidecartridge-tos/){: .btn .mr-4 }
[Next: FAQ](/sidecartridge-tos/faq/){: .btn }