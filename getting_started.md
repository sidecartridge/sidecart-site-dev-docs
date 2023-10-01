---
layout: default
title: Getting Started
nav_order: 2
---

# Getting Started
This section provides guidance on the initial steps to start working with the SidecarT board, including prerequisites, board assembly instructions, setup, configuration, and basic troubleshooting. By following the procedures outlined in this section, developers can ensure a smooth start to their journey with the SidecarT board.

## Prerequisites
To begin with the SidecarT board, developers are required to have a minimum experience with C. However, it’s desirable for developers to be proficient in C, 68000 Assembler, Microcontroller development, and have a deep understanding of Atari ST peculiarities. 

Additionally, developers need the following hardware:
- An Atari ST computer series: ST, STE, or Mega
- A SidecarT board
- A [Raspberry Pi Debug board](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) or an equivalent debug board to connect it to the SidecarT board
- A Windows PC, Linux or a Mac with a USB port to connect to the Raspberry Pi Debug board and the Raspberry Pi Pico W board to program it

Note: These prerequisites are considered as a minimum baseline. Being well-versed with the aforementioned technologies and having the required hardware will ensure a seamless initial experience with the SidecarT board.

## Board Assembly
Anyone with the requisite skills can opt to build their own SidecarT board. The schematics needed to assemble the board can be found in the [Github repository](https://github.com/diegoparrilla/atarist-sidecart-raspberry-pico/tree/main/schematics). It provides detailed blueprints to guide users through the assembly process.

However, it is worth noting that acquiring the board through our [online shop](<Insert Shop URL here>) is likely to be both cheaper and more convenient, given the complexities involved in assembling the board.

That being said, assembling the board independently can be a rewarding and enriching learning experience for those who are interested in a hands-on approach to understanding the intricate workings of the SidecarT board.

## Initial Setup and Configuration
The Initial Setup and Configuration is a multi-step process aimed at preparing the SidecarT board for use with the Atari ST, STE, or Mega computer. Here’s a summarized version of the [detailed instructions available here](https://sidecart.xyz/quickstart).

### Step 1: Acquire a SidecarT Board
Acquire a SidecarT board by either purchasing it from the store or by building one yourself. Ensure you have a Raspberry Pi Pico with the necessary 40-pin connectors or a Raspberry Pi Pico WH and a USB A to micro USB data cable.

### Step 2: Install Latest Firmware
Connect your Raspberry Pi Pico to your computer and install the latest firmware available [here](<Insert Link to Firmware>).

### Step 3: (Optional) Prepare microSD Card
Format your microSD card to FAT16. The microSD card is optional but recommended for extended storage.

### Step 4: (Optional) Copy ROM Images
Copy the ROM images to the `/roms` folder on the microSD card or obtain ROM images from a collection.

### Step 5: Connect SidecarT
Connect the SidecarT to the Atari computer, ensuring the Raspberry Pi Pico faces upwards before turning on your computer.

### Step 6: Switch on the Computer
On powering the computer, it starts in CONFIGURATOR mode, where you can set up the specific functions of the SidecarT.

### Step 7: Select ROM and Configure Wi-Fi (if applicable)
Select the ROM to emulate from the microSD card or configure Wi-Fi to fetch ROM images directly from an HTTP server.

### Step 8: Boot the ROM
Reset or power cycle your computer to load the image as a genuine cartridge ROM.

### Bonus: Load a Different ROM
Use the SELECT button on the SidecarT board to reconfigure or load a different ROM.

It does not matter if you are an experience developer or a novice enthusiast; the above steps are mandatory to get started with the SidecarT board. Please don't skip any of the steps, as it may lead to unexpected results.

## Basic Troubleshooting
[In this section, you may want to provide solutions to common problems that developers might encounter when they are getting started with the SidecarT board, as well as guidance on where to seek additional help or resources.]
