"""
    Predictive MinMax
"""

import random

from sklearn.linear_model import LinearRegression
from typing import Any

import pandas as pandas
from chess import Board

from minmax_heuristic.MinMaxBest import MyBestHeuristic


class Model:
    model: Any

    def __init__(self):
        ds = pandas.read_csv("./ts.csv")
        X = []
        for single in ds["data"]:
            x = single.replace("[", "").replace("]", "").replace(" ", ",").split(",")
            x.pop()
            X.append([int(numeric_string) for numeric_string in x])
        y = []
        for single in ds["target"]:
            y.append(single)
        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict(self, board):
        x = [MyBestHeuristic.matrix_to_int(board)]
        return int(self.model.predict(x))


class MyPredictiveHeuristic:
    move: Any
    model = Model()

    def __init__(self):
        pass

    def __repr__(self):
        pass

    # metric of evaluation
    def H_0(self, state: Board):
        return self.model.predict(state)

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
