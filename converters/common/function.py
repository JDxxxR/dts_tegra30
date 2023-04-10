from converters.common.exceptions.exceptions import MatchedTwice, NoMatch
from spec.functions import t30 as functions

def match_function(_func):
    func = _func.lower()
    found = ''
    for f in functions:
        if f == func:
            found = f

    if not bool(found):
        print(f'token {func} not found')
        raise NoMatch()

    return found

def replace_invalid_functions(entries):
    for entry in entries: # TODO: doublecheck if it matches for your board too
        if entry.func == 'RSVD':
            entry.func = 'rsvd1'

        if entry.func == 'RSVD0':
            entry.func = 'hdmi'

        entry.func = match_function(entry.func)

__all__ = [
    replace_invalid_functions,
]
