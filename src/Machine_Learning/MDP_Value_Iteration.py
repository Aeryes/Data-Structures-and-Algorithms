import random

# Peform the action and get the utility.
def getUtility(grid, row, col, action, actions):
    dirRow, dirCol = actions[action]
    newRow, newCol = row + dirRow, col + dirCol
    if newRow < 0 or newCol < 0 or newRow >= len(grid) or newCol >= len(grid) or (newRow == newCol == 1): # collide with the boundary or the wall
        return grid[row][col]
    else:
        return grid[newRow][newCol]

# Calculate the utility.
def calculateUtility(grid, row, col, action, discount, actions):
    reward = 0
    reward += 0.1 * discount * getUtility(grid, row, col, (action - 1) % 4, actions)
    reward += 0.8 * discount * getUtility(grid, row, col, action, actions)
    reward += 0.1 * discount * getUtility(grid, row, col, (action + 1) % 4, actions)
    return reward

#Value iteration entry point.
def valueIteration(grid, iterations, discount, actions, noise, actionStates):
    counter = 0

    while counter < iterations:
        for row in range(len(grid)):
            for col in range(len(grid)):
                #Check for wall, +2 and -2 rewards. If found then continue to the next iteration.
                if(grid[row][col] == -100) or (grid[row][col] == 2) or (grid[row][col] == -2):
                    continue
                else:
                    #Bellman equation. Perform all 4 actions.
                    tempList = []
                    for action in range(len(actions)):
                        tempList.append(calculateUtility(grid, row, col, action, discount, actions))

                    #grid[row][col] = max([calculateUtility(grid, row, col, action, discount, actions) for action in range(len(actions))])
                    maximum = max(tempList)
                    grid[row][col] = maximum

                    #Set the new action.
                    actionStates[row][col] = calculateDirection(tempList.index(maximum), noise)

        #Print the result
        printOutput(grid, actionStates)
        counter += 1

#Function to calculate direction attuned to noise value.
#If the result = '' the action has not changed.
def calculateDirection(actionNum, noise):

    action = 'n'

    #Figure out the action.
    if actionNum == 0:
        action = 's'
    if actionNum == 1:
        action = 'w'
    if actionNum == 2:
        action = 'n'
    if actionNum == 3:
        action = 'e' 

    randProbability = random.random()
    randProbability5050 = random.random()
    result = ''

    #North
    if (action == 'n') and (randProbability <= (noise / 2)):
        #Make another random number which will be 50/50.
        if randProbability5050 <= 0.50:
            result = 'w'
        else:
            result = 'e'
        return result
    elif randProbability == 0:
        result = 's'
        return result

    #South
    if (action == 's') and (randProbability <= (noise / 2)):
        #Make another random number which will be 50/50.
        randProbability5050 = random.random()
        if randProbability5050 <= 0.50:
            result = 'w'
        else:
            result = 'e'
        return result
    elif randProbability == 0:
        result = 'n'
        return result

    #East
    if (action == 'e') and (randProbability <= (noise / 2)):
        #Make another random number which will be 50/50.
        randProbability5050 = random.random()
        if randProbability5050 <= 0.50:
            result = 'n'
        else:
            result = 's'
        return result
    elif randProbability == 0:
        result = 'w'
        return result

    #West
    if (action == 'w') and (randProbability <= (noise / 2)):
        #Make another random number which will be 50/50.
        randProbability5050 = random.random()
        if randProbability5050 <= 0.50:
            result = 'n'
        else:
            result = 's'
        return result
    elif randProbability == 0:
        result = 'e'
        return result

    result = action
    return result

#Function to print out the grid and actions for each iteration.
def printOutput(grid, actions):
    result = ""

    for row in range(len(grid)):
        result += '\n'
        for col in range(len(grid[row])):
            result += "{:.2f}({}),".format(grid[row][col], actions[row][col])
    print(result)

def start():
    discount = 0.91
    actions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    noise = 0.15
    iteration = 30
    positiveTerminalLocation = [0,9,2.0]
    negativeTerminalLocation = [1,9,-2.0]
    stoneLocation = [2,8]

    gridStates = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],]

    actionStates = [
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],]

    #Prepare the initial state.
    #-100.0 = STONE
    #2.0 = Positive Reward.
    #-2.0 = Negative Reward.
    #'' = STONE in actionStates List.
    gridStates[positiveTerminalLocation[0]][positiveTerminalLocation[1]] = positiveTerminalLocation[2]
    gridStates[negativeTerminalLocation[0]][negativeTerminalLocation[1]] = negativeTerminalLocation[2]
    gridStates[stoneLocation[0]][stoneLocation[1]] = -100.0

    actionStates[stoneLocation[0]][stoneLocation[1]] = ''

    #Do the value iteration.
    valueIteration(gridStates, iteration, discount, actions, noise, actionStates)

#Driver code.
start()
