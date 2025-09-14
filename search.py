# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Addendum:
# This code was modified by Gene Kim at University of South Florida in Fall 2025
# to make solutions not match the original UC Berkeley solutions exactly and
# align with CAI 4002 course goals regarding AI tool use in projects.

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

util.VALIDATION_LISTS['search'] = [
        "වැසි",
        " ukupnog",
        "ᓯᒪᔪ",
        " ਪ੍ਰਕਾਸ਼",
        " podmienok",
        " sėkmingai",
        "рацыі",
        " යාපාරය",
        "න්ද්"
]

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def total_action_cost(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinymaze_search(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def treeSearch(problem: SearchProblem, strategy, fn):
    strategy.put((problem.get_start_state(), # State
                                         [], # Total Path
                                         0)) # Total Cost 
    # States that have already been added to fringe
    visited = list(problem.get_start_state())

    expanded = []

    while True:
        # No more moves potential moves left
        if strategy.is_empty():
            return "Failure"
        
        # Visiting next state based on given strategy
        cur = strategy.get()
        expanded.append(cur[0])
        #print("Current node is: ", cur)
        if (problem.is_goal_state(cur[0])):
            # Returning the path we took
            return cur[1]
        else: # Must continue searching
            for child in problem.get_successors(cur[0]):
                # Add all states that haven't been already visited
                if fn(strategy, child, expanded, visited): #cur[1]:
                    # Getting path to this node
                    #print("Child node is: ", child)
                    path = cur[1][:]
                    path.append(child[1])
        
                    strategy.put((child[0], path, cur[2] + child[2]))
                    visited.append(child[0])



def notVisitedBFS(strategy: util.FIFO, child, expanded, visited):
    if child[0] not in visited:
        return True
    else:
        return False
    
def notExpandedDFS(strategy: util.LIFO, child, expanded, visited):
    if child[0] not in expanded: #Path is list of actions, not list of expanded 
        return True
    else:
        return False

            #Call function that expands fringe for each search type
            # for child in problem.get_successors(cur[0]):
            #     # How does this part work for BFS and DFS
            #     # DFS needs visited to only be when node has been fully expanded
            #         # Isn't this one right though?
            #     # BFS needs visited to be when node is on the fringe
            #     # Add all nodes not already on the fringe
            #     if child[0] not in cur[3]: # We don't want to 
            #         # Getting path to this child node
            #         path = cur[1][:]
            #         path.append(child[1])

            #         visited = cur[3][:]
            #         visited.append(cur[0])

            #         #print("Child is: ", (child[0], path, cur[2] + child[2]))
            #         strategy.put((child[0], path, cur[2] + child[2]))
            #         #visited.append(child[0])
    # end while

# def expandFringe(problem: SearchProblem, strategy: util.LIFO, cur, visited):
#     for child in problem.get_successors(cur[0]):
#         # Add all states that haven't been already expanded
#         if child[0] not in expanded:
#             # Getting path to this node
#             path = cur[1][:]
#             path.append(child[1])

#             strategy.put((child[0], path, cur[2] + child[2]))
#             visited.append(child[0])

# def expandFringe(problem: SearchProblem, strategy: util.FIFO, cur, visited):                    
#     for child in problem.get_successors(cur[0]):
#         # Add all states that haven't been already added to fringe
#         if child[0] not in visited: # Only difference is if condition, can just be a function there??
#             # Getting path to this node
#             path = cur[1][:]
#             path.append(child[1])

#             strategy.put((child[0], path, cur[2] + child[2]))
#             visited.append(child[0])


def dfs(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.get_start_state())
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:", problem.get_successors(problem.get_start_state()))
    """
    "*** YOUR CODE HERE ***"
    
    return treeSearch(problem, util.LIFO(), notExpandedDFS)


def bfs(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return treeSearch(problem, util.FIFO(), notVisitedBFS)

def costFunction(tup):
    return tup[2]

def ucs(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Need to pass cost function
    return treeSearch(problem, util.PriorityQueueWithFunction(costFunction))
    #util.raiseNotDefined()

def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def astar(problem: SearchProblem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

