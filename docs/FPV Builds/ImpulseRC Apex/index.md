# Apex 5" HD on base frame kit

## A digital HD build on the Apex Base Frame Kit

:gb: For my first DIY build ever I wanted a strong 5" frame.

I chose the **ImpulseRC Apex Base Frame Kit** because I did not want to rely on a HD specific frame and loose the space made for the DJI Air Unit.

It was quite a challenge to get everything to fit properly but I love the result and I hope you'll appreciate the density and great balance of this build.

This ends up as a compact (but not too much) build without sacrifying the space for the electronics. It is clean (to my standards at least) and very powerful.

I enjoyed working on it very much and I hope you'll get a sense of it reading this build guide. Enjoy!

![Apex HD on Base Kit overview](images/IMG_20210110_114845.jpg){: style="opacity:0.5;"}

## Hardware list

!!! note
    Those links are **NOT** affiliate links. I just share the links where I actually bought the stuff needed for this build.

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

## Notes to self for future improvements

- [ ] Switch to the [Caddx Nebula Pro Vista Kit](https://caddxfpv.com/collections/%E5%B0%81%E9%9D%A2%E5%88%86%E7%B1%BB-hd-digital-cameras/products/nebula-pro-vista-kit-720p-120fps-low-latency-hd-digital-fpv-system) so we do not need the [Apex HD CAMERA SIDE PLATE KIT](https://www.drone-fpv-racer.com/apex-hd-camera-side-plate-kit-5208.html) any more, save 3 grams and money?
- [ ] Drop the ESC capacitor and replace it with TVS diodes [RUSHFPV RUSH BLADE Power Filter Board](https://www.drone-fpv-racer.com/rushfpv-rush-blade-power-filter-board-7437.html)

## Build steps

### Frame assembly

Follow the [official ImpulseRC Apex guide](http://apex-docs.impulserc.com/) to assemble the frame.

![Apex Base Kit](images/apex_kit.jpg)

### Caddx Vista on the 20x20 rear mounting holes

!!! note
    You will need 4 long M2 screws that are not provided with the kit. Nuts are the ones provided with the kit.

![Apex Base Kit 20x20 Caddx Vista screws](images/IMG_20210108_145719.jpg)

![Apex Base Kit 20x20 Caddx Vista mounted](images/IMG_20210108_220902.jpg)

The **20cm cable for Caddx Vista** is better protected than the standard one.

![Apex Base Kit 20x20 Caddx Vista cable](images/IMG_20210109_171121.jpg)

### Caddx Vista VTX antenna mounting

Use the **U.FL TBS Unify Pro/HV SMA** cable with the **provided Apex clamp** and fix it to the rear for the antenna.

![Apex Base Kit 20x20 Caddx Vista antenna mount](images/IMG_20210109_172100.jpg)

![Apex Base Kit 20x20 Caddx Vista antenna mount back](images/IMG_20210109_172120.jpg)

### ESC and XT60 mounting

Do not fear to cut short the XT60 leads: its TPU support will strain releave the cable on the standoff.

![Apex Base Kit XT60 cable cut](images/IMG_20210109_173831.jpg)

!!! warning
    Be mindful of the fact that **the ESC mounted in reverse position**to leverage the space at the front for the capacitor. You will need to reallocate the motor resources on the CLI (see the betaflight section below).

![Apex Base Kit ESC mount view](images/IMG_20210109_180115.jpg)

![Apex Base Kit ESC mount view side](images/IMG_20210109_180129.jpg)

![Apex Base Kit ESC mount view top](images/IMG_20210109_180145.jpg)

### RX wiring

Nothing surprising here, wiring the TBS Tracer Nano RX is straightforward!

![Apex Base Kit TBS Tracer RX wiring](images/tmotor_f7_pro2_hd_tbs_tracer_wiring.jpe)

![Apex Base Kit FC mount view](images/IMG_20210109_181018.jpg)

### FC mounting

Use the longest of the provided FC-to-ESC cables (it connects perfectly, mind the wire direction) and connect the Caddx Vista.

![Apex Base Kit FC mount view](images/IMG_20210109_180958.jpg)

![Apex Base Kit FC mount view focus](images/IMG_20210109_181052.jpg)

### RX placement

Once protected, the RX is stuck on top of the Caddx Vista using double sided tape.

![Apex Base Kit RX mount view](images/IMG_20210109_183016.jpg)

The Tracer Immortal T antennas fit well: one is zip tied in the lower plate by the provided clamp and the other is passing through the remaining hole in the upper VTX clamp.

![Apex Base Kit RX mount view back](images/IMG_20210109_183056.jpg)

![Apex Base Kit RX mount view fixed](images/IMG_20210110_114913.jpg)

### Finishing the build

Finish the build by placing the top plate and the plastic provided covers on the arms.

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

Since the ESC is mounted in reverse position, the motors need to be reassigned on the CLI. Depending on your wiring, IDs may change.

```
# resources
resource MOTOR 1 B01
resource MOTOR 2 B00
resource MOTOR 3 C07
resource MOTOR 4 C06
save
```

### Minimal CLI diff

This is the minimal CLI diff that I set up without advanced tuning. It flies very well but as I will tune it better I will add a section to this build guide.

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

# rxfail
rxfail 7 s 750

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
set rssi_channel = 8
set serialrx_provider = CRSF
set dshot_bidir = ON
set motor_pwm_protocol = DSHOT600
set small_angle = 180
set osd_warn_rssi = ON
set osd_rssi_alarm = 40
set osd_vbat_pos = 257
set osd_rssi_pos = 2486
set osd_rssi_dbm_pos = 161
set osd_tim_1_pos = 353
set osd_tim_2_pos = 321
set osd_flymode_pos = 2241
set osd_throttle_pos = 313
set osd_vtx_channel_pos = 193
set osd_craft_name_pos = 33
set osd_gps_speed_pos = 161
set osd_gps_lon_pos = 33
set osd_gps_lat_pos = 1
set osd_gps_sats_pos = 65
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
