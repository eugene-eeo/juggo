from collections import deque
from .utils import generate_ops, verify, vectors_eq


def all_paths(initial, max_caps):
    ops = generate_ops(max_caps)
    q = deque([[initial]])
    seen = set([initial])
    while q:
        path = q.popleft()
        u = path[-1]
        for op in ops:
            v = op(u)
            if v == u or v in seen: # no progress
                continue
            if verify(max_caps, v):
                seen.add(v)
                p = path + [v]
                q.append(p)
                yield u, v, p
    return []


def search(initial, max_caps, target):
    for _, vector, path in all_paths(initial, max_caps):
        if vectors_eq(vector, target):
            return path
