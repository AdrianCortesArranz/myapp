from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye__world():
    return 'bye, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
