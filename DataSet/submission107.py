from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This function returns the "Hello, World!" message
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
