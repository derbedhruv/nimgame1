#!/usr/bin/env python
# modified from https://github.com/miguelgrinberg/Flask-SocketIO/
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from nim import NimGame, minimaxPolicy

# --------------------------------------------------------- #
# new nimgame instance
# --------------------------------------------------------- #
NIMGAME_SIZE = 25
game = NimGame(NIMGAME_SIZE)

# cache values globally to speed up the minimax recursion
# dynamic programming ftw
cache = {}

# start at the startState
global state 
state = game.startState()
# --------------------------------------------------------- #

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)

# read secret key from external file
app.config['SECRET_KEY'] = open('secret').read().strip()
socketio = SocketIO(app, async_mode=async_mode)
thread = None

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('player_move', namespace='/test')
def receive_player_move(message):
    global state
    session['receive_count'] = session.get('receive_count', 0) + 1
    action = int(message['data'])
    print "player moved by", action
    state -= action
    if state == 0:
        print "You won!"

    # computer plays
    val, act = minimaxPolicy(game, state, 1)
    state -= act
    print "computer moves state to", state
    if state == 0:
        print "You Lost!"

    emit('server_response',
         {'data': str(state), 'count': session['receive_count']})

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('server_response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread, state
    emit('server_response', {'data': 'Connected', 'count': 0})

    ''' HERE IS WHERE YOU START THE GAME AND CREATE A NEW INSTANCE '''
    state = game.startState()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    # may the odds be ever in your favour
    socketio.run(app, debug=True)
