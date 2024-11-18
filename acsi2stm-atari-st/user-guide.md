---
layout: default
title: User Guide
nav_order: 3
nav_exclude: true
parent: ACSI2STM Hard Disk for Atari ST
---

# User Guide
{: .no_toc }

This section provides guidance on the initial steps and daily operation of ACSI2STM Hard Disk for Atari ST. The user guide is divided into the following sections:

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Plugging the device

### Instructions for Connecting the Device to the Atari ST Hard Disk Port

All Atari ST models and their derivatives feature a dedicated **hard disk port**, typically located on the rear of the machine. This port is a **DB19 female socket**, a rare connector type no longer manufactured.

#### Understanding the Hard Disk Port
- Commonly referred to by various names, including **DB19**, **Hard Disk Port**, **ACSI Port**, or **DMA Port**, this connector serves as the primary interface for external storage and peripherals.
- The port functions as a **bus**, allowing multiple devices to share the same connection. To achieve this, devices are typically **daisy-chained**, where each device includes a secondary female port to connect additional devices.

#### Key Considerations

1. **Connector Type:** Since the DB19 connector is no longer in production, the connector is built with a set of pins that match the Atari ST hard disk port.
2. **Clean the connector**: Before connecting the device, ensure that the Atari ST hard disk port is clean and free of dust or debris. This will help establish a secure connection and prevent signal interference.
3. **Alignment:** When connecting the device, ensure that the pins are correctly aligned with the port. Misalignment can cause damage to the pins or the port itself.

By following these guidelines, you can seamlessly connect your device to the Atari ST and leverage its hard disk port for expanded functionality.

#### Modern Alternatives: IDC20 and UltraSatan Connectors

Since **DB19 connectors** are no longer produced and are increasingly difficult to find, modern Atari-compatible hardware often standardizes around **IDC20** (flat cable) connectors. These offer a practical and flexible solution. 

The ACSI2STM version of SidecarTridge does have placeholders for the IDC20 connector and the connector is bundled with the kit, just in case you want to use it.

## The ASCI protocol

### Multiple Devices and ACSI IDs

The Atari ST hard disk interface uses **ACSI** (Atari Computer System Interface), a simplified derivative of the SCSI protocol, to communicate with connected peripherals. This allows for the connection of up to **8 devices** on the same port.

#### Assigning ACSI IDs
- Each device on the ACSI bus is assigned a unique **identifier** (ID), ranging from **0 to 7**. This ID ensures that each device can be addressed independently.
- Most ACSI-compatible peripherals include a selector (e.g., DIP switches or jumpers) to manually set their ID. However, some devices may have limited ID ranges or fixed IDs.

#### Important Rules for ACSI IDs
- **Do Not Assign Duplicate IDs:** Assigning the same ID to multiple devices will cause hardware conflicts. Devices attempting to send signals simultaneously on the bus can overload their internal circuitry, potentially leading to permanent damage.
- **ID Assignment Order:** It is best practice to start assigning IDs from **0** and increase sequentially for additional devices.
- **Software Limitations:** Some software imposes restrictions on supported IDs, so ensure your configuration aligns with your software's requirements.

### Internal Hard Drives in the Mega STE

While most Atari ST models rely solely on external ACSI devices, the **Mega STE** is unique in offering an **internal ACSI hard drive**. This internal drive shares the DMA port with external devices and is set to **ID 0** by default. The ID can, however, be changed using internal DIP switches if required.

### ACSI2STM ID Configuration

The **ACSI2STM** adapter introduces additional flexibility for configuring device IDs:
- It features a set of jumpers labeled **ID_SHIFT**, allowing users to adjust the device IDs of its SD slots.
- These jumpers also affect the mapping of **GemDrive drive letters**.
- **Limitations:** The ACSI2STM cannot freely map to all 8 IDs, so it is essential to consult its documentation for specific ID ranges and configurations.  

By properly managing ACSI IDs and understanding device-specific configurations, you can maximize the compatibility and reliability of your Atari ST setup.

### Device Drivers

Unlike modern systems, **Atari TOS** does not include a fully integrated hard drive driver. This means you cannot simply connect a hard drive and expect the familiar **C:** icon to appear on the GEM desktop automatically.

#### ACSI Drivers: How They Work

