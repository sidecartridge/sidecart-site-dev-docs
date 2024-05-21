---
layout: default
title: Introduction
nav_order: 1
nav_exclude: true
---

# Introduction
{: .no_toc }

The first chapter provides an overview of the SidecarTridge TOS emulator board. The goal is to give readers a concise understanding of what the device entails and what it seeks to achieve.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Overview

The SidecarTridge TOS emulator is an innovative solution designed to enhance the functionality and flexibility of the Atari ST series of computers. By leveraging bit-banged emulation, the SidecarTridge TOS emulator replicates the internal ROMs of the Atari ST, allowing users to access and run any TOS (The Operating System) version without the need to physically swap ROM chips. This advanced capability extends to the use of custom ROMs, including EmuTOS, an open-source TOS replacement.

The compact design of the SidecarTridge TOS emulator ensures a seamless integration into the Atari ST, with dimensions of just 5cm x 2cm x 0.7cm. It fits perfectly inside the Atari ST case, powered directly by the 5V rail, and communicates with the internal Atari ST bus to deliver necessary signals transparently to the motherboard. This means the Atari ST operates as usual, with no modifications required other than replacing the original ROM chips with the emulator.

The SidecarTridge TOS emulator simplifies the process of installing and switching between different TOS versions. Users can easily connect the emulator to a computer via USB, transfer TOS image files, and select the desired version through a simple program on the Atari ST. This user-friendly approach eliminates the hassle of manual ROM swapping, providing a more efficient and versatile experience for both developers and enthusiasts.

Key benefits of the SidecarTridge TOS emulator include:

- **Enhanced Flexibility**: Ability to run any TOS version or custom ROMs without physical ROM swaps.
- **Compact and Seamless Integration**: Fits inside the Atari ST case and operates transparently with the motherboard.
- **User-Friendly Setup**: Easy installation and configuration through USB connection and software interface.

In summary, the SidecarTridge TOS emulator is a powerful tool that modernizes the Atari ST, making it easier to explore, develop, and enjoy the wide range of TOS versions and custom ROMs available.

## Purpose and Objectives

### Purpose

The primary purpose of the SidecarTridge TOS emulator is to **provide Atari ST users with a versatile and modern solution for managing and utilizing various TOS versions and custom ROMs**. By eliminating the need for physical ROM swaps, the emulator addresses one of the main problems when considering upgrading the TOS, making it easier to switch between different operating systems and experiment with custom firmware.

### Objectives

The SidecarTridge TOS emulator aims to achieve several key objectives:

1. **Simplify TOS Management**: 
   - Provide a straightforward method for loading and switching between different TOS versions without opening the Atari ST case or handling physical ROM chips.
   
2. **Enable Custom ROM Usage**:
   - Support the loading and execution of custom ROMs, such as EmuTOS, allowing users to explore and utilize alternative and open-source operating systems.
   
3. **Maintain Seamless Integration**:
   - Ensure that the emulator integrates seamlessly with the Atari ST hardware, operating transparently without requiring significant modifications to the original system.
   
4. **Enhance User Convenience**:
   - Offer a compact, easy-to-install solution that fits within the existing Atari ST case and can be managed through a simple USB connection and software interface.
   
5. **Promote Preservation and Experimentation**:
   - Encourage the preservation of Atari ST systems by providing a modern tool for managing legacy software and support for new experimental and custom ROM development.
   
6. **Provide a Reliable and Robust Solution**:
   - Deliver a high-quality product that meets the needs of both casual users and technical enthusiasts, ensuring reliability and robustness in various use cases.

In summary, the SidecarTridge TOS emulator is designed to make TOS management more efficient and user-friendly while preserving the original functionality and integrity of the Atari ST system. By achieving these objectives, the emulator supports a wide range of users, from those looking to explore different TOS versions to developers working on custom firmware projects.

## Features and Benefits

### Features

1. **Bit-Banged Emulation**:
   - Leveraging the powerful Programmable Input Output (PIO) features of the Raspberry RP2040, the SidecarTridge TOS emulator emulates the internal ROMs of the Atari ST series through bit-banged emulation, eliminating the need for custom firmware or complex hardware.

2. **Multi-TOS Version Support**:
   - With 16MB of flash memory, the SidecarTridge TOS emulator allows users to store and access up to 64 different TOS versions without requiring physical ROM swaps.

3. **Custom ROM Support**:
   - The emulator can run any ROM image file, including custom ROMs and open-source TOS replacements like EmuTOS. This enables users to experiment with various firmware options and enhance the functionality of the Atari ST.

4. **Compact Design**:
   - Measuring just 5cm x 2cm x 0.7cm, the emulator fits seamlessly inside the Atari ST case.

