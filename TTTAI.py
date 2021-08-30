import copy


X ="X"
O ="O"
M = None


def ini_board():

    board = [[M, M, M],
             [M, M, M],
             [M, M, M]]
    return board


def player(board):
    i=0
    j=0
    k=0
    f=0 #Not Used
    while i<3:
        j=0
        while j<3:
            if board[i][j] == M:
                f += 1
            else:
                k += 1
            j += 1
        i +=1
    if k%2==0:
        return X
    else:
        return O


def actions(board):
    i=0
    j=0
    actionSet = []
    while i<3:
        j=0
        while j<3:
            if board[i][j] == M:
                actionSet.append((i, j))
            j += 1
        i += 1
    return actionSet


def move(board, action):

    i=action[0]
    j=action[1]
    board[i][j] = player(board)
    return board

def winner(board):
    winner = None;
    if (board[0][0] == X) and (board[0][1] == X) and (board[0][2] == X):
        winner = X
    if (board[0][0] == O) and (board[0][1] == O) and (board[0][2] == O):
        winner = O

    if (board[1][0] == X) and (board[1][1] == X) and (board[1][2] == X):
        winner = X
    if (board[1][0] == O) and (board[1][1] == O) and (board[1][2] == O):
        winner = O

    if (board[2][0] == X) and (board[2][1] == X) and (board[2][2] == X):
        winner = X
    if (board[2][0] == O) and (board[2][1] == O) and (board[2][2] == O):
        winner = O

    if (board[0][0] == X) and (board[1][0] == X) and (board[2][0] == X):
        winner = X
    if (board[0][0] == O) and (board[1][0] == O) and (board[2][0] == O):
        winner = O

    if (board[0][1] == X) and (board[1][1] == X) and (board[2][1] == X):
        winner = X
    if (board[0][1] == O) and (board[1][1] == O) and (board[2][1] == O):
        winner = O

    if (board[0][2] == X) and (board[1][2] == X) and (board[2][2] == X):
        winner = X
    if (board[0][2] == O) and (board[1][2] == O) and (board[2][2] == O):
        winner = O

    if (board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X):
        winner = X
    if (board[0][0] == O) and (board[1][1] == O) and (board[2][2] == O):
        winner = O

    if (board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X):
        winner = X
    if (board[0][2] == O) and (board[1][1] == O) and (board[2][0] == O):
        winner = O
    return winner


def terminal(board):
    i=0
    j=0
    full = True
    end = False
    while i<3:
        j=0
        while j<3:
            if board[i][j] == M:
                full = False
            j += 1
        i += 1

    if winner(board) == "X":
        end = True
    elif winner(board) == "O":
        end = True
    elif full:
        end = True

    return end


def utility(board):
    u = 0

    if winner(board) == X:
        u = 1
    elif winner(board) == O:
        u = -1
    else:
        u = 0

    return u

def maximiser(board):
    v = -2


    if terminal(board):


        return utility(board)

    else:
        for action in actions(copy.deepcopy(board)):
            v = max(v, minimiser(move(copy.deepcopy(board), action)))

    return v


def minimiser(board):
    v = 2


    if terminal(board):


        return utility(board)

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
        print(" O playing")
        for action in actions(copy.deepcopy(board)):

            u = maximiser(move(copy.deepcopy(board), action))

            if u < min:
                min = u
                moveSet= []
                moveSet.append(action)
            elif u == min:
                moveSet.append(action)

    return moveSet




