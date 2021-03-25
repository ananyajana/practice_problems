#A value of cell 1 means Source.
# A value of cell 2 means Destination.
# A value of cell 3 means Blank cell.
# A value of cell 0 means Wall
# we need to check if a path exists from source to destination
import numpy as np
from collections import deque

# To store matrix cell coordinates
class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt:Point, dist: int):
        self.pt = pt # the coordinates of the cell
        self.dist = dist # cell's distance from the course

# check whether given cell(row, col) is a valid cell or not
# N = # of rows = # of columns
def isValid(row:int, col:int, N):
    return (row >= 0) and (row < N) and (col >= 0) and (col < N)


# these arrays are used to get row and column
# numbers of a 4 neighbors of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

    # function to find the shortest path between a given source cell
    # to a destination cell
def BFS(mat, src:Point,dest:Point):
    # check source and destination cell
    # of the matrix have value 1
    N = len(mat)
    print('N: ', N)

    visited = [[False for i in range(N)] for j in range(N)]

    # create a quue for BFS
    q = deque()

    # distance of the source cell is 0
    s = queueNode(src, 0)
    q.append(s) # Enqueue source cell

    while q:
        curr = q.popleft() # Dequeue the front cell

        # If we have reached the  destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            print('reached destination')
            return curr.dist

        print('curr: ({}, {})'.format(pt.x, pt.y))
        print('not yet reached destination')
        # Otherwise  enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # If adjacent cell is valid, has path
            # and not visited yet, enqueue it
            if (isValid(row, col, N) and mat[row][col] != 0 and not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col), curr.dist + 1)
                q.append(Adjcell)

    # return -1 if destination cannot be reached
    return -1

# Driver code
def main():
    '''
    mat = [[3, 0, 3, 0, 0],
            [3, 0, 0, 0, 3],
            [3, 3, 3, 3, 3],
            [0, 2, 3, 0, 0],
            [3, 0, 0, 1, 3]]
    '''
    mat = [[1, 3],
            [3, 2]]
    # get the index of the source element
    mat_np = np.array(mat)
    res = np.where(mat_np == 1)
    s0 = res[0].item(0)
    s1 = res[1].item(0)
    source = Point(s0, s1)
    print('source: ({}, {})'.format(s0, s1))

    # get the index of the destination element
    res = np.where(mat_np == 2)
    s0 = res[0].item(0)
    s1 = res[1].item(0)
    dest = Point(s0, s1)
    print('dest: ({}, {})'.format(s0, s1))

    dist = BFS(mat, source, dest)
    if dist != -1:
        print("shortest path is:", dist)
    else:
        print("shortest path does not exist")

main()

