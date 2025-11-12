---
layout: default
title: Before you buy
nav_order: 2
nav_exclude: false
parent: ACSI2STM Hard Disk for Atari ST
---

# Before You Buy

The ACSI2STM Hard Disk device is designed to work with all Atari ST, Mega ST, STe, and Mega STe computers. However, there are some considerations to keep in mind before purchasing the device.

### Bad-DMA issues for Atari STE models

There is a known issue with some Atari STE models that causes the ACSI2STM device to malfunction due to flaw in the design of the DMA chip used in some models. This issue will corrupt the content of the SD card making the content unreadable. The issue is known as the "Bad-DMA" issue and it is present in some Atari STE models. We strongly recommend to check if your Atari STE model is affected by this issue before purchasing the ACSI2STM device. You can find more information about this issue [here](https://www.exxosforum.co.uk/atari/last/DMAfix/index.htm).

There is a new version of the firmware that can be used to avoid the Bad-DMA issue at the price of a much slower performance. You can find more information about this firmware [here](https://github.com/retro16/acsi2stm/blob/stable/doc/tutorial.md).

{: .warning}
The firmware I install in the ACSI2STM devices is the latest stable version but it does not include the Bad-DMA fix. If you want to install the Bad-DMA fix firmware, you must install the PIO firmware version at your own risk.

If you don't want to take the risk of the Bad-DMA issue, the [SidecarTridge MultiDevice](https://sidecartridge.com/products/sidecartridge-multidevice-atari-st/) GEMDRIVE is a good alternative. It cannot be affected by the Bad-DMA issue and it is compatible with all Atari ST models.

### TOS versions supported

The ACSI2STM device has two main modes of operation: the ACSI mode and the GEMDRIVE mode. Not all the TOS versions supports both modes. The ACSI mode is the legacy mode that uses the ACSI protocol to communicate with the Atari ST. The GEMDRIVE mode is the modern mode that traps the GEMDOS calls to access the SD card. 

We have tested the ACSI2STM device with the following TOS versions with the following results:

Here is the data split into a table with the requested columns:

| **TOS Version** | **ACSI Supported**                  | **GEMDRIVE Supported**           |
|------------------|------------------------------------|-----------------------------------|
| TOS 1.00         | HDDriver                           | No             |
| TOS 1.02         | HDDriver                           | No             |
| TOS 1.04         | HDDriver + ICD driver              | Yes            |
| TOS 1.62         | HDDriver + ICD driver              | Yes            |
| TOS 1.62         | HDDriver + ICD driver              | Yes            |
| TOS 2.06         | HDDriver + ICD driver              | Yes            |
| EmuTOS 1.3.0     | Integrated ACSI driver             | Yes            |

If you need support for large size partitions in TOS 1.00 or 1.02, the [SidecarTridge MultiDevice](https://sidecartridge.com/products/sidecartridge-multidevice-atari-st/) GEMDRIVE is a good alternative.

### Creating images for the ACSI mode

If you wan to use the legacy ACSI mode you will need to create images for the ACSI mode, or find already created images. 

Here goes some links with pre-created images for the ACSI mode:
- [2GB Empty Image with ICD Pro driver](http://atarist.sidecartridge.com.s3.amazonaws.com/atari_2gb_empty_ICD.img.zip)
- [Image with ACSI2STM utilities](http://atarist.sidecartridge.com.s3.amazonaws.com/acsi2stm-5.00-hd0.img)
- [Image disk with almost 200 games](http://atarist.sidecartridge.com.s3.amazonaws.com/1GB-GAMES.img.zip)
- [16MB Image with ICD Pro driver](http://joo.kie.sk/?page_id=306) (After installing the image, continue with the partition as explained in this [guide](http://joo.kie.sk/?page_id=306))

Probably the fastest way to burn the images into the SD card is using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

If you want to create your own TOS & DOS compatible images, you should use to [_Atari Hard Disk and File Systems Reference Guide_](http://atarist.sidecartridge.com.s3.amazonaws.com/atari-st-hd-file-systems-ref-guide.pdf) by Jean Louis-Guerin (DrCoolZic).

ICD Pro is a free driver that can be used with ACSI devices. You can download from here: [ICD Pro](http://joo.kie.sk/?page_id=306). Then you can follow the instructions in this [guide](http://joo.kie.sk/?page_id=306).

HDDRIVER is a commercial driver that can be used with ACSI devices. You can download from here: [hddriver.net](https://www.hddriver.net/). You can download a demo version from [here](https://www.hddriver.net/downloads/hddrdemo125_scsi.img).

You can learn more about the different options in the [official documentation](https://github.com/retro16/acsi2stm/blob/stable/doc/compatibility.md).

[Previous: Introduction](/acsi2stm-atari-st/introduction/){: .btn .mr-4 }
[Main](/acsi2stm-atari-st/){: .btn .mr-4 }
[Next: User Guide](/acsi2stm-atari-st/user-guide/){: .btn }
