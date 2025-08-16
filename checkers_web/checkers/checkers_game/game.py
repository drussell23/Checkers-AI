from .constants import RED, WHITE
from .board import Board
from .piece import Piece
from typing import Tuple, Dict, List, Optional

class Game:
    def __init__(self) -> None:
        self._init()

    def _init(self) -> None:
        self.selected: Optional[Piece] = None
        self.board: Board = Board()
        self.turn: Tuple[int, int, int] = RED
        self.valid_moves: Dict[Tuple[int, int], List[Piece]] = {}

    def winner(self) -> Optional[Tuple[int, int, int]]:
        return self.board.winner()

    def reset(self) -> None:
        self._init()

    def select(self, row: int, col: int) -> bool:
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row: int, col: int) -> bool:
        piece = self.board.get_piece(row, col)
        if self.selected and not piece and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self) -> None:
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self) -> Board:
        return self.board

    def ai_move(self, board: Board) -> None:
        self.board = board
        self.change_turn()






















