---
layout: default
title: Parameters
nav_order: 8
---

# Configuration Parameters

{: warning}
Please modify the parameters with caution, as they can affect the behavior of the SidecarT board. Read the [Configuration](/configuration) section for more information.

| Parameter  | Type      | Default | Description                               |
|:-----------|:----------|:--------|:------------------------------------------|
| BOOT_FEATURE | STRING     | CONFIGURATOR | Firmware mode to start after SidecarT reboot   |
| DELAY_ROM_EMULATION | BOOLEAN     | false | Enable or disable Delay/Ripper mode   |
| FLOPPIES_FOLDER | STRING     | /floppies | The folder where the SidecarT will find the Floppy images   |
| FLOPPY_IMAGE_A | STRING     |  | File with the floppy image to emulate in drive A   |
| FLOPPY_IMAGE_B | STRING     |  | File with the floppy image to emulate in drive B   |
| HOSTNAME | STRING | sidecart | The hostname of the SidecarT in the TCP/IP network |
| ROMS_FOLDER | STRING | /roms | The folder where the SidecarT will find the ROM images |
| ROMS_YAML_URL | STRING | http://roms.sidecart.xyz/roms.json | The URL of the JSON file with the ROMs information |
| SAFE_CONFIG_REBOOT | BOOL | true | If true, the SidecarT will reboot after a computer power cycle, otherwise it will reboot immediately |
| WIFI_PASSWORD | STRING |  | The password of the WiFi network to connect to |
| WIFI_SCAN_SECONDS | INTEGER | 15 | The number of seconds to scan for WiFi networks |
| WIFI_SSID | STRING |  | The SSID of the WiFi network to connect to |
| WIFI_AUTH | INTEGER |  | The authentication type of the WiFi network to connect to |
