from copy import deepcopy
import pygame
from checkers_game.board import Board
from checkers_game.piece import Piece
from checkers_game.game import Game
from typing import List, Tuple, Optional

RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position: Board, depth: int, max_player: bool, game: Game) -> Tuple[float, Optional[Board]]:
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            if maxEval < evaluation:
                best_move = move

            maxEval = max(maxEval, evaluation)
            
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            if minEval > evaluation:
                best_move = move

            minEval = min(minEval, evaluation)
            
        

        return minEval, best_move

    
def alphabeta(position: Board, depth: int, alpha: float, beta: float, max_player: bool, game: Game) -> Tuple[float, Optional[Board]]:
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = alphabeta(move, depth-1, alpha, beta, False, game)[0]

            if evaluation > maxEval:
                best_move = move

            maxEval = max(maxEval, evaluation)

            alpha = max(alpha, evaluation)

            if beta <= alpha:
                break
            

        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = alphabeta(move, depth-1, alpha, beta, True, game)[0]

            if evaluation < minEval:
                best_move = move

            minEval = min(minEval, evaluation)

            beta = min(beta, evaluation)
            if beta <= alpha:
                break
     
        return minEval, best_move


def simulate_move(piece: Piece, move: Tuple[int, int], board: Board, game: Game, skip: List[Piece]) -> Board:
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board: Board, color: Tuple[int, int, int], game: Game) -> List[Board]:
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game: Game, board: Board, piece: Piece) -> None:
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())

    pygame.display.update()
