from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# Define a simple route

@app.route('/')
def home():
    return 'Hello, World!'





if __name__ == '__main__':
    app.run(debug=True)


