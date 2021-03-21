# kosaraju algorithm
from collections import defaultdict

# class representation of a directed graph using adjacency list
class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of verteices
        # the dictionary consists of the list of vertices connected to a vertex i
        # graph[i[ is a list of the vertices that are connected to the vertex i
        # i.e there is a directed edge from i to graph[i][0], etc
        self.graph = defaultdict(list) # default dictionary to store graph

    # function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # a function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visied
        visited[v] = True
        # REcur for all verteices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # a function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # th emain functiona that finds and prints all strongly connected
    # componenets
    def print_SCCs(self):
        stack = []
        # Mark all the vertices as not visited(for the first DFS)
        visited = [False]*(self.V)
        # Fill the vertices in the stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        # create the reversed graph
        gr = self.getTranspose()
    
        # Mark all the vertices as not visited(for second DFS)
        visited = [False] * (self.V)

        # Now process all vertices in order defined by stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print('')

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print('Following are the strongly connected components in the given graph')
g.print_SCCs()

