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

    # A function used by DFS
    def DFSUtil(self, v, visited):

        #print('In DFSUtil')
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all vertices
        # adjacent to this vertes
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # the function to do DFS traversal. It uses
    # recursive DFSUtil
    def DFS(self, v):

        print('In DFS')
        # create a set to store the visited vertices
        visited = set()

        # call the recursive helper function
        # to print the DFS traversal
        self.DFSUtil(v, visited)

        # Driver code

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
g.DFS(2)
print('g[{}]: {} '.format(0, g.neighbors(0)))
print('g[{}]: {} '.format(1, g.neighbors(1)))
print('g[{}]: {} '.format(2, g.neighbors(2)))
print('g[{}]: {} '.format(3, g.neighbors(3)))
