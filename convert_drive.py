#!/usr/bin/env python3

from model.Drive import Drive
from converters.common.drive import replace_invalid_drive
from converters.common.function import replace_invalid_functions
from model.exporter.exporter import writeOut
from converters.common.dedup import dedup
from export.common.exportdts import export_dts
from export.export_drive import export

def main():
    drives = Drive.createFrom('boards/picassomf/drive.c')
    replace_invalid_drive(drives)
    # does not have a function

    matched = dedup(drives, lambda first, second: first.hsm == second.hsm and first.schmitt == second.schmitt and first.drive == second.drive and first.pull_down == second.pull_down and first.pull_up == second.pull_up and first.slew_rising == second.slew_rising and first.slew_falling == second.slew_falling)

    writeOut(matched, 'drive.json')
    export_dts(matched, 'drive.dts', export)


if __name__ == '__main__':
    main()
