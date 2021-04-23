# python program for Krushkal's algorithms ro find minimum spanning tree of
# a given connected, undirected and weighted graph

from collections import defaultdict

#Class to represent a graph

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = [] # default dictionary
        # to store the graph

    # function to add an edge to graph
    def add_edge(self, u, v, w):
       self.graph.append([u, v, w])

    # a utility function to find set of an element i
    # (used path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    # a function that does union of two sets x and y
    # ( uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # union by rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # the main function to construct MST using Krushkal's algorithm
    def Krushkal_mst(self):
        result = [] # this will store the resultant MST
        # An index variable, used for sorted edges
        i = 0
        # an index variable used fo result[]
        e = 0
        # Step 1: Sort all the edges in non-decreasing order of their
        # weight. If we are not allowed to change the given graph, we
        # can create a copy of the graph
        self.graph = sorted(self.graph, key=lambda item:item[2])

        parent = []
        rank = []
        # create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number o edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including this ede does not create a cycle, include it in
            # result and increment the index of the result for next edge
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print("{} -- {} == {}".format(u, v, weight))
        print("Minimum spanning tree", minimum_cost)

# driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

# function call
g.Krushkal_mst()
