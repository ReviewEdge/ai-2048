# Plays a lot of random 2048 games, saves best game


import game_2048
import sys, os
import logic
import fast_2048

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
for i in range(5000):
    blockPrint()
    result = fast_2048.main()
    enablePrint()

    if result[1]:
        print(f"Won in {result[0]} moves.")

    if result[0] > max:
        max = result[0]
        max_board = result[2]  
    
    if result[0] < min:
        min = result[0]
    
    progress+=1

    # if progress % 100 == 0:
    print(f"\nGames Played: {progress}")
    print(max_board)
    print(f"High Score: {max}\nMin: {min}")

print(f"\nMax: {max}\tMin: {min}")
