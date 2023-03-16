import puzzle_node as pn
import logic



def expectimax(node: pn.PuzzleNode, curr_depth, depth_limit):
    node.spawn_children()
    frontier = node.children
    computer_played_last = False
    if (node.last_move == pn.Move.TWO) or (node.last_move == pn.Move.FOUR):
        computer_played_last = True

    # Game Over condition
    if (computer_played_last) and (len(frontier) == 0):
        # results in a game over, so return a board goodness score of 0
        return (node.last_move, 0)

    # if we're at the dl, return the score for the current node's board
    elif curr_depth == depth_limit:
        return node.last_move, node.calc_board_goodness()
    
    # if it's player's turn, get the score of the best move
    elif computer_played_last:
        # return the best move and its score
        best_move = None
        best_score = -1
        for c in frontier:
            leaf_move, leaf_score = expectimax(c, curr_depth, depth_limit)

            if leaf_score > best_score:
                best_move = leaf_move
                best_score = leaf_score
        
        return (best_move, best_score)
    
    # if it's the computer's turn, get a weighted average score for child boards
    elif not computer_played_last:
        weighted_average = 0
        for c in frontier:
            if c.last_move == pn.Move.TWO:
                weight = .9
            if c.last_move == pn.Move.FOUR:
                weight = .1

            weighted_average += (weight * expectimax(c, curr_depth+1, depth_limit)[1])
        return (node.last_move , weighted_average)
    else:
        print("\n\n\nSomething went very wrong...")
        return





# Play first move of a game
def one_move():
    first_node = pn.PuzzleNode(logic.start_game(), 1, pn.Move.TWO)
    print(expectimax(first_node, 0, 3))



def get_next_move(curr_board, score, last_tile):
    if last_tile == 2:
        last_move = pn.Move.TWO
    if last_tile == 4:
        last_move = pn.Move.FOUR

    node = pn.PuzzleNode([row[:] for row in curr_board], score, last_move)

    return expectimax(node, 0, 2)[0]
