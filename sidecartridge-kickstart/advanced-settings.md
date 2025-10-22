---
layout: default
title: Advanced Settings
nav_order: 6
nav_exclude: false
parent: SidecarTridge Kickstart

# Advanced Settings
{: .no_toc }


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Overview

The **Advanced Settings** section provides options for configuring the device beyond the basic settings. The device comes configured with a set of default options that should work for all stock computer systems, but there are good reasons to try them:

1. Noisy bus computers: Tweaking the bus timings can help to fix crashes due to bad timing adjusting.
2. Offsetting the CPU clock: Adjusting bus timings can help to improve performance or stability in certain situations where the clock speed of the computer has been degraded.
3. Accelerated computers: Adjusting bus timings can help to improve compatibility with accelerated computers that may have different timing requirements.

## The CONFIG.TXT File

The `CONFIG.TXT` file is a plain text file that contains configuration options for the SidecarTridge ROM Emulator (the ROM Emulator is the custom board soldered on top of the SidecarTridge Kickstart Emulator carrier board). It is located in the root directory of the `ROMEMUL` volume you can find when plugging your device to a PC/Mac/Linux computer.

If you open it with a text editor you will find the following default configuration:
```
; Configure the ROM Emulator to wait 
; X number of ticks to stabilize the address
; signals. Each 'tick' consumes 12.5ns
; For Atari ST/STE/MegaST/MegaSTE a range between
; 2 and 8 is ok.
READ_BUS_TICKS = 4
; Wait to put in the data bus until the signal
; OE is active (active LOW). 0 value means ignore
; the OE signal (the case for Atari ST and Amiga)
; and 1 to wait for the signal to be active low
; This parameter should not affect in the TOS
; and Kickstart Emulators because the signals
; are artificially set to low always
USE_OE = 0
```

## READ_BUS_TICKS

The `READ_BUS_TICKS` parameter controls the number of _ticks_ the ROM Emulator waits to stabilize the address signals before reading from the bus. Each _tick_ consumes 12.5ns. For Amiga 500, Atari ST/STE/MegaST/MegaSTE systems, a value between 2 and 8 is generally acceptable. The 4 value seems to be the sweet spot for most configurations.

Depending on the specific hardware of your system, you may need to experiment with different values to achieve the best stability.

For example, if you are using a system with a noisy bus, you may need to increase the value to 6 or 8 to ensure that the address signals are stable before reading from the bus. 

On the other hand, if you are using a system with an accelerator that reduces the read bus timing, you may be able to decrease the value to 2 or 3.

The range of acceptable values for `READ_BUS_TICKS` are from 0 to 20. Any values outside this range will return to the default value of 4.

My experience with accelerated boards says that it won't work on anything faster than 20-24Mhz. But I encourage you to experiment with different settings to find the optimal configuration for your specific setup. Also, there are a lot of other factors that can affect the stability of an accelerated computer, such as the quality of the power supply, the type of RAM used, and the overall system configuration.

Use at your own risk, and save this page in your bookmarks to refer back to it later. Also, share your findings with the community to help others who may be facing similar issues.

## USE_OE

The `USE_OE` parameter controls whether the ROM Emulator waits for the Output Enable (OE) signal to be active before putting data on the data bus. A value of 0 means to ignore the OE signal (the case for Atari ST and Amiga), while a value of 1 means to wait for the signal to be active low. This parameter should not affect the TOS and Kickstart Emulators because the signals are artificially set to low always.

While this value is not commonly adjusted, it can be useful in certain situations where a custom hardware configuration requires it. Theoretically, setting this value to 1 could improve compatibility with certain hardware setups that rely on the OE signal, but stock Atari and Amiga ROMs don't require it.

{: .warning}
As a kind reminder, ALWAYS eject the `ROMEMUL` volume after making any changes to the files. This will ensure that the changes are correctly saved and reflected in the emulator.

[Previous: User Guide](/sidecartridge-kickstart/user-guide/){: .btn .mr-4 }
[Main](/sidecartridge-kickstart/){: .btn .mr-4 }
[Next: Compatibility](/sidecartridge-kickstart/compatibility/){: .btn }