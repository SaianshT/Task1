from flask import Flask, jsonify, send_file
import random
import os

app = Flask(__name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = 'dishes'

@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        # Your code here: 
        # 1. Get a list of all image files in the DISHES_DIR
        # 2. Choose a random image from the list
        # 3. Return the image file
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
