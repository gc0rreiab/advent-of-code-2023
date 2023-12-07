import sys
import re

#Debug in terminal with Colors
def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end=" ")
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end=" ")

elf_bag = { "red"   : 12,
            "green" : 13,
            "blue"  : 14}

class Game:    
    def __init__(self, id, r = 0, g = 0, b = 0):
        self.id = id
        self.cubes = {
             "red"  : r,
             "green": g,
             "blue" : b
        }

# Puzzle solution starts here
file = open('input.txt', 'r')
lines = file.readlines()

#Each line is a Game
sum = 0
for line in lines:
    id, sep, sub_games = line.strip().partition(': ')
    garbage, sep, id = id.partition(' ')
    id = int(id)

    G = Game(id, 0, 0, 0)
    sub_games = sub_games.split("; ")
    
    prRed("Game: ")
    print(line)
    prRed("ID: ")
    print(id)
    prRed("Sub Games: ")
    print(sub_games)
    print()
    i = 0
    for sub_game in sub_games:
        i += 1
        sub_game = sub_game.split(', ')
        prRed("Sub Game" + str(i) + ": ")
        print(sub_game, end=" ")
        print()
        j = 0
        #Dictionary to store the number of cubes for each color in each subgame  
        res_dct = {}
        for cubes in sub_game:
            j += 1
            quantity, sep, color = cubes.partition(' ')
            res_dct[f"{color}"] = int(quantity)
            prRed("Val " + str(j) + ": ")
            print(color + " : " + quantity)

        prRed("Dict: ")
        print(res_dct, end=" ")
        print()
        
        for key in res_dct.keys():
            if(res_dct[key] > G.cubes[key]):
                G.cubes[key] = res_dct[key]

    game_is_possible = False
    for key in elf_bag.keys():
     if (G.cubes[key] > elf_bag[key]):
        game_is_possible = False
        break
     else:
        game_is_possible = True
        
    if game_is_possible:
        prGreen("YES !")
        sum = sum + G.id
    else:
        prRed("NO !")

    print()
    print()      
    

print()
prRed("Sum: ")
print(sum)
        




