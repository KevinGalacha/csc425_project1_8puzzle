'''
Solving Eight Puzzle Game using Search Strategies
The eight-puzzle game is a 3 × 3 version of the 15-puzzle in which eight tiles can be moved around in nine spaces.
CSC 425 525 Artificial Intelligence
Instructor: Dr. Junxiu Zhou
Semester: Fall 2020

Your name: Justin Gallagher and Craig Mcghee
'''

import time
import numpy as np
from EightPuzzleGame_State import State
from EightPuzzleGame_UinformedSearch import UninformedSearchSolver
from EightPuzzleGame_InformedSearch import InformedSearchSolver


class EightPuzzleGame:
    titles = 8
    def __init__(self, initial=[], goal=[], tiles=8):
        self.initial = initial
        self.goal = goal
        self.tiles = tiles

    def start(self):
        # initialize the init state and goal state as 2d array
        init_tile = np.array([[2, 3, 6], [1, 4, 8], [7, 5, 0]]) # success!
        #init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]]) # success!

        init = State(init_tile, 0, 0)

        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        goal = State(goal_tile, 0, 0)

        self.tiles = 8

        print("*************** UNIFORMED BREADTH-FIRST SEARCH ***************")

        t0 = time.time()
        UIS_solver = UninformedSearchSolver(init, goal)
        UIS_solver.run()
        t1 = time.time()
        totalUISTime = t1 - t0

        print("*************** INFORMED BEST-FIRST SEARCH ***************")

        t0 = time.time()
        IS_solver = InformedSearchSolver(init, goal)
        IS_solver.run()
        t1 = time.time()
        totalISTime = t1 - t0

        print()
        print("*************** COMPARISON ANALYSIS ***************")
        print("Uniformed Breadth-First Search: ", totalUISTime)
        print("Informed Best-First Search Time: ", totalISTime)

# start the puzzle game
epp = EightPuzzleGame()
epp.start()

