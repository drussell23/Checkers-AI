from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from checkers.checkers_game.game import Game
from checkers.checkers_game.constants import RED, WHITE
from checkers.minimax.algorithm import minimax

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('game.html')

@app.route('/api/new_game', methods=['POST'])
def new_game():
    global game
    game = Game()
    return jsonify(game.board.to_dict())

@app.route('/api/get_board', methods=['GET'])
def get_board():
    return jsonify(game.board.to_dict())

@app.route('/api/move', methods=['POST'])
def move():
    data = request.get_json()
    row = data['row']
    col = data['col']

    if game.turn == RED:
        game.select(row, col)

    if game.turn == WHITE:
        _, new_board = minimax(game.get_board(), 3, WHITE, game)
        game.ai_move(new_board)

    return jsonify(game.board.to_dict())

@socketio.on('connect')
def handle_connect():
    emit('board_update', game.board.to_dict())

if __name__ == '__main__':
    socketio.run(app, debug=True)