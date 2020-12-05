import os

def render(board, mode="empty"):
    print("-"*23)
    temp = 0
    temp2 = 0
    for y in board:
        for x in y:
            if mode.lower() == "empty":
                if x != 0:
                    print(x, end=" ")
                else:
                    print(" ", end=" ")
            elif mode.lower() == "fill":
                print(x, end=" ")
            else:
                return None
            temp2 += 1
            if temp2 == 0:
                print("|", end=" ")
            if temp2 == 3:
                print("|", end=" ")
                temp2 = 0
        print("")
        temp += 1
        if temp == 3:
            print("-"*23)
            temp = 0

def newRender(board, mode="empty"):
    string = ""
    string += "-"*23 + "\n"
    temp = 0
    temp2 = 0
    for y in board:
        for x in y:
            if mode.lower() == "empty":
                if x != 0:
                    string = string + str(x) + " "
                else:
                    string = string + "  "
            elif mode.lower() == "fill":
                string = string + str(x) + " "
            else:
                return None
            temp2 += 1
            if temp2 == 0:
                string = string + "|" + " "
            if temp2 == 3:
                string = string + "|" + " "
                temp2 = 0
        string = string + "\n"
        temp += 1
        if temp == 3:
            string = string + "-"*23 + "\n"
            temp = 0
    print(string)

def check(y,x,num,board):
    for i in range(9):
        if (board[y][i] == num):
            return False
    for i in range(9):
        if (board[i][x] == num):
            return False
    ySC = (y//3)*3
    xSC = (x//3)*3
    for i in range(3):
        for j in range(3):
            if (board[ySC+i][xSC+j] == num):
                return False
    return True

def solve(board):
    for y in range(9):
        for x in range(9):
            if (board[y][x] == 0):
                for n in range(1,10):
                    if (check(y,x,n,board)):
                        board[y][x] = n
                        solve(board)
                        board[y][x] = 0
                return None
    newRender(board)

def inputSoduku():
    os.system('cls')

    # Board size = 9x9
    board = [[],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             []]
    for y in range(9):
        for x in range(9):
            newRender(board)
            n = input(f"{x},{y} > ")
            if n == "":
                board[y].append(0)
            else:
                board[y].append(int(n))
            os.system('cls')

    return board


if __name__ == '__main__':
    board = inputSoduku()
    print("Input:\n")
    newRender(board, "empty")
    print(" ")
    print("Output:\n")
    solve(board)
