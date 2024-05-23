---
layout: default
title: Public Floppy DB
nav_exclude: false
parent: SidecarTridge Multi-device
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

# Public Floppy Database

## Introduction

One notable feature of Sidecart is its ability to emulate Floppy Drives. This is executed efficiently; it does not consume any system RAM space. The driver needed for this emulation is exclusively located in the cartridge ROM, ensuring that system resources are used optimally and system performance is maintained.

One of the popular features of the SidecarT is the search and download of floppy images from the public database. This document explains how to add content to the public database of floppy images created by the users.

## How to contribute

1. **Host your floppy images in a public web storage**. The floppy images must be in .ST format, and it must be accessible through HTTP since HTTPS is not supported by the SidecarT firmware. The repository must be public and accessible without any authentication.

Example: I want to host a floppy image called `SILLYDEMO.ST` in my public webserver in the URL `http://ataristdb.sidecartridge.com/MISC/SILLYDEMO.ST`. 

2. **Checkout the repository**. Clone the `https://github.com:diegoparrilla/atarist-public-floppy-db` repository in your local machine, or fork it and clone your fork. If you are not familiar with Git, you can follow the instructions in the [Git documentation](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository). As an alternative, you can also use edit directly the files explained in the next steps in the GitHub web interface.

Example: 
```bash
git clone git@github.com:diegoparrilla/atarist-public-floppy-db.git
```

3. **Create your working branch**. Create a new branch in your local repository to add your floppy image. The name of the branch should be descriptive of the floppy you are adding. 

Example:
```bash
git checkout -b add-silly-demo
```

4. **Choose the folder with the category of your floppy**. The floppy images are organized in folders by category. If you don't find a category that fits your floppy, you can create a new one. The name of the folder must be in uppercase and without spaces.

Example: I want to host the `SILLYDEMO.ST` floppy in the `CRACKTROS` category. I will use the `CRACKTROS` folder.

5. **Edit the list.txt file**. Inside the folder of the category, there is a file called `list.txt`. This file contains the list of floppy images in the category. Add a new line with the URL of your floppy image. As a respect to the Atari ST community, please add the content in alphabetical order, and use the following format:

```
"NAME OF THE APPLICATION";"URL OF THE FLOPPY IMAGE"
```

If the `list.txt` file does not exist, create it.

Example:
```
"The Very Silly STE Demo (C) 2024 by @Logronoide";"http://ataristdb.sidecartridge.com/MISC/SILLYDEMO.ST"
```

6. **Commit your changes**. Commit your changes to your local repository. You can use the following commands to commit your changes:

Example:
```bash
git add .
git commit -m "Add Silly Demo floppy"
```

7. **Push your changes**. Push your changes to your fork of the repository. Please don't push directly to the main repository, as it is not allowed. Please create a pull request.

Example:
```bash
git push origin add-silly-demo
```

8. **Wait for the pull request to be reviewed**. After you push your changes, the pull request will be reviewed by the maintainers of the repository, and if everything is correct, it will be merged.

9. **Celebrate!**. Your floppy image is now available for the Atari ST community through the SidecarT Floppy Database.

## Requirements

Please ensure you have the following prerequisites before proceeding:

1. The floppy image must be in .ST format.
2. The floppy image must be accessible through HTTP since HTTPS is not supported by the SidecarT firmware.
3. The service is case sensitive, so the URL must be in the same case as the file name.

