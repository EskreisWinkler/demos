from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('square.html')

@app.route('/square', methods=['POST'])
def square_number():
    try:
        number = int(request.form['number'])
        result = number * number
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Please enter a valid integer'}), 400

if __name__ == '__main__':
    app.run(debug=True) 