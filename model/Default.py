from re import sub
from json import dumps, loads
from pprint import PrettyPrinter
from model.exporter.exporter import writeOut

'''
.pingroup	= TEGRA_PINGROUP_##_pingroup,
.func		= TEGRA_MUX_##_mux,
.pupd		= TEGRA_PUPD_##_pupd,
.tristate	= TEGRA_TRI_##_tri,
.io
'''
class Default:

    def __init__(self, pingroup, func, pupd, tristate, io):
        self.pingroup = pingroup
        self.func = func
        self.pupd = pupd
        self.tristate = tristate
        self.io = io
        

    @staticmethod
    def createFrom(_file):
        with open(_file, 'rt') as fd:
            lines = fd.readlines()
            result = []
            for line in lines:
                res = line.split('DEFAULT_PINMUX(')
                res = res[1].split('),\n')
                res = res[0]
                res = sub(r'\s*', '', res)
                res = res.split(',')

                pingroup, func, pupd, tristate, io = res
                result.append(
                    Default(
                        pingroup=pingroup,
                        func=func,
                        pupd=pupd,
                        tristate=tristate,
                        io=io
                    )
                )
            return result


    def export(self):
        return {
            'pingroup': self.pingroup,
            'func': self.func,
            'pupd': self.pupd,
            'tristate': self.tristate,
            'io': self.io,
        }

    def __str__(self):
        return dumps(self.export())

def import_default(_path):
    entries = []
    with open(_path, 'rt') as fd:
        res = load(fd)

        for token in res:
            d = Default(
                pingroup=token['pingroup'],
                func=token['func'],
                pupd=token['pupd'],
                tristate=token['tristate'],
                io=token['io']
            )
            entries.append(d)
    return entries
