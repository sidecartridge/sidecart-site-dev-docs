---
layout: default
title: Internal riser boards for Mega ST and Mega STE
nav_order: 8
nav_exclude: false
parent: ACSI2STM Hard Disk for Atari ST
---

# Internal riser boards for Mega ST and Mega STE
{: .no_toc }

The ACSI2STM internal riser boards are an add-on for the **ACSI2STM Compact** model. They let you mount the Compact board inside an Atari Mega ST or Mega STE, so you can keep the machine tidy and avoid running the device externally from the rear ACSI port.

{: .warning }
These riser boards are designed for the **ACSI2STM Compact** and rely on the 20-pin rear connector usually referred to as the "Satan Disk" connector. Compatibility with other ACSI2STM variants or third-party boards is not guaranteed.

## What this add-on does

- moves the ACSI2STM Compact inside the case
- avoids an external box and external cabling on the back of the computer
- provides a cleaner installation for Mega ST and Mega STE builds
- powers the Compact internally through the included wiring/cable set

## Two versions

There are two different riser boards because the internal layout of the **Mega ST** and **Mega STE** is not the same.

### Mega ST riser board

![ACSI2STM Mega ST riser board](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGAST-FRONT.png)

This version is designed for the Atari Mega ST and includes the extra power wiring needed for that machine.

**Kit contents:**
- Mega ST riser board
- pre-soldered 24-pin female connector
- pre-soldered 20-pin female connector
- pre-soldered USB-A power-only female connector
- two pre-soldered male pins for 5V power connection
- 20 cm female-to-female Dupont red connector
- USB-A to USB-C cable

![ACSI2STM Mega ST riser board kit](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGAST-KIT.png)

### Mega STE riser board

![ACSI2STM Mega STE riser board](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGASTE-FRONT.png)

This version is designed for the Atari Mega STE and matches the internal connector layout of that machine.

**Kit contents:**
- Mega STE riser board
- pre-soldered 30-pin female connector
- pre-soldered 20-pin female connector
- pre-soldered USB-A power-only female connector
- USB-A to USB-C cable

![ACSI2STM Mega STE riser board kit](/acsi2stm-atari-st/assets/images/riser/ACSI2STM-RISER-MEGASTE-KIT.png)

## Important compatibility note

To use these riser boards, your ACSI2STM Compact must expose the **20-pin connector at the back of the board**. All SidecarTridge-produced Compact boards were designed with this connector in mind, although depending on revision or kit option it may not always come pre-soldered.

If you are using a Compact board from another manufacturer, please verify the connector layout before buying the riser board.

## Recommended positioning in the docs

Think of this product as an **internal installation add-on for ACSI2STM Compact**, not as a standalone storage device. It belongs under the ACSI2STM Compact documentation because it extends that hardware rather than replacing it.

## Installation guide

The exact internal layout differs between the Mega ST and Mega STE, so treat the riser board as model-specific. The steps below are based on the available kit contents and the current product images.

{: .warning }
Always power the Atari off completely and disconnect it from mains power before opening the case.

### Installing the riser board in an Atari Mega ST

1. Open the Mega ST case and locate the area where the ACSI2STM Compact will sit without interfering with the floppy drive, shielding, or airflow.
2. Verify that your **ACSI2STM Compact** has the rear **20-pin connector** available for the riser board.
3. Fit the **Mega ST riser board** in its intended internal position.
4. Connect the Compact to the riser through the **20-pin connector**, making sure the board is fully seated and not under tension.
5. Use the included **5V power pins** and **female-to-female Dupont cable** to bring power from the Mega ST power source to the riser board as intended by the kit.
6. Connect the included **USB-A to USB-C cable** from the riser board’s power-only USB-A connector to the USB-C power input on the ACSI2STM Compact.
7. Double-check that the Compact, riser, and cables do not foul the keyboard frame, top cover, or any nearby metal shielding.
8. Reassemble the machine and perform a first boot test before fully closing everything permanently.

**Practical checks for Mega ST:**
- the Compact should remain mechanically stable when the case is moved
- the USB-C lead should not be sharply bent
- the Dupont power lead should be routed away from sharp metal edges

### Installing the riser board in an Atari Mega STE

1. Open the Mega STE case and identify the internal mounting area for the ACSI2STM Compact.
2. Verify that your **ACSI2STM Compact** exposes the rear **20-pin connector** required by the riser board.
3. Fit the **Mega STE riser board** into place using the connector layout intended for the Mega STE chassis.
4. Seat the Compact onto the riser through the **20-pin connector**, ensuring correct alignment and no lateral stress on the pins.
5. Connect the included **USB-A to USB-C cable** from the riser board’s power-only USB-A connector to the Compact’s USB-C power input.
6. Check that the whole assembly clears the internal shielding and any nearby drive/cable routing.
7. Reassemble the computer and test that the Compact powers correctly and is detected as expected.

**Practical checks for Mega STE:**
- confirm that the riser sits flat and the Compact is not twisted on the connector
- make sure the USB power cable does not get trapped by the lid or shielding
- verify that SD card access remains practical after installation

## What is still missing

This first version should be enough to explain the role of the add-on and the basic installation flow, but it would still benefit from:
- internal in-machine photos for both models
- exact mounting position notes per chassis revision
- cable-routing close-ups
- troubleshooting notes for bad seating or missing power
