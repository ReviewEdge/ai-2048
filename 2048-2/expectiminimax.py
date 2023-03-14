import puzzle_world as pw








# DON'T USE THIS CODE









start = pw.PuzzleWorld(None, None, None, None)
start.start_game()
moves = [pw.Move.UP, pw.Move.DOWN, pw.Move.LEFT, pw.Move.RIGHT]

def pick_my_move(world: pw.PuzzleWorld):    
    best_heur = float('-inf')
    best_world: pw.PuzzleWorld = False

    for m in moves:
        new_world = world.move(m)

        if new_world and (new_world.set_heur_score() > best_heur):
            best_world = new_world
            best_heur = new_world.heur_score

    # will return False if no moves work or if no world have a heuristic
    return best_world


def opp_move(world: pw.PuzzleWorld):
    total_score = 0
    child_worlds = []

    # check every cell in the board
    for r in world.board:
        for c in world.board:
            # if the cell is empty then simulate putting tiles there
            if world.board[r][c] == 0:
                new_board_2 = pw.PuzzleWorld(world)
                new_board_2.board[r][c] = 2
                # 2s spawn with .9 prob.
                total_score += (new_board_2.set_heur_score() * .9)
                child_worlds.append(new_board_2)

                new_board_4 = pw.PuzzleWorld(world)
                new_board_4.board[r][c] = 4
                # 4s spawn with .1 prob.
                total_score += (new_board_2.set_heur_score() * .1)
                child_worlds.append(new_board_4)

    return (total_score, child_worlds)


    

def expecitmax(world: pw.PuzzleWorld, is_my_move):
    # if parent was leaf node:
    #MAKE THIS SO IT ALSO HANDLES IF AT DEPTH LIMIT, SO SENDS UP JUST VALUE
    if not world:
        return False
    
    elif is_my_move:
        return expecitmax(pick_my_move(world), False)
    
    # if it's opponent's move, return weighted score total:
    else:
        for w in opp_move(world)[0]:
            exp




print(f"\n\nPicked this: \n{pick_my_move(start).parent_move}")




# attempt 2:
moves = [pw.Move.UP, pw.Move.DOWN, pw.Move.LEFT, pw.Move.RIGHT]

def expectimax(world: pw.PuzzleWorld, is_my_move, current_depth, depth_limit):
    # if parent was leaf node:
    #MAKE THIS SO IT ALSO HANDLES IF AT DEPTH LIMIT, SO SENDS UP JUST VALUE
    # if not world:
    #     returnnew_world.heur_score
    
    #elif is_my_move:
    if is_my_move:
        best_heur = float('-inf')
        best_world: pw.PuzzleWorld = False

        for m in moves:
            new_world = world.move(m)
            new_world.set_heur_score()

            if expectimax(new_world, False, current_depth, depth_limit) > best_heur:
                best_world = new_world
                best_heur = new_world.heur_score

        # will return False if no moves work or if no world have a heuristic
        return best_world

    
    # if it's opponent's move, return weighted score total:
    else:
        # for w in opp_move(world)[0]:
        #     exp


        total_score = 0
        child_worlds = []

        # check every cell in the board
        for r in world.board:
            for c in world.board:
                # if the cell is empty then simulate putting tiles there
                if world.board[r][c] == 0:
                    new_board_2 = pw.PuzzleWorld(world)
                    new_board_2.board[r][c] = 2
                    # 2s spawn with .9 prob.
                    total_score += (new_board_2.set_heur_score() * .9)
                    child_worlds.append(new_board_2)

                    new_board_4 = pw.PuzzleWorld(world)
                    new_board_4.board[r][c] = 4
                    # 4s spawn with .1 prob.
                    total_score += (new_board_2.set_heur_score() * .1)
                    child_worlds.append(new_board_4)