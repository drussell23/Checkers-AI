import pygame
from typing import Tuple
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

class Piece:
    """
    Represents a checkers piece on the board.
    """
    PADDING: int = 15
    OUTLINE: int = 2

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
        self.x: int = 0
        self.y: int = 0
        self.calc_pos()

    def calc_pos(self) -> None:
        """
        Calculate the pixel position of the piece based on its board position.
        """
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self) -> None:
        """
        Promote this piece to a king.
        """
        self.king = True

    def draw(self, win: pygame.Surface) -> None:
        """
        Draw the piece on the given pygame window.
        
        :param win: The pygame Surface where the piece is drawn.
        """
        radius: int = SQUARE_SIZE // 2 - self.PADDING
        # Draw an outline for better visibility.
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        # Draw the piece in its color.
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        # If the piece is a king, draw the crown image centered on the piece.
        if self.king:
            crown_x = self.x - CROWN.get_width() // 2
            crown_y = self.y - CROWN.get_height() // 2
            win.blit(CROWN, (crown_x, crown_y))

    def move(self, row: int, col: int) -> None:
        """
        Move the piece to a new board position and update its pixel position.
        
        :param row: The new row index.
        :param col: The new column index.
        :raises ValueError: If row or col are not integers.
        """
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Row and column must be integers.")
        self.row = row
        self.col = col
        self.calc_pos()

    def get_position(self) -> Tuple[int, int]:
        """
        Return the current board position as a (row, col) tuple.
        
        :return: Tuple containing row and column.
        """
        return self.row, self.col

    def __repr__(self) -> str:
        """
        Return a string representation of the piece.
        """
        return (f"Piece(color={self.color}, row={self.row}, col={self.col}, "
                f"king={self.king})")
