from collections import defaultdict
from graphviz import Digraph
from .utils import vectors_eq


class Node:
    def __init__(self, id, label=None):
        self.id = id
        self.label = label

    def apply(self, g):
        g.node(str(self.id), str(self.label))


class Edge:
    def __init__(self, src, dst, color='black'):
        self.src = src
        self.dst = dst
        self.color = color

    def apply(self, g):
        g.edge(
            str(self.src.id),
            str(self.dst.id),
            color=str(self.color),
            )

    def __eq__(self, other):
        return self.src == other.src and self.dst == other.dst


def pipeline(v, funcs):
    for f in funcs:
        v = f(v)
    return v


def plot(iterator):
    def count(a=[0]):
        a[0] += 1
        return a[0]

    nodes = defaultdict(lambda: Node(count()))
    edges = {}
    for u, v in iterator:
        edges[u, v] = Edge(nodes[u], nodes[v])
        nodes[u].label = repr(u)
        nodes[v].label = repr(v)

    return nodes, edges


def add_trace(color, vecs):
    def func(G):
        nodes, edges = G
        for i in range(1, len(vecs)):
            for edge in edges.values():
                if edge.src == nodes[vecs[i-1]] and edge.dst == nodes[vecs[i]]:
                    edge.color = color
        return G
    return func


def to_string(G):
    nodes, edges = G
    g = Digraph()
    for node in nodes.values(): node.apply(g)
    for edge in edges.values(): edge.apply(g)
    return str(g)
