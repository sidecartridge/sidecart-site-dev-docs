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

{:refdef: style="text-align: center;"}
![Atari 520ST](https://sidecart.xyz/assets/images/quickstart/atari520st.jpeg)
{: refdef}


- A SidecarT board

{:refdef: style="text-align: center;"}
![SidecarT without Raspberry Pi Pico](https://sidecart.xyz/assets/images/quickstart/board-single.png)
{: refdef}


- A [Raspberry Pi Pico WH board](https://www.raspberrypi.com/products/raspberry-pi-pico/?variant=raspberry-pi-pico-wh) to connect it to the SidecarT board. The `W` stands for **Wireless** and the `H` stands for **Header**. The `H` version comes with the header pins already soldered to the board and a JST debugger connector needed to connect the Raspberry Pi Debug Board.

{:refdef: style="text-align: center;"}
![Raspberry Pi Pico WH](https://sidecart.xyz/assets/images/quickstart/raspberry-pi-pico-rp2040-wh.png)
{: refdef}


- A [Raspberry Pi Debug board](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) or an equivalent debug board to connect it to the SidecarT board

{:refdef: style="text-align: center;"}
![Raspberry Pi Pico WH](/assets/images/debug-probe.jpg)
{: refdef}

- A Windows PC, Linux or a Mac with a USB port to connect to the Raspberry Pi Debug board and the Raspberry Pi Pico W board to program it

{: .note }
These prerequisites are considered as a minimum baseline. Being well-versed with the aforementioned technologies and having the required hardware will ensure a seamless initial experience with the SidecarT board.

## Board Assembly
Anyone with the requisite skills can opt to build their own SidecarT board. The schematics needed to assemble the board can be found in the [Github repository](https://github.com/diegoparrilla/atarist-sidecart-raspberry-pico/tree/main/schematics). It provides detailed blueprints to guide users through the assembly process.

However, it is worth noting that acquiring the board through our [online shop](<Insert Shop URL here>) is likely to be both cheaper and more convenient, given the complexities involved in assembling the board.

{: .warning }
Assembling the board independently can be a rewarding and enriching learning experience for those who are interested in a hands-on approach to understanding the intricate workings of the SidecarT board. Obviously, it is not recommended for those who are new to hardware development.

## Initial Setup and Configuration
The Initial Setup and Configuration is a multi-step process aimed at preparing the SidecarT board for use with the Atari ST, STE, or Mega computer. Here’s a summarized version of the [detailed instructions available here](https://sidecart.xyz/quickstart).

<figure class="video_container">
    <iframe
        src="https://www.youtube.com/embed/d1EatFnmPGs?iv_load_policy=3&amp;modestbranding=1&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;enablejsapi=1;loading=lazy"
        allowfullscreen allowtransparency></iframe>
</figure>


{: .important }
It does not matter if you are an experience developer or a novice enthusiast; the above steps are mandatory to get started with the SidecarT board. Please don't skip any of the steps, as it may lead to unexpected results.

