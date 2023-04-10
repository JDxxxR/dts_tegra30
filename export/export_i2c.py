
from export.common.shared import format_pins, replace_io, replace_pupd, replace_tristate, replace_od, replace_lock


def export(_i2c):

    first_pin = _i2c.pingroup[0]
    pins = format_pins(_i2c.pingroup)
    function = _i2c.func
    pull = replace_pupd(_i2c.pupd)
    tristate = replace_tristate(_i2c.tristate)
    io = replace_io(_i2c.io)
    od = replace_od(_i2c.od)
    #lock = replace_lock(_i2c.lock)
    #nvidia,lock = <{lock}>;

    return f'''
{first_pin} {'{'}
    nvidia,pins = {pins};
    nvidia,function = "{function}";
    nvidia,pull = <{pull}>;
    nvidia,tristate = <{tristate}>;
    nvidia,enable-input = <{io}>;
    nvidia,open-drain = <{od}>;

{'}'};

'''