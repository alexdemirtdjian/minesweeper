__author__ = 'alexandre'

import random
from pygame import *
import time
import os

# This is a class representing a cell
# it is a simple class with 4 attributes


class Cell():

    def __init__(self):
        self.open = False  # we set the cell at closed by default
        self.flag = False  # we do not set a flag
        self.number = 0    # we set for now 0 for the cell
        self.mine = False  # There is no mine for now


# This is a class representing a board
# It inherit from cell


class Board():

    def __init__(self, x_size, y_size, mines):
        # we initialize the borad with length, height and number of mines
        self.x_size = x_size
        self.y_size = y_size
        self.mines = mines
        # cells is a matrix containing the x_size * y_size cells
        self.cells = []
        # This is the number of safe cells to compare with the number of open cells
        # and determine if the player wins
        self.total_safe_cells = (x_size * y_size) - mines
        # We will compare revealed_cells with total_safe_cells
        self.revealed_cells = 0

        # we start by filling the board with empty cells
        for j in xrange(y_size):
            row = []
            for i in xrange(x_size):
                c = Cell()
                row.append(c)
            self.cells.append(row)

        # we then add the mines randomly
        remaining = mines  # we store remaining mines in this variable
        while remaining:
            (i, j) = (random.randint(0, self.y_size - 1), random.randint(0, self.x_size - 1))
            # we check before if it is not already a mine
            if not self.cells[i][j].mine:
                self.cells[i][j].mine = True
                self.cells[i][j].number = -1   # we set the mine number to
                remaining -= 1

    def update_cell(self, i, j):
        """
        this function takes a position in the board, assuming it is a bomb
        it will update the number of the neighbours
        :param i: int
        :param j: int
        :return: unit
        """
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 0 <= i + a < self.y_size:
                    if 0 <= j + b < self.x_size:
                        # if the neighbour is not a bomb
                        # and (a, b) != (0, 0), of course we do not update the current cell
                        if not self.cells[i + a][j + b].mine and ((a, b) != (0, 0)):
                            self.cells[i + a][j + b].number += 1

    def update_board(self):
        """
        This function will update the number of each cell in the board
        :return: unit
        """
        for i in xrange(self.y_size):
            for j in xrange(self.x_size):
                if self.cells[i][j].mine:  # it is a bomb, we update the neighbours
                    self.update_cell(i, j)  # we use the previous auxiliary function

    def reveal_cell(self, i, j, revealed):
        """
        This function takes a position and reveals it. In case it is a 0 cell
        it will reveal all the safe neighbours
        It takes an additional argument, revealed, which is a list containing the position
        of all the cell we revealed so far calling the function (it is a recursive function)
        The function returns the position of the revealed cells (only one cell most of the time)
        :param i: int
        :param j: int
        :param revealed: (int * int) list
        :return: (int * int) list
        """
        c = self.cells[i][j]
        res = revealed  # the position of the cell we will reveal
        if not c.open and not c.flag and (c.number != 0):  # it is not a 0 cell
            c.open = True   # we open it
            self.revealed_cells += 1   # one more cell revealed
            res.append((i, j))
        elif not c.open and not c.flag and (c.number == 0):  # it is a 0 cell not opened and not flagged
            c.open = True
            self.revealed_cells += 1
            res.append((i, j))  # we add (i, j) to the list of revealed cell
            # we reveal then the neighbours because they are all safe
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if 0 <= i + a < self.y_size:
                        if 0 <= j + b < self.x_size:
                            # we call recursively reveal_cell to open the other cells
                            # in case there is many 0s
                            self.reveal_cell(i + a, j + b, res)
        # else it is either flagged or opened, so we do not do anything
        return res  # we return the position of the cells we opened


# this is a dictionary representing the difficulty with the board associated
# key : string, values : (length, height, total_mines)
dico = {"easy": (10, 10, 10), "medium": (16, 16, 40), "expert": (30, 16, 99)}

cell_size = 1  # the size of a cell on the screen


# This file define a class representing a game

