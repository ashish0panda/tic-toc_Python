import random


def display_board(board):
    print("")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[0])+"   |   "+str(board[1])+"   |   "+str(board[2])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[3])+"   |   "+str(board[4])+"   |   "+str(board[5])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+str(board[6])+"   |   "+str(board[7])+"   |   "+str(board[8])+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        m=int(input("Enter Your move: "))
        if m in board:
            return m
        else:
            print("Already Choosen or invalid input")
            continue


def victory_for(board):
    if (board[0]=="O" and board[1]=="O" and board[2]=="O")\
       or (board[3]=="O" and board[4]=="O" and board[5]=="O")\
       or (board[6]=="O" and board[7]=="O" and board[8]=="O")\
       or (board[0]=="O" and board[3]=="O" and board[6]=="O")\
       or (board[1]=="O" and board[4]=="O" and board[7]=="O")\
       or (board[2]=="O" and board[5]=="O" and board[8]=="O")\
       or (board[0]=="O" and board[4]=="O" and board[8]=="O")\
       or (board[2]=="O" and board[4]=="O" and board[6]=="O"):
        print("You Win!")
        return True
    if (board[0]=="X" and board[1]=="X" and board[2]=="X")\
       or (board[3]=="X" and board[4]=="X" and board[5]=="X")\
       or (board[6]=="X" and board[7]=="X" and board[8]=="X")\
       or (board[0]=="X" and board[3]=="X" and board[6]=="X")\
       or (board[1]=="X" and board[4]=="X" and board[7]=="X")\
       or (board[2]=="X" and board[5]=="X" and board[8]=="X")\
       or (board[0]=="X" and board[4]=="X" and board[8]=="X")\
       or (board[2]=="X" and board[4]=="X" and board[6]=="X"):
        print("You Loss!")
        return True
    return False

def draw_move(board):
    return random.choice(board)        


number=[1,2,3,4,5,6,7,8,9]
display=[1,2,3,4,5,6,7,8,9]
display_board(display)
n=True
draw=True
while len(number)!=0:
    if n:
        s=draw_move(number)
        number.remove(s)
        display[s-1]="X"
        display_board(display)
        n=False
    else:
        s=enter_move(number)
        number.remove(s)
        display[s-1]="O"
        display_board(display)
        n=True
    if victory_for(display):
        draw=False
        break
if draw:
    print("Match Draw!")
