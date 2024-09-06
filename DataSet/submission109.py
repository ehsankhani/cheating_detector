from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This function returns an HTML message with inline styles
    return '<h1 style="color:blue;">Hello, World!</h1>'

if __name__ == '__main__':
    # Run the Flask application with HTML response
    app.run(debug=True)
