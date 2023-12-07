import sys
import re

#Debug text with Red Color
def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end=" ")
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end=" ")


elf_bag = { "red"   : 12,
            "green" : 13,
            "blue"  : 14}

class Game:    
    def __init__(self, id, max_r = 0, max_g = 0, max_b = 0):
        self.id = id
        self.max_r = max_r
        self.max_g = max_g
        self.max_b = max_b

# Puzzle solution starts here
file = open('input.txt', 'r')
lines = file.readlines()

#Each line is a Game
sum = 0
for line in lines:
    id, sep, sub_games = line.strip().partition(': ')
    garbage, sep, id = id.partition(' ')
    G = Game(int(id), 0, 0, 0)

    sub_games = sub_games.split("; ")
    
    prRed("Game: ")
    print(line)
    prRed("ID: ")
    print(int(id))
    prRed("Sub Games: ")
    print(sub_games)
    #input("Press Enter to continue...")
    print()
    i = 0
    for sub_game in sub_games:
        i += 1
        sub_game = sub_game.split(', ')
        prRed("Sub Game" + str(i) + ": ")
        print(sub_game, end=" ")
        print()
        j = 0
        res_dct = {}
        for cubes in sub_game:
            j += 1
            quantity, sep, color = cubes.partition(' ')
            res_dct[f"{color}"] = int(quantity)
            prRed("Val " + str(j) + ": ")
            print(color + " : " + quantity)

        prRed("Dict: ")
        print(res_dct, end=" ")
        
        for key in res_dct.keys():
            if(key == 'red'):
                if(res_dct[key] > G.max_r):
                        G.max_r = res_dct[key]
            elif(key == 'green'):
                if(res_dct[key] > G.max_g):
                        G.max_g = res_dct[key]
            elif(key == 'blue'):
                    if(res_dct[key] > G.max_b):
                        G.max_b = res_dct[key]

        print()
        print(G.id)
        print(G.max_r)
        print(G.max_g)
        print(G.max_b)


    if (G.max_r > elf_bag['red']) or (G.max_g > elf_bag['green']) or (G.max_b > elf_bag['blue']):
       prRed("NAO !")
    else:
        prGreen("SIM !")
        sum = sum + G.id 
    print()
    print()      
    
print()
print()
print()
prRed("Sum: ")
print(sum)
        


