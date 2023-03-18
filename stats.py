# Plays a lot of random 2048 games, saves best game


import sys, os
import logic
import ai_2048

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


max = 0
max_board = []
min = 9999999999
progress = 1
games_to_play = 50
for i in range(games_to_play):
    print(f"\nPlaying game {progress} / {games_to_play} ...")

    blockPrint()
    result = ai_2048.main()
    enablePrint()


    if result[0] > max:
        max = result[0]
        max_board = result[2]  
    
    if result[0] < min:
        min = result[0]
    
    progress+=1

    # if progress % 100 == 0:
    print(logic.mat_to_string(max_board))
    print(f"High Score: {max}\nLow Score: {min}")

print(f"\nMax: {max}\tMin: {min}")
