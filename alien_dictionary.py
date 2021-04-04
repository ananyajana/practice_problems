# to find the order of elelments in alien dictionary, we would need to 
# construct a graph in this way, first create a graph of size equal to
# the alphabet size of the alient language. then for every pair of
# consecutive words i.e. word1 and word2, find the first character of mismatch
# add an edge from the first mismatch chra in word1 to the first mismatch char 
# in word2. Once the process is over, do a topological sort of the elements
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency list
        #self.V = vertices   # No. of verties
        self.V = []   # No. of verties

    # function to add edge to graph
    def addEdge(self, u, v):
        print('adding edge {}->{}'.format(u, v))
        self.graph[u].append(v)
        # if the vertex u is not already part of the vertex list then add it
        if u not in self.V:
            self.V.append(u)
        # if the vertex v is not already part of the vertex list then add it
        if v not in self.V:
            self.V.append(v)

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
        #visited = [False]*len(self.V)
        visited = {i:False for i in self.V}
        stack = []

        # Call the recursive helper function ti store topological
        # sort starting from all vertices one by one
        for i in range(len(self.V)):
            # check if the ith vertex is not visited
            if visited[self.V[i]] == False:
                self.topologicalSortUtil(self.V[i], visited, stack)

        # print contents of the stack
        # list[<start>:<stop>:<step>]
        print(stack[::-1])

#  for the words baa abd baad, how will the graph look like
# if we have a disconnected graph then the dictionayr is ambiguous?
# e.g. in this canse theA =  dictionary could be both b, a, d and d, b, a
# are both valid?
# also how many words do we need to completely specify the dictionary uniquely?
def find_order(a, k, n):
    g = Graph(k)
    for i in range(n-1):
        idx = None
        min_len = min(len(a[i]), len(a[i+1]))
        print('min_len {}, a[{}]: {}, a[{}]:{}'.format(min_len, i, a[i], i+1, a[i+1]))
        for j in range(min_len):
            if a[i][j] != a[i+1][j]:
                idx = j
                break
        if idx is not None:
            print('idx', idx) 
            g.addEdge(a[i][idx], a[i+1][idx])
            
    '''
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    '''
    print('following is a topological sort of the given graph')
    g.topologicalSort()

            


N = 5 # 5 words in a dict
K = 4 # 4 letters in the alphabet
A = ["baa","abcd","abca","cab","cad"]
find_order(A, K, N)

    
        
N = 3
K = 3
A = ["caa","aaa","aab"]
find_order(A, K, N)

