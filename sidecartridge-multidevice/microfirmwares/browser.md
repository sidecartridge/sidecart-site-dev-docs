---
layout: default
title: SidecarTridge Multi-device File & Download Manager
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /microfirmwares/browser
  - /microfirmwares/browser/
---

# SidecarTridge Multi-device File & Download Manager
{: .no_toc }

{: .d-inline-block }

[Source code](https://github.com/sidecartridge/md-browser){: .label .label-blue }
[CHANGELOG](https://github.com/sidecartridge/md-browser/blob/main/CHANGELOG.md){: .label .label-green }
[Report BUG](https://github.com/sidecartridge/md-browser/issues){: .label .label-red }
[{{ site.MICROFIRMWARE_BROWSER_VERSION }}](){: .label .label-purple }

This microfirmware app for the **SidecarTridge Multi-device** lets you browse and download floppy images from the public database, manage files on your microSD card, and even work directly with Atari ST disk images—all from a browser-based UI that runs on your phone, tablet, or desktop.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## 🚀 Installation

To install the File & Download Manager app on your SidecarTridge Multi-device:

1. **Launch the Booster App** on your SidecarTridge Multi-device.
2. Open the **Booster web interface** in your browser.
3. Go to the **Apps** tab and select **File & Download Manager** from the list.
4. Click **Download** to install the app onto the microSD card.
5. Select the newly installed app and click **Launch**.

> ⚠️ The Booster loader is still considered **alpha** software. Use it at your own risk.

After installing, the File & Download Manager runs automatically every time the Atari powers on.

## 🕹️ Usage

On boot you’ll see a **QR code** screen. Scan it to open the web UI, or type the displayed hostname/IP address (for example, `http://sidecart.local`).

* Press **any key** to skip the QR code and boot GEMDOS.
* Press **ESC** to return to the Booster launcher.
* You can also jump back to Booster directly from the web UI header.

### 💾 Floppy Images Database

Click **Floppy DB** in the navigation bar to open the public floppy database. The page is divided into two discovery modes:

* **What’s New** – latest uploads curated by the community.
* **Main Catalog** – the long-term archive, organized by crew label or collection.

![Floppy Images Database Search Page](/sidecartridge-multidevice/assets/images/BROWSER-FLOPPYDB-MAIN.png)

Use the controls at the top to zero in on what you need:

* **Search box** – smart suggestions as you type (e.g., `xe` → `Xenon`).
* **Label chips** – filter by cracking team, app genre, collection tags, etc.
* **What’s New vs Main Catalog** – flip between recent additions and the deep archive.

![Floppy Images Database Search Results](/sidecartridge-multidevice/assets/images/BROWSER-FLOPPYDB-RESULT.png)

To download an image:

1. Click the green **download icon** next to the entry.
2. Pick the destination folder from the dialog.
3. Click **Download here** to start the transfer.

Files land directly on the microSD card. Load them with the [Drives Emulator](https://docs.sidecartridge.com/sidecartridge-multidevice/microfirmwares/drives_emulator/) or any other floppy solution (Gotek, etc.).

### 🗂️ File Manager

#### Overview

The File Manager is now a full microSD and floppy image workbench. You can:

* Browse folders, inspect file metadata, and color-coded attributes.
* Rename, delete, copy, and move files or folders with progress reporting.
* Upload multiple files at once or pull files directly from an internet URL.
* Create folders, blank Atari ST disk images, and `.st`/`.st.rw` containers.
* Convert `.MSA` ↔ `.ST` floppy images.
* Mount `.ST` and `.st.rw` images and work inside them (copy, rename, delete, import/export files).

#### Table View

Click **File Manager** in the nav. The table lists:

* **Name**, **Size**, **Timestamp**
* **Actions** (icons for copy, move, rename, delete, download, convert, browse image, etc.)

Toolbar actions include:

* **Upload files** (multi-select)
* **Upload from URL**
* **New Folder**
* **Blank ST Image** (create empty 360 KB/720 KB/1.44 MB/2.88 MB images in `.st` or `.st.rw` format)

![File Manager Table View](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-ROOT.png)

#### Row Colors & Navigation

* **Black** rows – normal files/folders
* **Gray** rows – hidden entries
* **Red** rows – read-only items

Click a folder to enter it; use the leading `..` row to go back.

![File Manager Navigation](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-NAVIGATION.png)

#### File Actions

Each row exposes context-aware actions. Depending on the file you can:

* Toggle **hidden** or **read-only** attributes
* **Rename**, **delete**, **download**, **copy**, or **move** items
* **Convert** between `.MSA` and `.ST`
* **Browse Image** for `.ST` / `.st.rw` contents

![File Details Actions](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-FILEACTIONS.png)

#### Creating a Blank ST Image

Need a fresh floppy? Click **Blank ST Image**, pick the size, file name, optional volume name, and whether it should be `.st` (read-only) or `.st.rw` (writable/browsable). The image drops straight into the current folder.

![Create Blank ST Image](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-BLANK-ST.png)

#### Converting MSA and ST Images

Use the **convert** icon to flip an `.MSA` into `.ST` (or vice versa) without leaving the browser. Handy when a release comes in the “wrong” format for your workflow.

#### Browsing Inside ST Images

Open any `.ST`/`.st.rw` file with **Browse Image**. The file mounts like a folder so you can inspect or manage its contents. Writable `.st.rw` images support rename, delete, import, and export operations with automatic 8.3 name handling when needed.

![Browsing Inside an ST Image](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-INSIDE-IMAGE.png)

#### Uploading Files

* **Upload files** – pick one or multiple files from your computer.
* **Upload from URL** – fetch a remote file directly into the current folder.

Progress bars track each transfer and completed files appear immediately.

![File Upload Dialog](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-UPLOADFILES.png)
![File Upload Done](/sidecartridge-multidevice/assets/images/BROWSER-FILEMANAGER-UPLOADEDFILES.png)

### 🔌 USB Mass Storage Mode

Prefer to work from your desktop OS? Plug the Multi-device into USB and the microSD mounts like any other drive. The QR screen displays a USB Mass Storage notice while this mode is active.

> You can leave the web UI open while USB mode is active. Just refresh the browser or your file explorer if you don’t immediately see changes from the other side.

### ⏏️ Exiting to GEMDOS or Booster

* **ESC** on the QR screen opens **Booster**.
* The **web UI header** includes a Booster button for quick returns.
* Any other key exits the app and boots GEM; the web UI stays live in your browser.
* Hold **SELECT** for 10 seconds to factory-reset the Multi-device (useful for troubleshooting).

### ♻️ System Reset Behavior

The File & Download Manager survives warm resets. Pressing RESET on the Atari does not interrupt downloads or file transfers.

### 🔄 Power Cycling

After power cycling, the app restarts at the QR code screen ready for another session.

### ⚙️ Advanced Features

#### Changing the microSD Card Speed

The Booster App lets you tune the SPI bus speed (1 MHz – 24 MHz; default 12.5 MHz):

1. Launch **Booster** (press **X** if you’re in another app).
2. Open the web UI and go to **Config**.
3. Set **SD card bus speed (KHz)** (e.g., `24000`).
4. Click **Save** and relaunch the File & Download Manager.

> Values below 1 MHz are clamped to 1 MHz; values above 24 MHz are clamped to 24 MHz. 24 MHz works for most cards, but drop it to 12.5 MHz or 6 MHz if you see instability.

## 📜 License

The source code is released under the **GNU General Public License v3.0**. See the [LICENSE](https://github.com/sidecartridge/md-browser/blob/main/LICENSE) file for details.

## 🤝 Contributing

Made with ❤️ by [SidecarTridge](https://sidecartridge.com)

[Previous: Multidevice Test](/sidecartridge-multidevice/microfirmwares/multidevice-test/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Debug Cart](/sidecartridge-multidevice/microfirmwares/debug-cart/){: .btn }
