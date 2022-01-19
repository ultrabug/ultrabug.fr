# ExpressLRS

## My usual settings

- 250Hz packet rate
- 100mW power
- ADC filtering off in Radio (Sys / Hardware)

## RSSI in DJI OSD setup

You need Betaflight 4.2+ to format the new RFMD:LQ% in the LQ OSD element.

- On Betaflight configuration tab, disable **RSSI_ADC**
- On Betaflight receiver tab, **set RSSI Channel to AUX 12**

!!! note
    AUX12/ch16 is set as the "RSSI Channel" - Displays the RSSI dBm scaled as a percentage from the current Sensitivity Limit to -50dBm and is a decent indicator of how much range is left before the LQI cliff (0 here = Sensitivity Limit).

- On Betaflight OSD, activate the **RSSI** element, you can setup a warning to something like 30 since the AUX12 is a percentage trying to tell you how much range is left on your link.

## LQ warning thresholds setup

- On the radio, get to the ELRS Lua script
- Check your packet rate setting, you'll see a dbm threshold in parenthesis (say 108dBm for 250Hz for example)
- On Betaflight OSD, activate **RSSI dBm** warning
- On Betaflight CLI, set the RSS dBm alarm to the dBm threshold from your package rate + 10 (-108 + 10 = -98 in our example)

```
set osd_rssi_dbm_alarm = -98
save
```

!!! note
    There is no real low threshold for LQ since it greatly depends on what you fly and how acceptable it is for you that some of your packets do not get through.

## HappyModel EP2

### Is your ceramic antenna defective?

- Switch your power to 10mW on the radio
- Get your radio and receiver about 1 meter away
- On your radio, get to your Telemetry page, the **1RSS** sensor value should be **no worse than 60-65 dB**
- Of course, the lower the dB the better
