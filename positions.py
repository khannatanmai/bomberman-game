import numpy as np

def true_pos(pos):
    pos_array = np.empty((8,2))

    pos_array[0][0] = pos[0]*2 + 2
    pos_array[0][1] = pos[1]*4 + 4

    for i in range(1,4):
        pos_array[i][0] = pos_array[0][0]
        pos_array[i][1] = pos_array[i-1][1] + 1

    pos_array[4][0] = pos_array[0][0] + 1
    pos_array[4][1] = pos_array[0][1]

    for i in range(5,8):
        pos_array[i][0] = pos_array[4][0]
        pos_array[i][1] = pos_array[i-1][1] + 1

    return pos_array
