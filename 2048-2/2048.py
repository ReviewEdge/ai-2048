# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic
import random_player as rp

# Driver code
if __name__ == "__main__":

    # calling start_game function
    # to initialize the matrix
    mat = logic.start_game()

while True:

    # get user input for next step

    # x = input("Move: ")

    
    x = rp.get_move()

    is_valid_move = True
    # to move up
    if x == "W" or x == "w":
        # call the move_up function
        mat, flag = logic.move_up(mat)
    # to move down
    elif x == "S" or x == "s":
        mat, flag = logic.move_down(mat)
    # to move left
    elif x == "A" or x == "a":
        mat, flag = logic.move_left(mat)
    # to move right
    elif x == "D" or x == "d":
        mat, flag = logic.move_right(mat)
    else:
        print("Invalid Key Pressed")
        is_valid_move = False

    if is_valid_move:
        status = logic.get_current_state(mat)
        print(status)
        if status == "GAME NOT OVER":
            logic.add_new_2(mat)
        else:




            # its never actually making it here because its not catching losses,
            # instead is just getting stuck in an infinite loop



            print("YOU LOST")
            break

    # print the matrix after each move
    print(f"{mat[0]}\n{mat[1]}\n{mat[2]}\n{mat[3]}")
