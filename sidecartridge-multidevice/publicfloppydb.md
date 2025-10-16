---
layout: default
title: Public Floppy DB
nav_exclude: false
parent: SidecarTridge Multi-device
redirect_from:
  - /publicfloppydb
  - /publicfloppydb/
---

# Public Floppy Database
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

One notable feature of Sidecart is its ability to emulate Floppy Drives. This is executed efficiently; it does not consume any system RAM space. The driver needed for this emulation is exclusively located in the cartridge ROM, ensuring that system resources are used optimally and system performance is maintained.

One of the popular features of the SidecarT is the search and download of floppy images from the public database. This document explains how to add content to the public database of floppy images created by the users.

## The repository

The GitHub repository is located at [sidecartridge/atarist-public-floppy-db](https://github.com/sidecartridge/atarist-public-floppy-db).

This repository is a way to share with the community the floppy images that are created by the users and that are not available in the public database. The images are uploaded to an external repository, while the metadata is stored in this repository.

## List of floppies available

You can find the full list in the folder here: https://ataristdb.sidecartridge.com/db/*.csv

Where the asterisk is the first letter of the name of the floppy. The database is sharded by the first letter of the name of the floppy to allow the database to be easily parsed by the SidecarTridge Multi-device Floppy Database.

All the floppies added through the pull requests will be added to the database and will be available for the community as follows:
- It will be added to the database in its corresponding shard.
- It will be available in the special shard `_.csv` that contains all the new stuff sorted by most recent addenda. The maximum size of this file is 300 rows, so the oldest will be deleted when they reach this pointer.

## How to contribute

If you have a Floppy Image that is not listed here, you can contribute to the database by submitting a pull request with the following information:

- Name of the Floppy
- Description
- Type: can only be `CRACKTROS`, `DEMOS`, `HOMEBREW`,  `INTROS`.

**You must include the Floppy Image file in the pull request in .ST format.** The file must be in a single file. If the floppy has more than one disk, you must create a separate pull request for each disk.

## How to create a Pull Request (PR) from the GitHub website

First, you need to have a GitHub account. If you don't have one, you can create one for free at the [GitHub website](https://github.com).

1. Fork the repository by clicking on the "Fork" button on the top right corner of the repository page.

2. Go to your forked repository and click on the "Add file" button and select "Upload files".

3. Drag and drop the Floppy image file to the file selection area.

4. In the `Commit changes` section, simply add the name of the Floppy Image. No need for a description or any other information at this point.

5. Select the "Create a new branch for this commit and start a pull request" option.

6. Enter a name for the branch and click on the "Propose changes" button.

7. **IMPORTANT: On the next page, click on `compare across forks` and select the original repository as the base repository `sidecartridge/atarist-public-floppy-db` and the `main` branch at the left side, and the branch you just created as the head repository at the right side.**

8. On the next page, **edit the description in the following fields**:
    - Filename: Enter the exact filename of the Floppy image file you uploaded. Please match the case and extension of the file. Only .ST files are allowed.
    - Name: Enter the name of the Flopy Image in human readable format. It must be short and descriptive.
    - Description: Enter a brief description of the Floppy Image.
    - Type: Enter the type of the Floppy Image. Recommended values are `DEMOS`, `GRAPHICS`, `MUSIC`,  `GAMES`, `INTROS` and `HOMEBREW_GAMES`. But another descriptive type can be used. Uppercase, please.

9. Click on the "Create pull request" button.

10. Wait for the repository owner to review your pull request. If everything is correct, your Floppy Image will be added to the database.

11. If there are any issues with your pull request, the repository owner will leave a comment on the pull request page. You can then make the necessary changes and resubmit the pull request.

12. Once your pull request is accepted and merged, you can delete the branch you created for the pull request.

## How to create a Pull Request (PR) from the command line

If you are familiar with Git and the command line, you can also create a pull request from your local machine. No need to explain how to do it here, as you probably already know how to do it. Just make sure to follow the same steps as above and include the Floppy image file in the pull request.

## Disclaimer

The Floppy images provided in this database are for educational and archival purposes only. The repository owner does not condone or support piracy in any form. The Floppy images are provided as-is and without any warranty. Use at your own risk.

[Previous: Board Revisions](/sidecartridge-multidevice/revisions/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Public ROM Database](/sidecartridge-multidevice/publicromdb/){: .btn }