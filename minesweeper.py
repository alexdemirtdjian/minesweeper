__author__ = 'alexandre'

import random
import pygame

# This file define a class representing a cell


class Cell():

    def __init__(self):
        self.open = False
        self.flag = False
        self.number = 0
        self.mine = False


# This file define a class representing a board
# It inherit from cell


class Board():

    def __init__(self, x_size, y_size, mines):
        self.x_size = x_size
        self.y_size = y_size
        self.mines = mines
        self.cells = []
        self.total_safe_cells = (x_size*y_size) - mines
        self.revealed_cells = 0
        # we start by filling the board with empty cells
        for j in xrange(y_size):
            row = []
            for i in xrange(x_size):
                c = Cell()
                row.append(c)
            self.cells.append(row)

        # we then add the mines randomly
        remaining = mines  # remaining mines
        while remaining:
            (i, j) = (random.randint(0, self.y_size - 1), random.randint(0, self.x_size - 1))
            if not self.cells[i][j].mine:
                self.cells[i][j].mine = True
                self.cells[i][j].number = -1
                remaining -= 1

    def get_size(self):
        return self.x_size, self.y_size

    def update_tile(self, i, j):
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 0 <= i + a < self.y_size:
                    if 0 <= j + b < self.x_size:
                        if not self.cells[i + a][j + b].mine and ((a, b) != (0, 0)):  # it is not a bomb and not 0,0
                            self.cells[i + a][j + b].number += 1

    def update_board(self):
        for i in xrange(self.y_size):
            for j in xrange(self.x_size):
                if self.cells[i][j].mine:  # it is a bomb, we update the neighbours
                    self.update_tile(i, j)

    def reveal_blank(self, i, j):
        c = self.cells[i][j]
        # we will wrk on the c cell assuming it is a 0
        # cell, not opened, not flagged
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 0 <= i + a < self.y_size:
                    if 0 <= j + b < self.x_size:
                        self.reveal_tile(i + a, j + b)

    def reveal_tile(self, i, j):
        c = self.cells[i][j]
        if not c.open and not c.flag and (c.number != 0):  # we make sure it is not a 0 cell
            c.open = True
            self.revealed_cells += 1  # one more call revealed
        elif not c.open and not c.flag and (c.number == 0):
            self.reveal_blank(i, j)
        # else it is either flagged or opened, so we do not do anything




# This file define a class representing a game
# It inherit from board

dico = {"easy": (10, 10, 10), "medium": (16, 16, 40), "expert": (30, 16, 99)}
# this is a dictionary representing the difficulty with the board (length, height, total_mines)

cell_size = 1  # the size of a cell on the screen
# level =

class Game():

    def __init__(self, difficulty="medium"):
        self.state = "playing"  # "win" or "loose"
        self.difficulty = difficulty  # "easy", "medium", "hard"
        self.length = dico[difficulty][0]
        self.height = dico[difficulty][1]
        self.total_mines = dico[difficulty][2]
        self.board = Board(self.length, self.height, self.total_mines)

"""
    @staticmethod
    def newgame(self, difficulty="medium"):


    def action_left(self):
        (x, y) = pygame.mouse.get_pos()
        # if the user clicked on the new game button
        if (x, y) in

        # else if the user changed the difficulty
        elif (x, y) in

        # else if the user clicked on the board
        elif (x, y) in
        (n, m) = (int(x) % cell_size, int(y) % cell_size)
        # we check if the user clicked on the board
        # then we perform the right click
        if not self.board.cells[n][m].flag:  # we check the cell is not flagged
            self.board.reveal_tile(n, m)
            if self.board.cells[n][m].mine:  # it is a mine !
                self.state = "loose"
            if self.board.revealed_cells == self.board.total_safe_cells:  # we win
                self.state = "win"

    def action_right(self):
        (x, y) = pygame.mouse.get_pos()
        (n, m) = (int(x) % cell_size, int(y) % cell_size)
        # we check if the user clicked on the board
        # then we perform the right click
        if not self.board.cells[n][m].open:
            self.board.cells[n][m].flag = not self.board.cells[n][m].flag
            # we make the opposite value for the flag

    # pygame.mouse.get_pressed()[0] or [2]

    def new_game(self, difficulty="medium"):
        self.state = "new game"  # it is a temporary state to exit the while loop of the play function
        g = Game(difficulty)  # we define a new game
        g.play()  # then we play on it


#    def print_game(self):



    def play(self):
        # we print the all board
        # self.pint_game()
        while self.state == "playing":
            # we catch the user input
            # click left or right
            # the action method may update the state (win, loose, newgame)
        if self.state == "win":
            # we change the face to win
            # we wait until the player click on a new game button
            # on click : self.newgame()
        elif self.state == "loose":  # self.stats == "loose"
            # we change the face to loose
            # we wait until the player click on a new game button
        else:
            # we will use this state when player will ask a new game
            # we will use a temporary newgame state, to exit the while loop
            # we will exit the play function, then re play
            return
"""

if __name__ == "__main__":
    c = Cell()
    print c
    print c.flag, c.mine, c.number, c.open
    b = Board(15, 15, 50)
    b.update_tile(5, 5)
    b.update_board()
    print b
    for i in xrange(15):
        print map(lambda c: c.number, b.cells[i])
