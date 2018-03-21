import numpy as np

rows = 8
cols = 8


class State():
    def __init__(self, arr, num):
        self.arr = arr
        self.num = num

def isValidRow(arr, row, col):

    count = 0
    for i in range(cols):
        if arr[row][i] == 1:
            count = count + 1
        if count >= 2:
            return False
    return True

def isValidDia(arr, row, col):
    offset = 0
    if row < col:
        offset = row
    else:
        offset = col

    i = row - offset
    j = col - offset
    while i < row and j < col:
        if arr[i][j] == 1:
            return False
        i = i + 1
        j = j + 1

    i = row + 1
    j = col - 1
    while i < rows and j > 0:
        if arr[i][j] == 1:
            return False
        i = i + 1
        j = j - 1

    return True






frindge = []
initState = State(np.zeros((rows, cols)), 0)
frindge.insert(0, initState)
while frindge:
    state = frindge.pop()
    cur_col = state.num
    for i in range(rows):
        new_arr = np.array(state.arr)
        new_arr[i][cur_col] = 1
        if isValidDia(new_arr, i, cur_col) and isValidRow(new_arr, i, cur_col):

            if cur_col == cols - 1:
                print('A valid result:')
                print(new_arr)

            else:
                new_state = State(new_arr, state.num + 1)
                frindge.insert(0, new_state)