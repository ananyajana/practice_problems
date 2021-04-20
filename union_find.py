''' union-find algorithm to detect cycle in a undirected graph
we have one edge for any two vertex i.e. 1-2 is either 1-2 or
2-1 but not both'''
# https://www.geeksforgeeks.org/union-find/

from collections import defaultdict

# This class representa a undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset associated with an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # A utility funciton to do the union of two subsets
    def union(self, parent, x, y):
        parent[x] = y
        
    # the main function to check whether a given graph contains a cycl or not
    def is_cyclic(self):
        # Allocate memory for creating V subsets and initialize
        # all subsets as a single element sets
        parent = [-1]*(self.V)

        # iterate though all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is a cycle in the graph
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)

# create a graph given in the above diagram
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.is_cyclic():
    print('Graph contains cycle')
else:
    print('Graph does not contain cycle')
