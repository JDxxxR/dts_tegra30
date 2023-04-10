from export.common.shared import format_pins, replace_io, replace_pupd, replace_tristate, replace_ioreset, replace_od, replace_lock


def export(_vimux):
    first_pin = _vimux.pingroup[0]
    pins = format_pins(_vimux.pingroup)
    function = _vimux.func
    pull = replace_pupd(_vimux.pupd)
    tristate = replace_tristate(_vimux.tristate)
    io = replace_io(_vimux.io)
    od = replace_od(_vimux.od)
    #lock = replace_lock(_vimux.lock)
    ioreset = replace_ioreset(_vimux.ioreset)

    #nvidia,lock = <{lock}>;
    return f'''
{first_pin} {'{'}
    nvidia,pins = {pins};
    nvidia,function = "{function}";
    nvidia,pull = <{pull}>;
    nvidia,tristate = <{tristate}>;
    nvidia,enable-input = <{io}>;
    nvidia,ioreset = <{ioreset}>;
{'}'};
'''
