# app.py
from flask import Flask, request, jsonify
from borsh import BorshSerialize, BorshDeserialize

app = Flask(__name__)

@app.route('/')
def index():
    return "Echoes of Eldoria API Server"

@app.route('/random_number', methods=['POST'])
def random_number():
    data = request.get_json()
    random_number = data.get('random_number')
    response = RandomNumber(random_number=random_number)
    return jsonify(response.__dict__)

@app.route('/game_state', methods=['POST'])
def game_state():
    data = request.get_json()
    game_state = GameState(**data)
    return jsonify(game_state.__dict__)

@app.route('/character', methods=['POST'])
def character():
    data = request.get_json()
    character = Character(**data)
    return jsonify(character.__dict__)

@app.route('/attack', methods=['POST'])
def attack():
    data = request.get_json()
    attack = Attack(**data)
    return jsonify(attack.__dict__)

@app.route('/player_account', methods=['POST'])
def player_account():
    data = request.get_json()
    player_account = PlayerAccount(**data)
    return jsonify(player_account.__dict__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)