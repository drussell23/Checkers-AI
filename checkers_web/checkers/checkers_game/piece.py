from typing import Tuple, Dict, Any

class Piece:
    """
    Represents a checkers piece on the board.
    """

    def __init__(self, row: int, col: int, color: Tuple[int, int, int]) -> None:
        """
        Initialize a Piece.
        
        :param row: The row index on the board.
        :param col: The column index on the board.
        :param color: The RGB color of the piece.
        """
        self.row: int = row
        self.col: int = col
        self.color: Tuple[int, int, int] = color
        self.king: bool = False

    def make_king(self) -> None:
        """
        Promote this piece to a king.
        """
        self.king = True

    def move(self, row: int, col: int) -> None:
        """
        Move the piece to a new board position.
        
        :param row: The new row index.
        :param col: The new column index.
        """
        self.row = row
        self.col = col

    def to_dict(self) -> Dict[str, Any]:
        """
        Return a dictionary representation of the piece.
        """
        return {
            'row': self.row,
            'col': self.col,
            'color': self.color,
            'king': self.king
        }

    def __repr__(self) -> str:
        """
        Return a string representation of the piece.
        """
        return (f"Piece(color={self.color}, row={self.row}, col={self.col}, "
                f"king={self.king})")
