import logic

class PuzzleWorld:

    def __init__(self, board, score, heur_score, parent):
        if board == None:
            self.board = self.start_game()
        else:
            self.board = board
            self.score = score
            if heur_score == None:
                self.heur_score = self.get_heur_score()
            else:
                self.heur_score = heur_score
            self.parent = parent


    def move_up(self):
        result = logic.move_up(self.board)

        # returns false if the move is not valid
        if not result[1]:
            return False

        #doesn't use heuristic yet
        new_world = PuzzleWorld(result[0], self.score+result[2], 0, self)
        return new_world

    def move_down(self):
        result = logic.move_down(self.board)

        # returns false if the move is not valid
        if not result[1]:
            return False

        #doesn't use heuristic yet
        new_world = PuzzleWorld(result[0], self.score+result[2], 0, self)
        return new_world

    def move_left(self):
        result = logic.move_left(self.board)

        # returns false if the move is not valid
        if not result[1]:
            return False

        #doesn't use heuristic yet
        new_world = PuzzleWorld(result[0], self.score+result[2], 0, self)
        return new_world

    def move_right(self):
        result = logic.move_right(self.board)

        # returns false if the move is not valid
        if not result[1]:
            return False

        #doesn't use heuristic yet
        new_world = PuzzleWorld(result[0], self.score+result[2], 0, self)
        return new_world

    def start_game(self):
        self.board = logic.start_game()
        self.score = 0
        self.heuristic_score = self.get_heuristic()
        self.parent = None

    #TODO: IMPLEMENT THIS
    def get_heur_score(self):
        return 0
    
    def __str__(self):
        return logic.mat_to_string(self.board)
