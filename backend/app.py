from flask import Flask, jsonify
from ioc_processor import process_iocs

app = Flask(__name__)

@app.route('/api/iocs', methods=['GET'])
def get_iocs():
    iocs = process_iocs()
    return jsonify(iocs)

if __name__ == '__main__':
    app.run(debug=True)
