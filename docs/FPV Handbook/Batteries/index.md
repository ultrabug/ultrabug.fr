# Batteries notes

!!! danger
    LiPo batteries are **dangerous** and can catch fire when they are damaged
    or badly maintained. What is written here is meant as a quick reminder and
    does not replace a fully comprehensive guide on battery management.

## Calculating charging amperage

The safest amperage to charge a battery pack is `1C` that we calculate by
taking its mAh rating divided by 1000.

Quick examples of `1C` calculation:

- 1500 mAh battery = 1500 / 1000 = 1.5A charge
- 850 mAh battery = 850 / 1000 = 0.8A or 0.9A charge

If you're in a hurry, you can charge at `2C` which is basically twice the
amperage you calculated above but do not do it too often.

## Parallel charging reminder

!!! warning
    All batteries charged in parallel **should have the same cell count**!

- Preferably parallel charge batteries of the same brand and model.
- Batteries cells voltage should not diverge from more than 0.1V per cell.
  This means that the **sum of the cell voltage difference should not exceed
  0.1 x (cell count)**.
- **Plug in the XT60 plug first on the parallel charging board**, then the
  balance lead.
- After you plug your batteries in the parallel charging board, allow a few
  minutes for them to settle as some current will naturally distribute over
  them.
- The calculation of charging amperage should be multiplied by the number of
  batteries being charged in parallel but should not exceed 1C per battery.
