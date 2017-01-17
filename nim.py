'''
    MINIMAX NIM GAME CLASS AND SOLVER
    AUTHOR: Dhruv Joshi
    ---------------------------------
    Based on concepts learned in CS221 - Artificial Intelligence at Stanford (Fall 2016)
'''
class NimGame:
    # --------------------------------------------------------- #
    # The game definition class                                 #
    # --------------------------------------------------------- #
    # A nim game is a type of zero sum game played by 2 players #
    # Read more at https://en.wikipedia.org/wiki/Nim            #
    # This class models the game and the methods allow the      #
    # evaluation of state space for different type of solvers   #
    # --------------------------------------------------------- #
    def __init__(self, n):
        # initialize the game - only the number 'n' is required
        # which tells us how many objects are there in a heap
        # this is the variant of the "subtraction game"
        self.n = n

    def startState(self):
        # Starting state - there are n objects in a single heap
        return self.n

    def isEnd(self, state):
        # the game has reached the end state if there are no objects
        return True if state == 0 else False

    def utility(self, state, player):
        # The utility is +inf for the player having won
        # and -inf for the adversary having won
        if state == 0:
            if player == 1:
                # you lost
                return float('-inf')
            else:
                # you won!
                return float('+inf')

    def actions(self, state):
        # the possible actions at a particular state
        if state >= 3:
            return [1,2,3]
        return range(1, state+1)

    def successor(self, state, action):
        # The (distinct) successor state if an action 
        # is taken at a particular state
        if action > state:
            return 0
        return state - action


def minimaxPolicy(game, state, player):
    # --------------------------------------------------------- #
    # The minimax solver in state space for a general game      #
    # --------------------------------------------------------- #
    # The minimax solver assumes a zero-sum 2-player game being #
    # played, between a human "player" and an AI "adversary"    #
    # It returns optimal (value, action) at a state.            #
    # It needs to recursively compute the value, therefore      #
    # define the recursion function within this function.       #
    #
    # Read more about minimax here:                             #
    # https://en.wikipedia.org/wiki/Minimax                     #
    # --------------------------------------------------------- #
    def recurse(state, player):
        # ----------------------------------------------------------------- #
        # The recursive function checks the sub-tree of a particular state  #
        # and minimizes expected value for the player while maximizing the  #
        # expected value of a player's move, i.e. assuming the player is    #
        # behaving using an optimal strategy
        # ----------------------------------------------------------------- #

        # start with the base case
        if game.isEnd(state) == True:
            # return the utility of the state, no more actions that can be taken
            return (game.utility(state, player), None)
        if cache.has_key((state, player)):
            return cache[(state, player)]

        # otherwise, look at all possible actions in the game
        # toggle the player each time it is called (since it is a 2-player game)
        # we thus represent the present player by 1 or -1 to ease toggling
        choices = [(recurse(game.successor(state, action), -1*player)[0], action) for action in game.actions(state)]

        # return the max of the choice of (utility, optimalAction) if it is the agent and min if it is the opponent
        # the min/max function will only be applied to hte first element of the tuple in the list "choices"
        # This is because we want to maximize/minimize over the expected utility, NOT the action
        # But we want the action as well.
        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        cache[(state, player)] = val
        return val

    # Recurse over the choices for the state, return the second argument of returned tuple
    # The solver will go all the way till the end of the tree to choose the optimal next action
    #
    # Returned values:
    # value = the optimal value (utility of the end state reached by both players taking a series of optimal actions)
    # action = the optimal action for the adversary to take next to minimize the expected utlity of the player
    value, action = recurse(state, player)
    return (value, action)

# cache values globally to speed up the minimax recursion
# dynamic programming ftw
cache = {}