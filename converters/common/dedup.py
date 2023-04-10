
def dedup(entries, lamda_verify):
    for f in entries:
        f._used = False

    matched = [] # containes the added up things
    for entry in entries:
        if entry._used:
            continue
        matched.append(entry)
        entry.pingroup = [entry.pingroup] # remap
        for f in entries:
            if lamda_verify(entry, f) and entry is not f: # may not be the same
                f._used = True
                entry.pingroup.append(f.pingroup)
    return matched

__all__ = [
    dedup,
]
