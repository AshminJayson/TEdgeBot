from flask import Flask

app = flask(__name__)

@app.route('/')
def index():
    return "plain text"

if __name__ == '__main__':
    app.run()