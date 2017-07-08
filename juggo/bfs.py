from collections import deque
from .utils import generate_ops, verify, vectors_eq


def all_paths(initial, limits):
    ops = list(generate_ops(limits))
    q = deque([[initial]])
    seen = set([initial])
    while q:
        path = q.popleft()
        u = path[-1]
        for op in ops:
            v = op(u)
            if v == u: # no progress
                continue
            if verify(limits, v) and v not in seen:
                seen.add(v)
                p = path + [v]
                q.append(p)
                yield u, v, p
    return []


def search(initial, limits, target):
    for _, vector, path in all_paths(initial, limits):
        if vectors_eq(vector, target):
            return path
