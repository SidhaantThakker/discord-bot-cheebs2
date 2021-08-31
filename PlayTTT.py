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

    inp = ""

    if x == "0":
        inp = "00"
    if x == "1":
        inp = "01"
    if x == "2":
        inp = "02"
    if x == "3":
        inp = "10"
    if x == "4":
        inp = "11"
    if x == "5":
        inp = "12"
    if x == "6":
        inp = "20"
    if x == "7":
        inp = "21"
    if x == "8":
        inp = "22"
    if len(x) == 2:
        inp = x

    return inp


if __name__ == "__main__":
    while not end:
        user = input("Enter Move")
        inp = conv(user)
        p = int(inp[0])
        q = int(inp[1])
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
