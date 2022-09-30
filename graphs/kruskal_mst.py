from graph import Graph
from priority_queues.binary_heap_array import HeapPQ


class Partition:
    """ A tree based implementation of the Partition data structure """
    class Position:
        __slots__ = "_element", "_parent", "_size"

        def __init__(self, e):
            self._element = e
            self._parent = self
            self._size = 1

        def element(self):
            return self._element

    def make_group(self, e):
        return self.Position(e)

    def find(self, p):
        """ Find the root node of p. """
        if p._parent != p:
            p._parent = self.find(p._parent)  # Each visited node's parent becomes the root node
        return p._parent

    def union(self, p, q):
        """ union groups containing the position p and q. """
        a = self.find(p)
        b = self.find(q)

        if a is not b:    # if edge connects vertices of different clusters
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size


def kruskal_mst(G):

    tree = []  # the resulting mst
    # add each vertex to their own cluster
    partition = Partition()
    position = {}  # a mapping from a vertex to its position
    for v in G.vertices():
        position[v] = partition.make_group(v)

    # sort edges by weights
    pq = HeapPQ()
    for e in G.edges():
        pq.add(e.element(), e)

    while not pq.is_empty():
        w_uv, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = partition.find(position[u])   # the cluster containing vertex u
        b = partition.find(position[v])   # the cluster containing vertex v
        if a != b:
            tree.append(edge)
            partition.union(a, b)

    return tree


if __name__ == "__main__":
    # Build graph with non-negative weights
    g = Graph()
    va = g.insert_vertex('a')
    vs = g.insert_vertex('s')
    vz = g.insert_vertex('z')
    vx = g.insert_vertex('x')
    vd = g.insert_vertex('d')
    vc = g.insert_vertex('c')
    vf = g.insert_vertex('f')
    vv = g.insert_vertex('v')
    g.insert_edge(va, vs, 2)
    g.insert_edge(va, vz, 3)
    g.insert_edge(vs, vx, 1)
    g.insert_edge(vx, vd, 6)
    g.insert_edge(vx, vc, 5)
    g.insert_edge(vd, vc, 1)
    g.insert_edge(vd, vf, 4)
    g.insert_edge(vc, vf, 7)
    g.insert_edge(vc, vv, 4)
    g.insert_edge(vf, vv, -11)
    mst = kruskal_mst(g)
    min_cost = sum([e.element() for e in mst])
    print("minimum cost: ", min_cost)

