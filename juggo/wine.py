from .utils import pour_t


def solve(m, s):
    """
    Solves the 3-Jug problem given 2 jugs of capacities *m*,
    *s*, where ``m >= s >= 1``, and ``b % 2 == 0``. Initial
    state is ``(b, 0, 0)`` where *b = m + s* and the target
    state is ``(b/2, b/2, 0)``.
    """
    assert (m + s) % 2 == 0
    assert m >= s >= 1

    # [ b', m', s' ]
    b = m + s
    b_to_s = pour_t(2, 0, s)
    s_to_m = pour_t(1, 2, m)
    m_to_b = pour_t(0, 1, b)

    def gen_cycles():
        u = (b, 0, 0)
        for _ in range(m):
            u = b_to_s(u); yield u # 1
            u = s_to_m(u); yield u # 2

            if u[1] == m:
                u = m_to_b(u); yield u # 3
                u = s_to_m(u); yield u # 4

    target = (b // 2, b // 2, 0)
    for v in gen_cycles():
        yield v
        if v == target:
            break
