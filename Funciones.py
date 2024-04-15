from Tablero import HIDDEN_BOARD, GUESS_BOARD, letters_to_numbers
from random import randint



def print_board(board):
    print("    A B C D E F G H I J ")
    print("    --------------------")
    row_number= 1
    for row in board: 
        new_func(row_number, row)
        row_number +=1

def new_func(row_number, row):
    print(" %d|%s|" % (row_number," | ".join(row)))



def create_ships (board):
    for ship in range (4):
        ship_row, ship_column= randint (0, 9), randint(0, 9)
        while board [ship_row][ship_column] == "X":
           ship_row, ship_column= randint(0,9), randint(0, 9)
        board[ship_row][ship_column] = "X" 


def get_ship_location():
    row=input("Introduce el número de fila del 1 al 9")
    while row not in "123456789":
        print("Por favor introduce una coordenada válida ")
        row=input("Introduce un número de fila del 1 al 9")
    column= input("Introduce una letra de columna de la A-J").upper()
    while column not in "ABCDEFGHIJ":
        print("Introduce una letra de columna válida")
        column= input("Introduce una letra de columna de la A-J").upper()
    return int (row)- 1, letters_to_numbers[column]




def count_hit_ships (board):
    count=0
    for row in board:
        for column in row:
            if column =="X":
             count +=1
    return count


create_ships(HIDDEN_BOARD)
turns=5
while turns > 0:
    print("Bienvenido a al juego")
    print_board  (GUESS_BOARD)
    row, column=get_ship_location()
    if GUESS_BOARD[row][column]=="_":
        print("Ya has adivinado, intenta de nuevo")
    elif HIDDEN_BOARD [row][column]=="X":
        print ("Felicitaaciones, acertaste")
        GUESS_BOARD [row] [column]="X"
        turns-=1
    else:
        print("Fallaste")
        GUESS_BOARD [row][column] = "_"
    if count_hit_ships (GUESS_BOARD)== 5: 
        print ("GANASTE!")
        break
        print("Tienes" + str(turns)+ "turnos")
    if turns == 0:
        print ("GAME OVER")
        break