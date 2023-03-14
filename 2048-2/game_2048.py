import logic
import random
import expectimax as em
import puzzle_world as pw

def move_to_str(move):
    if move == pw.Move.UP:
        return "w"
    if move == pw.Move.DOWN:
        return "s"
    if move == pw.Move.LEFT:
        return "a"
    if move == pw.Move.RIGHT:
        return "d"
    


def main():
    # call start_game function to initialize the matrix
    mat = logic.start_game()


#     try_this_board = [[0, 4, 0, 0],
# [2, 16, 4, 0],
# [32, 4, 0, 0],
# [4, 16, 8, 2]]
    
#     mat = try_this_board

    # game loop
    move_count = 0
    score = 0
    while True:
        print(f"\nMOVE #{move_count}\tSCORE: {score}")
        valid_moves = logic.get_valid_moves(mat)
        
        if valid_moves == "WIN":
            print("YOU GOT 2048, YOU WIN")
            return score, True, mat

        elif not valid_moves:
            print("GAME OVER, YOU LOST")
            return score, False, mat

        else:

            # RANDOM AI:
            # x = valid_moves[random.randint(0, len(valid_moves)-1)]



            # expectimax AI:
            # em.suggest_next_move(mat)

            # get user input for next move
            # x = input("Move: ").lower()

            x = move_to_str(em.get_next_move_vary_depth(mat, 2))
            print(f"MOVE PICKED: {x}")



            if x not in valid_moves:
                print("Invalid move")
            else:
                # move up
                if x == "w":
                    mat, flag, si = logic.move_up(mat)
                # move down
                elif x == "s":
                    mat, flag, si = logic.move_down(mat)
                # move left
                elif x == "a":
                    mat, flag, si = logic.move_left(mat)
                # move right
                elif x == "d":
                    mat, flag, si = logic.move_right(mat)
                
                move_count+=1
                score += si

                # add a new tile
                logic.add_new_tile(mat)


        # print the matrix after each move
        print(logic.mat_to_string(mat))


# Driver code
if __name__ == "__main__":
    main()