class Game():

    def __init__(self, difficulty="medium"):

        self.state = "playing"  # state of the game
        self.difficulty = difficulty  # "easy", "medium", "expert"
        self.length = dico[difficulty][0]  # the x_size of the board
        self.height = dico[difficulty][1]  # the y_size of the board
        self.total_mines = dico[difficulty][2]
        self.board = Board(self.length, self.height, self.total_mines)  # we can now initialize the board
        self.board.update_board()  # we not forget to update the number on the cells
        self.res = min(26, 800/max(self.length, self.height))   # we make sure the size of one case doesn't exceed 26


    def new_game(self, difficulty="medium"):
        """
        This function create an new game object, and launch the playing loop
        :param difficulty: string, medium by default
        :return: unit
        """
        self.state = "new game"  # it is a temporary state to exit the while loop of the play function
        time.sleep(0.001)
        self.state = "playing"
        g = Game(difficulty)  # we define a new game
        g.play()  # then we play on it


    # The main function
    #
    def play(self):
        """
        Tris is the core program launching an "infinite loop", on which we can though escape
         changing the state of the game
        :return: unit
        """
        init()

        #
        # We start by initializing some variables
        #

        # we set up the displaying variables
        window = Surface((520, 620))  # game window
        window.fill((127, 140, 141))  # filling the background with light grey rgb
        x, y = window.get_size()  # we get the size of the screen

        # initialize a screen for display
        # 32 bit of resolution (max)
        screen = display.set_mode((self.length*self.res, self.height*self.res + 100))  # (self.length*self.res, self.height*self.res), 0, 32)
        # we paste (blit) the grid
        screen.blit(window, (-(x-self.length*26)/2, -(y-self.height*26)/2))

        background = screen.copy()
        # the colors of the digit we will print (rgb format)
        #
        colors = {1: (52, 152, 219),
                  2: (39, 174, 96),
                  3: (192, 57, 43),
                  4: (142, 68, 173),
                  5: (44, 62, 80),
                  6: (26, 188, 156),
                  7: (241, 196, 15),
                  8: (127, 140, 141)}

        #
        # Here are the sprites
        #

        # we create here the sprites representing the digit cells
        white_surface = Surface((self.res, self.res))  # the background of the sprites
        white_surface.fill(transform.average_color(background)[:-1])
        white_surface.fill(-1, (0, 0, self.res - 1, self.res - 1))
        # we define here a list of sprite representing the sprite with digit
        # the blank white_surface is for the 0 sprite
        sprite_digit = [white_surface] + [white_surface.copy() for _ in range(8)]
        for i in xrange(1, 9):
            ft = font.Font(font.get_default_font(), g.res)
            fi = ft.render(str(i), 1, colors[i])
            fr = fi.get_rect()  # we get the rect area of the fi surface
            fr.center = (self.res - 1)/2, (self.res - 1)/2  # we define the center of our sprite
            sprite_digit[i].blit(fi, fr.topleft)

        # loading other sprites

        boom = image.load(os.path.abspath('sprites/boom.png'))  # the sprite rendered when we lose
        mine = image.load(os.path.abspath('sprites/mine.png'))  # the sprite rendered when we win (neutralized mine)
        flag = image.load(os.path.abspath('sprites/danger.png'))  # when we put a flag
        deg = image.load(os.path.abspath('sprites/deg3.png'))  # a transparent sprite, when we reveal the cell
        playagain = image.load(os.path.abspath('sprites/playagain.jpg'))
        display.set_icon(mine)

        # clickable is a list containing all the rects that are clickable
        # we will use them to detect where the user clicks
        clickable = [screen.blit(deg, ((x % self.length)*self.res, (x/self.length)*self.res + 100))
                     for x in range(self.height*self.length)]

        menu_clickable = [screen.blit(playagain, ((self.length-2)*self.res/2, 30))]
        display.flip()  # we update the screen

        # we enter the while loop, and stay until we change the state from playing
        while self.state == "playing":
            # we listen for user input
            # click left or right ?
            # the action method may update the state (win, lose, new_game)
            # for instance left click on a bomb changes the state to "lose"
            e = event.wait()  # we look for a click or a touch button

            if e.type == MOUSEBUTTONDOWN:  # there is a click !
                if Rect((mouse.get_pos()), (1, 1)).collidelist(menu_clickable) >= 0:  # we click on a menu button
                    print Rect((mouse.get_pos()), (1, 1)).collidelist(menu_clickable)
                    self.new_game()
                # what case did we collide ?
                # we transform the click into a (1px, 1px) rect
                # we find the first cell we collide, defined by x_p
                x_p = Rect((mouse.get_pos()), (1, 1)).collidelist(clickable)
                # we made the euclidian division of x_p by g.length
                # since we work with matrix
                (a, b) = (x_p / g.length, x_p % g.length)

                if e.button == 1:  # it is a left click
                    if not self.board.cells[a][b].flag:  # we check if it is not flagged

                        # we click on a mine !!
                        if self.board.cells[a][b].mine:
                            # we have lost, so we reveal all the mines
                            for i in xrange(g.height):
                                for j in xrange(g.length):
                                    if self.board.cells[i][j].mine:  # it is a mine, we explode it
                                        screen.blit(boom, clickable[i*g.length + j])
                                    elif not self.board.cells[i][j].open:  # not opened cell
                                        screen.blit(sprite_digit[self.board.cells[i][j].number], clickable[i*self.length + j])
                            # self.state = "lose"   # we get out the while loop

                        # we click on a cell not opened and not a mine
                        elif not self.board.cells[a][b].open:
                            # we open on the board all the safe cells we can
                            # one if the digit is >= 1, several if it is 0
                            # and we store the safe cells we opened into lst
                            lst = self.board.reveal_cell(a, b, [])
                            # now we loop on lst, to reveal (blit method) on the screen
                            for elem in lst:
                                (a, b) = elem  # the position of the cell
                                x_p = a*g.length + b  # we infer the position in "clickable" list
                                screen.blit(background, clickable[x_p].topleft, clickable[x_p])
                                screen.blit(sprite_digit[self.board.cells[a][b].number], clickable[x_p].topleft)
                                self.board.cells[a][b].open = True

                    # no more cell left : we win !!
                    if self.board.total_safe_cells == self.board.revealed_cells:
                        # we find all the mines, so we neutralize them
                        for i in xrange(self.height):
                            for j in xrange(self.length):
                                if self.board.cells[i][j].mine:  # we neutralize the mines
                                    screen.blit(mine, clickable[i*g.length + j])
                        # print winning message
                        # self.state = "win"  # we get out the while loop changing the state

                # it is a right click on a non revealed cell
                elif e.button == 3 and not self.board.cells[a][b].open:
                    if not self.board.cells[a][b].flag:  # it was not already flagged
                        screen.blit(flag, clickable[x_p])  # so we put a flag
                        self.board.cells[a][b].flag = True
                    else:  # it was already flagged
                        screen.blit(background, clickable[x_p].topleft, clickable[x_p])  # so we remove it
                        screen.blit(deg, clickable[x_p].topleft)
                        self.board.cells[a][b].flag = False
                display.flip()  # we update the screen
            if e.type == QUIT:  # the user quit
                event.post(event.Event(QUIT))
                break


if __name__ == "__main__":
    g = Game()  # we create a new game
    board_g = g.board  #
    #for i in xrange(15):
    #    print map(lambda c: c.number, board_g.cells[i])
    #print g.length, g.height
    #print g.total_mines
    print g.play()
