from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Test app 2 is running!"

if __name__ == '__main__':
    print("Starting test app 2")
    app.run(debug=True, host='0.0.0.0', port=5000)