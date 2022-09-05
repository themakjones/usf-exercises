from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, json
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()
game_board = boggle_game.make_board()

@app.route('/')
def start_page():
    session['game-board'] = game_board
    return render_template('game.html', board=session['game-board'])

@app.route('/guess')
def eval_guess():
    guess = request.args['word']
    res = boggle_game.check_valid_word(game_board, guess)
    return json.jsonify(f'{"result" : res }')
    