5. **Seamless Integration**:
   - Communicates with the Atari ST bus and provides necessary signals to the motherboard without requiring modifications to the computer. Simply replace the original ROM chips with the emulator for use with Atari ST, STE, Mega ST, and Mega STE computers.

6. **USB Connectivity**:
   - Connects to a computer via USB, appearing as a mass storage device for easy ROM file transfer. Users can copy TOS image files to the device, select the desired version, and reboot the Atari ST to apply changes. It works with Windows, macOS, and Linux without needing additional drivers.

7. **User-Friendly Software**:
   - Includes an easy-to-use software interface for selecting and managing TOS versions and custom ROMs directly from the Atari ST computer. This software provides a convenient way to switch between different firmware options.

8. **Transparent Operation**:
   - Ensures the Atari ST boots normally, with the system unaware that the ROM chips have been replaced with the emulator. Power on the Atari ST, and it will boot as usual.

### Benefits

1. **Ease of Use**:
   - Simplifies the process of managing and switching between different TOS versions and custom ROMs, eliminating the need for physical ROM swaps.

2. **Run Any Software**:
   - Provides the ability to run multiple TOS versions and custom firmware, making it perfect for enthusiasts who want to experiment with applications that only run on specific TOS versions or developers who need to test their software on different TOS versions.

3. **Preservation of Original Hardware**:
   - Maintains the integrity of the original Atari ST hardware by fitting inside the case and utilizing existing power and communication pathways.

4. **Convenience**:
   - Offers a plug-and-play solution that is easy to install and manage, reducing complexity for users.

5. **Support for Development and Experimentation**:
   - Enables developers and enthusiasts to experiment with custom ROMs and firmware, fostering innovation and exploration.

6. **Increased Reliability**:
   - Changing ROMs through software rather than physical manipulation reduces the risk of damage to the Atari ST hardware, ensuring long-term reliability.

7. **Cost-Effective Solution**:
   - Eliminates the need for purchasing and swapping multiple ROM chips, providing a more economical way to manage TOS versions.

8. **Future-Proofing**:
   - Supports ongoing development and updates, ensuring the Atari ST remains relevant and functional with the latest software advancements.

By incorporating these features and benefits, the SidecarTridge TOS emulator significantly enhances the usability and versatility of the Atari ST, making it an invaluable tool for enthusiasts, developers, and users seeking to explore the full potential of the system.

## Intended Audience

The SidecarTridge TOS emulator is designed to meet the needs of a diverse range of users, including:

1. **Atari ST Enthusiasts**:
   - Individuals passionate about the Atari ST series who want to enhance their systems with modern capabilities, easily switch between different TOS versions, and experiment with custom ROMs.

2. **Developers**:
   - Software developers looking to test their applications across various TOS versions and custom firmware without relaying on software emulators.

3. **Retro Computing Hobbyists**:
   - Hobbyists dedicated to preserving and exploring retro computing systems. The emulator offers a convenient and non-invasive way to run and experiment with different operating systems on their Atari ST machines.

4. **Retro Computing Repair shops**:
   - Professionals providing support and repair services for vintage Atari ST computers. The emulator allows for quick and easy testing of different TOS versions, facilitating troubleshooting and repairs.

The SidecarTridge TOS emulator is an invaluable tool for anyone seeking to maximize the functionality, flexibility, and longevity of their Atari ST computers. Whether you are a developer or enthusiast, the emulator provides a powerful and user-friendly solution for managing and exploring the wide range of TOS versions and custom ROMs available.

## Project Background

The development of the SidecarTridge TOS emulator originated from a need identified during the creation of the SidecarTridge multi-device cartridge. One of the significant challenges encountered was testing firmware across different TOS versions. Existing software solutions often proved unreliable, leading to a cumbersome and inefficient testing process.

Frustrated by the limitations of software-based testing, I decided to develop a hardware solution that could emulate the ROMs at the signal level. This led to the creation of the SidecarTridge TOS emulator, a device designed to replicate the functionality of the venerable 27C256 ROMs (and their equivalents) used in the Atari ST.

By leveraging the bit-banged emulation capabilities, the SidecarTridge TOS emulator provides a reliable and effective means of testing and running different TOS versions. This innovation not only addressed the initial testing challenges but also opened up new possibilities for managing and utilizing various TOS versions and custom ROMs with ease.

The SidecarTridge TOS emulator embodies a solution that combines modern technology with the classic Atari ST hardware, providing users with a versatile and efficient tool for enhancing their retro computing experience.

## Key Components

