class NoSuchPupd(Exception):
    pass

class NoSuchTristate(Exception):
    pass

class NoSuchIo(Exception):
    pass

class NoSuchLock(Exception):
    pass

class NoSuchOd(Exception):
    pass

class NoSuchIoreset(Exception):
    pass

class NoSuchHsm(Exception):
    pass

class NoSuchSchmitt(Exception):
    pass

class NoSuchDrive(Exception):
    pass

class NoSuchSlewRate(Exception):
    pass

def replace_pupd(inpt):
    if inpt == 'PULL_DOWN':
        return 'TEGRA_PIN_PULL_DOWN'
    if inpt == 'PULL_UP':
        return 'TEGRA_PIN_PULL_UP'
    if inpt == 'NORMAL':
        return 'TEGRA_PIN_PULL_NONE'
    raise NoSuchPupd()


def replace_tristate(inpt):
    if inpt == 'NORMAL':
        return 'TEGRA_PIN_DISABLE'
    if inpt == 'TRISTATE':
        return 'TEGRA_PIN_ENABLE'
    raise NoSuchTristate()

def replace_io(inpt):
    if inpt == 'INPUT':
        return 'TEGRA_PIN_ENABLE'
    if inpt == 'OUTPUT':
        return 'TEGRA_PIN_DISABLE'
    print(f'io {inpt} not found')
    raise NoSuchIo()

def replace_lock(inpt): # TODO: this is not quite correct: disable = 1 
    if inpt == 'DISABLE':
        return '0'
    if inpt == 'ENABLE':
        print('WARNING: is this plausible?', inpt)
        return '1'
    raise NoSuchLock()

def replace_od(inpt):
    if inpt == 'ENABLE':
        return 'TEGRA_PIN_ENABLE'
    if inpt == 'DISABLE':
        return 'TEGRA_PIN_DISABLE'
    raise NoSuchOd()

def replace_ioreset(inpt):
    if inpt == 'ENABLE':
        print('WARN: is this plausible?', inpt)
        return '1'
    if inpt == 'DISABLE':
        return '0'
    raise NoSuchIoreset()


def replace_hsm(inpt):
    if inpt == 'ENABLE':
        return '1'
    if inpt == 'DISABLE':
        return '0'
    print(f'not found hsm {inpt}')
    raise NoSuchHsm()

def replace_schmitt(inpt):
    if inpt == 'ENABLE':
        return 'TEGRA_PIN_ENABLE'
    if inpt == 'DISABLE':
        return 'TEGRA_PIN_DISABLE'
    raise NoSuchSchmitt()

def replace_lpm(inpt):
    if inpt == 'DIV_1':
        return 'TEGRA_PIN_LP_DRIVE_DIV_1'
    if inpt == 'DIV_2':
        return 'TEGRA_PIN_LP_DRIVE_DIV_2'
    if inpt == 'DIV_4':
        return 'TEGRA_PIN_LP_DRIVE_DIV_4'
    if inpt == 'DIV_8':
        return 'TEGRA_PIN_LP_DRIVE_DIV_8'
    raise NoSuchDrive()

def replace_slew_rate(inpt):
    if inpt == 'FASTEST':
        return 'TEGRA_PIN_SLEW_RATE_FASTEST'
    if inpt == 'FAST':
        return 'TEGRA_PIN_SLEW_RATE_FAST'
    if inpt == 'SLOWEST':
        return 'TEGRA_PIN_SLEW_RATE_SLOWEST'
    if inpt == 'SLOW':
        return 'TEGRA_PIN_SLEW_RATE_SLOW'
    raise NoSuchSlewRate()

def format_pins(pins):
    res = ''
    for index, pin in enumerate(pins):
        res += f'"{pin}"'
        if index < len(pins) -1:
            res += ', '
    return res
