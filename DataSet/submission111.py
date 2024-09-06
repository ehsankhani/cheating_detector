from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_json():
    # This function returns a JSON response
    response = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask application with JSON response
    app.run(debug=True)
