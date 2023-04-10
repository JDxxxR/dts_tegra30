
from spec.pingroups import t30 as pingroup
from converters.common.exceptions.exceptions import MatchedTwice, NoMatch

def match_pingroup(_token):
    token = _token.lower()
    result = ''
    is_twice = False
    for pg in pingroup:
        if pg.startswith(token + '_') or pg == token:

            if bool(result):
                is_twice = True

            result = pg

    for pg in pingroup:
        if pg == token:
            result = pg
            is_twice = False

    if is_twice:
        print(f'error the token {token} was found twice')
        raise MatchedTwice()

    if not bool(result):
        print(f'no result for token {token} was found')
        raise NoMatch()
    
    return result

def replace_invalid_pingroups(entries):
    for entry in entries:
        if entry.pingroup.startswith('GPIO_'):
            entry.pingroup = entry.pingroup.split('GPIO_')[1]
        res = match_pingroup(entry.pingroup)
        entry.pingroup = res

__all__ = [
    replace_invalid_pingroups,
]
