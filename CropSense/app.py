from flask import Flask, render_template, request, redirect, url_for, session, send_file

import hashlib
import sqlite3
import joblib
import numpy as np
import pandas as pd
import os
import csv

from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = 'cropsense2026'
app.config['PERMANENT_SESSION_LIFETIME'] = 86400
# Load trained model
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Load trained model
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# ================= DATABASE PATH =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "crop.db")

print("Database Path:", DB_PATH)

# =================================================

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


# ================= PDF DOWNLOAD =================

@app.route('/download/pdf/<int:id>')
def download_pdf(id):

    conn = get_db()
    record = conn.execute(
        "SELECT * FROM predictions WHERE id=?",
        (id,)
    ).fetchone()
    conn.close()


    if not record:
        return redirect(url_for('records'))

    pdf_file = os.path.join(
    app.root_path,
    f"prediction_{id}.pdf"
)

    c = canvas.Canvas(pdf_file)

    c.drawString(100, 800, "CropSense Prediction Report")
    c.drawString(100, 770, f"Crop: {record['crop_name']}")
    c.drawString(100, 740, f"Confidence: {record['confidence']}%")
    c.drawString(100, 710, f"Nitrogen: {record['nitrogen']}")
    c.drawString(100, 680, f"Phosphorus: {record['phosphorus']}")
    c.drawString(100, 650, f"Potassium: {record['potassium']}")
    c.drawString(100, 620, f"Temperature: {record['temperature']}")
    c.drawString(100, 590, f"Humidity: {record['humidity']}")
    c.drawString(100, 560, f"pH: {record['ph']}")
    c.drawString(100, 530, f"Rainfall: {record['rainfall']}")

    c.save()
    print("PDF File:", pdf_file)
    print("Exists:", os.path.exists(pdf_file))

    return send_file(pdf_file, as_attachment=True)

@app.route('/download/csv/<int:id>')
def download_csv(id):

    conn = get_db()

    record = conn.execute(
        "SELECT * FROM predictions WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if not record:
        return redirect(url_for('records'))

    csv_file = os.path.join(
    app.root_path,
    f"prediction_{id}.csv"
)

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Crop",
            "Confidence",
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall"
        ])

        writer.writerow([
            record['crop_name'],
            record['confidence'],
            record['nitrogen'],
            record['phosphorus'],
            record['potassium'],
            record['temperature'],
            record['humidity'],
            record['ph'],
            record['rainfall']
        ])
    # Check whether the CSV file was created
    print("CSV File:", csv_file)
    print("Exists:", os.path.exists(csv_file))

    return send_file(csv_file, as_attachment=True)

    

@app.route('/download/png/<int:id>')
def download_png(id):

    conn = get_db()

    record = conn.execute(
        "SELECT * FROM predictions WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    if not record:
        return redirect(url_for('records'))

    image_path = os.path.join(
        "static",
        "images",
        f"{record['crop_name']}.jpg"
    )

    return send_file(
        image_path,
        as_attachment=True
    )

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
@app.route('/download_all_csv')
def download_all_csv():

    conn = get_db()

    records = conn.execute(
        "SELECT * FROM predictions"
    ).fetchall()

    conn.close()

    csv_file = os.path.join(
    app.root_path,
    "all_predictions.csv"
)

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Crop",
            "Confidence",
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall",
            "Date"
        ])

        for row in records:

            writer.writerow([
                row['id'],
                row['crop_name'],
                row['confidence'],
                row['nitrogen'],
                row['phosphorus'],
                row['potassium'],
                row['temperature'],
                row['humidity'],
                row['ph'],
                row['rainfall'],
                row['created_at']
            ])

    return send_file(
        csv_file,
        as_attachment=True
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )