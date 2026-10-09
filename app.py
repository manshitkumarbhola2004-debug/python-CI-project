
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Server is running"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)