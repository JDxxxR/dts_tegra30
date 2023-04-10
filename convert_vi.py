#!/usr/bin/env python3

from model.VImux import VImux
from converters.common.pingroups import replace_invalid_pingroups
from converters.common.function import replace_invalid_functions
from model.exporter.exporter import writeOut
from converters.common.dedup import dedup
from export.common.exportdts import export_dts
from export.export_vi import export

def main():
    vis = VImux.createFrom('boards/picassomf/vimux.c')
    replace_invalid_pingroups(vis)
    replace_invalid_functions(vis)

    matched = dedup(vis, lambda first, second: first.func == second.func and first.pupd == second.pupd and first.tristate == second.tristate and first.io == second.io and first.lock == second.lock and first.od == second.od and first.ioreset == second.ioreset)
    writeOut(vis, 'vimux.json')
    export_dts(matched, 'vimux.dts', export)

if __name__ == '__main__':
    main()
