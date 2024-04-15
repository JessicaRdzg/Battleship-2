
from random import randint


HIDDEN_BOARD=[[" "]* 10 for x in range (10)] # del 0 al 9 excluyendo el 10 
GUESS_BOARD=[[" "]* 10 for x in range (10)] #tablero donde se jugará

letters_to_numbers= {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}   #Las letras se cov


def print_board(board):
    print("    A B C D E F G H I J ") #Header que serán las letras que signifiquen numeros del 0 al 9.
    print("   ---------------------")
    row_number= 1 #va a mostrar del 1 al 9 
    for row in board: 
        print(" %d|%s|" % (row_number,"|".join(row)))
        row_number +=1

 #darle formato a la tabla, por cada fila que estamos iterando vamos a poner una raya.


def create_ships (board):
    for ship in range (4): #4 barcos 
        ship_row, ship_column= randint (0, 9), randint(0, 9) #posicionar el barco entre la coordenada 0, 9 en fila/columna
        while board [ship_row][ship_column] == "X": #si el barco elige la misma posiciòn donde hay una x, se cambiará 
           ship_row, ship_column= randint(0,9), randint(0, 9)
        board[ship_row][ship_column] = "X"  #coloca el barco 


def get_ship_location():
    row=input("Introduce el número de fila del 1 al 9")
    while row not in "123456789":
        print("Por favor introduce una coordenada válida ")
        row=input("Introduce un número de fila del 1 al 9")
    column= input("Introduce una letra de columna de la A-J").upper()
    while column not in "ABCDEFGHIJ":
        print("Introduce una letra de columna válida")
        column= input("Introduce una letra de columna de la A-J").upper()
    return int (row)- 1, letters_to_numbers[column] #va a empezar en 0



def count_hit_ships (board):
    count=0
    for row in board:
        for column in row:
            if column =="X":
             count +=1
    return count


create_ships(HIDDEN_BOARD)
print(HIDDEN_BOARD)
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

#while turns > 0 