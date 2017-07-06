def vectors_eq(A, B):
    for a, b in zip(A, B):
        if a is None or b is None:
            continue
        if a != b:
            return False
    return True


def verify(max_caps, state):
    for u, limit in zip(state, max_caps):
        if u < 0 or u > limit:
            return False
    return True


def set_t(i, val):
    def l(state):
        v = list(state[:])
        v[i] = val
        return tuple(v)
    return l


def pour_t(i, j, cap):
    def l(state):
        v = list(state[:])
        v[i] = min(v[i] + v[j], cap)
        v[j] = 0
        return tuple(v)
    return l


def fill_t(i, j, cap):
    def l(state):
        v = list(state[:])
        v[j] = v[j] - (cap - v[i])
        v[i] = cap
        return tuple(v)
    return l


def generate_ops(max_caps):
    ops = []
    for i, cap in enumerate(max_caps):
        ops.extend([
            set_t(i, cap),  # fill v[i]
            set_t(i, 0),    # empty v[i]
        ])
    for i, cap in enumerate(max_caps):
        for j, cap2 in enumerate(max_caps):
            if i == j:
                continue
            ops.extend([
                pour_t(i, j, cap), # pour v[j] to v[i]
                fill_t(i, j, cap), # fill v[i] to max with v[j]
            ])
    return ops
