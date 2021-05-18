import numpy as np
from EightPuzzleGame_State import State
'''
This class implements the Best-First-Search (BFS) algorithm along with the Heuristic search strategies

In this algorithm, an OPEN list is used to store the unexplored states and 
a CLOSED list is used to store the visited state. OPEN list is a priority queue. 
The priority is insured through sorting the OPEN list each time after new states are generated 
and added into the list. The heuristics are used as sorting criteria.

In this informed search, reducing the state space search complexity is the main criterion. 
We define heuristic evaluations to reduce the states that need to be checked every iteration. 
Evaluation function is used to express the quality of informed-ness of a heuristic algorithm.

Justin Gallagher 

'''

class InformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def sortFun(self, e):
        return e.weight

    """
     * check if the generated state is in open or closed
     * the purpose is to avoid a circle
     * @param s
     * @return
    """

    def check_inclusive(self, s):
        in_open = 0
        in_closed = 0
        ret = [-1, -1]

        for item in self.openlist:
            if item.equals(s):
                in_open = 1
                ret[1] = self.openlist.index(item)
                break

        for item in self.closed:
            if item.equals(s):
                in_closed = 1
                ret[1] = self.closed.index(item)
                break

        if in_open == 0 and in_closed == 0:
            ret[0] = 1  # the child is not in open or closed
        elif in_open == 1 and in_closed == 0:
            ret[0] = 2  # the child is already in open
        elif in_open == 0 and in_closed == 1:
            ret[0] = 3  # the child is already in closed
        return ret

    """
     * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """

    def state_walk(self):
        # add closed state
        self.closed.append(self.current)
        self.openlist.remove(self.current)
        # move to the next heuristic state
        walk_state = self.current.tile_seq
        row = 0
        col = 0

        for i in range(len(walk_state)):
            for j in range(len(walk_state[i])):
                if walk_state[i, j] == 0:
                    row = i
                    col = j
                    break

        self.depth = self.current.depth + 1

        ''' The following program is used to do the state space walk '''
        # ↑ move up
        if (row - 1) >= 0:
            # create temp 2d array and fill with current tile_seq
            tmp2D = [[0] * 3 for _ in range(3)]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            # create a temp state via the temp 2d array
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move up)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row-1][col]
            temp.tile_seq[row-1][col] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            # flag 1
            if flag[0] == 1:
                self.heuristic_test(temp)
                self.openlist.append(temp)
            # flag 2
            if flag[0] == 2:
                if temp.depth < self.openlist[flag[1]].depth:
                    self.openlist[flag[1]] = temp
            # flag 3
            if flag[0] == 3:
                if temp.depth < self.closed[flag[1]].depth:
                    self.closed.remove(self.closed[flag[1]])
                    self.openlist.append(temp)

        # ↓ move down
        if (row + 1) < len(walk_state):
            # create temp 2d array and fill with current tile_seq
            tmp2D = [[0] * 3 for _ in range(3)]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            # create a temp state via the temp 2d array
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move down)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row+1][col]
            temp.tile_seq[row+1][col] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            # flag 1
            if flag[0] == 1:
                self.heuristic_test(temp)
                self.openlist.append(temp)
            # flag 2
            if flag[0] == 2:
                if temp.depth < self.openlist[flag[1]].depth:
                    self.openlist[flag[1]] = temp
            # flag 3
            if flag[0] == 3:
                if temp.depth < self.closed[flag[1]].depth:
                    self.closed.remove(self.closed[flag[1]])
                    self.openlist.append(temp)

        # ← move left
        if (col - 1) >= 0:
            # create temp 2d array and fill with current tile_seq
            tmp2D = [[0] * 3 for _ in range(3)]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            # create a temp state via the temp 2d array
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move left)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row][col-1]
            temp.tile_seq[row][col-1] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            # flag 1
            if flag[0] == 1:
                self.heuristic_test(temp)
                self.openlist.append(temp)
            # flag 2
            if flag[0] == 2:
                if temp.depth < self.openlist[flag[1]].depth:
                    self.openlist[flag[1]] = temp
            # flag 3
            if flag[0] == 3:
                if temp.depth < self.closed[flag[1]].depth:
                    self.closed.remove(self.closed[flag[1]])
                    self.openlist.append(temp)

        # → move right
        if (col + 1) < len(walk_state):
            # create temp 2d array and fill with current tile_seq
            tmp2D = [[0] * 3 for _ in range(3)]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            # create a temp state via the temp 2d array
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move right)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row][col+1]
            temp.tile_seq[row][col+1] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            # flag 1
            if flag[0] == 1:
                self.heuristic_test(temp)
                self.openlist.append(temp)
            # flag 2
            if flag[0] == 2:
                if temp.depth < self.openlist[flag[1]].depth:
                    self.openlist[flag[1]] = temp
            # flag 3
            if flag[0] == 3:
                if temp.depth < self.closed[flag[1]].depth:
                    self.closed.remove(self.closed[flag[1]])
                    self.openlist.append(temp)

        # sort the open list first by h(n) then g(n)
        self.openlist.sort(key=self.sortFun)
        self.current = self.openlist[0]

    """
     * Solve the game using heuristic search strategies
     
     * There are three types of heuristic rules:
     * (1) Tiles out of place
     * (2) Sum of distances out of place
     * (3) 2 x the number of direct tile reversals
     
     * evaluation function
     * f(n) = g(n) + h(n)
     * g(n) = depth of path length to start state
     * h(n) = (1) + (2) + (3)
    """

    def heuristic_test(self, current):
        curr_seq = current.tile_seq
        goal_seq = self.goal.tile_seq

        # (1) Tiles out of place
        h1 = 0
        for i in range(len(curr_seq)):
            for j in range(len(curr_seq[i])):
                if not curr_seq[i, j] == goal_seq[i, j]:
                    h1 += 1

        # (2) Sum of distances out of place
        h2 = 0
        for i in range(len(curr_seq)):
            for j in range(len(curr_seq[i])):
                if not curr_seq[i, j] == goal_seq[i, j]:
                    h2 += abs(curr_seq[i, j] - goal_seq[i, j])

        # (3) 2 x the number of direct tile reversals
        h3 = 0
        for i in range(len(curr_seq)):
            for j in range(len(curr_seq[i])):
                if i + 1 < len(curr_seq):
                    if not curr_seq[i + 1, j] == 0 and not curr_seq[i, j] == 0:
                        if curr_seq[i + 1, j] == goal_seq[i, j] and curr_seq[i, j] == goal_seq[i + 1, j]:
                            h3 += 1
                if j + 1 < len(curr_seq[i]):
                    if not curr_seq[i, j + 1] == 0 and not curr_seq[i, j] == 0:
                        if curr_seq[i, j + 1] == goal_seq[i, j] and curr_seq[i, j] == goal_seq[i, j + 1]:
                            h3 += 1
        h3 *= 2

        # (4) Number of tiles out of row + number of tiles out of column
        h4 = 0
        curr_seq = np.array(curr_seq)
        goal_seq = np.array(goal_seq)
        for i in range(len(curr_seq)):
            for j in range(len(curr_seq[i])):
                if not curr_seq[i, j] == 0:
                    if not curr_seq[i, j] == goal_seq[i, j]:
                        currLoc = np.where(curr_seq == curr_seq[i, j])
                        goalLoc = np.where(goal_seq == curr_seq[i, j])
                        if (currLoc[0] - goalLoc[0]) != 0:
                            h4 += 1
                        if (currLoc[1] - goalLoc[1]) != 0:
                            h4 += 1
        # set the heuristic value for current state
        current.weight = current.depth + h1 + h2 + h3 + h4

    # You can choose to print all the states on the search path, or just the start and goal state 
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)
        print()

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print("choosen state !!!!!")
            print(self.current.tile_seq)
            print()
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
