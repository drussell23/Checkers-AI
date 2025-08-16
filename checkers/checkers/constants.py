import os
import pygame
from typing import Tuple, Optional

# Initialize pygame
pygame.init()

# Constants for screen dimensions and board configuration
WIDTH: int = 800
HEIGHT: int = 800
ROWS: int = 8
COLS: int = 8
SQUARE_SIZE: int = WIDTH // COLS

# RGB color definitions
RED: Tuple[int, int, int]   = (255, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
BLACK: Tuple[int, int, int] = (0, 0, 0)
BLUE: Tuple[int, int, int]  = (0, 0, 255)
GREY: Tuple[int, int, int]  = (128, 128, 128)

def load_image(
    filename: str, 
    scale_size: Optional[Tuple[int, int]] = None, 
    colorkey: Optional[Tuple[int, int, int]] = None
) -> pygame.Surface:
    """
    Load an image from the 'assets' folder, optionally scale it, and apply a colorkey.
    If a display surface is available, convert the image for optimal blitting.
    
    :param filename: Name of the image file.
    :param scale_size: Tuple (width, height) to scale the image.
    :param colorkey: RGB color to treat as transparent.
    :return: The loaded pygame.Surface.
    """
    filepath = os.path.join(os.path.dirname(__file__), '..', 'assets', filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Asset not found: {filepath}")
    
    try:
        image = pygame.image.load(filepath)
    except pygame.error as e:
        raise SystemExit(f"Cannot load image: {filepath}\n{e}")
    
    # Only convert if a display mode has been set.
    if pygame.display.get_surface():
        image = image.convert_alpha() if image.get_alpha() else image.convert()
    
    if colorkey is not None:
        image.set_colorkey(colorkey)
    if scale_size:
        image = pygame.transform.scale(image, scale_size)
    
    return image

# Load crown image robustly
CROWN: pygame.Surface = load_image('crown.png', scale_size=(44, 25))
