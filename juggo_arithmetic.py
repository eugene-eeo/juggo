from juggo import generate_ops, verify


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



def path(m, n, d):
    """
    Finds the sequence of operations to get from
    (0, 0) to (0, d). Uses the solve(m, n, d)
    function.
    """
    vec = (0, 0)
    ops = generate_ops((m, n))
    seq = solve(m, n, d)
    prev = 0

    def find(k, vec):
        for label, op in ops:
            v = op(vec)
            if v != vec and sum(v) == k and verify((m, n), v):
                return label, v
        return False, False

    for k in seq:
        label, v = find(k, vec)
        # if the curent sum cannot be reached via the previous operations,
        # find the state with an equivalent previous sum first
        if not label:
            label, vec = find(prev, vec)
            yield label, vec
            label, v = find(k, vec)

        yield label, v
        vec = v
        prev = k

    if vec[1] != d:
        label, vec = find(d, vec)
        yield label, vec
