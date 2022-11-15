import Node 

class Game:
        def __init__(self):
            self.initialNode = Node(3,3,1, None)

        def breadthFirstSearch(self):
            frontier = [self.initialNode]
            explored = []
            currentState = frontier.pop(0)

            while not currentState.isGoalState():
                explored.append(currentState)
                actions = currentState.validActions()
                for action in actions:
                    newState = currentState.getChildNode(action)
                    if newState not in explored and newState not in frontier:
                        frontier.append(newState)

                if len(frontier) == 0:
                    print("No Solution Found.")
                    return

                currentState = frontier.pop(0)
            
            print("Solution Found")

            finalPath = []
            while currentState.parent is not None:
                finalPath.append(currentState)
                currentState = currentState.parent

            finalPath.append(currentState)

            for state in reversed(finalPath):
                if state.action is not None:
                    print(state)

            print(f"Total steps: {len(finalPath)-1}")

game = Game()
game.breadthFirstSearch()



        