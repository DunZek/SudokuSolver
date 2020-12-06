import sys  # To detect the operating system
import os  # For command-line operations

# "Render" the soduku board
def newRender(board, mode="empty"):
    string = "" # set the string
    string += "-"*23 + "\n" #add the header to the string
    temp = 0 # set the temp var for the horizontal splits
    temp2 = 0 # set the temp var for the vertical splits
    for y in board: # loop all lines in the variable
        for x in y: # loop all items in all the lines
            if mode.lower() == "empty": # check what render mode is activated and render empty slots that way
                if x != 0: # if slot is not 0 
                    string += str(x) + " " # render the number
                else: # otherwise if the slot is 0
                    string += "  " # render " "
            elif mode.lower() == "fill": # if the mode is "fill"
                string = string + str(x) + " " # render the number
            else: # if neither of the render modes are chosen
                return None # exit with None
            temp2 += 1 # add 1 to temp2 (verticle lines)
            if temp2 == 3: # if 3 numbers has passed
                string += "|" + " " # render "| " (verticle line)
                temp2 = 0 # set count to 0
        string += "\n" # after every line render "\n" (newline)
        temp += 1 # add 1 to line count
        if temp == 3: # if line count is 3
            string += "-"*23 + "\n" # render "-----------------------" (horizontal line)
            temp = 0 # set count to 0
    print(string) # render the final product

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
    # TODO: Vary the board size?
    board = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

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

    # 1. Prepare the command-line
    if sys.platform == 'win32': os.system('cls')
    elif sys.platform == 'darwin': os.system('clear')

    # 2. Manually instantiate an unsolved sudoku board
    board = inputSoduku()

    print("Input:\n")
    
    # newRender(board, "empty")
    # print(" ")
    # print("Output:\n")

    # # Solving algorithm
    # solve(board)
