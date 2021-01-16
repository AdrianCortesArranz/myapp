from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World! por fin funciona esta mierda'

@app.route('/bye')
def bye__world():
    return 'bye, World! me voy de la fucking live '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
