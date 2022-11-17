from Node import Node 

class Game:
        def __init__(self):
            self.initialNode = Node(3,3,1, None)

        def breadthFirstSearch(self):
            frontier = [self.initialNode]
            exploredStates = []
            currentState = frontier.pop(0)

            while not currentState.isGoalState():
                exploredStates.append(currentState.state)
                actions = currentState.validActions()
                print(f"exploring: <{currentState.state[0]},{currentState.state[1]},{currentState.state[2]}>")
                for action in actions:
                    newState = currentState.createChildNode(action, currentState)
                    if newState.state not in exploredStates:
                        frontier.append(newState)
                        exploredStates.append(newState.state)

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

            for i ,state in enumerate(reversed(finalPath)):
                print(f"Move {i}: <{state.state[0]},{state.state[1]},{state.state[2]}>")

            print(f"Total steps: {len(finalPath)-1}")


if __name__ == "__main__":
    game = Game()
    game.breadthFirstSearch()


        