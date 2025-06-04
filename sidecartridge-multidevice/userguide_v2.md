---
layout: default
title: User Guide Firmware V2.0 (ALPHA)
nav_order: 3
nav_exclude: true
parent: SidecarTridge Multi-device
redirect_from:
  - /userguide_v2/
  - /userguide_v2
---

# User Guide
{: .no_toc }

{: .warning }
This is an **ALPHA** version of the firmware, and it is not recommended for production use. It is intended for developers and makers who want to experiment with the Multi-device board and contribute to its development with code or just submitting bugs. If you are a novice user, please refer to the [previous version of the firmware](https://docs.sidecartridge.com/sidecartridge-multidevice/userguide/) for a more stable experience.


<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Booster Manager Mode

### What is the Booster Manager Mode?

The **Booster Manager Mode** is a new feature introduced in the SidecarTridge Multi-device firmware version 2.0 (ALPHA). It allows users to manage microfirmware apps on the device through a web interface, making it easier to install, launch, and manage apps.

Thanks to the  Booster Manager Mode, users can now easily manage microfirmware apps on the SidecarTridge Multi-device board. This mode is designed to simplify the process of installing and launching apps, providing a user-friendly web interface accessible from any device connected to the same WiFi network. As a side effect, it also helps developers to build their own microfirmware apps and test them on the device without needing to integrate with the main firmware.

In **Manager mode**, the Booster app will automatically connect to your configured WiFi network and will automatically connect to the public repository of microfirmware apps, displaying them in the web interface. The web interface is accessible from any computer or mobile device connected to the same WiFi network as the Booster app.

If your DHCP network supports a DNS with `.local` domains, you can access the web interface using `http://sidecart.local`. Otherwise, use the IP address assigned by your DHCP server and visible on your computer screen.

> **Note**: The device needs a SDHC or SDXC microSD card formatted with **exFAT** or **FAT32** file system to work properly. The app will warn the user if the microSD card is not present or not formatted correctly.

### Apps view

The **Apps view** shows:

- The list of instalable apps from the public repository.
- The list of installed apps on the device.
- The list of apps that are not installed but are available on the microSD card.

This view is the default view when you access the web interface.

![Booster Manager Apps View 1](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-APPS-1.png)

Each app shows the following information:
- **Name**: The name of the app.
- **Version**: The version of the app.
- **Description**: A short description of the app.
- **Features**: A list of features supported by the app as a taxonomy.
- **Computer**: The computers supported by the app as a taxonomy.

At the right hand side of each app, you can see the following buttons:
- **Download**: Download the app from the public repository to the micro SD card. But it does not launch it yet.
- **Delete**: Delete the app from the device microSD card. You can download the app again if you want to.

![Booster Manager Apps View 2](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-APPS-2.png)

- **Launch**: Launch the app. This will install the app in the flash memory of the device and after reboot it will be launched automatically. If you want to launch an app that is already installed, you can use the **Launch** button at any time.

![Booster Manager Apps View 3](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-APPS-3.png)

When launching an app, the computer screen will show a message indicating that the app is being launched. The Booster app will make its best effort to also reboot the computer, but this may not always be possible. So assume that the computer is not rebooted and you need to do it manually.

The Booster microfirmware app is now installed in the flash memory of the device, and every time you power on the device, it will automatically launch the app. 

To return to the Booster app, the user needs to use the command menu on the microfirmware app to do it, or press the SELECT button for more than 10 seconds and then power off and power on the device and the computer.

> **Note**: In this Alpha version, the **DEV APP** is a placeholder development app for anybody who wants to develop a microfirmware app. It is not a real app and it does not do anything.

### WiFi view

The **WiFi view** shows the list of available WiFi networks and permits some basic network configuration options:

![Booster Manager WiFi View](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-WIFI-1.png)

- **Country**: The country code of the WiFi network. This is used to configure the WiFi module to use the correct channels and frequencies.
- **Hostname**: The hostname of the device. This is used to identify the device on the network. By default is `sidecart`. 
- **Wifi Power**: The power of the WiFi module. From 0 to 4. 
- **Show RSSI**: Show the RSSI of the WiFi module. This is used to show the signal strength of the WiFi network.
- **DHCP Enabled**: Enable or disable the DHCP server. This is used to assign IP addresses to the devices connected to the Booster app. In Alpha, only DHCP is tested.

Don't forget to click the **Save** button to save the changes!

It's also possible to change the WiFi network. To do this, click on the new WiFi network from the list. A new window will open with the WiFi network details. Enter the password and click the **Connect** button.

![Booster Manager WiFi View 2](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-WIFI-2.png)

The Booster app will save the WiFi credentials to flash memory and reboot. It will then connect to your WiFi network and show a message on the computer screen.

> **Note**: If the Booster app is not able to connect to the WiFi network, press SELECT button for ten seconds and power off and power on the device and the computer to start the Factory mode again.

### Device view

The **Device view** shows the device information and some basic configuration options:

![Booster Manager Device View](/sidecartridge-multidevice/assets/images/BOOSTER-MANAGER-CONFIG-1.png)

- **Apps folder**: The folder where the apps are stored. By default is `/apps`. This folder is created on the microSD card when the Booster app is launched for the first time if it does not exist.
- **Apps catalog URL**: The URL of the apps catalog. By default is `http://atarist.sidecartridge.com/apps.json`. You can configure your own apps catalog URL if you want to use your own apps. In the alpha version, the `apps.json` file must be hosted in a HTTP server. HTTPS is not supported yet.
- **Boot feature**: The UUID of the microfirmware app to load at boot time, or the Booster mode: `FABRIC` o `MANAGER`. If the app cannot find the UUID of the microfirmware in the flash memory, it will load the Booster app in **Manager mode**.
- **Safe SELECT reboot**: Not used in alpha version.
- **SD card baud rate (KB)**: The baud rate of the SD card. By default is `12500`. It can be safely increased to `25000`. Above this value, the SD card may not work properly or the value will be ignored.

Don't forget to click the **Save** button to save the changes!

It also provides two buttons to reboot the device:

- **Reboot the device**: Reboot the device and load the microfirmware app in flash memory. This is the normal way to reboot the device.
- **Reboot the device in default fabric settings**: Reboot the device and load the Booster app in **Factory mode**. This is useful to reset the device to factory settings or to change the WiFi network.

[Previous: Getting Started](/sidecartridge-multidevice/getting_started_v2/){: .btn .mr-4 }
[Main](/sidecartridge-multidevice/){: .btn .mr-4 }
[Next: Microfirmwares](/sidecartridge-multidevice/microfirmwares/){: .btn }