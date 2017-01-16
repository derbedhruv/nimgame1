class NimGame:
    def __init__(self, n):
        self.n = n
    def startState(self):
        return self.n
    def isEnd(self, state):
        return True if state == 0 else False
    def utility(self, state, player):
        if state == 0:
            if player == 1:
                # you lost
                return float('-inf')
            else:
                # you won!
                return float('+inf')
    def actions(self, state):
        if state >= 3:
            return [1,2,3]
        return range(1, state+1)
    def successor(self, state, action):
        if action > state:
            return 0
        return state - action

def minimaxPolicy(game, state, player):
    # returns optimal (value, action) at a state
    # need to recursively compute the value, therefore define hte recursion function
    def recurse(state, player):
        if game.isEnd(state) == True:
            # return the utility of the state, no more actions that can be taken
            return (game.utility(state, player), None)
        if cache.has_key((state, player)):
            return cache[(state, player)]
        # otherwise, look at all possible actions in the game
        choices = [(recurse(game.successor(state, action), -1*player), action)[0] for action in game.actions(state)]
        # and return the max one if it is the agent and min if it is the opponent
        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        cache[(state, player)] = val
        return val
    # Now recurse over the choices for the state, return the second argument of returned tuple
    value, action = recurse(state, player)
    return value

game = NimGame(5)
cache = {}

if minimaxPolicy(game, game.startState(), 1) == float('+inf'):
    print "player wins"
else:
    print "adversary wins"
# print [game.successor(game.startState(), action) for action in game.actions(game.startState())]
