from flask import Flask, jsonify
app = Flask(__name__)
request_counter = 0


@app.route('/count-requests', methods=['GET'])
def count_requests():
    global request_counter
    request_counter += 1
    return jsonify(counter=request_counter)


@app.route('/reset-counter', methods=['POST'])
def reset_requests():
    global request_counter
    request_counter = 0
    return jsonify(counter=request_counter)


if __name__ == '__main__':
    app.run(debug=True)
