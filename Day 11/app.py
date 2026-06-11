from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/records')
@app.route('/records')
def records():

    crops = [
        {"id":101,"crop":"Rice","n":90,"p":42,"k":43,"yield":"4.8 Ton"},
        {"id":102,"crop":"Maize","n":70,"p":50,"k":35,"yield":"3.6 Ton"},
        {"id":103,"crop":"Cotton","n":120,"p":60,"k":40,"yield":"2.4 Ton"},
        {"id":104,"crop":"Wheat","n":80,"p":40,"k":45,"yield":"4.5 Ton"},
        {"id":105,"crop":"Banana","n":100,"p":55,"k":50,"yield":"6.5 Ton"},
        {"id":106,"crop":"Mango","n":60,"p":30,"k":35,"yield":"4.2 Ton"},
        {"id":107,"crop":"Coffee","n":90,"p":45,"k":40,"yield":"1.8 Ton"},
        {"id":108,"crop":"Coconut","n":110,"p":65,"k":55,"yield":"5.1 Ton"},
        {"id":109,"crop":"Orange","n":70,"p":35,"k":30,"yield":"2.7 Ton"},
        {"id":110,"crop":"Watermelon","n":50,"p":25,"k":20,"yield":"3.3 Ton"}
    ]

    return render_template('records.html', crops=crops)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)