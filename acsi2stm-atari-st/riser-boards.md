---
layout: default
title: Internal riser boards for Mega ST and Mega STE
nav_order: 8
nav_exclude: false
parent: ACSI2STM Hard Disk for Atari ST
---

# Internal riser boards for Mega ST and Mega STE
{: .no_toc }

{: .warning }
Think of this product as an **internal installation add-on for ACSI2STM Compact**, not as a standalone storage device. It belongs under the ACSI2STM Compact documentation because it extends that hardware rather than replacing it. These riser boards are designed for the **ACSI2STM Compact** and rely on the IDC 20-pin rear connector usually referred to as the "Satan Disk" connector. Compatibility with other ACSI2STM variants or third-party boards is not guaranteed.


These internal riser boards are installation add-ons for the **ACSI2STM Compact** model, designed specifically for the Atari Mega ST and Mega STE. They let you mount the Compact board inside the computer, keeping the setup tidy and avoiding an external device hanging from the rear ACSI port.

{: .important }
These riser boards are **not compatible with the ACSI2STM Mini**.

## What this add-on does

- moves the ACSI2STM Compact inside the case
- avoids an external box and external cabling on the back of the computer
- provides a cleaner installation for Mega ST and Mega STE builds
- powers the Compact internally through the included wiring/cable set

## Two versions

There are two different riser boards because the internal layout of the **Mega ST** and **Mega STE** is not the same.

### Mega ST riser board

![ACSI2STM Mega ST riser board kit](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGAST-KIT.png)

This version is designed for the Atari Mega ST and includes the extra power wiring needed for that machine.

**Kit contents:**
- Mega ST riser board
- pre-soldered 24-pin female connector
- pre-soldered IDC 20-pin female connector
- pre-soldered USB-A power-only female connector
- two pre-soldered male pins for 5V power connection
- 20 cm female-to-female Dupont red connector
- USB-A to USB-C cable


### Mega STE riser board

![ACSI2STM Mega STE riser board kit](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGASTE-KIT.png)

This version is designed for the Atari Mega STE and matches the internal connector layout of that machine.

**Kit contents:**
- Mega STE riser board
- pre-soldered 30-pin female connector
- pre-soldered IDC 20-pin female connector
- pre-soldered USB-A power-only female connector
- USB-A to USB-C cable


## Important compatibility note

To use these riser boards, your ACSI2STM Compact must expose the **IDC 20-pin connector at the back of the board**. All SidecarTridge-produced Compact boards were designed with this connector in mind, although depending on revision or kit option it may not always come pre-soldered.

If you are using a Compact board from another manufacturer, please verify the connector layout before buying the riser board.

## Before you start

Before opening the computer, make sure that:

- you are using an **ACSI2STM Compact**
- your Compact has the rear **IDC 20-pin connector** required by the riser board
- you are comfortable opening the machine and checking cable routing inside the case
- the Atari is fully powered off and disconnected from mains power

## Installation guide

The exact internal layout differs between the Mega ST and Mega STE, so treat the riser board as model-specific. The steps below are based on the available kit contents and the current product images.

{: .warning }
Always power the Atari off completely and disconnect it from mains power before opening the case.

### Installing the riser board in an Atari Mega ST

![ACSI2STM Compact on Mega ST riser board](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGAST-BOARD.png)

1. Open the Mega ST case and locate the area where the ACSI2STM Compact will sit without interfering with the floppy drive, shielding, or airflow.
2. Verify that your **ACSI2STM Compact** has the rear **IDC 20-pin connector** available for the riser board.
3. Fit the **Mega ST riser board** in its intended internal position.
4. Connect the Compact to the riser through the **IDC 20-pin connector**, making sure the board is fully seated and not under tension.
5. Use the included **5V power pins** and **female-to-female Dupont cable** to supply **5V power only** from the Mega ST motherboard to the riser board. On the Mega ST motherboard, use pin 1 or pin 2 of connector **J18**, which both provide 5V. J18 is located between the power supply and the floppy drive, on the left side of the power supply connector. See the image below for reference.
6. The red Dupont lead is the power lead included with the Mega ST kit. If you are not sure about the power connection, do not improvise with alternative points on the motherboard.

![ACSI2STM Compact on Mega ST riser board J18 jumper](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGAST-BOARD-J18.PNG)

7. Connect the included **USB-A to USB-C cable** from the riser board’s power-only USB-A connector to the USB-C power input on the ACSI2STM Compact.
8. Double-check that the Compact, riser, and cables do not foul the keyboard frame, top cover, or any nearby metal shielding.
9. Reassemble the machine and perform a first boot test before fully closing everything permanently.

**Practical checks for Mega ST:**
- the Compact should remain mechanically stable when the case is moved
- the USB-C lead should not be sharply bent
- the Dupont power lead should be routed away from sharp metal edges


### Installing the riser board in an Atari Mega STE

![ACSI2STM Compact on Mega STE riser board](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGASTE-BOARD.png)

1. Open the Mega STE case and identify the internal mounting area for the ACSI2STM Compact.
2. Verify that your **ACSI2STM Compact** exposes the rear **IDC 20-pin connector** required by the riser board.
3. Fit the **Mega STE riser board** into place using the connector layout intended for the Mega STE chassis.
4. Seat the Compact onto the riser through the **IDC 20-pin connector**, ensuring correct alignment and no lateral stress on the pins.
5. Connect the included **USB-A to USB-C cable** from the riser board’s power-only USB-A connector to the Compact’s USB-C power input.
6. Unlike the Mega ST version, the Mega STE kit does **not** use the extra Dupont power lead included with the Mega ST board.
7. Check that the whole assembly clears the internal shielding and any nearby drive/cable routing.
8. Reassemble the computer and test that the Compact powers correctly and is detected as expected.

**Practical checks for Mega STE:**
- confirm that the riser sits flat and the Compact is not twisted on the connector
- make sure the USB power cable does not get trapped by the lid or shielding
- verify that SD card access remains practical after installation

## Troubleshooting after installation

If the installation does not work as expected, check the following first:

- **The device is not detected:** make sure the Compact is fully seated on the IDC 20-pin connector and that the riser is aligned correctly.
- **The Compact does not power on:** verify the USB-A to USB-C power link, and on Mega ST also re-check the 5V connection at J18.
- **The lid does not close cleanly:** inspect cable routing again and make sure no lead is trapped under shielding or pressed sharply against the case.

Before closing the case completely, it is a good idea to perform a partial test boot and confirm that the board sits flat, powers correctly, and has no pinched cables.

[Previous: Enclosures/Cases](/acsi2stm-atari-st/cases/){: .btn .mr-4 }
[Main](/acsi2stm-atari-st/){: .btn .mr-4 }
[Next: FAQ](/acsi2stm-atari-st/faq/){: .btn }