When purchasing a hard drive for the Atari ST, users typically received a driver on a floppy disk. The most common driver was Atari’s **AHDI driver**, notorious for its numerous limitations and bugs. In response, third-party companies developed superior alternatives that were more reliable and feature-rich. See the [Before You Buy section](/acsi2stm-atari-st/before-buy.md) for more information.

All these drivers operate on the same basic principle:

1. **Driver File**: A small **TOS/PRG file** serves as the driver. This file is typically placed in the **AUTO** folder on the driver floppy disk.
2. **Tools**: Alongside the driver, the floppy disk includes:
   - A **formatting/partitioning tool**, used to prepare the hard drive.
   - A **boot sector installer**, to make the drive bootable.

The formatting and partitioning tool works much like modern equivalents: format the drive, define partitions, apply the settings, and reboot to finalize. 

{: .warning}
Formatting the a modern SD card with a tool designed 30 years ago can be a daunting task. It is recommended to use a preconfigured image to avoid frustation and time consuming tasks.

#### TOS Issues

Atari TOS has a variety of quirks and bugs. While some of these issues can be mitigated with software patches, no configuration has proven to be fully stable when scaling beyond basic use. Key limitations include:

1. **Size Limitations**:
   - Partition sizes are subject to strict limitations depending on the version of TOS.
   - Tools like **BigDOS** can help alleviate some of these restrictions but require compatible drivers.

2. **Cluster Size Limitations**:
   - Unlike Windows, which scales FAT filesystems by increasing **cluster sizes**, TOS scales them by increasing **physical sector sizes**. 
   - TOS often fails unpredictably when working with FAT filesystems formatted in the Windows style.

3. **Folder Count Limitations**:
   - TOS struggles when managing large numbers of folders, leading to erratic behavior.
   - **FOLDR100.PRG** is a common tool used to increase folder limits, though its success varies.

4. **Lack of File/Folder Caching**:
   - TOS lacks a built-in caching mechanism for files and folders.
   - **CACHE100.PRG** attempts to address this shortcoming by providing rudimentary caching functionality.

5. **Fundamental Instability**:
   - Even with numerous patches and tools, no configuration of TOS has been proven to handle extensive scaling reliably.

