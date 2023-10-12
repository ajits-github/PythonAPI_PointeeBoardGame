from flask import Flask, jsonify
from game.logic import game_round, coupon_values, highest_value_coupon

app = Flask(__name__)

@app.route('/play/<int:rounds>', methods=['GET'])
def play_game(rounds):
    for _ in range(rounds):
        game_round()
    
    if rounds in [25, 50, 100]:
        return jsonify({
            "coupon_values": coupon_values(),
            "highest_value_coupons": highest_value_coupon()
        })
    else:
        return "Valid redemption rounds are 25, 50, or 100."

@app.route('/')
def index():
    return "Welcome to the PAYBACK game API!", 200
