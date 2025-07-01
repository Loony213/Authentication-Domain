from flask import Flask
from flask_cors import CORS
from routes.login_routes import login_bp
from routes.register_routes import register_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
