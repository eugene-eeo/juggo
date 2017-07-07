from .utils import generate_ops, verify


def solve(m, n, d):
    """
    Solves mx + ny = d, where 0 < m < n and d < n.
    Returns the integer sequence.
    """
    assert 0 < m < n
    assert d < n

    k = 0
    while k != d:
        k += m
        yield k
        if k > n:
            k -= n
            yield k



def find_transforms(m, n, d):
    """
    Finds the sequence of operations to get from
    (0, 0) to (0, d). Uses the solve(m, n, d)
    function.
    """
    vec = (0, 0)
    ops = list(generate_ops((m, n)))
    seq = solve(m, n, d)
    prev = 0

    def find(k, vec):
        for op in ops:
            v = op(vec)
            if v != vec and sum(v) == k and verify((m, n), v):
                return v
        return None

    for k in seq:
        v = find(k, vec)
        # if the curent sum cannot be reached via the previous operations,
        # find the state with an equivalent previous sum first
        if v is None:
            vec = find(prev, vec)
            yield vec
            v = find(k, vec)
        yield v
        vec = v
        prev = k

    assert sum(vec) == d
    if vec != (0, d):
        yield (0, d)
