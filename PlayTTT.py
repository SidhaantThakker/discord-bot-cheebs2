import TTTAI
import copy
import random

end = False
b = TTTAI.ini_board()
X = "X"
O = "O"
M = None


def display(board):
    i = 0
    j = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == M:
                board[i][j] = " "
            j += 1
        i += 1

    print(board[0])
    print(board[1])
    print(board[2])


def conv(x):
    if x >= 10:
        return (x // 10 - 1, x % 10 - 1)
    else:
        x -= 1
        return (x // 3, x % 3)


if __name__ == "__main__":
    while not end:
        user = input("Enter Move")
        p, q = conv(int(user))
        b[p][q] = X
        end = TTTAI.terminal(copy.deepcopy(b))
        if end:
            display(copy.deepcopy(b))
            if TTTAI.winner(b) == X:
                print("X wins")
            elif TTTAI.winner(b) == O:
                print("O wins")
            else:
                print("Tie")
            break
        AI = random.choice(TTTAI.minimax(copy.deepcopy(b)))
        p = AI[0]
        q = AI[1]
        b[p][q] = O
        display(copy.deepcopy(b))
        end = TTTAI.terminal(copy.deepcopy(b))
        if end:
            display(copy.deepcopy(b))
            if TTTAI.winner(b) == X:
                print("X wins")
            elif TTTAI.winner(b) == O:
                print("O wins")
            else:
                print("Tie")
            break


def dispdiscy(board):
    i = 0
    j = 0
    output = ""
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == M:
                board[i][j] = "N"
            j += 1
        i += 1

    i = 0
    j = 0

    while i < 3:
        j = 0
        while j < 3:
            if j < 2:
                output = output + board[i][j] + "|"
            else:
                output = output + board[i][j]
            j += 1

        output = output + "\n"
        i += 1

    return output


def canplay(board, p, q):

    if board[p][q] == M:
        return True
    else:
        return False
