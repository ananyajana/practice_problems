arr1 = [[1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [2, 1, 0, 0, 2],
        [2, 2, 2, 2, 2]]
import numpy as np
b = np.array(arr1)
def floodfill(arr, x, y, prevC, newC):
    if x < 0 or x >= arr.shape[0] or y< 0 or y >= arr.shape[1] or arr[x][y] != prevC or arr[x][y] ==  newC:
        return
    arr[x][y] = newC
    floodfill(arr, x+1, y, prevC, newC)
    floodfill(arr, x-1, y, prevC, newC)
    floodfill(arr, x, y+1, prevC, newC)
    floodfill(arr, x, y+1, prevC, newC)



floodfill(b, 1, 1, 1, 2)

print(b)
