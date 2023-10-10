from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def move(direction):
    if direction == 'north':
        print('Entering the Garden')
        return
    if direction == 'south':
        print('Entering the Castle')
        return
    if direction == 'east':
        print("Entering the forest")
        return
    if direction == 'west':
        print("Entering the cave")
        return
    else:
        print("bad input")
        playing = False
        return