from flask import Blueprint, request, jsonify
import pyodbc

register_bp = Blueprint('register_bp', __name__)

def get_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=sqlserver,1433;'
                      'DATABASE=auth_db;'
                      'UID=sa;'
                      'PWD=YourStrong@Pass123')

    cursor = conn.cursor()
    return conn, cursor

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        conn, cursor = get_connection()

        # Verifica si el email ya está registrado
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return jsonify({'error': 'El correo ya está registrado'}), 409

        # Inserta nuevo usuario
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()

        return jsonify({'message': 'Usuario registrado correctamente'}), 201

    except Exception as e:
        print(f"ERROR REGISTER: {e}")
        return jsonify({'error': str(e)}), 500
