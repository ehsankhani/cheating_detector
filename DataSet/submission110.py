from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This function returns the "Hello, World!" message
    return 'Hello, World!'

@app.route('/about')
def about():
    # This function returns an "About" message on a different route
    return 'This is the About page.'

if __name__ == '__main__':
    # Run the Flask application with an additional route
    app.run(debug=True)
