_t20 = ['drive_ao1', 'drive_ao2', 'drive_at1', 'drive_at2', 'drive_cdev1', 'drive_cdev2', 'drive_csus', 'drive_dap1', 'drive_dap2', 'drive_dap3', 'drive_dap4', 'drive_dbg', 'drive_lcd1', 'drive_lcd2', 'drive_sdmmc2', 'drive_sdmmc3', 'drive_spi', 'drive_uaa', 'drive_uab', 'drive_uart2', 'drive_uart3', 'drive_vi1', 'drive_vi2', 'drive_xm2a', 'drive_xm2c', 'drive_xm2d', 'drive_xm2clk', 'drive_sdio1', 'drive_crt', 'drive_ddc', 'drive_gma', 'drive_gmb', 'drive_gmc', 'drive_gmd', 'drive_gme', 'drive_owr', 'drive_uda']

# hint: prefixed everything with `drive_` because `Documentation/devicetree/bindings/pinctrl/nvidia,tegra30-pinmux.txt` did not
# removed (because duplicated from tegra2?):
# drive_dap2 drive_ao1 drive_ao2, drive_drive_at1, drive_drive_at2, drive_drive_cdev1 drive_cdev2 drive_crt drive_csus drive_dap1 drive_dap3 drive_dap4 drive_drive_dbg drive_drive_ddc drive_gma drive_drive_gmb drive_drive_gmc drive_drive_gmd drive_drive_gme drive_lcd1 drive_drive_lcd2 drive_owr drive_sdio1 drive_spi drive_uaa drive_drive_uab drive_drive_uart2 drive_drive_uart3 drive_uda drive_drive_vi1
_t30 = ['drive_at3', 'drive_at4', 'drive_at5', 'drive_cec', 'drive_dev3', 'drive_gmf', 'drive_gmg', 'drive_gmh', 'drive_gpv', 'drive_sdio2', 'drive_sdio3']

t30 = _t20 + _t30

__all__ = [
    t30
]