ASCI2STM is designed to work with all Atari ST, Mega ST, STe, and Mega STe computers, but it does not behaves the same way with all TOS versions. We strongly recommend to use a device like the [SidecarTridge TOS Emulator](https://sidecartridge.com/products/sidecartridge-tos-atari-st/) to avoid the TOS limitations and change the TOS version on the fly.

## The GEMDRIVE protocol

### GemDrive: High-Level Filesystem Driver

The **GemDrive** protocol enables the Atari ST to read **SD cards** without relying on the ancient and buggy TOS/BIOS filesystem implementation. It operates similarly to the GEMDOS drive functionality in the Hatari emulator, hooking into high-level filesystem calls and implementing them directly on the **STM32** microcontroller using modern SD card libraries.

{: .note}
The GemDrive hard disk emulation of the [SidecarTridge Multidevice](https://sidecartridge.com/products/sidecartridge-multidevice-atari-st/) is a solution that comes from the same roots as the ACSI2STM device: the Hatari emulator. The reaons for each device are different, but share similar goals.

### How to Use GemDrive

1. **Boot Process**:
   - During a cold boot or reset, the **ACSI2STM** scans all SD card slots and determines the mode for each:
     - **ACSI Mode**: Activated if the card contains an ACSI disk image or is Atari bootable.
     - **GemDrive Mode**: Activated for PC-formatted SD cards or empty slots to support hot-swapping.
   - GemDrive always loads via the boot sector of the first slot in GemDrive mode.

2. **Drive Letter Management**:
   - If ACSI mode is active for any slot, GemDrive shifts its drive letters to **L:** to avoid conflicts with ACSI drivers.
   - If no SD card is detected, GemDrive designates the floppy drive or existing boot device as the boot drive.

3. **Behavior**:
   - GemDrive supports hot-swapping SD cards.
   - Only the first partition of the SD card is used to prevent drive letter confusion.

This innovative approach bypasses many of TOS’s limitations, enabling a modern, efficient, and compatible SD card-based storage solution for Atari ST systems.

### Mixing GemDrive with ACSI Drivers and Devices

#### Mixing GemDrive with ICD PRO
To combine **GemDrive** with **ICD PRO**:
- Use only one bootable ICD PRO SD card.
- Insert ICD PRO SD cards after the GemDrive SD cards.
- GemDrive will boot first and assign drive letters starting at **L:**.

**Alternative:** Instead of making the ICD disk bootable, place **ICDBOOT.PRG** in the AUTO folder of the GemDrive SD card.

#### Mixing GemDrive with the PP Driver (ACSID07)
For the **PP driver**:
- Set **ACSI2STM** to start at ACSI ID 0.
- Insert the SD card with the PP driver in the first slot and additional SD cards in other slots.
- The PP driver will load first, and GemDrive will use drive letters starting at **L:**.

#### Mixing GemDrive with Other ACSI Drivers
If GemDrive conflicts with your driver:
- Install **GEMDRIVE.PRG** in the AUTO folder to resolve booting issues.

### Installing EmuTOS with GemDrive

Installing **EmuTOS** with **GemDrive** on the **ACSI2STM** device is a challenging process. Please read the [project documentation for detailed instructions](https://github.com/retro16/acsi2stm/blob/stable/doc/gemdrive.md).

## Firmware Updates

### Updating the Firmware from the Atari ST

Starting from version **4.0**, the **ACSI2STM** allows firmware updates directly from the Atari ST. The process uses the Seagate SCSI standard commands, compatible with both ACSI and GemDrive modes. Follow these steps to update your unit's firmware:

#### **Steps to Update the Firmware**
1. **Prepare the Firmware Files:**
   - Download the release package from the Github Repository and extract its contents.
   - Choose the desired firmware variant (refer to the [documentation for available variants](https://github.com/retro16/acsi2stm/blob/stable/doc/firmware.md)). The version provided by default is the standard firmware: **acsi2stm-VERSION.ino.bin**.
   - Locate the firmware file (e.g., `acsi2stm-VERSION.ino.bin`) and rename it to **HDDFLASH.BIN**. 

2. **Copy the Files to an ST-Compatible Medium:**
   - Copy the following files to a medium accessible by your Atari ST:
     - **HDDFLASH.BIN** (the renamed firmware file).
     - **HDDFLASH.TOS** (the update program).
   - Supported media include:
     - Floppy disks.
     - ACSI drives.
     - GemDrive SD cards.

3. **Run the Update Program:**
   - On your Atari ST, execute **HDDFLASH.TOS**.
   - When prompted, select the hard drive to update (typically **ID 0**).
   - Confirm by pressing **Y** to begin the flashing process.

4. **Reboot After Completion:**
   - Once the update is complete, both the Atari ST and the ACSI2STM unit will automatically restart.

#### **Notes and Tips**

- **Pre-Packaged Disk Images:**  
  The release package includes disk images with a pre-configured **FIRMWARE** folder. This folder contains the standard firmware variant already named **HDDFLASH.BIN**, simplifying the process. Just launch **HDDFLASH.TOS** to begin.

- **Updating Multi-Slot Units:**  
  For ACSI2STM units with multiple SD slots, you only need to update one slot. The firmware update applies to the entire unit, eliminating the need for multiple updates.

- **Running From GemDrive:**  
  If you use **GEMDRIVE.PRG** to load GemDrive, ensure you update this file along with the firmware. An older version of **GEMDRIVE.PRG** may not be compatible with the new firmware.

- **Failsafe Recovery:**  
  If the update fails or the unit becomes unresponsive:
  - Use a USB-to-UART dongle to upload the firmware manually.
  - Refer to the recovery instructions in the documentation.

### Flashing the Firmware to the STM32

If you need to flash the firmware to the STM32 microcontroller, you will need a special USB-to-UART dongle. The process is detailed in the [official documentation](https://github.com/retro16/acsi2stm/blob/stable/doc/quick_start.md#flashing-firmware).


[Previous: Before You Buy](/acsi2stm-atari-st/before-buy.md){: .btn .mr-4 }
[Main](/acsi2stm-atari-st/){: .btn .mr-4 }
[Next: Troubleshooting](/acsi2stm-atari-st/troubleshooting){: .btn }
