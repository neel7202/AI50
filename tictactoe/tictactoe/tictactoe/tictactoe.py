"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    for row in board:
        for value in row:
            if value == X:
                numX += 1
            elif value == O:
                numO += 1
    if numX <= numO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for row in range(3):
        for value in range(3):
            if board[row][value] == EMPTY:
                actionSet.add((row, value))
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("action not possible")
    else:
        newBoard = copy.deepcopy(board)
        newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    for val in range(0, 3):
        if board[0][val] == board[1][val] == board[2][val] != EMPTY:
            return board[0][val]
        elif board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    complete = True
    for row in board:
        for val in row:
            if val == EMPTY:
                complete = False
    if winner(board) == X or winner(board) == O:
        complete = True
    return complete


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        for action in actions(board):
            if minValue(result(board, action)) == maxValue(board):
                 return action
    else:
        for action in actions(board):
             if maxValue(result(board, action)) == minValue(board):
                 return action


def maxValue(board):
    if terminal(board) == True:
        return utility(board)
    else:
        v = -1000
        for action in actions(board):
            v = max(v, minValue(result(board, action)))
        return v


def minValue(board):
    if terminal(board) == True:
        return utility(board)
    else:
        v = 10000
        for action in actions(board):
            v = min(v, maxValue(result(board, action)))
        return v
