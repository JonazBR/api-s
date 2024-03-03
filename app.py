from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/sherlock', methods=['GET'])
def check_username():
    username = request.args.get('username')
    result = subprocess.run(['python', 'sherlock.py', '--print-found', username], capture_output=True, text=True)
    return jsonify({'output': result.stdout, 'error': result.stderr})

if __name__ == '__main__':
    app.run(debug=True)
