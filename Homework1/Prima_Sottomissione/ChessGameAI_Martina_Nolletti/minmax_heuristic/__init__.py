"""
    Heuristic
"""
import random
from typing import Any

from chess import Board


# weight of piece
def weight(piece):
    if piece == 6:
        return 10000
    if piece == 5:
        return 9
    elif piece == 4:
        return 5
    elif piece == 3 or piece == 2:
        return 3
    return 1


class MyHeuristic:
    move: Any

    def __init__(self):
        pass

    def __repr__(self):
        pass

    # metric of evaluation
    def H_0(self, state: Board):
        pieces = state.piece_map()
        ret = 0
        for index in pieces:
            if pieces[index].color:
                ret += weight(pieces[index].piece_type)
            else:
                ret -= weight(pieces[index].piece_type)
        return ret

    # min max
    def H_L(self, state: Board, l: int):
        if l == 0:
            return self.H_0(state)
        possible_moves = list(state.legal_moves)
        random.shuffle(possible_moves)
        if len(possible_moves) > 0:

            best_move = possible_moves.pop()
            state.push(best_move)
            best_value = self.H_L(state, l - 1)
            state.pop()
            while len(possible_moves) > 0:
                next_move = possible_moves.pop()
                state.push(next_move)
                next_value = self.H_L(state, l - 1)
                state.pop()
                if next_value > best_value and state.turn:
                    best_value = next_value
                    best_move = next_move
                if next_value < best_value and not state.turn:
                    best_value = next_value
                    best_move = next_move
            self.move = best_move
            return best_value
        else:
            if state.turn:
                return -10000
            else:
                return 10000
