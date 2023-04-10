
from json import dumps, loads

def writeOut(res, path):
    print(f'writing to {path}')
    result = []
    for token in res:
        result.append(token.export())
    result = dumps(result, indent=4)
    with open(path, 'wt') as fd:
        # pp = PrettyPrinter(indent=4, stream=fd)
        # pp.pprint(result)
        fd.writelines([result])

__all__ = [
    writeOut,
]
