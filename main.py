from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_my_ip', methods=['GET'])
def get_my_ip():
    requester_ip = request.remote_addr
    return jsonify({'Your IP is': requester_ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)