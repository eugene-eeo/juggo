from collections import deque, defaultdict


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


def all_paths(initial, ops, max_caps):
    q = deque([(initial, [])])
    V = set([initial])
    while q:
        state, path = q.popleft()
        for label, op in ops:
            if path and label == path[-1]: # no progress
                continue
            vec = op(state)
            if vec == state or vec in V: # no progress
                continue
            if verify(max_caps, vec):
                V.add(vec)
                p = path + [label]
                yield state, vec, p
                q.append((vec, p))
    return []


def search(initial, target, ops, max_caps):
    for _, vector, path in all_paths(initial, ops, max_caps):
        if vectors_eq(vector, target):
            return path


class Edge:
    def __init__(self, start, end, label, color='black'):
        self.start = start
        self.end = end
        self.label = label
        self.color = color

    def __str__(self):
        return '%s -> %s [label="%s", color="%s"]' % (self.start, self.end, self.label, self.color)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def pairwise(xs):
    xs = iter(xs)
    prev = next(xs)
    for n in xs:
        yield prev, n
        prev = n


def plot(initial, target, ops, max_caps):
    def count(a=[0]):
        a[0] += 1
        return a[0]
    nodes = defaultdict(count)
    edges = []
    for u, v, path in all_paths(initial, ops, max_caps):
        edge = Edge(nodes[u], nodes[v], label=path[-1])
        found = any(e == edge for e in edges)
        if not found:
            edges.append(edge)
        if vectors_eq(v, target):
            last = nodes[v]
            for label in path[::-1]:
                for e in edges:
                    if e.label == label and e.end == last:
                        e.color = 'red'
                        last = e.start
                        break
            break
    V = ['%s [label="%s"]' % (v, k) for k, v in nodes.items()]
    E = [str(e) for e in edges]
    return V, E


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
