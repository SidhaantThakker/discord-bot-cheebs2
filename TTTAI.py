import copy


X = 1
O = -1
M = 0


def ini_board():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board


def player(board):
    k = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                k += 1

    if k % 2 == 0:
        return X
    else:
        return O


def actions(board):
    actionSet = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == M:
                actionSet.append((i, j))

    return actionSet


def move(board, action):
    i = action[0]
    j = action[1]

    board[i][j] = player(board)
    return board


def winner(board):
    """
    Returns 1 = X if X has won,
           -1 = O if O has won,
            0 = M if neither has won (yet).
    """
    row = col = d1 = d2 = 0

    for i in range(3):
        for j in range(3):
            row += board[i][j]
            col += board[j][i]

        # check if this row or col has 3 Xs (1s)
        if row == 3 or col == 3:
            return X

        # check if this row or col has 3 Os (-1s)
        if row == -3 or col == -3:
            return O

        d1 += board[i][i]
        d2 += board[i][2 - i]

    if d1 == 3 or d2 == 3:
        return X

    if d1 == -3 or d2 == -3:
        return O

    return M


def terminal(board):
    full = True

    for i in range(3):
        for j in range(3):
            if board[i][j] == M:
                full = False

    end = full or (winner(board) != M)

    return end


def maximiser(board):
    v = -2

    if terminal(board):
        return winner(board)

    else:
        for action in actions(copy.deepcopy(board)):
            v = max(v, minimiser(move(copy.deepcopy(board), action)))

    return v


def minimiser(board):
    v = 2

    if terminal(board):
        return winner(board)

    else:
        for action in actions(copy.deepcopy(board)):
            v = min(v, maximiser(move(copy.deepcopy(board), action)))

    return v


def minimax(board):
    moveSet = []
    max = -2
    min = 2

    if player(board) == X:
        print("X playing")
        for action in actions(copy.deepcopy(board)):

            u = minimiser(move(copy.deepcopy(board), action))

            if u > max:
                max = u
                moveSet = []
                moveSet.append(action)
            elif u == max:
                moveSet.append(action)

    elif player(board) == O:
        print("O playing")
        for action in actions(copy.deepcopy(board)):

            u = maximiser(move(copy.deepcopy(board), action))

            if u < min:
                min = u
                moveSet = []
                moveSet.append(action)
            elif u == min:
                moveSet.append(action)

    return moveSet
