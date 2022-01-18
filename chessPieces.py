import pygame as pg
import chess
"""
File containing the classes of the chess pieces. 
Sprite images taken from https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces, courtesy of Colin M. L. Burnett, under the CC BY-SA 3.0 license (https://creativecommons.org/licenses/by-sa/3.0/deed.en)
"""


class Piece(pg.sprite.Sprite):
    "This is a base class for a chess piece"

    def __init__(self, colour = "light"):
        self.moves = 0
        self.set_colour(colour)
        self.symbol = chess.piece_symbol(1)
        self.image = pg.transform.scale(pg.image.load('images/Chess_' + str(self.symbol) + str(self.colour[0]) + 't45.png'), (80, 80))
        self.rect = self.image.get_rect()

    def set_colour(self, colour):
        if colour == "light":
            self.colour = "light"
        else:
            self.colour = "dark"


class Pawn(Piece):
    "This is the class for a pawn"

    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = chess.piece_symbol(1)
        self.image = pg.transform.scale(pg.image.load('images/Chess_p' + str(self.colour[0]) + 't45.png'), (80, 80))
        

class Knight(Piece):
    "This is the class for a knight"

    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = chess.piece_symbol(2)
        self.image = pg.transform.scale(pg.image.load('images/Chess_n' + str(self.colour[0]) + 't45.png'), (80, 80))
    

class Bishop(Piece):
    "This is the class for a bishop"

    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = chess.piece_symbol(3)
        self.image = pg.transform.scale(pg.image.load('images/Chess_b' + str(self.colour[0]) + 't45.png'), (80, 80))

    

class Rook(Piece):
    "This is the class for a rook"

    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = chess.piece_symbol(4)
        self.image = pg.transform.scale(pg.image.load('images/Chess_r' + str(self.colour[0]) + 't45.png'), (80, 80))

    

class Queen(Piece):
    "This is the class for a queen"

    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = chess.piece_symbol(5)
        self.image = pg.transform.scale(pg.image.load('images/Chess_q' + str(self.colour[0]) + 't45.png'), (80, 80))

    

class King(Piece):
    "This is the class for a king"

    def __init__(self, colour):
        super().__init__(colour)
        self.symbol = chess.piece_symbol(6)
        self.image = pg.transform.scale(pg.image.load('images/Chess_k' + str(self.colour[0]) + 't45.png'), (80, 80))

    