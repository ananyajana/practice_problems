# find the minimum # of dice throws required to reach from source to
# destination. If there were no snake and ladder then each vertex would
# be connected to 5 next vertices. But as there are ladders and snakes,
# there are some short-circuit type connections. suppose there is a 
# connection from 1 to 2 and there is a ladder in 2 ending at 22. That
# means there is an edge from 1 to 22. similarly for snake.
# so the problem is reduced to finding the shortest part. Here each edge
# weight is equal, hence the problem can be solved using BFS search

# An entry used in BFS
class QueueEntry(object):
    def __init__(self, v=0, dist=0):
        self.v = v
        self.dist = dist

# this function returns the minimum number of dice throws required to 
# reach last cell in the snake and ladder game. Move[] is an array of size
# N where N is no. of cells on the board. If there is no snake or ladder from
# cell i, then move[i] is -1. Otherwise move[i[ contains cell to which snake
# or ladder at i takes to.
def get_min_dice_throws(move, N):
    # the graph has N vertices. Mark all as not visited
    visited = [False] * N

    # create a queue for BFS
    queue = []

    # Mark the node 0 as visited and enqueeue it
    visited[0] = True

    # Distance of 0'th vertex is also 0. enqueue 0th vertex
    queue.append(QueueEntry(0,0))

    # Do a BFS starting from vertex at index 0
    qe = QueueEntry() # A queu entru qe
    while queue:
        qe = queue.pop(0)
        v = qe.v # vertex no. of queue entry
        
        # if front vertex i.e. the popped vertex from queue is
        # the destination. we are done
        if v == N - 1:
            break

        # Otherwise dequeue the front vertex and enqueue its adjacent
        # vertices (or cell numbers reachable throught a dice throw)
        j = v + 1
        while j <= v + 6 and j < N:
            # If this cell is already visited, then ignore
            if visited[j] is False:
                # Otherwise calculate its distasnce and mark it as
                # visited
                a = QueueEntry()
                a.dist = qe.dist + 1
                visited[j] = True

                # check if there is a snake or ladder at j then tail of the
                # snake or top of the ladder becomes adjacent to 'i'
                a.v = move[j] if move[j] != -1 else j
                queue.append(a)

            j += 1

    # We reach here when 'qe' has the last vertex
    # return the distance of vertex in 'qe'
    return qe.dist

N = 30
move = [-1] * N

# Ladders
move[2] = 21
move[4] = 7
move[10] = 25
move[19] = 28

# Snakes
move[26] = 0
move[20] = 8
move[16] = 3
move[18] = 6

print('Min dice throws required is {0}'.format(get_min_dice_throws(move, N)))
