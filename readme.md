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

To manage properly the dependency we will set up a virtualenvironement

* install python on your machine

* install pip
`easy_install pip`

* install virtualenv
`pip install virtualenv`

* create a virtual environment dedicated to the project
`virtualenv env_minesweeper`

* to enter the virtual env type to quit the virtual env type just deactivate
`source env_minesweeper/bin/activate`
simply ```deactivate``` to exit the virtual environment

* install all the requirements for the project
`pip install -r requirements.txt`


Improvements (TODO) :
---------------------

* Add several level of difficulty

* print the number mine left

* print the time

* let the user choose the size and the number of mines

* adding sound