def vectors_eq(A, B):
    for a, b in zip(A, B):
        if a is None or b is None:
            continue
        if a != b:
            return False
    return True


def verify(limits, state):
    for u, limit in zip(state, limits):
        if u < 0 or u > limit:
            return False
    return True


def set_t(i, val):
    def l(u):
        v = list(u[:])
        v[i] = val
        return tuple(v)
    return l


def pour_t(i, j, cap):
    """
    Pour from v[j] to v[i], where *cap* is the maximum
    capacity of jug *i*.
    """
    def l(u):
        v = list(u[:])
        x, y = v[i], v[j]
        if x + y > cap:
            v[i] = cap
            v[j] = x + y - cap
        else:
            v[i] = x + y
            v[j] = 0
        return tuple(v)
    return l


def generate_ops(limits):
    for i, cap in enumerate(limits):
        yield set_t(i, cap)  # fill v[i]
        yield set_t(i, 0)    # empty v[i]
    for i, cap in enumerate(limits):
        for j, _ in enumerate(limits):
            if i != j:
                # pour v[j] to v[i]
                yield pour_t(i, j, cap)
