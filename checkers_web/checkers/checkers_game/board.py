from .constants import ROWS, COLS, WHITE, RED
from .piece import Piece
from typing import List, Tuple, Dict, Optional, Any

class Board:
    def __init__(self) -> None:
        self.board: List[List[Optional[Piece]]] = []
        self.red_left: int = 12
        self.white_left: int = 12
        self.red_kings: int = 0
        self.white_kings: int = 0
        self.create_board()

    def move(self, piece: Piece, row: int, col: int) -> None:
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            if not piece.king:
                piece.make_king()
                if piece.color == WHITE:
                    self.white_kings += 1
                else:
                    self.red_kings += 1

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        return self.board[row][col]

    def evaluate(self) -> float:
        return self.white_left - self.red_left + (self.white_kings * 1.5 - self.red_kings * 1.5)

    def get_all_pieces(self, color: Tuple[int, int, int]) -> List[Piece]:
        pieces = []
        for row in self.board:
            for piece in row:
                if piece and piece.color == color:
                    pieces.append(piece)
        return pieces

    def create_board(self) -> None:
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(None)
                else:
                    self.board[row].append(None)

    def remove(self, pieces: List[Piece]) -> None:
        for piece in pieces:
            self.board[piece.row][piece.col] = None
            if piece:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self) -> Optional[Tuple[int, int, int]]:
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        return None

    def get_valid_moves(self, piece: Piece) -> Dict[Tuple[int, int], List[Piece]]:
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start: int, stop: int, step: int, color: Tuple[int, int, int], left: int, skipped: List[Piece]=[]) -> Dict[Tuple[int, int], List[Piece]]:
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current is None:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start: int, stop: int, step: int, color: Tuple[int, int, int], right: int, skipped: List[Piece]=[]) -> Dict[Tuple[int, int], List[Piece]]:
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current is None:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def to_dict(self) -> Dict[str, Any]:
        return {
            "board": [[p.to_dict() if p else None for p in row] for row in self.board],
            "red_left": self.red_left,
            "white_left": self.white_left,
            "red_kings": self.red_kings,
            "white_kings": self.white_kings
        }