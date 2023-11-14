---
layout: default
title: Parameters
nav_order: 8
---

# Configuration Parameters

{: warning}
Please modify the parameters with caution, as they can affect the behavior of the SidecarT board. Read the [Configuration](/configuration) section for more information.

| Parameter  | Type      | Default | Description                               | Released |
|:-----------|:----------|:--------|:------------------------------------------|:---------|
| BOOT_FEATURE | STRING     | CONFIGURATOR | Firmware mode to start after SidecarT reboot   | v0.0.1 |
| DELAY_ROM_EMULATION | BOOLEAN     | false | Enable or disable Delay/Ripper mode   | v0.0.9 |
| FLOPPIES_FOLDER | STRING     | /floppies | The folder where the SidecarT will find the Floppy images   | v0.0.10 |
| FLOPPY_DB_URL | STRING | http://ataristdb.sidecart.xyz | The URL of the Atari ST floppy database | v0.0.11 |
| FLOPPY_IMAGE_A | STRING     |  | File with the floppy image to emulate in drive A   | v0.0.10 |
| FLOPPY_IMAGE_B | STRING     |  | File with the floppy image to emulate in drive B   |  |
| HOSTNAME | STRING | sidecart | The hostname of the SidecarT in the TCP/IP network | v0.0.1 |
| LATEST_RELEASE_URL | STRING |http://atarist.sidecart.xyz/version.txt | The URL of the file with the latest SidecarT release version | v0.0.1 |
| ROMS_FOLDER | STRING | /roms | The folder where the SidecarT will find the ROM images | v0.0.1 |
| ROMS_YAML_URL | STRING | http://roms.sidecart.xyz/roms.json | The URL of the JSON file with the ROMs information | v0.0.1 |
| SAFE_CONFIG_REBOOT | BOOL | true | If true, the SidecarT will reboot after a computer power cycle, otherwise it will reboot immediately | v0.0.9 |
| WIFI_PASSWORD | STRING |  | The password of the WiFi network to connect to | v0.0.1 |
| WIFI_SCAN_SECONDS | INTEGER | 15 | The number of seconds to scan for WiFi networks | v0.0.1 |
| WIFI_SSID | STRING |  | The SSID of the WiFi network to connect to | v0.0.1 |
| WIFI_AUTH | INTEGER |  | The authentication type of the WiFi network to connect to | v0.0.1 |

