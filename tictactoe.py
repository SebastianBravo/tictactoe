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
    if terminal(board):
        return "Game is already over"

    num_x = 0
    num_o = 0

    for row in board:
    	for cell in row:
    		if cell == X:
    			num_x += 1
    		elif cell == O:
    			num_o += 1

    if num_x > num_o:
    	return O
    else:
    	return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return "Game is already over"

    possible_actions = set()

    for i in range(len(board)):
    	for j in range(len(board[i])):
            cell = board[i][j]
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    result_board = copy.deepcopy(board)

    if board[i][j] == EMPTY:
        result_board[i][j] = player(board)
        return result_board
    else:
        raise ValueError 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_win = [X, X, X]
    o_win = [O, O, O]

    diagonals = [[board[0][0], board[1][1], board[2][2]],
                [board[2][0], board[1][1], board[0][2]]]
    rows = copy.deepcopy(board)
    columns = []

    for num_col in range(3):
        column = [row[num_col] for row in board]
        columns.append(column)

    three_in_a_row = diagonals + columns + rows

    if x_win in three_in_a_row:
        return X
    elif o_win in three_in_a_row:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """ 
    full = not any(EMPTY in row for row in board)

    if winner(board) or full:
        return True
    else:
        return False


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
    values_actions = {}

    if player(board) == X:
        for action in actions(board):
            v = min_value(result(board, action))
            values_actions[v] = action

        max_v = max(values_actions.keys())

        return values_actions[max_v]

    else:
        for action in actions(board):
            v = max_value(result(board, action))
            values_actions[v] = action

        min_v = min(values_actions.keys())

        return values_actions[min_v]


def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v