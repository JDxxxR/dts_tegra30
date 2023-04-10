

def export_dts(matched, _path, export_func):
    dts = ''
    for found in matched:
        res = export_func(found)
        dts += res
    
    with open(_path, 'wt') as dts_file:
        dts_file.writelines(dts)
