from collections import defaultdict

# This class represents a directed graph using
# the adjacency list representation

# we need to capture the condition when one node
# what would happen if there is loop in the graph and
# we run dfs or bfs?
class Graph:
    # Constructor
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices #No. of vertices
        # default dictionary to store the grpah
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        # add u to v_s list
        self.graph[u].append(v)

        # add V to _s list
        self.graph[v].append(u)

    # A recursive function that uses
    # visited[] and parent to detect
    # cycle in subgraph reachable from vertex v
    def isCyclicUtil(self, v, visited, parent):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not
            # visited then recurse on it
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v):
                    return True

            # If an adjacent vertex is visited and not parent
            # of current vertex. then there is a cycle
            elif parent != i:
                return True
        return False

    # Returns true if the graph
    # contains a cycle, else false.
    def isCyclic(self):
    
        # Mark all the vertices
        # as not visited
        visited = [False] * (self.V)

        # Call the recursive helpper
        # function to detect cycle in a different DFS tree
        for i in range(self.V):
            # Don't recur fo ru if it is already visited
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, -1) == True:
                    return True
        return False
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

print('Following is the DFS from (starting from vertex 2)')
if g.isCyclic():
    print('contains cycle')
else:   
    print('contains no cycle')

g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
if g1.isCyclic():
    print('contains cycle')
else:   
    print('contains no cycle')
