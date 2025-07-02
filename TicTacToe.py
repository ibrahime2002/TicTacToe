print("Just a change for github repository")
print("Another change in the github using edit buttob")

def displayBoard(myList):
    print(myList[1] + ' | ' + myList[2] + ' | ' + myList[3] + "    1   2   3")
    print("---------")
    print(myList[4] + ' | ' + myList[5] + ' | ' + myList[6] + "    4   5   6")
    print("---------")
    print(myList[7] + ' | ' + myList[8] + ' | ' + myList[9] + "    7   8   9")

def playerInput():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, please choose your marker (X or O): ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def placeMarker(myList, marker, position):
    myList[position] = marker

def winCheck(myList, mark):
    return ((myList[1] == myList[2] == myList[3] == mark) or
            (myList[4] == myList[5] == myList[6] == mark) or
            (myList[7] == myList[8] == myList[9] == mark) or
            (myList[1] == myList[4] == myList[7] == mark) or
            (myList[2] == myList[5] == myList[8] == mark) or
            (myList[3] == myList[6] == myList[9] == mark) or
            (myList[1] == myList[5] == myList[9] == mark) or
            (myList[7] == myList[5] == myList[3] == mark))

import random
def chooseFirst():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def spaceCheck(myList, position):
    return myList[position] == ' '

def fullBoardCheck(myList):
    for i in range(1, 10):
        if spaceCheck(myList, i):
            return False
    return True

def playerChoice(myList):
    pos = 0
    while pos not in range(1, 10) or not spaceCheck(myList, pos):
        pos = int(input("Choose a position to mark (1-9): "))
    return pos

def replay():
    response = ''
    while response not in ['YES', 'NO']:
        response = input("Do you want to replay the game? (Yes or No): ").upper()
    return response == 'YES'

print("WELCOME TO TIC TAC TOE")

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = playerInput()
    turn = chooseFirst()
    print(turn + " will go first")

    playGame = input("Ready to play? y or n: ").lower()
    gameOn = playGame == 'y'
    
    while gameOn:
        if turn == 'Player 1':
            displayBoard(theBoard)
            print("Player 1: ")
            position = playerChoice(theBoard)
            placeMarker(theBoard, player1_marker, position)
            if winCheck(theBoard, player1_marker):
                displayBoard(theBoard)
                print('Player 1 has won the game!')
                gameOn = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('The game is a tie!')
                    gameOn = False
                else:
                    turn = 'Player 2'
        else:
            displayBoard(theBoard)
            print("Player 2: ")
            position = playerChoice(theBoard)
            placeMarker(theBoard, player2_marker, position)
            if winCheck(theBoard, player2_marker):
                displayBoard(theBoard)
                print('Player 2 has won the game!')
                gameOn = False
            else:
                if fullBoardCheck(theBoard):
                    displayBoard(theBoard)
                    print('The game is a tie!')
                    gameOn = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
