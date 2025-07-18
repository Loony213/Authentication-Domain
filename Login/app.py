from flask import Flask, jsonify
from flask_cors import CORS
from routes.login_routes import login_bp

app = Flask(__name__)
CORS(app)

# Registrar Blueprint de login
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
