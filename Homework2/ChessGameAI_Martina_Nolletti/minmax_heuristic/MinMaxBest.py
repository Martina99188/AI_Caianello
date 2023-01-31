"""
    MinMax Best
"""

import random
from typing import Any

import chess
from chess import Board

import minmax_heuristic
from minmax_heuristic import weight


class MyBestHeuristic:
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

    # minimax best (best subnodes)
    def H_L(self, state: Board, l: int):
        if l == 0:
            return self.H_0(state)
        possible_moves = []
        neighbors = list(state.legal_moves)
        random.shuffle(neighbors)
        for neighbor in neighbors:
            # move simulation
            state.push(neighbor)
            minmax = minmax_heuristic.MyHeuristic()
            # assigning value to the move
            neighbor_value = minmax.H_L(state, 1)
            possible_moves.append((neighbor, neighbor_value))
            state.pop()
        # sorting
        possible_moves = sorted(possible_moves, key=lambda x: (x[1]))
        filtered_possible_moves = []
        if len(possible_moves) > 0:
            if state.turn:
                for i in range(0, 2):
                    if len(possible_moves) > 0:
                        filtered_possible_moves.append(possible_moves.pop())
            else:
                filtered_possible_moves = possible_moves[0:2]
            possible_moves = filtered_possible_moves
            best_move = possible_moves.pop()[0]
            state.push(best_move)
            best_value = self.H_L(state, l - 1)
            if l == 4 and best_value != 10000 and best_value != -10000:
                MyBestHeuristic.write(state, best_value)
            state.pop()
            while len(possible_moves) > 0:
                next_move = possible_moves.pop()[0]
                state.push(next_move)
                next_value = self.H_L(state, l - 1)
                if l == 4 and next_value != 10000 and next_value != -10000:
                    MyBestHeuristic.write(state, next_value)
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

    @staticmethod
    def matrix_to_int(board):
        l = [None] * 64
        for sq in chess.scan_reversed(board.occupied_co[chess.WHITE]):
            l[sq] = board.piece_type_at(sq)
        for sq in chess.scan_reversed(board.occupied_co[chess.BLACK]):
            l[sq] = -board.piece_type_at(sq)
        return [0 if v is None else v for v in l]

    @staticmethod
    def write(board, value):
        f = open("./ts.csv", "a")
        list = MyBestHeuristic.matrix_to_int(board)
        f.write("[")
        for item in list:
            f.write(f"{item} ")
        f.write("],")
        f.write(f"{value}\n")
        f.close()


