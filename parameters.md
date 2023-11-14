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

<table style="width: 100%;">
  <tr>
    <th>Parameter</th>
    <th>Type</th>
    <th style="width: 100%;">Description</th>
    <th>Released</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>BOOT_FEATURE<p class="label label-green">v0.0.1</p></td>
    <td>STRING</td>
    <td>Firmware mode to start after SidecarT reboot</td>
    <td>v0.0.1</td>
    <td>CONFIGURATOR</td>
  </tr>
  <tr>
    <td>DELAY_ROM_EMULATION</td>
    <td>BOOLEAN</td>
    <td>Enable or disable Delay/Ripper mode</td>
    <td>v0.0.9</td>
    <td>false</td>
  </tr>
  <tr>
    <td>FLOPPIES_FOLDER</td>
    <td>STRING</td>
    <td>The folder where the SidecarT will find the Floppy images</td>
    <td>v0.0.10</td>
    <td>/floppies</td>
  </tr>
  <tr>
    <td>FLOPPY_DB_URL</td>
    <td>STRING</td>
    <td>The URL of the Atari ST floppy database</td>
    <td>v0.0.11</td>
    <td>http:// ataristdb.sidecart.xyz</td>
  </tr>
  <tr>
    <td>FLOPPY_IMAGE_A</td>
    <td>STRING</td>
    <td>File with the floppy image to emulate in drive A</td>
    <td>v0.0.10</td>
    <td></td>
  </tr>
  <tr>
    <td>FLOPPY_IMAGE_B</td>
    <td>STRING</td>
    <td>File with the floppy image to emulate in drive B</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>HOSTNAME</td>
    <td>STRING</td>
    <td>The hostname of the SidecarT in the TCP/IP network</td>
    <td>v0.0.1</td>
    <td>sidecart</td>
  </tr>
  <tr>
    <td>LATEST_RELEASE_URL</td>
    <td>STRING</td>
    <td>The URL of the file with the latest SidecarT release version</td>
    <td>v0.0.1</td>
    <td>http:// atarist.sidecart.xyz/ version.txt</td>
  </tr>
  <tr>
    <td>ROMS_FOLDER</td>
    <td>STRING</td>
    <td>The folder where the SidecarT will find the ROM images</td>
    <td>v0.0.1</td>
    <td>/roms</td>
  </tr>
  <tr>
    <td>ROMS_YAML_URL</td>
    <td>STRING</td>
    <td>The URL of the JSON file with the ROMs information</td>
    <td>v0.0.1</td>
    <td>http:// roms.sidecart.xyz/roms.json</td>
  </tr>
  <tr>
    <td>SAFE_CONFIG_REBOOT</td>
    <td>BOOL</td>
    <td>If true, the SidecarT will reboot after a computer power cycle, otherwise it will reboot immediately</td>
    <td>v0.0.9</td>
    <td>true</td>
  </tr>
  <tr>
    <td>WIFI_PASSWORD</td>
    <td>STRING</td>
    <td>The password of the WiFi network to connect to</td>
    <td>v0.0.1</td>
    <td></td>
  </tr>
  <tr>
    <td>WIFI_SCAN_SECONDS</td>
    <td>INTEGER</td>
    <td>The number of seconds to scan for WiFi networks</td>
    <td>v0.0.1</td>
    <td>15</td>
  </tr>
  <tr>
    <td>WIFI_SSID</td>
    <td>STRING</td>
    <td>The SSID of the WiFi network to connect to</td>
    <td>v0.0.1</td>
    <td></td>
  </tr>
  <tr>
    <td>WIFI_AUTH</td>
    <td>INTEGER</td>
    <td>The authentication type of the WiFi network to connect to</td>
    <td>v0.0.1</td>
    <td></td>
  </tr>
</table>
