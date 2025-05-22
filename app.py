from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Please provide two numbers (num1 and num2)"}), 400
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        return jsonify({
            "result": result,
            "num1": num1,
            "num2": num2
        })
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400

if __name__ == '__main__':
    app.run(debug=True)