# python program to print BFS traversal
# from a given source vertes. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph using
# the adjacency list representation

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store the grpah
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by BFS
    def BFS(self, s):
        
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # create a queue for BFS
        queue = []
    
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # vertex has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def neighbors(self, v):
        return self.graph[v]

g = Graph()
print('graph is : ', g)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print('Following is the DFS from (starting from vertex 2)')
g.BFS(2)
print('g[{}]: {} '.format(0, g.neighbors(0)))
print('g[{}]: {} '.format(1, g.neighbors(1)))
print('g[{}]: {} '.format(2, g.neighbors(2)))
print('g[{}]: {} '.format(3, g.neighbors(3)))
