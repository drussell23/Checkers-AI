# Checkers AI

This repository contains a Python implementation of a checkers game featuring an AI opponent. The AI uses a minimax algorithm with an option for alpha-beta pruning to choose its moves, all built using [Pygame](https://www.pygame.org/).

## Requirements

- **Python:** Version 3.6 or later (the project has been tested with Python 3.10.8).
- **Pygame:** Version 2.5.2 (or later).  
  Install with:  
  ```
  pip install pygame
  ```

## Installation

1. **Clone the Repository**  
   Open your terminal and run:
   ```
   git clone https://github.com/drussell23/Checkers-AI.git
   ```
2. **Navigate to the Checkers Directory**  
   Change into the directory that contains the game code:
   ```
   cd Checkers-AI/checkers
   ```
3. **Install Dependencies**  
   If you have a `requirements.txt` file, install the dependencies with:
   ```
   pip install -r requirements.txt
   ```
   Otherwise, manually ensure that Pygame is installed.

## Running the Program

The main game script requires two command-line arguments:

1. **Depth:** The depth level for the AI’s search (how many moves ahead it will consider).
2. **Algorithm Flag:**  
   - Enter `1` to use the alpha-beta pruning version of the algorithm.
   - Enter `0` to use the basic minimax algorithm.

**Usage:**
```
python main.py [depth] [1 for AB, 0 for MM]
```

### Examples

- **Run with a search depth of 3 using Alpha-Beta Pruning:**
  ```
  python main.py 3 1
  ```
- **Run with a search depth of 3 using the basic Minimax algorithm:**
  ```
  python main.py 3 0
  ```

*(Refer to the source code in [main.py](https://github.com/drussell23/Checkers-AI/blob/main/checkers/main.py) cite63 for more details on how the arguments are parsed and used.)*

## Gameplay

Once you run the program:
- A game window will appear.
- Use your mouse to select and move pieces.
- The AI will automatically make moves on its turn based on your chosen algorithm and search depth.

## Code Structure

- **main.py:**  
  Contains the main loop and command-line argument handling.  
  *(See cite63 for details.)*
- **game.py:**  
  Manages the game logic and board updates.
- **constants.py:**  
  Defines game constants such as board dimensions, colors, and square sizes.
- **minimax/algorithm.py:**  
  Contains the implementations of the minimax and alpha-beta pruning algorithms.

## Customization

Feel free to explore and modify the code to adjust game mechanics, improve the AI, or enhance the user interface.

## License

[Include your license information here, e.g., MIT License]

## Acknowledgments

- Built using [Pygame](https://www.pygame.org/).
- Special thanks to all contributors for their efforts and feedback.

---

This README should give users all the necessary information to install, run, and understand the Checkers AI program.