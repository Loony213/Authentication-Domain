from flask import Blueprint, request, jsonify
import pyodbc
import jwt
import datetime

login_bp = Blueprint('login_bp', __name__)
SECRET_KEY = "supersecretkey"

def get_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=sqlserver,1433;'
                      'DATABASE=auth_db;'
                      'UID=sa;'
                      'PWD=YourStrong@Pass123')

    cursor = conn.cursor()
    return conn, cursor

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        conn, cursor = get_connection()
        cursor.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
        row = cursor.fetchone()

        if not row:
            return jsonify({'error': 'Credenciales inválidas'}), 401

        # Generar token JWT
        token = jwt.encode({
            'user_id': row[0],
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm='HS256')

        # Asegura que sea string (algunas versiones devuelvenn bytes)
        if isinstance(token, bytes):
            token = token.decode('utf-8')

        return jsonify({'token': token})

    except Exception as e:
        print(f"ERROR LOGIN: {e}")
        return jsonify({'error': str(e)}), 500
