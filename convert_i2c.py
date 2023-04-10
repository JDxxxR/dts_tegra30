#!/usr/bin/env python3

from model.I2Cmux import I2Cmux
from converters.common.pingroups import replace_invalid_pingroups
from converters.common.function import replace_invalid_functions
from model.exporter.exporter import writeOut
from converters.common.dedup import dedup
from export.common.exportdts import export_dts
from export.export_i2c import export


def main():
    i2cs = I2Cmux.createFrom('boards/picassomf/i2cmux.c')
    replace_invalid_pingroups(i2cs)
    replace_invalid_functions(i2cs)
    writeOut(i2cs, 'i2cmux.json')

    matched = dedup(i2cs, lambda first, second: first.func == second.func and first.pupd == second.pupd and first.tristate == second.tristate and first.io == second.io and first.lock == second.lock and first.od == second.od)

    export_dts(matched, 'i2cmux.dts', export)
    
if __name__ == '__main__':
    main()
