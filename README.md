Maze Solver Python Project Guide

This function solves the Maze problem using Backtracking. It mainly uses solveMazeUtil() to solve the problem. It returns false if no path is possible, otherwise return true and prints the path in the form of 1s.

Approach................
************************
In a maze.... we have to find path from source to destination...

in left top corner [0][0]  is the source maze and in right bottom corner is destination

There are few cells which are blocked sowe can not go to that cells. we can move in any direction.

* Create a solution matrix of the same structure

* whenever we move in a cell ... mark that cell in solution matrix.

* At the end print solution

Function A ^^^^^^^^^^^^

Algorithm..............
***********************

* Create a solution matrix, initially filled with 0’s.

* Create a recursive funtion, which takes initial matrix, output matrix and position of source (i, j).

* if the position is out of the matrix or the position is not valid then return.

* Mark the position output[i][j] as 1 and check if the current position is destination or not. If destination is reached print the output matrix and return.

* Recursively call for position (i+1, j) and (i, j+1).

* Unmark position (i, j), i.e output[i][j] = 0.


Function B ^^^^^^^^^^

Input..................
***********************

* Open the code in vs editor

* Open cmd terminal in vs code

* Type command (maze.py) and press enter

* Now type size of matrix(example- 4) and press enter 

* Now enter matrix as size you entered before with space and enter
(example
1 0 1 0
1 1 1 1
0 1 1 0
0 1 0 1 )

** Note **
@ Please enter only binary digits (0,1) where 0 means blocked cell and 1 means active cell.
@ If you put size 3 it means 3 rows and 3 column, same goes in 4, 5 etc 

* Solution will be printed sucessfully


Function C ^^^^^^^^^^^^

Output.................
***********************

* It will print (No Path Found) if no path is available

* Or you will get solved matrix if path is possible.


2nd Method to run program without vs code

* Pull code From git repo  ( https://github.com/attainu/python-project-Karan-Kumar-au9/tree/master )

* Keep all files in same folder (maze.py, inputmaze.py outputmaze.py)

* Double click on maze.py file and open it in cmd.

* Now enter size of matrix in first row

* Now enter matrix and press enter

* you will find input saved in inputmaze.txt file and solution in outputmaze.txt


