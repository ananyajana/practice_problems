# No. of vertices in the graph
V = 4

# Define infinity as the large enough value. This value witl be used for vertices not connected to each other
INF = 999999

# solves all pair shortest path via Floyd Warshall Algorithm
def floyd_warshall(graph):
    """ dist[][] will be the output matrix
    that will finally have the shortest distances
    between every pair of vertices """
    """ Initializing the solution matrix
    same as input graph matrix OR we can say
    that the initial values of shortest distances
    are shortest paths considering no intermediate vertices """

    """ Why is it being declared in this way? dist is the same as g"""
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    """ Add all vertices one by one to the set of intermediate vertices
    ---> Before start of an iteration, we have shortest distances between
    all pairs of vertices such that the shortest distances consider only the
    vertices in the set {0, 1, 2, .. k-1} as intermediate vertices.
    ---> After the end of a iteration, vertex no. k is added to the set of
    intermediate vertices and the set becomes {0, 1, 2, ...k}"""

    for k in range(V):
        # pick all vertices as source oneby one
        for i in range(V):
            # Pick all vertices as destination for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print_solution(dist)

# A function to print the solution
def print_solution(dist):
    print('Following matrix shows the shortest distances (all pair)')
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print('%7s'%('INF'))
            else:
                print('%7d\t'%(dist[i][j]))
            if j == V-1:
                # is this for a newline at the end of every row?
                print('')

# code to test the above program
# let us create the following weighted graph
"""
    (0)------>(3)
     |   10   /|\
     |         |
   5 |         |1
    \|/        |
    (1)------>(2) 
           3      """
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

# print the solution 
floyd_warshall(graph)
