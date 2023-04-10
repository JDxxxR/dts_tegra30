from re import sub
from json import dumps, loads
from pprint import PrettyPrinter
from model.exporter.exporter import writeOut


'''
#define SET_DRIVE(_name, _hsm, _schmitt, _drive, _pulldn_drive, _pullup_drive, _pulldn_slew, _pullup_slew) \
	{                                               \
		.pingroup = TEGRA_DRIVE_PINGROUP_##_name,   \
		.hsm = TEGRA_HSM_##_hsm,                    \
		.schmitt = TEGRA_SCHMITT_##_schmitt,        \
		.drive = TEGRA_DRIVE_##_drive,              \
		.pull_down = TEGRA_PULL_##_pulldn_drive,    \
		.pull_up = TEGRA_PULL_##_pullup_drive,		\
		.slew_rising = TEGRA_SLEW_##_pulldn_slew,   \
		.slew_falling = TEGRA_SLEW_##_pullup_slew,	\
	}
'''

class Drive:
    def __init__(self, pingroup, hsm, schmitt, drive, pull_down, pull_up, slew_rising, slew_falling):
        self.pingroup = pingroup
        self.hsm = hsm
        self.schmitt = schmitt
        self.drive = drive
        self.pull_down = pull_down
        self.pull_up = pull_up
        self.slew_rising = slew_rising
        self.slew_falling = slew_falling

    @staticmethod
    def createFrom(_file):
        with open(_file) as fd:
            lines = fd.readlines()
            result = []
            for line in lines:
                res = line.split('SET_DRIVE(')
                res = res[1].split('),\n')
                res = res[0]
                res = sub(r'\s*', '', res)
                res = res.split(',')

                pingroup, hsm, schmitt, drive, pull_down, pull_up, slew_rising, slew_falling = res

                result.append(
                    Drive(
                        pingroup, hsm, schmitt, drive, pull_down, pull_up, slew_rising, slew_falling
                    )
                )
        return result

    def export(self):
        return {
            'pingroup': self.pingroup,
            'hsm': self.hsm,
            'schmitt': self.schmitt,
            'drive': self.drive,
            'pull_down': self.pull_down,
            'pull_up': self.pull_up,
            'slew_rising': self.slew_rising,
            'slew_falling': self.slew_falling
        }
    
    def __str__(self):
        return dumps(self.export())
