import numpy as NP

class Node:

    def __init__(self, mWrongSide, cWrongSide, boatWrongSide, parent):
        self.state = [mWrongSide, cWrongSide, boatWrongSide]
        self.parent = parent

    def isGoalState(self):
        #check if state = [0,0,0]
        if self.state == [0,0,0]:
            return True
        return False

    def getChildNode(self, action):
        #create Node with updated state from action
        mWS, cWS, bWS = NP.subtract(self.state, action)
        return mWS, cWS, bWS

    def validActions(self, nodeState):
        #returns list of all valid moves
        pass