The SidecarTridge TOS emulator comprises several key components, each playing a vital role in its functionality and ease of use. Below is a list and description of the main components:

1. **SidecarTridge ROM Emulator Board**:
   - This is the core of the SidecarTridge TOS emulator. It leverages the Programmable Input Output (PIO) features of the Raspberry RP2040 to emulate a ROM chip at the signal level. This board houses the necessary circuitry and flash memory to store multiple custom ROMs, provides the interface for USB connectivity, and communicates with the Atari ST bus through  TTL (5 volts)to CMOS (3.3 Volts) bus level shifters.

2. **SidecarTridge Atari ST Model Carrier Board**:
   - The carrier board is designed to fit seamlessly into various models of the Atari ST series, including the ST, STE, Mega ST, and Mega STE. It connects the ROM emulator board to the Atari ST bus, allowing the emulator to communicate with the motherboard and provide the necessary signals transparently. The current versions of the carriers boards are designed to fit the Atari ST, STE, Mega ST, and Mega STE models with 2 ROM sockets, but a six ROM socket version is in development.

3. **USB Cable**:
   - A standard USB-C cable is needed to connect the SidecarTridge ROM emulator board to a computer. This connection is used for transferring TOS image files and custom ROMs to the emulator, making it appear as a mass storage device for easy file management. The USB cable also provides power to the emulator during the firmware update process and file transfer.

4. **RESCUE connector**:
   - The RESCUE connector is a crucial accessory for troubleshooting and recovery. In case of any issues with a new ROM image, the RESCUE cable can be used to restore the system to a known good TOS version, ensuring the Atari ST can boot correctly and reliably.

These components work together to provide a seamless and user-friendly experience, enabling users to manage and switch between different TOS versions and custom ROMs with ease. The SidecarTridge TOS emulator offers a modern and efficient solution for enhancing the capabilities of the Atari ST series computers.

## How It Works

The SidecarTridge TOS emulator operates through a combination of advanced hardware and software techniques, replicating the functionality of the original Atari ST ROMs at the signal level. This section explains the technical aspects of how the emulator functions, including bit-banged emulation and interaction with the Atari ST bus.

### Bit-Banged Emulation

1. **Programmable Input Output (PIO) of the Raspberry RP2040**:
   - The emulator leverages the PIO capabilities of the Raspberry RP2040 microcontroller. This technology allows precise control over the timing and sequencing of signals, enabling the emulator to mimic the behavior of the original 27C256 ROMs (and their equivalents) used in Atari ST computers. The PIO provides the necessary flexibility and accuracy to emulate the ROMs effectively, even at frequencies up to 16MHz in the MegaSTE model.

2. **Signal Level Emulation**:
   - Bit-banging refers to the technique of manually driving the signals that would typically be handled by dedicated hardware. In this context, the emulator generates the necessary address and data signals to fully emulate the ROM chips. This involves coordinating the timing of these signals to match the original ROM's behavior precisely.

### Flash Memory Storage

1. **USB Interface for ROM Management**:
   - Users can connect the emulator to a computer via USB to manage ROM files. The emulator appears as a FAT16 mass storage device, allowing users to easily copy TOS image files and custom ROMs. This USB interface simplifies the process of updating and switching ROMs without physically interacting with the Atari ST’s internals. The file system has been enhanced to provide information about the status of the emulator and the installed ROMs, as well as the ability to modify the default and rescue ROMs.

### Hot Swapping the ROMs from the Atari ST

1. **Software Control**:
   - A user-friendly software interface is provided for managing the ROMs. Users can select the desired TOS version or custom ROM from the Atari ST itself, making the process of switching ROMs as simple as launching a program, selecting the TOS, and rebooting the system.

2. **Boot Process**:
   - When powering the computer on, the SidecarTridge TOS emulator is already active and ready to provide the necessary ROM signals to the Atari ST. The computer boots as usual, unaware that the ROM chips have been replaced with the emulator. There is no need to modify the Atari ST hardware or perform any additional steps to enable the emulator.

### Developing and Testing Custom ROMs

1. **Custom ROM Support**:
   - A simple API will be provided to allow developers to create their own software to upload ROMs from the Atari ST computers themselves.

By incorporating these technical elements, the SidecarTridge TOS emulator provides a robust and flexible solution for managing and running different TOS versions and custom ROMs on the Atari ST series, enhancing the usability and functionality of these classic computers.


[Previous: Index](/sidecartridge-tos)
{: .btn .btn-purple .fs-5 .mb-4 .mt-4 style="color: white;"}
[Next: Before You Buy](/sidecartridge-tos/before-buy/)
{: .btn .btn-purple .fs-5 .mb-4 .mt-4 style="color: white;"}
