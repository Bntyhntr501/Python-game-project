#
from characters.player import *
from command import *
from utils.until import *

commands = {
        "help": help,
        "exit": exit
        }
player = Player("Default", 1, 1, 1)

def nameInput(prompt):
    name = input(prompt)
    return name.strip()

def getName():
    tempName = ""
    while 1:
        tempName = nameInput("What is your name? ")

        if len(tempName) < 1:
            continue

        yes = yesOrNo(tempName + ", is that your name?")

        if yes:
            return tempName
        else:
            continue

def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False

def runCMD(cmd, args, player):
    commands[cmd](player, args)



def main(player):

    player.name = getName()

    while (not player.dead):
        line = input = (">> ")
        input = line.split()
        input.append("EOI")
        if isValidCMD(input[0]):
            runCMD(input[0], input[1], player)

main(player)
