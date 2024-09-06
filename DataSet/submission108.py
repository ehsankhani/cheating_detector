from flask import Flask

app = Flask(__name__)

@app.route('/home')
def greet():
    # This function returns the "Hello, World!" message, but at a different route
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask application with a different route
    app.run(debug=True)
