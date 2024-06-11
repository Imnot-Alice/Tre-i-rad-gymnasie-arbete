import numpy as np
import copy


def player(boardState):
    xCount = 0
    oCount = 0
    for i in range(9):
        if boardState[i] == 1:
            xCount += 1
        elif boardState[i] == -1:
            oCount += 1
    if xCount > oCount:
        return "O"
    else:
        return "X"
    

def actions(boardState):
    actionList = []
    for i in range(9):
        if boardState[i] == 0:
            actionList.append(i)
    return actionList

def result(boardState, action):
    newState = copy.deepcopy(boardState)
    if player(newState) == "X":
        newState[action] = 1
    else:
        newState[action] = -1
    return newState


        
def terminal(boardState):
    if 0 not in boardState:
        return True
    else:
        if abs(boardState[0] + boardState[1] + boardState[2]) == 3:
            return True
        elif abs(boardState[3] + boardState[4] + boardState[5]) == 3:
            return True
        elif abs(boardState[6] + boardState[7] + boardState[8]) == 3:
            return True
        elif abs(boardState[0] + boardState[3] + boardState[6]) == 3:
            return True
        elif abs(boardState[1] + boardState[4] + boardState[7]) == 3:
            return True
        elif abs(boardState[2] + boardState[5] + boardState[8]) == 3:
            return True
        elif abs(boardState[0] + boardState[4] + boardState[8]) == 3:
            return True
        elif abs(boardState[2] + boardState[4] + boardState[6]) == 3:
            return True
        else:
            return False
        
def evaluate(boardState):
    if abs(boardState[0] + boardState[1] + boardState[2]) == 3:
        if boardState[0] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[3] + boardState[4] + boardState[5]) == 3:
        if boardState[3] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[6] + boardState[7] + boardState[8]) == 3:
        if boardState[6] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[0] + boardState[3] + boardState[6]) == 3:
        if boardState[0] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[1] + boardState[4] + boardState[7]) == 3:
        if boardState[1] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[2] + boardState[5] + boardState[8]) == 3:
        if boardState[2] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[0] + boardState[4] + boardState[8]) == 3:
        if boardState[0] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[2] + boardState[4] + boardState[6]) == 3:
        if boardState[2] == -1:
            return -1
        else:
            return 1
    elif 0 not in boardState:
        return 0
    else:
        raise RuntimeError


def playX(boardState):
    if terminal(boardState) == True:
        return evaluate(boardState)
    else:
        v = -10
        actionlist = actions(boardState)
        actionsN = len(actionlist)
        for i in range(actionsN):
            newState = result(boardState, actionlist[i])
            v = max(v, playO(newState))
        return v

def playO(boardState):
    if terminal(boardState) == True:
        return evaluate(boardState)
    else:
        v = 10
        actionlist = actions(boardState)
        actionsN = len(actionlist)
        for i in range(actionsN):
            newState = result(boardState, actionlist[i])
            v = min(v, playX(newState))
        return v


def play(boardState):
    if player(boardState) == "X":
        valueList = []
        optAction = [0, -10]
        actionlist = actions(boardState)
        actionsN = len(actionlist)
        for i in range(actionsN):
            newState = result(boardState, actionlist[i])
            v = playO(newState)
            valueList.append([i, v])
        for i in range(len(valueList)):
            if valueList[i][1] > optAction[1]:
                optAction = valueList[i]
        return actionlist[optAction[0]]
    else:
        valueList = []
        optAction = [0, 10]
        actionlist = actions(boardState)
        actionsN = len(actionlist)
        for i in range(actionsN):
            newState = result(boardState, actionlist[i])
            v = playX(newState)
            valueList.append([i, v])
        for i in range(len(valueList)):
            if valueList[i][1] < optAction[1]:
                optAction = valueList[i]
        return actionlist[optAction[0]]
