from graph import Graph

def dfs(g, u, visited):

  """ 
  g: graph
  u: start vertex
  visited: {v: e, ...} visited vertices and the edge that was 
  used to visit them (tree edge)
  """

  for e in g.incident_edges(u):
    v = e.opposite(u)

    if v not in visited:
      visited[v] = e

      dfs(g, v, visited)


def reconstuct_path(g, u, v):

  visited = {u: None}
  dfs(g, u, visited)
  path = []
  if v in visited:    # v is reachable from u

    walk = v
    path.append(v)
    while walk is not u:
      e = visited[walk]
      parent = e.opposite(walk)
      path.append(parent)
      walk = parent
    
    path.reverse()

  return path


if __name__ == "__main__":
  g = Graph()
  va = g.insert_vertex('a')
  vs = g.insert_vertex('s')
  vz = g.insert_vertex('z')
  vx = g.insert_vertex('x')
  vd = g.insert_vertex('d')
  vc = g.insert_vertex('c')
  vf = g.insert_vertex('f')
  vv = g.insert_vertex('v')
  g.insert_edge(va, vs)
  g.insert_edge(va, vz)
  g.insert_edge(vs, vx)
  g.insert_edge(vx, vd)
  g.insert_edge(vx, vc)
  g.insert_edge(vd, vc)
  g.insert_edge(vd, vf)
  g.insert_edge(vc, vf)
  g.insert_edge(vc, vv)
  g.insert_edge(vf, vv)


  # Depth first search
  visited = {va: None}
  dfs(g, va, visited)


  # path from vertex u to vertex v
  path = reconstuct_path(g, vz, vc)

  print([v.element() for v in path])
