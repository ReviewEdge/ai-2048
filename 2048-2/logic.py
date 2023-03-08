#!/usr/bin/python
# -*- coding: utf-8 -*-
# logic.py to be
# imported in the 2048.py file

# importing random package
# for methods to generate random
# numbers.

import random


# function to initialize game / grid
# at the start

def start_game():

    # makes empty matrix
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    # spawn first 2 tiles
    add_new_tile(mat)
    add_new_tile(mat)

    print('Commands are as follows : ')
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    print(mat_to_string(mat))

    return mat


# adds either 2 or 4 tile to a random empty cell
def add_new_tile(mat):
    while True:
        r = random.randint(0,3)
        c = random.randint(0,3)

        if mat[r][c] == 0:
            if random.randint(0,9) == 9:
                mat[r][c] = 4
            else:
                mat[r][c] = 2
            break


def get_valid_moves(mat):
    # if any cell contains 2048 we have won
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WIN"

    valid_moves = []

    # check if moving in each direction will change anything
    if move_up(mat)[1]:
        valid_moves.append("w")
    if move_left(mat)[1]:
        valid_moves.append("a")
    if move_down(mat)[1]:
        valid_moves.append("s")
    if move_right(mat)[1]:
        valid_moves.append("d")
    
    return valid_moves


# function to compress the grid
# after every step before and
# after merging cells.
def compress(mat):

    # was anything changed upon compression?
    changed = False

    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    # shift entries of each cell to it's extreme left, row by row
    for i in range(4):
        pos = 0

        # loop to traverse each column
        # in respective row
        for j in range(4):
            if mat[i][j] != 0:

                # if cell is non empty then
                # we will shift it's number to
                # previous empty cell in that row
                # denoted by pos variable
                new_mat[i][pos] = mat[i][j]

                if j != pos:
                    changed = True
                pos += 1

    # return new compressed matrix
    # and the flag variable.
    return (new_mat, changed)



# function to merge the cells in matrix after compressing
def merge(mat):

    changed = False
    score_increase = 0
    for i in range(4):
        for j in range(3):

            # if current cell has same value as
            # next cell in the row and they
            # are non empty then...
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:

                # double current cell value and empty the next cell
                # mat[i][j] = mat[i][j] * 2
                # mat[i][j + 1] = 0

                score_increase = mat[i][j] * 2
                mat[i][j] = score_increase
                mat[i][j + 1] = 0

                # make bool variable True indicating the new grid after 
                # merging is different.
                changed = True

    return (mat, changed, score_increase)


# function to reverse the matrix
# means reversing the content of each row (reversing the sequence)
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat


# function to get the transposition
# of matrix (swapping rows and columns)
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# update the matrix if we move left
def move_left(grid):

    # first compress the grid
    (new_grid, changed1) = compress(grid)

    si = 0
    # then merge the cells.
    (new_grid, changed2, si) = merge(new_grid)

    changed = changed1 or changed2

    # again compress after merging.
    (new_grid, temp) = compress(new_grid)

    # return new matrix and bool changed
    # telling whether the grid is same
    # or different

    # return (new_grid, changed, score_increse)
    return (new_grid, changed, si)


# function to update the matrix
# if we move / swipe right
def move_right(grid):

    # to move right we just reverse
    # the matrix

    new_grid = reverse(grid)

    # then move left

    (new_grid, changed, si) = move_left(new_grid)

    # then again reverse matrix will
    # give us desired result

    new_grid = reverse(new_grid)
    return (new_grid, changed, si)


# function to update the matrix
# if we move / swipe up
def move_up(grid):

    # to move up we just take
    # transpose of matrix

    new_grid = transpose(grid)

    # then move left (calling all
    # included functions) then

    (new_grid, changed, si) = move_left(new_grid)

    # again take transpose will give
    # desired results

    new_grid = transpose(new_grid)
    return (new_grid, changed, si)


# function to update the matrix
# if we move / swipe down
def move_down(grid):

    # to move down we take transpose

    new_grid = transpose(grid)

    # move right and then again

    (new_grid, changed, si) = move_right(new_grid)

    # take transpose will give desired
    # results.

    new_grid = transpose(new_grid)
    return (new_grid, changed, si)


def mat_to_string(mat):
    return f"{mat[0]}\n{mat[1]}\n{mat[2]}\n{mat[3]}"
