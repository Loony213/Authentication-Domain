from flask import Flask
from flask_cors import CORS
from Login.login import login_bp
from Register.register import register_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_bp, url_prefix='/api/auth')
app.register_blueprint(register_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
