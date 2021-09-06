import TTTAI
import copy
import random

end = False
b = TTTAI.ini_board()
X = 1
O = -1
M = 0


def display(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = "X" if board[i][j] == X else "O" if board[i][j] == O else " "

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
            winner = TTTAI.winner(b)

            if winner == X:
                print("X wins")
            elif winner == O:
                print("O wins")
            else:
                print("Tie")
            break

        AI = random.choice(TTTAI.minimax(copy.deepcopy(b)))
        b[AI[0]][AI[1]] = O
        display(copy.deepcopy(b))
        end = TTTAI.terminal(copy.deepcopy(b))

        if end:
            display(copy.deepcopy(b))
            winner = TTTAI.winner(b)

            if winner == X:
                print("X wins")
            elif winner == O:
                print("O wins")
            else:
                print("Tie")
            break


def dispdiscy(board):
    output = ""

    for i in range(3):
        for j in range(3):
            output += "X" if board[i][j] == X else "O" if board[i][j] == O else "N"

            if j < 2:
                output += "|"

        output += "\n"

    return output


def canplay(board, p, q):
    return board[p][q] == M
