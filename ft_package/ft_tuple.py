## replace value inside a tuple by slicing
def replace(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix + 1:]