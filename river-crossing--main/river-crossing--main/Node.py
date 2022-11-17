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

    def getChildNodeState(self, action):
        #create Node with updated state from action
        result = NP.add(self.state, action)
        #print(f"{self.state} - {action} = ({mWS}, {cWS}, {bWS})")
        return result

    def createChildNode(self, action, parentNode):
        newMWrongSide, newCWrongSide, newBoatWrongSide = self.getChildNodeState(action)
        newChild = Node(newMWrongSide, newCWrongSide, newBoatWrongSide, parentNode)
        return newChild

    def validActions(self):
        #returns list of all valid moves
        actions = []
        everyMove = [NP.array([1,1,1]), NP.array([1,0,1]), NP.array([0,1,1]), NP.array([0,2,1]), NP.array([2,0,1])]
        for move in everyMove:
            if self.state[2] == 1:
                move *= -1
            newState = self.getChildNodeState(move)
            if not (-2 in newState or -1 in newState or 4 in newState or 5 in newState or newState[2] > 1 or newState[2] < 0 or (newState[0] not in [0,3] and newState[0] != newState[1])):
                actions.append(move)
        return actions

