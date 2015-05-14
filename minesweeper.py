__author__ = 'alexandre'

import random
from pygame import *
import time

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


    """
    def reveal_blank(self, i, j):
        # we will work on the cell assuming it is a 0 cell
        # not opened and not flagged
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
            c.open = True
            self.reveal_blank(i, j)
            self.revealed_cells += 1
        # else it is either flagged or opened, so we do not do anything
    """

    def reveal_tile(self, i, j, revealed):  #  revealed : list containng position of already cell we reveal in the call of reveal_til
        c = self.cells[i][j]
        res = revealed
        if not c.open and not c.flag and (c.number != 0):  # we make sure it is not a 0 cell
            c.open = True
            self.revealed_cells += 1  # one more call revealed
            res.append((i, j))
        elif not c.open and not c.flag and (c.number == 0):  # it is a 0 cell not opened and not flagged
            c.open = True
            self.revealed_cells += 1
            res.append((i, j))
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if 0 <= i + a < self.y_size:
                        if 0 <= j + b < self.x_size:
                            self.reveal_tile(i + a, j + b, res)
        return res
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
        self.board.update_board()



    """
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


    """














    def new_game(self, difficulty="medium"):
        self.state = "new game"  # it is a temporary state to exit the while loop of the play function
        g = Game(difficulty)  # we define a new game
        g.play()  # then we play on it


    def play(self):
        init()
        # We start by initializing some variables

        # we set up the diplaying variables
        fond = Surface((520, 520))  # game window
        fond.fill(-1)  # filling the background
        x, y = fond.get_size()  # we get the size of the screen
        res = 800/max(self.length, self.height)  # we define the resolution
        # we make sure the size of one case doesn't exceed 26
        if res > 26:
            res = 26
        screen = display.set_mode((g.length*res, g.height*res), 0, 32)  # initialize a screen for display
        screen.blit(fond, (-(x-g.length*26)/2, -(y-g.height*26)/2))
        fond = screen.copy()



        # Here are the sprites

        # we define here the sprites representing the digit cells
        police = font.Font(font.get_default_font(), res)
        police0 = font.Font(font.get_default_font(), res+2)
        blanc = Surface((res, res))
        blanc.fill(transform.average_color(fond)[:-1])
        blanc.fill(-1, (0, 0, res - 1, res - 1))
        imgchiffre = [blanc] + [blanc.copy() for _ in range(8)]
        for i in xrange(1, 9):
            #fi0=police0.render(str(i),1,(255,255,255))
            #fr0=fi0.get_rect()
            fi = police.render(str(i), 1, (i % (2*124), i % (8*31), i % (4*62)))
            fr = fi.get_rect()
            fr.center = (res - 1)/2, (res - 1)/2
            # imgchiffre[i].blit(fi0,fr.topleft)
            imgchiffre[i].blit(fi, fr.topleft)

        # loading other sprites
        boom = image.load('sprites/boom.png')
        mine = image.load('sprites/mine.png')
        flag = image.load('sprites/danger.png')
        deg = image.load('sprites/deg3.png')
        display.set_icon(mine)

        # cases : all the rects that are clickable
        # we will use them to detect where the user clicks
        cases = [screen.blit(deg, ((x % self.length)*res, (x/self.length)*res)) for x in range(self.height*self.length)]
        display.flip()  # we update the screen


        # we print the all board
        # self.pint_game()
        while self.state == "playing":
            # we catch the user input
            # click left or right
            # the action method may update the state (win, loose, newgame)

            e = event.wait()  # we look for a click or a touch button
            if e.type == MOUSEBUTTONDOWN:  # there is a click !
                # what case did we collide ?
                x_p = Rect((mouse.get_pos()), (1, 1)).collidelist(cases)
                print x_p  # DEBUG
                (a, b) = (x_p / g.length, x_p % g.length)
                print (a, b)  # DEBUG
                # it is a right click
                if e.button == 1:
                    if not self.board.cells[a][b].flag:  # we check if it is not flagged
                        # we clicked on a mine
                        if self.board.cells[a][b].mine:
                            for i in xrange(g.height):
                                for j in xrange(g.length):
                                    if self.board.cells[i][j].mine:
                                        screen.blit(boom, cases[i])
                                    elif not self.board.cells[i][j].number:  # not opened
                                        print "open not mine"  # DEBUG
                                        screen.blit(imgchiffre[self.board.cells[i][j].number], cases[i])
                            self.state = "loose"   # we get out the while loop

                        elif not self.board.cells[a][b].open:  # we clicked on a cell not opened and not a mine

                            # self.reveal_cell_with_sprites
                            lst = self.board.reveal_tile(a, b, [])
                            # we reveal the tile and store the revealed pos in a list
                            for elem in lst:
                                (a, b) = elem
                                x_p = a*g.length + b
                                screen.blit(fond, cases[x_p].topleft, cases[x_p])
                                screen.blit(imgchiffre[self.board.cells[a][b].number], cases[x_p].topleft)
                                self.board.cells[a][b].open = True


                    # no more case left : we win
                    if self.board.total_safe_cells == self.board.revealed_cells:
                        for i in xrange(self.height):
                            for j in xrange(self.length):
                                if self.board.cells[i][j].mine:  # we reveal he mines
                                    screen.blit(mine, cases[i])
                        self.state = "win"  # we get out the while loop

                # it is a left click on a non revealed case
                elif e.button == 3 and not self.board.cells[a][b].open:
                    if not self.board.cells[a][b].flag:  # it was not already flagged
                        screen.blit(flag, cases[x_p])
                        self.board.cells[a][b].flag = True
                    else:  # it was flagged
                        screen.blit(fond, cases[x_p].topleft, cases[x_p])
                        screen.blit(deg, cases[x_p].topleft)
                        self.board.cells[x_p].flag = False
                display.flip()  # we update the screen
            if e.type == QUIT:  # the user quit
                event.post(event.Event(QUIT))
                break
            #display.flip()
            #while event.wait().type!=QUIT:pass
        # we exit the while loop winning or loosing
        if self.state in ["win", "loose"]:
            print "exit the loop"  # DEBUG
            time.sleep(5)
            # we change the state to win
            # we wait until the player click on a new game button
            # on click on main button : new game
            e = event.wait()  # we look for a click or a touch button
            if e.type == MOUSEBUTTONDOWN:  # there is a click !
                # what case did we collide ?
                p = Rect((mouse.get_pos()),(1,1)).collidelist(main_button)
                # it is a right click
                if e.button == 1:
                    self.newgame()  # we start a new game
        else:  # we exit the while loop asking for a new game
            self.newgame()

"""
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


    # print transform.average_color(fond)  # screen, surface de rendu

    g = Game()  # we create a new game

    board_g = g.board
    for i in xrange(15):
        print map(lambda c: c.number, board_g.cells[i])
    print g.length, g.height
    print g.total_mines
    print board_g.reveal_tile(4, 4, [])

    print g.play()
