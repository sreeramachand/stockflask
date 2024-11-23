from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about/<name>')
def about(name):
    return f'You are a wonderful person, {name}! <3'

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    