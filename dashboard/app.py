# dashboard/app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/live_data')
def live_data():
    data = {
        "temperature": round(random.uniform(20, 100), 2),
        "vibration": round(random.uniform(0, 5), 2),
        "pressure": round(random.uniform(100, 200), 2)
    }
    return jsonify(data)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
