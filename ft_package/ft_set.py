## replace value from old to new one
def replace(s, new, old):
    s.discard(old)
    s.add(new)