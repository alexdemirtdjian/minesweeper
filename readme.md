A simple object oriented minesewwper using pygame
=================================================

This is a pygame project containing a simple minesweeper

![Alt text](/img/minesweeperScreenshot.png?raw=true "Screenshot of minesweeper")

Global layout :

It is organised into three class :

- cell : representing a cell with a couple of attributes
- board : representing the board
- game : representing the game and containing the main loop

Install :
---------

To run the program you need to install pygame

For this we will use a virtual environment

First check to have python 2.6 > installed

Install pip ```sudo easy_install pip```

Then install virtual_environment ```sudo pip install virtual_env```

To run the virtual env : virtual_env /bin/activate

simply ```deactivate```to exit the virtual environment

pip install -r requirements


Improvements (TODO) :
---------------------

* Add several level of difficulty

* print the number mine left

* print the time

* let the user choose the size and the number of mines

* adding sound