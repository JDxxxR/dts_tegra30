from json import dumps, loads
from re import sub
from model.exporter.exporter import writeOut

'''
#define I2C_PINMUX(_pingroup, _mux, _pupd, _tri, _io, _lock, _od)	\
	{																\
		.pingroup	= TEGRA_PINGROUP_##_pingroup,					\
		.func		= TEGRA_MUX_##_mux,								\
		.pupd		= TEGRA_PUPD_##_pupd,							\
		.tristate	= TEGRA_TRI_##_tri,								\
		.io		= TEGRA_PIN_##_io,									\
		.lock		= TEGRA_PIN_LOCK_##_lock,						\
		.od		= TEGRA_PIN_OD_##_od,								\
		.ioreset	= TEGRA_PIN_IO_RESET_DEFAULT,					\
	}
'''

class I2Cmux:
    def __init__(self, pingroup, func, pupd, tristate, io, lock, od):
        self.pingroup = pingroup
        self.func = func
        self.pupd = pupd
        self.tristate = tristate
        self.io = io
        self.lock = lock
        self.od = od

    @staticmethod
    def createFrom(_file):
        with open(_file, 'rt') as fd:
            lines = fd.readlines()
            result = []
            for line in lines:
                res = line.split('I2C_PINMUX(')
                res = res[1].split('),\n')
                res = res[0]
                res = sub(r'\s*', '', res)
                res = res.split(',')

                pingroup, func, pupd, tristate, io, lock, od = res

                result.append(
                    I2Cmux(pingroup, func, pupd, tristate, io, lock, od)
                )
        return result


    def export(self):
        return {
            'pingroup': self.pingroup,
            'func': self.func,
            'pupd': self.pupd,
            'tristate': self.tristate,
            'io': self.io,
            'lock': self.lock,
            'od': self.od
        }

    def __str__(self):
        return dumps(self.export())
