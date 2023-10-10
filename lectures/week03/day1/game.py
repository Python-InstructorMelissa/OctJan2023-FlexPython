from os import system, name
import random
import time

from classes.item import *
# from classes.player import *
from classes.playerType import *
from messages.messages import *
from functions.functions import *

sword = Item("Slayer", "weapon", 10)
bowArrow = Item("Bow & Arrow", "weapon", 7)
healingPotion = Item("Healing Potion", "consumable", 10)

playing = True

while playing:
    message = print(welcome)
    question = input(playerName)
    player01 = PlayerType(question)
    question = input(f"{player01.name}, what side will you be working for today\n")
    player01.side = question
    message = print(f"{player01.name} so you will be working for the {player01.side} Side")
    clear()
    message = input(f"{player01.name}\nDo you have a companion with you today?\nY / N\n")
    if message[0] == 'n' or message[0] == 'N':
        message = print(f"Sorry at this time we are only allowing 2 player access")
        playing = False
    else:
        question = input(otherPlayerName)
        player02 = PlayerType(question)
        question = input(f"{player02.name}, what side will you be working for today\n")
        player02.side = question
        message = print(f"Player 1:\n{player01.name} who will be on the {player01.side} side.\n\nPlayer 2:\n{player02.name} who will be on the {player02.side} side.")
        question = input(f"What direction would you like to go?\n\nnorth / south / east / west\n")
        answer = question
        message = print(answer)
        move(answer)
    playing = False