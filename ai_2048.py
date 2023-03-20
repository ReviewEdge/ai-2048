# 2048 game
# Contains the game loop, allows player to make moves and play game

import logic
import expectimax2 as em2
import puzzle_node as pn
import time


def move_to_str(move):
    if move == pn.Move.UP:
        return "w"
    if move == pn.Move.DOWN:
        return "s"
    if move == pn.Move.LEFT:
        return "a"
    if move == pn.Move.RIGHT:
        return "d"
    

def main():
    print("---2048---")
    print("--- AI ---\n\n")
    start = time.process_time()
    lastmove = time.process_time()

    mat = logic.start_game()
    move_count = 0
    score = 0
    last_tile = 2
    flag = True

    # game loop
    while True:
        print(f"Time to Process Move: {time.process_time() -lastmove  } seconds")
        print(f"\nMove Count: {move_count}\tScore: {score}\n{logic.mat_to_string(mat)}\nTotal Elapsed Time: {time.process_time() - start} seconds")
        lastmove = time.process_time()

        # Ask AI for next move
        next_move = em2.get_next_move_vary_depth(mat, score, last_tile)
        print(f"Move picked: {next_move}")

        x = move_to_str(next_move)

        if not x:
            print("GAME OVER!")
            print(f"\n\n\nTotal Moves: {move_count}\tFinal Score: {score}\n{logic.mat_to_string(mat)}")
            return score, False, mat

        # move up
        if x == "w":
            mat, flag, score = logic.move_up(mat, score)
        # move down
        elif x == "s":
            mat, flag, score = logic.move_down(mat, score)
        # move left
        elif x == "a":
            mat, flag, score = logic.move_left(mat, score)
        # move right
        elif x == "d":
            mat, flag, score = logic.move_right(mat, score)

        if not flag:
            print("GAME OVER!")
            print(f"\n\n\nTotal Moves: {move_count}\tFinal Score: {score}\n{logic.mat_to_string(mat)}")
            return score, False, mat

        move_count+=1

        # add a new tile
        last_tile = logic.add_new_tile(mat)



# Driver code
if __name__ == "__main__":
    main()