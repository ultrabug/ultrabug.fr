# Apex 5" HD on base frame kit

## A digital HD build on the Apex Base Frame Kit

:fr: Pour mon premier build DIY je voulais un 5" solide.

J'ai choisi le **ImpulseRC Apex Base Frame Kit** car je ne voulais pas dépendre d'une frame spécifique HD et perdre la place faite spécifiquement pour le DJI Air Unit.

Ce fut un challenge de tout faire tenir proprement mais j'adore le résultat et j'espère que vous apprécierez la densité et l'équilibre du build.

Cela donne vie à un build compact (mais pas trop) sans sacrifier la place pour l'électronique. C'est propre (en tout cas pour moi) et très puissant.

J'ai pris énormément de plaisir à travailler dessus et j'espère que vous le sentirez au long de votre lecture. Amusez-vous bien !

![Apex HD on Base Kit overview](images/IMG_20210110_114845.jpg){: style="opacity:0.5;"}

## Hardware list

!!! note
    Les liens ci-dessous ne sont **PAS** des liens d'affiliation. Ce sont tout simplement les liens où j'ai moi-même commandé le matériel nécessaire à ce build.

- [X] [ImpulseRC Apex Base Frame Kit](https://www.drone-fpv-racer.com/apex-5-base-frame-kit-5135.html)
    - [X] [T-Motor Combo F7 HD FC + F55A PRO II](https://www.drone-fpv-racer.com/t-motor-combo-f7-hd-fc-f55a-pro-ii-5548.html)
    - [X] [TBS Motor Steele Ethix Stout V3](https://www.drone-fpv-racer.com/tbs-moteur-steele-ethix-stout-v3-5183.html)
    - [X] [TBS Tracer Nano RX](https://www.drone-fpv-racer.com/tbs-tracer-micro-tx-6960.html)
    - [X] [Cable U.FL TBS Unify Pro/HV SMA](https://www.drone-fpv-racer.com/cable-d-antenne-ufl-pour-tbs-unify-pro-899.html)
    - [X] [Caddx Vista HD System](https://www.drone-fpv-racer.com/caddx-vista-hd-system-5821.html) (see improvement notes below)
    - [X] [Apex HD CAMERA SIDE PLATE KIT](https://www.drone-fpv-racer.com/apex-hd-camera-side-plate-kit-5208.html) (see improvement notes below)
    - [X] [20cm Coaxial Cable for Caddx Vista](https://www.drone-fpv-racer.com/cable-coaxial-pour-caddx-vista-6441.html) (20cm !)
    - [X] [Support XT60 on standoff - TPU by DFR](https://www.drone-fpv-racer.com/support-xt60-sur-entretoise-tpu-by-dfr-6044.html)
- [X] [HQProp ETHIX P3 Peanut Butter & Jelly 5.1x3x3 - PC (2x CW + 2xCCW)](https://www.drone-fpv-racer.com/hqprop-ethix-p3-peanut-butter-jelly-51x3x3-pc-2x-cw-2xccw-6886.html)
- [X] [TrueRC Singularity 5.8GHz SMA - LHCP](https://www.drone-fpv-racer.com/antenne-truerc-singularity-58ghz-sma-lhcp-5469.html)
- [X] [Strap Lipo KEVLAR 240x16mm - DFR](https://www.drone-fpv-racer.com/strap-lipo-kevlar-antiderapant-240x16mm-dfr-3155.html)

## Notes pour améliorations futures

- [ ] Passer sur le [Caddx Nebula Pro Vista Kit](https://caddxfpv.com/collections/%E5%B0%81%E9%9D%A2%E5%88%86%E7%B1%BB-hd-digital-cameras/products/nebula-pro-vista-kit-720p-120fps-low-latency-hd-digital-fpv-system) pour ne plus dépendre du [Apex HD CAMERA SIDE PLATE KIT](https://www.drone-fpv-racer.com/apex-hd-camera-side-plate-kit-5208.html) et gagner 3 grammes et quelques euros ?
- [ ] Remplacer le capacitor de l'ESC par des diodes TVS [RUSHFPV RUSH BLADE Power Filter Board](https://www.drone-fpv-racer.com/rushfpv-rush-blade-power-filter-board-7437.html)

## Build steps

### Frame assembly

Suivre le [guide officiel de ImpulseRC](http://apex-docs.impulserc.com/) pour assembler la frame.

![Apex Base Kit](images/apex_kit.jpg)

### Caddx Vista on the 20x20 rear mounting holes

!!! note
    Vous aurez besoin de 4 longues vis M2 non incluses dans le kit. Les écrous sont cependant ceux fournis avec le kit.

![Apex Base Kit 20x20 Caddx Vista screws](images/IMG_20210108_145719.jpg)

![Apex Base Kit 20x20 Caddx Vista mounted](images/IMG_20210108_220902.jpg)

Le **câble de 20cm pour Caddx Vista** est mieux protégé que celui d'origine.

![Apex Base Kit 20x20 Caddx Vista cable](images/IMG_20210109_171121.jpg)

### Caddx Vista VTX antenna mounting

Utiliser le câble **U.FL TBS Unify Pro/HV SMA** avec le **sabot Apex fourni** fixé à l'arrière pour l'antenne.

![Apex Base Kit 20x20 Caddx Vista antenna mount](images/IMG_20210109_172100.jpg)

![Apex Base Kit 20x20 Caddx Vista antenna mount back](images/IMG_20210109_172120.jpg)

### ESC and XT60 mounting

N'ayez pas peur de couper fort les câbles de la prise XT60 : son support TPU va sécuriser le câble contre l'arrachement sur l'entretoise.

![Apex Base Kit XT60 cable cut](images/IMG_20210109_173831.jpg)

!!! warning
    Notez bien que **l'ESC est monté à l'envers** afin d'utiliser l'espace disponible à l'avant pour placer le capacitor. Vous devrez réallouer les ressources moteurs dans la CLI (voir la section betaflight ci-après).

![Apex Base Kit ESC mount view](images/IMG_20210109_180115.jpg)

![Apex Base Kit ESC mount view side](images/IMG_20210109_180129.jpg)

![Apex Base Kit ESC mount view top](images/IMG_20210109_180145.jpg)

### RX wiring

Aucune surprise dans le branchement du TBS Tracer Nano RX !

![Apex Base Kit TBS Tracer RX wiring](images/tmotor_f7_pro2_hd_tbs_tracer_wiring.jpe)

![Apex Base Kit FC mount view](images/IMG_20210109_181018.jpg)

### FC mounting

Utilisez le câble FC-vers-ESC fourni le plus long (cela passe parfaitement, attention il y a un sens) et connectez la Caddx Vista.

![Apex Base Kit FC mount view](images/IMG_20210109_180958.jpg)

![Apex Base Kit FC mount view focus](images/IMG_20210109_181052.jpg)

### RX placement

Une fois protégé, le RX tient sur le Caddx Vista grâce à du scotch double face.

![Apex Base Kit RX mount view](images/IMG_20210109_183016.jpg)

Les antennes Tracer Immortal T tiennent bien : une est zippée sur le sabot de la plate du bas fourni et l'autre tient fermement dans le trou du sabot VTX du haut.

![Apex Base Kit RX mount view back](images/IMG_20210109_183056.jpg)

![Apex Base Kit RX mount view fixed](images/IMG_20210110_114913.jpg)

### Finishing the build

Finissez le build en plaçant la top plate et les caches en plastiques sur les bras fournis.

![Apex Base Kit RX mount view fixed](images/IMG_20210110_114900.jpg)

## Betaflight configuration

- Betaflight target: **TMTR/TMOTORF7(STM32F7X2)**

Ports:

![Apex Build Betaflight ports](images/2021-02-03-215841_1688x260_scrot.png)

Bi-directional DShot is enabled and supported natively by the BLHeli32 ESC:

![Apex Build Betaflight config](images/2021-02-03-215828_1663x1431_scrot.png)

Filter settings to accomodate the bi-directional DShot:

![Apex Build Betaflight filter config](images/2021-02-03-215759_1674x652_scrot.png)

Modes:

![Apex Build Betaflight modes](images/2021-02-03-215725_1688x390_scrot.png)

Joshua Bardwell's OSD for DJI FPV Google settings:

![Apex Build Betaflight OSD](images/2021-02-03-220958_370x353_scrot.png)

### Motor resource reallocation

Comme l'ESC a été monté à l'envers il est nécessaire de repositionner les moteurs dans la CLI. Selon votre montage, les ID peuvent changer.

```
# resources
resource MOTOR 1 B01
resource MOTOR 2 B00
resource MOTOR 3 C07
resource MOTOR 4 C06
save
```

### Minimal CLI diff

CLI diff de la configuration minimale sans tuning approfondi pour l'instant. Ca vol déjà super bien mais j'ajouterai une section à ce guide lorsque j'ajusterai le tuning.

```
# 
# Building AutoComplete Cache ... Done!
# 
# diff all

# version
# Betaflight / STM32F7X2 (S7X2) 4.2.6 Jan  5 2021 / 19:08:42 (a4b6db1e7) MSP API: 1.43
# config: manufacturer_id: TMTR, board_name: TMOTORF7, version: e02dd6f2, date: 2020-11-04T11:31:26Z

# start the command batch
batch start

# reset configuration to default settings
defaults nosave

board_name TMOTORF7
manufacturer_id TMTR
mcu_id 002f00263338510639393832
signature 

# resources
resource MOTOR 1 B01
resource MOTOR 2 B00
resource MOTOR 3 C07
resource MOTOR 4 C06

# feature
feature -RX_PARALLEL_PWM
feature RX_SERIAL
feature TELEMETRY

# beacon
beacon RX_LOST
beacon RX_SET

# serial
serial 1 1 115200 57600 0 115200
serial 4 64 115200 57600 0 115200

# aux
aux 0 0 0 1800 2100 0 0
aux 1 1 2 1300 1700 0 0
aux 2 13 1 1300 2100 0 0
aux 3 35 2 1800 2100 0 0

# master
set gyro_lowpass2_hz = 375
set dyn_notch_width_percent = 0
set dyn_notch_q = 250
set dyn_notch_min_hz = 90
set dyn_notch_max_hz = 350
set dyn_lpf_gyro_min_hz = 300
set dyn_lpf_gyro_max_hz = 750
set acc_calibration = 26,3,238,1
set min_check = 1000
set rssi_channel = 12
set serialrx_provider = CRSF
set dshot_bidir = ON
set motor_pwm_protocol = DSHOT600
set small_angle = 180
set osd_vbat_pos = 257
set osd_rssi_pos = 2486
set osd_rssi_dbm_pos = 161
set osd_tim_1_pos = 353
set osd_tim_2_pos = 321
set osd_flymode_pos = 2241
set osd_throttle_pos = 313
set osd_vtx_channel_pos = 193
set osd_craft_name_pos = 33
set osd_gps_speed_pos = 2209
set osd_gps_lon_pos = 2081
set osd_gps_lat_pos = 2049
set osd_gps_sats_pos = 2113
set osd_home_dir_pos = 2275
set osd_home_dist_pos = 2145
set osd_flight_dist_pos = 184
set osd_altitude_pos = 2177
set osd_warnings_pos = 2441
set osd_avg_cell_voltage_pos = 2516
set osd_disarmed_pos = 2411
set osd_flip_arrow_pos = 65
set osd_core_temp_pos = 248
set osd_log_status_pos = 97
set osd_gps_sats_show_hdop = OFF

profile 0

# profile 0
set dyn_lpf_dterm_min_hz = 105
set dyn_lpf_dterm_max_hz = 255
set dterm_lowpass2_hz = 225
set d_pitch = 32
set d_roll = 30
set d_min_roll = 0
set d_min_pitch = 0

profile 1

profile 2

# restore original profile selection
profile 0

rateprofile 0

rateprofile 1

rateprofile 2

rateprofile 3

rateprofile 4

rateprofile 5

# restore original rateprofile selection
rateprofile 2

# save configuration
save
```