import sys
import pygame as pg
import pygame.freetype as pgft

# imports all the Classes and CONSTANTS needed
from chessPieces import *
from constants import *

def set_board_surface():
    board_surface = pg.Surface(BOARD_SIZE)
    for i in range(8):
        for j in range(8):
            square = pg.rect.Rect(j*80, i*80, 80, 80)
            if (i + j) % 2 == 0:
                pg.draw.rect(board_surface, LIGHT_GRAY, square)
            elif (i + j) % 2 == 1:
                pg.draw.rect(board_surface, LIGHT_BLUE, square)
    return board_surface

# create the board indexes and populates it with the standard strating arrangement
def create_starting_board():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(None)

    board[0] = [Rook("dark"), Knight("dark"), Bishop("dark"), Queen("dark"), King("dark"), Bishop("dark"), Knight("dark"), Rook("dark")]
    board[7] = [Rook("light"), Knight("light"), Bishop("light"), Queen("light"), King("light"), Bishop("light"), Knight("light"), Rook("light")]
    
    for i in range(8):
        board[1][i] = Pawn("dark")
    for i in range(8):
        board[6][i] = Pawn("light")

    return board

def get_square_coords(board):
    mouse_pos = pg.Vector2(pg.mouse.get_pos()) - BOARD_COORDS
    x, y = int(mouse_pos[0] // 80), int(mouse_pos[1] // 80)
    try:
        if x >= 0 and y >= 0:
            return board[x][y], x, y
    except IndexError:
        return None, None, None

def pawn_promotion(pawn_pos, piece_type = "Queen"):    # Queen is default because it is the most common promotion target
    pawn_pos.kill()
    if piece_type == "Queen":
        pawn_pos = Queen(pawn_pos.colour)
    elif piece_type == "Knight":
        pawn_pos = Knight(pawn_pos.colour)
    elif piece_type == "Rook":
        pawn_pos = Rook(pawn_pos.colour)
    elif piece_type == "Bishop":
        pawn_pos = Bishop(pawn_pos.colour)

    return pawn_pos
    

def main():
    # Initializes the window and layout
    pg.init()
    screen = pg.display.set_mode(WINDOW_SIZE)
    pg.display.set_caption("Chess")
    screen.fill(DARK_GRAY)

    # draws the chessboard surface
    board_surface = set_board_surface()
    screen.blit(board_surface, BOARD_COORDS)
    board = create_starting_board()
    for i in range(8):
        for j in range(8):
            if board[i][j] != None:
                screen.blit(board[i][j].image, (j*80+30, i*80+40))


    # draws the textbox for logging moves
    logs = pg.Surface((300, WINDOW_HEIGHT))
    logs.fill(GRAY)
    screen.blit(logs, (700, 0))

    # sets the font to be used for writing to logs
    myFont = pgft.SysFont("Arial", 20)

    clock = pg.time.Clock()

    # variable to store a selected piece for dragging
    selected_piece = None
    # determines which player's turn it is
    turn = 0
    move_count = 1 + (turn // 2)

    # Main loop of the game
    while True:
        piece, x, y = get_square_coords(board)

        # specifies which player's turn it is
        if turn % 2 == 0:
            player = "white"
        elif turn % 2 == 1:
            player = "black"
        
        
        # blocks the other player's pieces from being moved on a player's turn
        # if player == "white":
        #     if piece.colour == "dark":
        #         selected_piece != piece

        # check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if piece != None:
                    selected_piece = piece, x, y
            

        # increments the turn counter, stating that it is now the other player's turn
        turn += 1
        
        # updates the screen
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()