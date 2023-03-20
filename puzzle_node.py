from enum import Enum
import logic


class Move(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    TWO = 4
    FOUR = 5

moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]

class PuzzleNode:
    def __init__(self, board, score, last_move):
        self.board = board
        self.score = score
        self.board_goodness = None
        self.last_move = last_move
        self.children = []

    # get and set heuristic value for board based on game score
    def calc_board_goodness(self):
        self.board_goodness = self.score + 1
        return self.board_goodness
    
     
    # counts how many empty tiles in a board
    def get_num_empty_tiles(self):
        all = 16
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board)):
                if self.board[r][c] != 0:
                    all-=1
        return all


    # hueristic of more empty cells
    def calc_board_goodness_empty(self):
        self.board_goodness =  PuzzleNode.get_num_empty_tiles(self)
        return self.board_goodness
    

    # hueristic of more left to right increase
    def calc_board_monotonic(self):
        mon= 8 # max possible 4 rows+4 col
        n = len(self.board)
        # check rows
        for i in range(n):
            if not all(self.board[i][j] <= self.board[i][j+1] for j in range(n-1)):
                mon-=1
        # check columns
        for j in range(n):
            if not all(self.board[i][j] <= self.board[i+1][j] for i in range(n-1)):
                mon-=1
        return mon


    # hueristic of all rows and columns or decreasing    
    def calc_board_monotonic2(self):
        mon = 0
        n = len(self.board)
        # check rows
        for i in range(n):
            if all(self.board[i][j] >= self.board[i][j+1] for j in range(n-1)):
                mon += 1
            if all(self.board[i][j] <= self.board[i][j+1] for j in range(n-1)):
                mon += 1
        # check columns
        for j in range(n):
            if all(self.board[i][j] >= self.board[i+1][j] for i in range(n-1)):
                mon += 1
            if all(self.board[i][j] <= self.board[i+1][j] for i in range(n-1)):
                mon += 1
        return mon


    # hueristic of snake pattern in rows and col
    def calc_board_monotonic3(self):
        mon = 0
        n = len(self.board)
        # check rows
        for i in range(n):
            if i % 2 == 0:
                if all(self.board[i][j] >= self.board[i][j+1] for j in range(n-1)):
                    mon += 1
            else:
                if all(self.board[i][j] >= self.board[i][j+1] for j in range(n-1)):
                    mon += 1
        # check columns
        for j in range(n):
            if j % 2 == 0:
                if all(self.board[i][j] <= self.board[i+1][j] for i in range(n-1)):
                    mon += 1
            else:
                if all(self.board[i][j] >= self.board[i+1][j] for i in range(n-1)):
                    mon += 1
        return mon
    
   
    def spawn_children(self):
        # don't do anything if children already have been spawned
        if len(self.children) > 0:
            return
        # simulates moves if it's the players turn
        if (self.last_move == Move.TWO) or (self.last_move == Move.FOUR):
            for m in moves:
                if m == Move.LEFT:
                    child_data = logic.move_left(self.board, self.score)
                    # if it's a new, valid board
                    if child_data[1]:
                        child = PuzzleNode(child_data[0], child_data[2], m)
                        self.children.append(child)

                if m == Move.RIGHT:
                    child_data = logic.move_right(self.board, self.score)
                    # if it's a new, valid board
                    if child_data[1]:
                        child = PuzzleNode(child_data[0], child_data[2], m)
                        self.children.append(child)

                if m == Move.UP:
                    child_data = logic.move_up(self.board, self.score)
                    # if it's a new, valid board
                    if child_data[1]:
                        child = PuzzleNode(child_data[0], child_data[2], m)
                        self.children.append(child)

                if m == Move.DOWN:
                    child_data = logic.move_down(self.board, self.score)
                    # if it's a new, valid board
                    if child_data[1]:
                        child = PuzzleNode(child_data[0], child_data[2], m)
                        self.children.append(child)
            
        # it's the computer's move (to spawn a tile)
        else:
            # check every cell in the board
            for r in range(0, len(self.board)):
                for c in range(0, len(self.board)):
                    # if the cell is empty then simulate putting tiles there
                    if self.board[r][c] == 0:
                        # place a 2 tile
                        new_board_2 = [row[:] for row in self.board]
                        new_board_2[r][c] = 2
                        self.children.append(PuzzleNode(new_board_2, self.score, Move.TWO))
                        
                        # place a 4 tile
                        new_board_4 = [row[:] for row in self.board]
                        new_board_4[r][c] = 4
                        self.children.append(PuzzleNode(new_board_4, self.score, Move.FOUR))
