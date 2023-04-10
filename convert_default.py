#!/usr/bin/env python3

from model.Default import Default, writeOut

from converters.common.dedup import dedup

from converters.common.pingroups import replace_invalid_pingroups
from converters.common.function import replace_invalid_functions

from export.common.exportdts import export_dts
from export.export_default import export


def main():
    defaults = Default.createFrom('boards/picassomf/defaultmux.c')

    # match pingroups
    replace_invalid_pingroups(defaults)

    # match functions
    replace_invalid_functions(defaults)
    writeOut(defaults, 'debug.default.json')
    
    # deduplicate pingroups
    matched = dedup(defaults, lambda first, second: second.func == first.func and second.pupd == first.pupd and second.tristate == first.tristate and second.io == first.io)

    # export
    export_dts(matched, 'default.dts', export)

if __name__ == '__main__':
    main()
