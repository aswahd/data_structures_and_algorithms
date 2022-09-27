from graph import Graph
from dijkstra_shortest_path import HeapExtended


def prim_jarnik_mst(G):
    """ Returns the edges of G such that they form a minimum spanning tree. """

    tree = []  # edges of mst
    pq = HeapExtended()  # heap ds
    d = {}  # A mapping from a vertex and its minimum distance to a vertex in the spanning tree
    pq_locator = {}   # A mapping from a vertex to its location in the priority queue

    for v in G.vertices():
        if len(d) == 0:
            d[v] = 0   # root vertex
        else:
            d[v] = float('inf')
        pq_locator[v] = pq.add(d[v], (v, None))     # (vertex, edge)

    while not pq.is_empty():
        key, e = pq.remove_min()  # get the edge and vertex with the minimum edge-weight
        u, e = e
        if e is not None:  # the root vertex doesn't have a previous edge
            tree.append(e)
        del pq_locator[u]
        # Recalculate the minimum edge-weight between u and its adjacent vertices
        for e in G.incident_edges(u):
            v = e.opposite(u)

            if v in pq_locator:
                w_uv = e.element()
                if w_uv < d[v]:
                    d[v] = w_uv
                    # update the distance key in the priority queue
                    pq.update(pq_locator[v], d[v], (v, e))
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
    g.insert_edge(vf, vv, -4)

    mst = prim_jarnik_mst(g)
    min_cost = sum([e.element() for e in mst])
    print("minimum cost: ", min_cost)
