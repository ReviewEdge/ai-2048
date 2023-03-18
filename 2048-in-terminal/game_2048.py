# Play 2048 via keyboard input

import logic
import puzzle_node as pn


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
    # call start_game function to initialize the matrix
    mat = logic.start_game()

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

            # Play a random game:
            # x = valid_moves[random.randint(0, len(valid_moves)-1)]

            # Get user input for next move:
            x = input("Move: ").lower()

 
            if x not in valid_moves:
                print("Invalid move")
            else:
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
                
                move_count+=1

                # add a new tile
                logic.add_new_tile(mat)


        # print the matrix after each move
        print(logic.mat_to_string(mat))


# Driver code
if __name__ == "__main__":
    main()