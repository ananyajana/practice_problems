from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency list
        self.V = vertices   # No. of verties

    # function to add edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topological sort
    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # the function to do topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function ti store topological
        # sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # print contents of the stack
        # list[<start>:<stop>:<step>]
        print(stack[::-1])

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print('following is a topological sort of the given graph')
g.topologicalSort()


        
    
        

