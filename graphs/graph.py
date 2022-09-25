class Graph:

    class Vertex:

        ___slots__ = "_element"

        def __init__(self, element=None):
            self._element = element

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

        # def __repr__(self):
        #     return f'{self._element}'


    class Edge:
        __slots__ = "_origin", "_destination", "_element"

        def __init__(self, origin, destination, element=None):
            self._origin = origin
            self._destination = destination
            self._element = element

        def element(self):
            return self._element

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):

            return self._origin if v is self._destination else self._destination

        def __hash__(self):
            return hash((self._origin, self._destination))

        # def __repr__(self):
        #     return f'({self._origin._element}, {self._destination._element})'

    def __init__(self, directed=False):
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing

    def is_directed(self):
        return self.outgoing is not self.incoming

    def vertex_count(self):
        return len(self.outgoing)

    def edge_count(self):
        count = sum(len(v) for v in self.outgoing.values())

        return count if self.is_directed() else count // 2

    def vertices(self):
        return self.outgoing.keys()

    def edges(self):
        result = set()
        
        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
            
        return result

    def get_edge(self, u, v):
        return self.outgoing[u].get(v)  # return None if not adjacent

    def degree(self, v, out=True):
        # if out is True, and the graph is directed
        # return the number (degree) of the outgoing edges
        return len(self.outgoing[v]) if out else len(self.incoming[v])

    def incident_edges(self, v, outgoing=True):
        # if out is True, and the graph is directed
        # return outgoing edges
        adj = self.outgoing if outgoing else self.incoming

        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x):
        v = self.Vertex(x)
        self.outgoing[v] = {}
        self.incoming[v] = {}

        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self.outgoing[u][v] = e
        self.incoming[v][u] = e

    def remove_vertex(self, v):
        self.outgoing.pop(v)
        self.incoming.pop(v, None)  # if directed

        for _v in self.vertices():
            for destination in list(self.outgoing[_v]):
                if destination is v:
                    del self.outgoing[_v][v]

    def remove_edge(self, e):
        origin, destination = e.endpoints()
        del self.outgoing[origin][destination]
        del self.outgoing[destination][origin]


if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)

    g.insert_edge(v1, v2, 1.2)
    g.insert_edge(v1, v3, 1.3)
    g.insert_edge(v2, v3, 2.3)

    # remove
    g.remove_edge(g.get_edge(v1, v2))
    g.remove_edge(g.get_edge(v1, v3))
    g.remove_vertex(v1)

    for v in g.vertices():
        print(v.element())

    for e in g.edges():
        print(e.element())

    print(g.vertex_count())
    print(g.edge_count())

