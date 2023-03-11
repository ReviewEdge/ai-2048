import puzzle_world as pw
import sys, os



# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
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


def get_next_move(curr_board, dl):
    curr_puzzle = pw.PuzzleWorld(curr_board, 0, 0)
    # curr_puzzle.set_heur_score()
    curr_node = pw.Node(curr_puzzle, 0, True)

    best_m = (pw.Move.UP, -1)
    for m in pw.moves:
        try_m_score = expectimax(pw.Node(curr_node.puzzle.move(m), 0, False), 0 , dl)
        if try_m_score > best_m[1]:
            best_m = (m, try_m_score)

    return best_m[0]
