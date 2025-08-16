document.addEventListener('DOMContentLoaded', () => {
    const boardElement = document.getElementById('board');

    function drawBoard() {
        for (let row = 0; row < 8; row++) {
            for (let col = 0; col < 8; col++) {
                const square = document.createElement('div');
                square.classList.add('square');
                if ((row + col) % 2 === 0) {
                    square.classList.add('black-square');
                } else {
                    square.classList.add('red-square');
                }
                boardElement.appendChild(square);
            }
        }
    }

    drawBoard();
});