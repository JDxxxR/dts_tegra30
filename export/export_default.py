from builtins import Exception

from export.common.shared import format_pins, replace_io, replace_pupd, replace_tristate

def export(_default):
    first_pin = _default.pingroup[0]
    pins = format_pins(_default.pingroup)
    function = _default.func
    pull = replace_pupd(_default.pupd)
    tristate = replace_tristate(_default.tristate)
    io = replace_io(_default.io)

    return f'''{first_pin} {'{'}
    nvidia,pins = {pins};
    nvidia,function = "{function}";
    nvidia,pull = <{pull}>;
    nvidia,tristate = <{tristate}>;
    nvidia,enable-input = <{io}>;
{'}'};

'''


__all__ = [
    export,
]
