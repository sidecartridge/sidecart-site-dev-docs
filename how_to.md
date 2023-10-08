---
layout: default
title: How to
nav_order: 7
---

# How to
This section showcases a variety of different configurations and parametric setups for the SidecarT board. You don't need to be a developer to follow these guides, but you will need to be familiar with the basics of the Atari ST and the SidecarT board. If you are new to the SidecarT project, please refer to the [Getting Started](/getting_started) section first.

## Set up your own HTTP server for your ROMs

### Introduction

The SidecarT board is designed to be used with a web server to host the ROMs. This is the recommended way to use the board if you don't want to store the ROM files in the microSD card, as it allows for a more flexible and user-friendly experience. This guide will show you how to set up a local HTTP server on your computer and configure the SidecarT board to use it.

### Set up a HTTP server

There are many ways to set up a HTTP server and there are plenty of tutorials online. It's also possible to use a storage cloud service like Amazon S3 to host the ROMs. For the purpose of this guide, we will only reference some standard HTTP server setups from the internet.

{: .note }
The SidecarT bord does not support HTTPS at the moment. Make sure to disable HTTPS and use HTTP only.

{: .note }
The SidecarT board also only supports access through port 80 and without proxy. Make sure to configure your server accordingly.

{: .note }



- [Apache](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)
- [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)



### Create the `roms.json` file

The `roms.json` file is a JSON file that contains the list of ROMs available on the server. The SidecarT board will use this file to display the list of ROMs in the `Configurator` application. The file must be located at any accessible path on the server. For example, if the server is running on `http://yourserver`, the file can be located at `http://yourserver/roms.json`.


The format of the file is as follows:

- The file must be a JSON array of objects.
- Each object must contain the following fields:
  - `url`: The URL of the ROM file. It does not need to be in the same server as the `roms.json` file.
  - `name`: The name of the ROM.
  - `description`: A short description of the ROM.
  - `tags`: An array of tags describing the ROM.
  - `size_kb`: The size of the ROM in kilobytes.

An example of a `roms.json` file is shown below:

```json
[
    {
        "url": "http://roms.sidecart.xyz/Missile%20Command.STC",
        "name": "Missile Command",
        "description": "A classic arcade game where players defend cities from incoming missiles.",
        "tags": [
            "arcade",
            "action"
        ],
        "size_kb": 128
    },
    {
        "url": "http://roms.sidecart.xyz/Buggy%20Boy.img",
        "name": "Buggy Boy",
        "description": "An off-road racing game where players drive a buggy and avoid obstacles.",
        "tags": [
            "racing",
            "arcade"
        ],
        "size_kb": 128
    },
    ...
    ,
    {
        "url": "http://roms.sidecart.xyz/Joust%20and%20Moon%20Patrol.STC",
        "name": "Joust and Moon Patrol",
        "description": "A combo of two arcade classics - Joust, a competitive bird-riding game, and Moon Patrol, a lunar vehicle shooter.",
        "tags": [
            "arcade",
            "action",
            "shooter"
        ],
        "size_kb": 128
    }
]
```

The full content of the sample `roms.json` file can be found [here](http://roms.sidecart.xyz/roms.json). You can use this file as a template to create your own `roms.json` file.

### Upload the ROM images to the server

The ROM images can be uploaded to any accessible path on the server. For example, if the server is running on `http://yourserver`, the ROM images can be located at `http://yourserver/roms/`. 

If the ROM images have a suffix with the name `.STC` and also the first four bytes are zeroed out, the SidecarT board will automatically detect the ROM as a STEEM ROM and will offset the four bytes out. Otherwise, the ROM will be detected as a standard Atari ST ROM. 

{: .warning }
Don't forget to update the `url` field in the `roms.json` file to point to the correct location of the ROM images.


### Change the SidecarT board configuration

The SidecarT board can be configured to use any HTTP server by changing the `ROMS_YAML_URL` parameter in the configuration parameters of the `Configursator`. The default value of this parameter is `http://roms.sidecart.xyz/roms.json`. You should change this value to point to your own `roms.json` file.

{: .note }
The `ROMS_YAML_URL` is not the right name for this parameter. It will be renamed in the future to `ROMS_JSON_URL`.

### Test the configuration

Once the parameter is changed, you can test the configuration by running the `Configurator` application. The application will display the list of ROMs available on the server. You can select a ROM and run it to test it.

