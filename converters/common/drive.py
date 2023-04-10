
from spec.drive import t30 as drive
from converters.common.exceptions.exceptions import MatchedTwice, NoMatch

def match_drive(_token):
    token = 'drive_' + _token.lower()
    result = ''
    for d in drive:
        if d == token:

            if bool(result):
                print(f'{result} matched twice')
                raise MatchedTwice()

            result = token
    
    if not bool(result):
        print(f'did not entry drive {_token}')
        raise NoMatch()

    return result

def replace_invalid_drive(entries):
    for entry in entries:
        res = match_drive(entry.pingroup)
        entry.pingroup = res


__all__ = [
    replace_invalid_drive,
]
