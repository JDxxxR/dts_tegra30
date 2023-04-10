from export.common.shared import replace_hsm, replace_schmitt, format_pins, replace_lpm, replace_slew_rate

def export(_drive):

    first_pin = _drive.pingroup[0]
    pins = format_pins(_drive.pingroup)
    hsm = replace_hsm(_drive.hsm)
    schmitt = replace_schmitt(_drive.schmitt)
    lpm = replace_lpm(_drive.drive)
    pull_down = _drive.pull_down
    pull_up = _drive.pull_up
    rising = replace_slew_rate(_drive.slew_rising)
    falling = replace_slew_rate(_drive.slew_falling)

    return f'''
{first_pin} {'{'}
    nvidia,pins = {pins};
    nvidia,high-speed-mode = <{hsm}>;
    nvidia,schmitt = <{schmitt}>;
    nvidia,low-power-mode = <{lpm}>;
    nvidia,pull-down-strength = <{pull_down}>;
    nvidia,pull-up-strength = <{pull_up}>;
    nvidia,slew-rate-rising = <{rising}>;
    nvidia,slew-rate-falling = <{falling}>;
{'}'};
'''
