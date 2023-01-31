"""
    This is the main driver file. It will be responsible for displaying the object.

    NOTES IMPORTANT: When the program is running, hover the mouse over the board
    because it sometimes crashes!!!!!
"""

import chess
from minmax_heuristic import MyHeuristic
from alphabeta_heuristic import MyHeuristic2
import pygame as p

WIDTH = HEIGHT = 512
# dimensions of a chess board are 8x8
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
# for animations later on
MAX_FPS = 15
IMAGES = {}


# Initialize a global dictionary of images. This will be called exactly once in the main
def loadImages():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("img/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: can access an image by saying 'IMG['wP']'


# The main driver of the code. This will update the graphics.
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    # only do this once, before the while loop
    loadImages()
    running = True
    gameOver = False
    board = chess.Board()
    minmax = MyHeuristic()
    alphabeta = MyHeuristic2()
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            clock.tick(MAX_FPS)
            p.display.flip()
            if not gameOver:
                if board.turn:
                    minmax.H_L(board, 1)
                    board.push(minmax.move)
                else:
                    alphabeta.H_L(board, 2)
                    board.push(alphabeta.move)
                gameOver = board.is_game_over()
            drawGameState(screen, make_chess_matrix(board))


# Responsible for all the graphics within a current game state
def drawGameState(screen, board):
    # draw squares on the board
    drawBoard(screen)
    # add in piece highlighting or move suggestions (later)
    # draw pieces on top of those squares
    drawPieces(screen, board)


"""
    Draw squares on the board. The top left square is always light.
"""


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
    Draw the pieces on the board.
"""


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != ".":
                if piece.isupper():
                    piece = "w" + piece
                else:
                    piece = "b" + piece.upper()
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def make_chess_matrix(board):
    pgn = board.epd()
    foo = []
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo


if __name__ == '__main__':
    main()
