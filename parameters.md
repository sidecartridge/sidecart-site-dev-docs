---
layout: default
title: Parameters
nav_order: 8
---

# Configuration Parameters

{: warning}
Please modify the parameters with caution, as they can affect the behavior of the SidecarT board. Read the [Configuration](/configuration) section for more information.

| Parameter            | Type      | Description                                            | Released | Default                              |
|:---------------------|:----------|:-------------------------------------------------------|:---------|:-------------------------------------|
| BOOT_FEATURE         | STRING    | Firmware mode to start after SidecarT reboot           | v0.0.1   | CONFIGURATOR                         |
| DELAY_ROM_EMULATION  | BOOLEAN   | Enable or disable Delay/Ripper mode                    | v0.0.9   | false                                |
| FLOPPIES_FOLDER      | STRING    | The folder where the SidecarT will find the Floppy images | v0.0.10  | /floppies                            |
| FLOPPY_DB_URL        | STRING    | The URL of the Atari ST floppy database                | v0.0.11  | http:// ataristdb.sidecart.xyz        |
| FLOPPY_IMAGE_A       | STRING    | File with the floppy image to emulate in drive A       | v0.0.10  |                                      |
| FLOPPY_IMAGE_B       | STRING    | File with the floppy image to emulate in drive B       |          |                                      |
| HOSTNAME             | STRING    | The hostname of the SidecarT in the TCP/IP network     | v0.0.1   | sidecart                             |
| LATEST_RELEASE_URL   | STRING    | The URL of the file with the latest SidecarT release version | v0.0.1   | http:// atarist.sidecart.xyz/ version.txt |
| ROMS_FOLDER          | STRING    | The folder where the SidecarT will find the ROM images | v0.0.1   | /roms                                |
| ROMS_YAML_URL        | STRING    | The URL of the JSON file with the ROMs information     | v0.0.1   | http:// roms.sidecart.xyz/ roms.json   |
| SAFE_CONFIG_REBOOT   | BOOL      | If true, the SidecarT will reboot after a computer power cycle, otherwise it will reboot immediately | v0.0.9   | true                                 |
| WIFI_PASSWORD        | STRING    | The password of the WiFi network to connect to         | v0.0.1   |                                      |
| WIFI_SCAN_SECONDS    | INTEGER   | The number of seconds to scan for WiFi networks        | v0.0.1   | 15                                   |
| WIFI_SSID            | STRING    | The SSID of the WiFi network to connect to             | v0.0.1   |                                      |
| WIFI_AUTH            | INTEGER   | The authentication type of the WiFi network to connect to | v0.0.1   |                                      |
