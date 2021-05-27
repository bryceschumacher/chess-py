import pygame as p
import chessGame


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = ["wp", "bp", "wR", "bR", "wN", "bN", "wB", "bB", "wK", "bK", "wQ", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + ".png")
        