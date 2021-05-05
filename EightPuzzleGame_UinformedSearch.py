import numpy as np
from EightPuzzleGame_State import State

'''
This class implement one of the Uninformed Search algorithm
This is a breadth first search algorithm that checks to uses some loop avoidance by only adding states to the open list
if they are not already in the open list or the closed list

Craig Mcghee

'''


class UninformedSearchSolver:
    current = State()
    goal = State()
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def check_inclusive(self, s):
        in_open = 0
        in_closed = 0
        ret = -1

        for item in self.openlist:
            if item.equals(s):
                in_open = 1
                #ret[1] = self.openlist.index(item)
                break

        for item in self.closed:
            if item.equals(s):
                in_closed = 1
                #ret[1] = self.closed.index(item)
                break

        if in_open == 0 and in_closed == 0:
            ret = 1  # the child is not in open or closed
        else:
            ret = 0
        #the only thing that needs to be checked is if it is not in either list as to avoid a looping situation
        return ret

    """
     * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """

    def state_walk(self):
        #add the current state to the closed list
        self.closed.append(self.current)
        #remove the current state from the open list
        self.openlist.remove(self.current)

        #get the empty space from the given tile sequence
        walk_state = self.current.tile_seq
        row = -1
        col = -1
        for i in range(len(walk_state)):
            for j in range(len(walk_state[i])):
                if walk_state[i, j] == 0:
                    row = i
                    col = j
                    break

        #increase the depth counter
        self.depth = self.current.depth + 1

        #start the sequence to decide what the possible moves from the given state are and how the lists change

        #move up ↑
        if (row - 1) >= 0:
            #populate a 2d array with the current states tile space
            tmp2D = [[0] * len(walk_state) for _ in range(len(walk_state))]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            #create a temporary state, temp, to act as the current state
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move up)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row - 1][col]
            temp.tile_seq[row - 1][col] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            #see what list to add the modified state to, if any
            if flag == 1:
                self.openlist.append(temp)

        #move down ↓
        if (row + 1) < len(walk_state):
            tmp2D = [[0] * len(walk_state) for _ in range(len(walk_state))]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            # create a temporary state, temp, to act as the current state
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move up)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row + 1][col]
            temp.tile_seq[row + 1][col] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            # see what list to add the modified state to, if any
            if flag == 1:
                self.openlist.append(temp)

        #move left ←
        if(col - 1) >= 0:
            tmp2D = [[0] * len(walk_state) for _ in range(len(walk_state))]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            # create a temporary state, temp, to act as the current state
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move up)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row][col - 1]
            temp.tile_seq[row][col - 1] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            # see what list to add the modified state to, if any
            if flag == 1:
                self.openlist.append(temp)

        #move right →
        if (col +1) < len(walk_state):
            tmp2D = [[0] * len(walk_state) for _ in range(len(walk_state))]
            for i in range(len(tmp2D)):
                for j in range(len(tmp2D[i])):
                    tmp2D[i][j] = self.current.tile_seq[i][j]
            #create a temporary state, temp, to act as the current state
            temp = State()
            temp.tile_seq = np.array(tmp2D)
            temp.depth = self.depth
            temp.weight = self.current.weight
            # swap the elements in tile_seq according to the move being made (move up)
            tmpvar = temp.tile_seq[row][col]
            temp.tile_seq[row][col] = temp.tile_seq[row][col + 1]
            temp.tile_seq[row][col + 1] = tmpvar
            # set flag equal to the check inclusive return
            flag = self.check_inclusive(temp)
            #see what list to add the modified state to, if any
            if flag == 1:
                self.openlist.append(temp)

        #set the first state in the open state to the current state
        self.current = self.openlist[0]

    # Check the following to make it work properly
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print()
            print("choosen state !!!!!")
            print(self.current.tile_seq)
            path += 1

        print()
        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
        print()