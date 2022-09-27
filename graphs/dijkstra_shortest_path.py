from graph import Graph
from priority_queues.binary_heap_array import HeapPQ


class HeapExtended(HeapPQ):

    class Locator(HeapPQ._Item):
        __slots__ = "_index"

        def __init__(self, k, v, idx):
            super().__init__(k, v)
            self._index = idx

    def swap(self, i, j):
        super().swap(i, j)
        self._data[i]._index = j
        self._data[j]._index = i

    def bubble(self, i):
        """ perform upheap or downheap bubbling """
        if i > 0 and self._data[i] < self._data[self.parent(i)]:
            self.upheap_bubble(i)
        else:
            self.downheap_bubble(i)

    def add(self, key, value):
        """ Add a key - value pair."""""
        token = self.Locator(key, value, len(self._data))   # initialize locator index
        self._data.append(token)
        self.upheap_bubble(len(self._data) - 1)
        return token

    def remove(self, loc):
        """ Remove and return the (k, v) pair identified by Locator loc. """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")

        if j == len(self) - 1:  # item at last position
            self._data.pop()  # just remove it
        else:
            self.swap(j, len(self) - 1)  # swap item to the last position
            self._data.pop()  # remove it from the list
            self.bubble(j)  # fix item displaced by the swap

        return (loc.key, loc.value)

    def update(self, loc, new_key, new_value):
        """ Replace entry at k with (new_key, new_value) """
        loc._key = new_key
        loc._value = new_value
        self.bubble(loc._index)


def dijkstra(G, s):
    """
    :arg G Graph
    :arg s Start vertex
    :return shortest distance from s to every other vertex in G
    """

    cloud = {}  # return distance map
    D = {v: float('inf') for v in G.vertices() if v is not s}
    D[s] = 0
    pqlocator = {}   # vertex to its index in the heap pq
    # Add each vertex to a priority queue (heap)
    heap = HeapExtended()

    for v, d in D.items():
        pqlocator[v] = heap.add(d, v)

    while not heap.is_empty():

        d, u = heap.remove_min()
        cloud[u] = d  # add it to shortest path container
        del pqlocator[u]
        for e in G.incident_edges(u, outgoing=True):
            v = e.opposite(u)
            if v not in cloud:

                # Edge relaxation
                if d + G.get_edge(u, v).element() < D[v]:
                    D[v] = d + G.get_edge(u, v).element()

                    # Update distance/key of vertex v in the heap
                    heap.update(pqlocator[v], D[v], v)  # old_key, new_key, new_value

    return cloud


def reconstruct_path_tree(G, s, d):
    """
        G: graph
        s: start
        d: result of dijkstra's algorithm

      return {vertex: edge that was used to access vertex (parent)}
    """
    tree = {}
    for v in d:
        if v is not s:
            for e in G.incident_edges(v, outgoing=False):  # consider incoming edges
                u = e.opposite(v)
                w_uv = e.element()
                if d[u] + w_uv == d[v]:
                    tree[v] = e   # edge e is used to reach v

    return tree


if __name__ == "__main__":

    # Build graph
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
    g.insert_edge(vf, vv, 11)

    cloud = dijkstra(g, vs)  # {vertex: shortest_distance}
    for v in cloud:
        print(f'{v.element()}: {cloud[v]}')
    print('------------------------------------')
    tree = reconstruct_path_tree(g, vs, cloud)
    for v in tree:
        print(f"{v.element()}: {tree[v].element()}")

    # Construct path (s, z)
    path = []
    v = vv
    while True:
        path.append(v)
        if v is vs:
            break
        v = tree[v].opposite(v)
    path.reverse()
    path = [v.element() for v in path]
    print(path)




