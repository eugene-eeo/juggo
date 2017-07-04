from collections import deque


def vectors_eq(A, B):
    for a, b in zip(A, B):
        if a is None or b is None:
            continue
        if a != b:
            return False
    return True


def verify(state, max_caps):
    for u, limit in zip(state, max_caps):
        if u < 0 or u > limit:
            return False
    return True


def set_t(i, val):
    def l(state):
        v = state[:]
        v[i] = val
        return v
    return l


def pour_t(i, j, cap):
    def l(state):
        v = state[:]
        v[i] = min(v[i] + v[j], cap)
        v[j] = 0
        return v
    return l


def fill_t(i, j, cap):
    def l(state):
        v = state[:]
        v[j] = v[j] - (cap - v[i])
        v[i] = cap
        return v
    return l


def generate_ops(max_caps):
    ops = []
    for i, cap in enumerate(max_caps):
        ops.extend([
            ('fill %s' % (cap,),  set_t(i, cap)),
            ('empty %s' % (cap,), set_t(i, 0)),
        ])
    for i, cap in enumerate(max_caps):
        for j, cap2 in enumerate(max_caps):
            if i == j:
                continue
            ops.extend([
                (
                    'pour %s to %s' % (cap2, cap),
                    pour_t(i, j, cap),
                ),
                (
                    'fill %s with %s' % (cap, cap2),
                    fill_t(i, j, cap),
                ),
            ])
    return ops


def search(initial, target, ops, max_caps):
    q = deque([(initial, [None])])
    while q:
        state, path = q.popleft()
        if vectors_eq(state, target):
            return path[1:]
        for label, op in ops:
            if label == path[-1]: # no progress
                continue
            vec = op(state)
            if vec == state: # no progress
                continue
            if verify(vec, max_caps):
                q.append([
                    vec,
                    path + [label],
                ])
    return []
