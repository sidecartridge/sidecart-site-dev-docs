---
layout: default
title: Board revisions
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /revisions
  - /revisions/
---

# Board revisions
{: .no_toc }
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

You cand find here information about the different revisions of the SidecarT board. You can find the revision of your board by looking at the silkscreen on the bottom of the board.

## Revision 0: The original

{:refdef: style="text-align: center;"}
![SidecarT revision 0](https://sidecartridge.com/assets/blog/images/sidecart-rev0.png)
{: refdef}


Owners of the SidecarT board before February 2024 have Revision 0, the original model. This version emerged from careful planning and minor modifications to the prototype, aiming for a small-scale production of 25-30 boards. However, demand exceeded expectations. To manage costs, a two-layer PCB was chosen, emphasizing economical shipping and manufacturing. The design also prioritized track width for reliability in electronic environments, and the board size was influenced by the cartridge connector, Pico W dimensions, and PCB design considerations.

## Revision 1: The Hidden Failure

{:refdef: style="text-align: center;"}
![SidecarT revision 1](https://sidecartridge.com/assets/blog/images/sidecart-rev1.png)
{: refdef}

The transition from Revision 0 to Revision 1 of the SidecarT board involved a shift to a four-layer PCB, reducing its size to about 70% of its predecessor and repositioning components, including the Pico W headers and the SELECT button. This redesign aimed at improving signal stability and physical robustness but introduced challenges such as compatibility issues with certain Atari ST models and fragile case mounting holes. Feedback from users highlighted the importance of backward compatibility with Revision 0 cases, pointing to the need for a balanced design approach in future revisions. **This revision was never on sale, only a few prototypes were made.**

## Revision 2: The Hybrid

{:refdef: style="text-align: center;"}
![SidecarT revision 2](https://sidecartridge.com/assets/blog/images/sidecart-rev2.png)
{: refdef}

### Revision 2.0
Starting in Febrary 2024, revision 2.0 integrates the best features from its predecessors with new enhancements. It maintains the four-layer PCB and mirrors Revision 0's size for case compatibility. This version introduces larger case mounting holes, optimizes button placement, adds a power LED indicator, and offers a castellated Pico W option for a lower profile. Designed with backward compatibility in mind, it respects the community's investments while accommodating minor adjustments for existing cases.

### Revision 2.1
Revision 2.1 introduces two minor updates to Revision 2.0: the power LED's resistor has been changed to a 6k8 to dim the LED, and it reverts to the original Ground and UART headers configuration due to JLCPB's new charges for this SMT option as if it were a through-hole component.

### Revision 2.2.0
Revision 2.2.0 introduces several important enhancements to Revision 2.1:
- Dual USB-A ports for power output only.  The power lines are protected by fuses and schottky diodes to protect your Atari ST, SidecarTridge and USB devices.
- Dual JST SH 2xmale 1.0mm pitch connectors for the RESET and SELECT buttons.  This allows for easier installation and removal of the buttons in enclosures.

### Revision 2.2.1
Revision 2.2.1 introduces aminor addition to Revision 2.2.0:
- Single JST SH 3xmale 1.0mm pitch connectors for the UART and GND pins.  Now it's easier to connect to the Raspberry Pi Debug probe for developers.

### Revision 2.3.0
Revision 2.3.0 introduces a minor addition to Revision 2.2.x series to improve the radio signal of the Pico W module:
- Minor rewiring of some tracks under the Pico W radio module.
- Larger no-copper area under the Pico W radio module.

## Want to contribute?

You can contribute to page. Please scroll to the bottom of the page and click on the "Edit this page on GitHub" link. You can then submit a pull request with your changes.