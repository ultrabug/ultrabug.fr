# Caddx Vista

## Setup MSP for DJI FPV Vista / Air Unit

Take away:

- When MSP is working, you get the quad voltage instead of `N/A` and the `low power mode` message when you plugin, then as soon as you arm the quad the `unlocked` message and `frame rate` message appear
- Temperature protection set to **Off** will make the unit output its full power as soon as you plug in the quad (requested to get the video out via USB)
- Vista and Air Unit have protections against over heating, they will not allow themselves to be damaged because they over heat

Joshua Bardwell made a good [video about DJI FPV short range because of MSP](https://www.youtube.com/watch?v=t6CBYsfmBsk) misconfiguration.

## How to tell if a Vista or Air Unit is damaged

- Take a multimeter
- Check the continuity between Ground and TX, then RX : **there should be none**
- Check the resistance between Ground and TX, then RX : **it should be mega ohms worth**

## How to switch to FCC 700mW output

- [Oscar Liang's guide on FCC mode](https://oscarliang.com/dji-fpv-system-fcc-700mw/)

## How to switch to 1200mW output

- [Oscar Liang's guide on 1200mW output](https://oscarliang.com/dji-fpv-system-1200mw-output/)

## SBUS Baud Fast low latency performance with DJI FPV

- On the DJI FPV goggles go to `Settings > Device > Protocol` and make sure to
select `Sbus Baud Fast`
- On Betaflight CLI, type `set sbus_baud_fast=ON`
