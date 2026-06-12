from flask import Flask, render_template, request, redirect
import sqlite3
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Create database
def init_db():
    conn = sqlite3.connect("crop.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS crops(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL,
        temperature REAL,
        humidity REAL,
        ph REAL,
        rainfall REAL,
        crop_name TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Page
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        features = [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]]

        prediction = model.predict(features)

        crop_name = label_encoder.inverse_transform(prediction)[0]

        conn = sqlite3.connect("crop.db")

        conn.execute("""
        INSERT INTO crops(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall,
            crop_name
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall,
            crop_name
        ))

        conn.commit()
        conn.close()

        return redirect('/records')

    return render_template('predict.html')

# Records Page
@app.route('/records')
def records():

    conn = sqlite3.connect("crop.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops")

    crops = cursor.fetchall()

    conn.close()

    return render_template('records.html', crops=crops)

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Run App
if __name__ == '__main__':
    app.run(debug=True)