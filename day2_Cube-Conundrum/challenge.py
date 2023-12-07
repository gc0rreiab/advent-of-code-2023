import sys
import re

#Debug in terminal with Colors
def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end=" ")
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end=" ")
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk),  end=" ")
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk),  end=" ")

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

#To solve only the first part, change it to False. Otherwise keep True to solve part two too.
part_two = True

#Each line is a Game
sum = 0
if part_two : sum2 = 0

for line in lines:
    id, sep, sub_games = line.strip().partition(': ')
    garbage, sep, id = id.partition(' ')
    id = int(id)

    G = Game(id, 0, 0, 0)
    sub_games = sub_games.split("; ")
    
    prPurple("Game: ")
    print(line.strip())
    prPurple("ID: ")
    print(id)
    prPurple("Sub Games: ")
    print(sub_games)
    i = 0
    for sub_game in sub_games:
        i += 1
        sub_game = sub_game.split(', ')
        #Dictionary to store the number of cubes for each color in each subgame  
        cube_dct = {}
        for cubes in sub_game:
            quantity, sep, color = cubes.partition(' ')
            cube_dct[f"{color}"] = int(quantity)

        prPurple("Sub Game " + str(i) + " Dict: ")
        print(cube_dct, end=" ")
        print()
        
        for key in cube_dct.keys():
            if(cube_dct[key] > G.cubes[key]):
                G.cubes[key] = cube_dct[key]


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

    if part_two:
        aux = 1
        for key in elf_bag.keys():
            aux =  aux * G.cubes[key]
        sum2 = sum2 + aux
            
    print()
    print()      
    
prYellow("Part I solution:\t")
print(sum)
if part_two is True:
    prYellow("Part II solution:\t")
    print(sum2)
            
        



