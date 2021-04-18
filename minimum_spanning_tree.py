''' MST using Prim's algorithm. Assumes adjacency matrix representation'''

import numpy as np

maxint = 999999
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for rown in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def print_mst(self, parent):
        print('Edge \tWeight')
        for i in range(1, self.V):
            print('{}-{}\t{}'.format(parent[i], i, self.graph[i][parent[i]]))

    # Autility function to find the vertex with minimum distance value
    # from the set of vertices not yet included in shortest path tree
    def min_key(self, key, mst_set):
        # initialize the min value
        min_val = maxint
        for v in range(self.V):
            if key[v] < min_val and mst_set[v] == False:
                min_val = key[v]
                min_index = v

        return min_index

    # function to construct and print MST for a graph represented using
    # adjacency matrix representation
    def prim_mst(self):
        # key values used to pick minimum weight edge in cur
        key = [maxint] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked up as the first
        # vertex
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1 # First node is always the root of the st
        
        for cout in range(self.V):
            # Pick the minimum distance vertex from the set of vertices
            # not yet processed. u is always equal to src in first iteration
            u = self.min_key(key, mst_set)

            # put the minimum distance vertex in the smst
            mst_set[u] = True
            
            # Update dist value of the adjacent verteices of the picked
            # vertex only if the current distance is greater than new 
            # distance and the vertex is not already in the shortest path tree
            for v in range(self.V):
                # graph[u][v] is non-zero only for adjacent vertices of m
                # mst_set[v] is false for ertices not yet included in MST
                # update the key only if graph[u][v] is smaller than key[v]
                # using the newly picked up vertex, if the distance can be updated
                # we will need to update that
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > np.amax(np.array(self.graph[u])):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

g.prim_mst()
