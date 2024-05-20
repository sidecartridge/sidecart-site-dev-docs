---
layout: default
title: Programming SidecarT
nav_order: 7
---

# Programming SidecarT
{: .no_toc }

This section provides developers with in-depth guidance on programming the SidecarT board. It covers the ROM emulation, the asynchronous and synchronous programs and how to develop the firmware and drivers. It also covers deployment procedures, debugging strategies, and optimization techniques. A thorough understanding of these topics is essential for developing efficient, stable, and maintainable software for SidecarT.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Architecture review

Before starting with the programming of the SidecarT board, it is important to understand the two basic ROM emulation modes available and describe in detail in the section [Architecture and Design](/architecture_and_design/#the-sidecart-board-from-the-atari-st-perspective). To summarize the two modes:

- Full ROM emulation mode: the Atari ST effortlessly reads the shared RAM memory as if perusing through a full address range of the ROM memory expansion, void of any perceptible differences. The Atari ST is NOT aware of the existence of the SidecarT.
- Hybrid ROM emulation mode: the Atari ST accesses the shared RAM memory but only a specific subrange of addresses of the ROM memory expansion. The other subranges are allocated to implement a command protocol between the host and the microcontroller, fostering an interactive session with applications running on the RP2040. The Atari ST is aware of the existence of the SidecarT.

## ROM Emulation 101: Full ROM Emulation Mode

{: .important}
Please keep at thand the [Raspberry Pi Pico C/C++ SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf) It will be very useful to understand the code and the explanations in this section.

The full ROM emulation mode is the simplest mode to understand and to use. It is also the most efficient mode in terms of performance. In this mode, the RP2040 microcontroller tries to mimic how a ROM circuit would perform. The PIO features of the RP2040 do the heavy lifting, using the following capabilities:

### The main read and write loop

- The GPIO pins of the RP2040 are configured as inputs and outputs to emulate the address and data buses of the ROM circuit. To do so, the RP2040 uses the PIO state machines to read and write data the signals of the address and data buses at very deterministic and precise time. You can read the PIO code in the file [`romemul.pio`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.pio#L62C1-L95C1) to understand how the PIO state machines are configured. 

{: .warning }
This is a critical section of the ROM emulation code, and any change can have a dramatic impact. If you want to change the ROM emulation code, you should be very familiar with the PIO state machines and the PIO assembler language.

- The DMAs (Direct Memory Access) of the RP2040 are used to read and write data from the shared RAM memory. Once the RP2040 has read the data from the GPIO inputs, it will use a FIFO queue to store the binary representation of the ROM address in a registry of a DMA instance to access the equivalent address in the shared RAM memory. The code to configure the DMA read address is in the file [`romemul.c`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.c#L156C1-L170C15).

- Once we have the DMA read address configured, we can start the DMA read operation. The DMA will read the data from the shared RAM memory and store it in another FIFO queue connected to the PIO state machine. The code to start the DMA read operation is in the file [`romemul.c`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.c#L138C1-L154C16).

- The PIO state machine will read the data from the FIFO queue, will change the direction of the GPIO inputs to outputs, and write it to the now GPIO outputs. The code to read the data from the FIFO queue and write it to the GPIO outputs is in the file [`romemul.pio`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.pio#L96C1-L123C6). The PIO code will maintain in the data bus the information until the !ROMx signals changes from `ACTIVE` to `INACTIVE`.

### Monitoring the changes in the !ROMx signals

The code must monitor constantly when the !ROMx signals change from `INACTIVE` to `ACTIVE` and vice versa. The code to monitor the changes in the !ROMx signals is in the file [`romemul.pio`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.pio#L42C1-L60C1) and it uses the PIO state machines to detect the changes in the !ROMx signals. When the !ROMx signals change from `INACTIVE` to `ACTIVE`, the code will raise an interrupt to inform to the main loop in `romemul_read` that the Atari ST is trying to read data from the ROM memory expansion.

It's guaranteed that no access to ROM3 or ROM4 will ever happen concurrently. So the main loop only needs to read the address and write the data to the bus mantaining the signals in the bus enough time for the Atari ST to read the data.

### Orchestrating the access to the read and write bus

It's critical to guarantee that never at any single time the RP2040 tries to access the address and data bus at the same time. To do so, we have a little state machine of four states (READ_WRITE, NOT_READ_WRITE, READ_NOT_WRITE, NOT_READ_NOT_WRITE) to enable the access to the bus or keeping it in high impedance (see the section [Hardware interface](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.pio#L42C1-L60C1)).

The PIO code uses this state machine as a side-set to enable the access to the bus. It's the references to the state machine at the right side of the assembly instructions.

### Initializing the ROM emulation

In the [`main.c`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/main/romemul/main.c) is where the full Emulation initializes. The code is:

```c
    // Canonical way to initialize the ROM emulator:
    // No IRQ handler callbacks, copy the FLASH ROMs to RAM, and start the state machine
    init_romemul(NULL, NULL, true);
    while (true)
    {
        tight_loop_contents();
    }
``` 

The function `init_romemul` initializes the ROM emulation. The first two parameters are the IRQ handler callbacks. In this case, we don't need any IRQ handler callbacks, so we pass `NULL` as the value of the parameters (we will need these parameters for the Hybrid ROM emulation mode). The third parameter is a boolean value to indicate if we want to copy the FLASH ROMs to RAM. In this case, we want to copy the FLASH ROMs to RAM, so we pass `true` as the value of the parameter.

The function `init_romemul` will copy the FLASH ROMs to RAM, and it will start the state machine. The function `tight_loop_contents` will keep the RP2040 in a tight loop, so the RP2040 will be busy all the time.

The `init_romemul` assumes that there is information in the FLASH that must copy to the RAM range of the shared memory with the ROM of the Atari ST. The information in the FLASH is the ROM code and/or data we want our Atari ST to read from the ROM in the cartridge port expansion.

The base address of the FLASH is `XIP_BASE + FLASH_ROM_LOAD_OFFSET`. `XIP_BASE` is the base address of the FLASH, and `FLASH_ROM_LOAD_OFFSET` is the offset where the ROM code and/or data is located in the FLASH. You can read these constants in the file [`constants.c`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/main/romemul/constants.c). The destination address in the RAM is defined by the constant `ROM_IN_RAM_ADDRESS`.

So the ROM emulation code *assumes* that the ROM code and/or data is already located in the FLASH at the address `XIP_BASE + FLASH_ROM_LOAD_OFFSET` before its initialization and it will copy it to the RAM at the address `ROM_IN_RAM_ADDRESS`. Who is responsible for copying the ROM code and/or data to the FLASH? The answer is the `Configurator` program. 

### Memory mapping

The memory mapping of the SidecarT board is defined in the file [`memmap_romemul.id`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/main/romemul/memmap_romemul.ld) and it performs significant changes to the standard memory mapping of a RP2040 application. The memory mapping of the SidecarT board is:
- FLASH: Reduced from the 2MBytes found in the Raspberry Pi Pico W boards to 1916Kbytes.
- RAM: Reduced from the 264KBytes found in the Raspberry Pi Pico W boards to 128Kbytes.
- SCRATCH_X: No changes.
- SCRATCH_Y: No changes.
- CONFIG_FLASH: FLASH memory reserved for the configuration parameters of the SidecarT board. 4Kbytes.
- ROM_IN_RAM: RAM memory reserved for the ROM emulation. 128Kbytes.

If a developer wants to develop software only using 64Kbytes of shared RAM (or ROM_IN_RAM), then it would be possible to modify this file and give back that memory to the general RAM of the RP2040.

### Debugging

It's not easy to debug the PIO section of the code, but it's possible to interrupt the DMA channels with IRQs and read the data from the FIFO queues. The code to do so is in the file [`romemul.c`](https://github.com/sidecartridge/atarist-sidecart-raspberry-pico/blob/d2e7a2183a06a3a33a59dd23e89b5a2de5f59de5/romemul/romemul.c#L27C1-L52C2). To enable these functions, they must be passed as argument in the `init_romemul` function. Example:

```c
  init_romemul(NULL, dma_irq_handler_lookup_callback, true);
```

We will gain access to the read address obtained from the bus, but also to the data read from the shared RAM memory before pushing it to the FIFO to the PIOs.

{: .warning }
Try to reduce to the maximum the number of printing code to the UART. The UART is a very slow peripheral, and it will slow down the execution of the code. Assume that when you are debugging, the code executed will be slower than the code executed in the Atari ST side.

## Extending the ROM Emulation: Hybrid ROM Emulation Mode

## How to write data to the ROM

## The Asynchronous Commands

## The Synchronous Commands

## Writing new firmware on the RP2040 side

## Writing new firmware/drivers on the Atari ST side 

### New firmware/drivers running on the Atari ST RAM

### New firmware/drivers running on the Atari ST ROM

### Example: Writing a RTC driver

