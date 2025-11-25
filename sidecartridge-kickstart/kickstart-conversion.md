---
layout: default
title: Amiga Forever Kickstart ROM Conversion Guide
nav_order: 9
nav_exclude: false
parent: SidecarTridge Kickstart

---

#  Amiga Forever Kickstart ROM Conversion Guide
{: .no_toc }

This guide provides step-by-step instructions on how to convert Amiga Forever Kickstart ROM files into a format compatible with the SidecarTridge Kickstart emulator for Commodore Amiga 500/2000. By following these steps, you will be able to create ROM images that can be used with the emulator.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## Prerequisites

Before starting the conversion process, ensure you have purchased the [Amiga Forever Plus Edition](https://www.amigaforever.com/plus/), which includes the necessary Kickstart ROM files. You will also need a computer with internet access and web browser.

## Finding the Kickstart ROM Files in Amiga Forever

The ISO image of Amiga Forever Plus Edition contains the Kickstart ROM files needed for the conversion. Follow these steps to locate the ROM files:

1. Download the Amiga Forever Plus Edition ISO image from the official website.
2. Mount the ISO image on your computer using a virtual drive software. No need to burn it to a physical disc.
3. Navigate to the mounted ISO image to the folder path: `Amiga Files\Shared\rom`.

Inside the `rom` folder, you will find various Kickstart ROM files with the `.rom` extension. You will also find a `rom.key` file that contains the decoding key for the encoded ROM files.

{: .note}
Only the ROM files licensed to Cloanto are encoded and require decoding using the `rom.key` file. Other ROM files are provided in their original format and do not require decoding.

## Converting the Kickstart ROM Files

To convert the Kickstart ROM files into a format compatible with the SidecarTridge Kickstart emulator, simply open the online conversion tool available at [our website](https://sidecartridge.com/assets/html/kickstart-converter.html).

![SidecarTridge Kickstart ROM Converter](/sidecartridge-kickstart/assets/images/kickstart-converter.png)

To begin the conversion process, first drag and drop or select multiple Kickstart ROM files from the Amiga Forever `rom` folder into the conversion tool. Then upload the `rom.key` file by selecting it from the same folder or dragging and dropping it into the designated area in the conversion tool.

Once the files are uploaded press the "DECODE & DOWNLOAD" button. The tool will decode the encoded ROM files using the provided key and package all the converted ROM files into a single ZIP archive for easy download. If any errors occur during the conversion process, they will be displayed in the "Errors" section of the tool. If only one file is uploaded, the tool will provide the converted ROM file directly for download without packaging it into a ZIP archive.

## Next Steps

After downloading the converted Kickstart ROM files, you can proceed to copy them to the SidecarTridge Kickstart emulator's storage. Follow the instructions in the [Getting Started](https://docs.sidecartridge.com/sidecartridge-kickstart/getting-started/) section of the documentation to learn how to transfer the ROM files and configure the emulator for use with your Commodore Amiga 500/2000.

## Compatibility

Make sure to check the [Compatibility](https://docs.sidecartridge.com/sidecartridge-kickstart/compatibility/) section of the documentation to verify that the converted Kickstart ROM files are compatible with your specific Commodore Amiga motherboard model.


[Previous: Before You Buy](/sidecartridge-kickstart/before-buy/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Hardware Installation](/sidecartridge-kickstart/hardware-installation/){: .btn }
