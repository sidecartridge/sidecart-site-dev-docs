---
layout: default
title: Public Floppy DB
nav_order: 15
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

The easiest way to explore the database is the browsable web catalog, the [Atari ST Public Floppy Database](https://ataristpublicfloppydb.sidecartridge.com). Use **What's New** for the latest community uploads or search the full archive by name and label. It runs in any browser, so you don't need an Atari or the device to look around.

If you prefer the raw data, you can find the full list in the folder here: https://ataristdb.sidecartridge.com/db/*.csv

Where the asterisk is the first letter of the name of the floppy. The database is sharded by the first letter of the name of the floppy to allow the database to be easily parsed by the SidecarTridge Multi-device Floppy Database.

All the floppies added through the pull requests will be added to the database and will be available for the community as follows:
- It will be added to the database in its corresponding shard.
- It will be available in the special shard `_.csv` that contains all the new stuff sorted by most recent addenda. The maximum size of this file is 300 rows, so the oldest will be deleted when they reach this pointer.

## How to contribute

There are two ways to add a floppy to the database. **Sending it by email is the recommended method** for everyone: it is quick, needs no GitHub account, and every submission is reviewed by a human before it is published. Submitting a Pull Request is an advanced alternative for users who are comfortable with GitHub.

### Option 1 (recommended): Submit by email

1. Create a new email and **attach your floppy image in `.ST` format** (a single disk image only).

2. Send it to the address shown in the image below. The address is shown as an image on purpose to reduce spam, so please type it manually into your email client:

    ![SidecarTridge Public Floppy DB submission address](/sidecartridge-multidevice/assets/images/PUBLIC-FLOPPY-DB-SUBMISSION-EMAIL.png)

3. In the **body** of the email, include these three lines:

    ```
    Name: <short, descriptive, unique title of the disk>
    Category: <one of the six categories below>
    Description: <optional one-line description>
    ```

    **Category must be exactly one of these six (uppercase):**

    - `DEMOS`
    - `GRAPHICS`
    - `MUSIC`
    - `GAMES`
    - `INTROS`
    - `HOMEBREW_GAMES`

**Rules:**

- **One floppy per email.** For multi-disk sets, send one email per disk.
- Attach the raw `.ST` image only (no `.zip`, `.msa`, or executables).
- `Name` should be unique and clearly describe the disk.
- `Description` is optional.

Every submission is **reviewed manually** before it is added, so it will not appear in the database instantly. Once your floppy has been reviewed and added, you will receive a reply by email, and the new content will be available in the [Atari ST Public Floppy Database](https://ataristpublicfloppydb.sidecartridge.com) web catalog and directly from the **File Manager** of your SidecarTridge Multidevice.

### Option 2 (advanced): Submit a Pull Request

If you are a GitHub user, you can also contribute directly by opening a Pull Request against [sidecartridge/atarist-public-floppy-db](https://github.com/sidecartridge/atarist-public-floppy-db). Include the Floppy Image file in `.ST` format (one file per PR; multi-disk sets need one PR per disk) and the same fields described above.

#### From the GitHub website

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
    - Category: Enter the category of the Floppy Image. It must be exactly one of `DEMOS`, `GRAPHICS`, `MUSIC`, `GAMES`, `INTROS` or `HOMEBREW_GAMES`. Uppercase, please.

9. Click on the "Create pull request" button.

10. Wait for the repository owner to review your pull request. If everything is correct, your Floppy Image will be added to the database.

11. If there are any issues with your pull request, the repository owner will leave a comment on the pull request page. You can then make the necessary changes and resubmit the pull request.

12. Once your pull request is accepted and merged, you can delete the branch you created for the pull request.

#### From the command line

If you are familiar with Git and the command line, you can also create a pull request from your local machine. No need to explain how to do it here, as you probably already know how to do it. Just make sure to follow the same steps as above and include the Floppy image file in the pull request.

## Disclaimer

The Floppy images provided in this database are for educational and archival purposes only. The repository owner does not condone or support piracy in any form. The Floppy images are provided as-is and without any warranty. Use at your own risk.

[Previous: Board Revisions](/sidecartridge-multidevice/revisions/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Public ROM Database](/sidecartridge-multidevice/publicromdb/){: .btn }