from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='192.168.33.10')

@app.route('/')
def hello_world():
    return 'Hello, World!'
