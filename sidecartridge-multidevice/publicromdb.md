---
layout: default
title: Public ROM DB
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /publicromdb
  - /publicromdb/
---

# Public ROM Database
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Introduction

The original purpose of the SidecarTridge Multidevice was to emulate ROMs for the Atari ST computer. One of its standout features is access to a public ROM database, allowing ROMs to be downloaded directly to the device and accessible from the computer. This document explains how to add content to the public database of ROMs created by the users.

## List of ROMs available
You can find the full list in the JSON file [here](http://roms.sidecartridge.com/roms.json) and in this markdown file: https://github.com/sidecartridge/atarist-roms-database/blob/main/roms.md

All ROMs are available for download clicking on the links. The files are not hosted on this repository, but on a separate server.

## How to contribute

If you have a ROM image that is not listed here, you can contribute to the database by submitting a pull request with the following information:

- Name of the ROM
- Description
- Size in KB
- The ROM image file
- Tags (optional)

You must include the ROM image file in the pull request. The file must be in a single file in a raw format, such as `.bin`, `.img`, `.rom`, or in the STEEM format for cartridge ROMs (`.stc`).

## How to create a Pull Request (PR) from the GitHub website

First, you need to have a GitHub account. If you don't have one, you can create one for free at the [GitHub website](https://github.com).

1. Go to the repository [here](https://github.com/sidecartridge/atarist-roms-database). Fork the repository by clicking on the "Fork" button on the top right corner of the repository page.

2. Go to your forked repository and click on the "Add file" button and select "Upload files".

3. Drag and drop the ROM image file to the file selection area.

4. In the `Commit changes` section, simply add the name of the ROM. No need for a description or any other information at this point.

5. Select the "Create a new branch for this commit and start a pull request" option.

6. Enter a name for the branch and click on the "Propose changes" button.

7. On the next page, click on `compare across forks` and select the original repository as the base repository `sidecartridge/atarist-roms-database` and the `main` branch at the left side, and the branch you just created as the head repository at the right side.

8. On the next page, **edit the description in the following fields**:
    - Filename: Enter the exact filename of the ROM image file you uploaded. Please match the case and extension of the file.
    - Name: Enter the name of the ROM in human readable format.
    - Description: Enter a brief description of the ROM.
    - Tags: Enter any tags that describe the ROM. Single words and comma separated.
    - Size (KB): Enter the size of the ROM in kilobytes. Must be 64 or 128. Only the numbers are allowed.

9. Click on the "Create pull request" button.

10. Wait for the repository owner to review your pull request. If everything is correct, your ROM will be added to the database.

11. If there are any issues with your pull request, the repository owner will leave a comment on the pull request page. You can then make the necessary changes and resubmit the pull request.

12. Once your pull request is accepted and merged, you can delete the branch you created for the pull request.

## How to create a Pull Request (PR) from the command line

If you are familiar with Git and the command line, you can also create a pull request from your local machine. No need to explain how to do it here, as you probably already know how to do it. Just make sure to follow the same steps as above and include the ROM image file in the pull request.

## Disclaimer

The ROM images provided in this database are for educational and archival purposes only. The repository owner does not condone or support piracy in any form. The ROM images are provided as-is and without any warranty. Use at your own risk.

