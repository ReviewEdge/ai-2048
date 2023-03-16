# An implementation of expectimax to solve 2048

import puzzle_world as pw
import sys, os


# Disables print statements
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restores print statements
def enablePrint():
    sys.stdout = sys.__stdout__


def expectimax(node: pw.Node, curr_depth, depth_limit):
    # print(curr_depth) # delete me
    
    children = node.spawn_children()

    # if dead end (loss), return false
    if not children:
        return False
    
    # if you've gone as deep as you can, return the score
    elif curr_depth == depth_limit:
        return node.heur_score
    
    # if chance nodes, get max
    elif not children[0].is_my_move:
            max_score = 0

            for c in children:
                leaf_score = expectimax(c, curr_depth, depth_limit)

                if leaf_score > max_score:
                    max_score = leaf_score

            return max_score

    else:
        average_score = 0.0

        for c in children:
            # increase current depth because you made a move to get the child
            average_score += expectimax(c, curr_depth+1, depth_limit)
        
        return average_score / len(children)


# try_this_board = [[0, 4, 0, 0],
# [2, 16, 4, 0],
# [32, 4, 0, 0],
# [4, 16, 8, 2]]

# start = pw.PuzzleWorld(None, None, None)
# start.start_game()
# start.board = try_this_board
# start_node = pw.Node(start, 0, True)

# for m in pw.moves:
#      print(f"\n{m}: {expectimax(pw.Node(start_node.puzzle.move(m), 0, False), 0 , 3)}")

# print(expectimax(start_node, 0, 3))


# suggests next move based on current board, at a set depth
def suggest_next_move(curr_board):
    start = pw.PuzzleWorld(None, None, None)
    blockPrint()
    start.start_game()
    enablePrint()
    start.board = curr_board
    start_node = pw.Node(start, 0, True)

    print("\n")
    for m in pw.moves:
        print(f"{m}: {expectimax(pw.Node(start_node.puzzle.move(m), 0, False), 0 , 3)}")



# returns the best next move based on inputted board, at a set depth of exploration
def get_next_move(curr_board, dl):
    curr_puzzle = pw.PuzzleWorld(curr_board, 0, 0)
    # curr_puzzle.set_heur_score()
    curr_node = pw.Node(curr_puzzle, 0, True)

    best_m = (pw.Move.LEFT, -1)
    for m in pw.moves:
        try_m_score = expectimax(pw.Node(curr_node.puzzle.move(m), 0, False), 0 , dl)
        if try_m_score > best_m[1]:
            best_m = (m, try_m_score)

    return best_m[0]



# counts how many non-empty tiles in a board
def get_num_tiles(board):
    all = 0
    for r in range(0, len(board)):
        for c in range(0, len(board)):
            if board[r][c] != 0:
                all+=1
    return all
    


# gets next move, but goes deeper if there are more tiles 
# (because they are less possibilities , e.g. a smaller branching factor)
def get_next_move_vary_depth(curr_board, dl):
    use_dl = dl

    amt = get_num_tiles(curr_board)

    # if 9 < amt < 11:
    #     use_dl = 4
    if 12 < amt < 14:
        use_dl = dl+1
    elif 14 < amt:
        use_dl = dl+2

    print(f"Tiles: {amt}\tDepth: {use_dl}")

    curr_puzzle = pw.PuzzleWorld(curr_board, 0, 0)

    
    # print(f"Tiles: {amt}\tDepth: {use_dl}\tH-score: {curr_puzzle.set_heur_score()}")


    # curr_puzzle.set_heur_score()
    curr_node = pw.Node(curr_puzzle, 0, True)

    best_m = (pw.Move.UP, -1)
    for m in pw.moves:
        try_m_score = expectimax(pw.Node(curr_node.puzzle.move(m), 0, False), 0 , use_dl)
        if try_m_score > best_m[1]:
            best_m = (m, try_m_score)

    return best_m[0]
