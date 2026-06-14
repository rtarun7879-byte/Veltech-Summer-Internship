from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import sqlite3
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'cropsense2026'
app.config['PERMANENT_SESSION_LIFETIME'] = 86400
# Load trained model
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

DB_PATH = "crop.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL,
        temperature REAL,
        humidity REAL,
        ph REAL,
        rainfall REAL,
        crop_name TEXT,
        confidence REAL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

CROP_EMOJIS = {
    'rice': '🌾', 'maize': '🌽', 'chickpea': '🫘', 'kidneybeans': '🫘',
    'pigeonpeas': '🌿', 'mothbeans': '🌿', 'mungbean': '🌿', 'blackgram': '🌿',
    'lentil': '🫘', 'pomegranate': '🍎', 'banana': '🍌', 'mango': '🥭',
    'grapes': '🍇', 'watermelon': '🍉', 'muskmelon': '🍈', 'apple': '🍎',
    'orange': '🍊', 'papaya': '🍈', 'coconut': '🥥', 'cotton': '🌸',
    'jute': '🌿', 'coffee': '☕'
}

# ── Auth Routes ──────────────────────────────────────────

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm  = request.form['confirm']
        if password != confirm:
            return render_template('signup.html', error="Passwords do not match.")
        hashed = hashlib.sha256(password.encode()).hexdigest()
        try:
            conn = get_db()
            conn.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hashed))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except:
            return render_template('signup.html', error="Username already exists.")
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed   = hashlib.sha256(password.encode()).hexdigest()
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, hashed)
        ).fetchone()
        conn.close()
        if user:
            session.permanent = True
            session['user'] = username
            return redirect(url_for('home'))
        return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# ── Main Routes ──────────────────────────────────────────

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) as c FROM predictions").fetchone()['c']
    latest = conn.execute("SELECT crop_name, confidence, created_at FROM predictions ORDER BY id DESC LIMIT 3").fetchall()
    conn.close()
    return render_template('index.html', total=total, latest=latest, emojis=CROP_EMOJIS)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            nitrogen    = float(request.form['nitrogen'])
            phosphorus  = float(request.form['phosphorus'])
            potassium   = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity    = float(request.form['humidity'])
            ph          = float(request.form['ph'])
            rainfall    = float(request.form['rainfall'])
        except (ValueError, KeyError):
            return render_template('predict.html', error="Please fill all fields with valid numbers.")

        features = pd.DataFrame(
            [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]],
            columns=['N','P','K','temperature','humidity','ph','rainfall']
        )
        prediction    = model.predict(features)
        probabilities = model.predict_proba(features)[0]
        confidence    = round(float(probabilities[prediction[0]]) * 100, 2)
        crop_name     = label_encoder.inverse_transform(prediction)[0]

        conn = get_db()
        cursor = conn.execute("""
        INSERT INTO predictions (nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall,crop_name,confidence)
        VALUES (?,?,?,?,?,?,?,?,?)
        """, (nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall, crop_name, confidence))
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return redirect(url_for('result', id=record_id))

    return render_template('predict.html')

@app.route('/result/<int:id>')
def result(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    record = conn.execute("SELECT * FROM predictions WHERE id=?", (id,)).fetchone()
    conn.close()
    if not record:
        return redirect(url_for('predict'))
    emoji = CROP_EMOJIS.get(record['crop_name'], '🌱')
    return render_template('result.html', record=record, emoji=emoji)

@app.route('/records')
def records():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    crops = conn.execute("SELECT * FROM predictions ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('records.html', crops=crops, emojis=CROP_EMOJIS)

@app.route('/records/delete/<int:id>', methods=['POST'])
def delete_record(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    conn.execute("DELETE FROM predictions WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('records'))

@app.route('/records/clear', methods=['POST'])
def clear_records():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    conn.execute("DELETE FROM predictions")
    conn.execute("DELETE FROM sqlite_sequence WHERE name='predictions'")
    conn.commit()
    conn.close()
    return redirect(url_for('records'))

@app.route('/about')
def about():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)