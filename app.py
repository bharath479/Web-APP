#sample Flask application
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_message = request.form['message']
    return render_template('result.html', message=user_message)

if __name__ == '__main__':
    app.run(debug=True)

