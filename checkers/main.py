import pygame
import sys
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
from minimax.algorithm import alphabeta

FPS = 60
ALPHA = float('-inf')
BETA = float('inf')
DEPTH = 2

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# uncomment 36, comment 37 = minmax
# comment 36, uncomment 37 = Alpha Beta
# Line 93 in algorithm.py commented = no ai thinking shown
#

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():

    args = sys.argv[1:]

    if not args or len(args) != 2 or not args[0].isnumeric() or not args[1].isnumeric():
        print("usage: [main.py] [depth] [1 for AB 0 for MM]")
        sys.exit(1)

    if int(args[1]) == 1:
        AB = True
    else:
        AB = False

    DEPTH = int(args[0])

    print(f'Initializing AI with depth {DEPTH}. Using AlphaBeta: {AB}')

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:

            if not AB:
                value, new_board = minimax(game.get_board(), DEPTH, WHITE, game)
            else:
                value, new_board = alphabeta(game.get_board(), DEPTH, ALPHA, BETA, WHITE, game)
            # print(value, new_board)

            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

if __name__ == '__main__':
    main()
