---
layout: default
title: Frequently Asked Questions
nav_order: 6
nav_exclude: false
parent: ACSI2STM Hard Disk for Atari ST
---

# Frequently Asked Questions
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

### What is the difference between GEMDRIVE and ACSI modes?

- **GEMDRIVE Mode**: Allows easy file transfers between Atari and modern PCs using FAT16, FAT32, or ExFAT formatted SD cards. No additional drivers are needed.  
- **ACSI Mode**: Emulates a traditional ACSI hard drive, supporting legacy Atari software with custom partitions. Requires Atari hard disk drivers like HDDRIVER or ICD Pro.  

Choose **GEMDRIVE** for convenience and modern workflows, and **ACSI** for full compatibility with vintage software.

### What slots support ACSI mode?

Depends on the TOS version.

#### EMUTOS and TOS 2.0x

Only the leftmost slot labeled SD0 (C: / L:) is available for ACSI mode.

#### Other TOS versions

These TOS versions can execute the embedded GEMDRIVE driver. These driver can change the order of the GEMDRIVE and ACSI units.

### Why can't see GEMDRIVE units in EmuTOS and TOS 2.0x?

To use GEMDRIVE units under EmuTOS and TOS 2.0x you must ensure that the **GEMDRIVE.PRG** driver is executed at boot time. This driver is included firmware package of the project in the **tools** folder of the [release package](https://github.com/retro16/acsi2stm/releases/tag/5.00).

### Why do I need a USB-C cable?

The ACSI2STM requires a USB-C cable to power the device because it cannot draw enough power from the Atari's ACSI port. The USB-C cable should be connected to a USB power source, such as a computer, USB charger, SidecarTridge Multi-device, or a USB power bank.

### Can I use the ACSI2STM with SidecarTridge Multi-device?

Yes, the ACSI2STM is compatible with the SidecarTridge Multi-device, allowing you to connect multiple devices to your Atari simultaneously. The SidecarTridge Multi-device can power the ACSI2STM using its USB-C port, simplifying the setup and reducing cable clutter.

### My Atari STE suffer from the Bad-DMA issue. Can I use the ACSI2STM?

The latest firmware of the ACSI2STM includes a workaround for the Bad-DMA issue on Atari STE computers called PIO mode. You must enable this mode by following the instructions in the documentation. PIO mode may reduce the performance of the ACSI2STM by a factor of 10, but it ensures compatibility with Atari STE computers affected by the Bad-DMA issue.

### Can I upgrade the firmware of the ACSI2STM from the Atari itself?

Yes, the latest firmware of the ACSI2STM can be updated directly from the Atari using the firmware update utility. This feature ensures that you can benefit from future enhancements and bug fixes without needing additional hardware or tools.

### What is the difference between the GEMDRIVE in the ACSI2STM and the SidecarTridge Multi-device?

Both drink from the sources of the Hatari emulator. The GEMDRIVE in the ACSI2STM uses the specific messaging system of the ACSI device to communicate with the Atari, but in the SidecarTridge Multi-device, the GEMDRIVE uses the messaging system implemented over the cartridge port. Both try to bypass the limitations of the Atari ST operating system to access small disk drives. 



[Previous: Troubleshooting](/acsi2stm-atari-st/troubleshooting/){: .btn .mr-4 }
[Main](/acsi2stm-atari-st/){: .btn .mr-4 }
[Next: FAQ](/acsi2stm-atari-st/faq/){: .btn }