import logic
from enum import Enum


class Move(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]

# represents a board state (doesn't know wether it's my move or the game's move)            
class PuzzleWorld:

    def __init__(self, board, score, heur_score: int):
        self.board = board
        self.score = score
        self.heur_score = heur_score


    def move(self, direction):
        if direction == Move.UP:
            result = logic.move_up(self.board)
        if direction == Move.DOWN:
            result = logic.move_down(self.board)
        if direction == Move.LEFT:
            result = logic.move_left(self.board)
        if direction == Move.RIGHT:
            result = logic.move_right(self.board)

        # returns false if the move is not valid
        if not result[1]:
            return False

        new_world = PuzzleWorld(result[0], self.score+result[2], 0)
        new_world.set_heur_score()
        return new_world
    

    def start_game(self):
        self.board = logic.start_game()
        self.score = 0
        self.heuristic_score = self.set_heur_score()


    #TODO: IMPLEMENT THIS
    def set_heur_score(self):
        #make this actually do something helpful:
        self.heur_score = self.score
        return self.heur_score
    

    def __str__(self):
        return logic.mat_to_string(self.board)


# represents a game state
# knows if it's my move or the game's move
# method for generating all possible child-states
class Node:
    
    def __init__(self, puzzle: PuzzleWorld, heur_score, is_my_move):
        self.puzzle = puzzle

        if is_my_move:
            self.heur_score = puzzle.set_heur_score()
        else:
            if heur_score:
                self.heur_score = heur_score
            else:
                self.heur_score = 0

        self.children = []
        self.is_my_move = is_my_move

    # sets children to the possible children the current board could result in
    # if it's my move, it simulates the possible moves you could make
    # if it's the game's move, it simulates all the places 2 and 4 tiles could spawn in
    def spawn_children(self):
        if self.is_my_move:
            for m in moves:
                new_puzzle = self.puzzle.move(m)

                # create a child if the move was valid
                if new_puzzle:
                    new_puzzle.set_heur_score()

                    # create new "opponent's move" Node, using the newly generated board
                    self.children.append(Node(new_puzzle, None, False))


        # simulate random tile possibilities, and calculate my averaged heur_score based on the possible children
        else:

            #NOT SURE IF THIS IS RIGHT
            if not self.puzzle:

                # print(f"throwing false: {self}\n{self.puzzle.board}")

                return False 
            

            # check every cell in the board
            for r in range(0, len(self.puzzle.board)):
                for c in range(0, len(self.puzzle.board)):
                    # if the cell is empty then simulate putting tiles there
                    if self.puzzle.board[r][c] == 0:
                        new_world_2 = PuzzleWorld(self.puzzle.board, self.puzzle.score, None)
                        new_world_2.board[r][c] = 2
                        # 2s spawn with .9 prob.
                        new_world_2.set_heur_score()
                        self.heur_score += (new_world_2.heur_score * .9)
                        self.children.append(Node(new_world_2, new_world_2.heur_score, True))

                        new_board_4 = PuzzleWorld(self.puzzle.board, self.puzzle.score, None)
                        new_board_4.board[r][c] = 4
                        # 4s spawn with .1 prob.
                        new_board_4.set_heur_score()
                        self.heur_score += (new_board_4.heur_score * .1)
                        self.children.append(Node(new_board_4, new_board_4.heur_score, True))
       
        # return newly spawned children
        return self.children