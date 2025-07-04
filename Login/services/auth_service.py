import jwt
import datetime
from flask import jsonify
from models.user_model import UserModel

SECRET_KEY = "supersecretkey"

class AuthService:
    @staticmethod
    def login_user(email, password):
        # Encontrar al usuario en la base de datos usando email y password
        user = UserModel.find_user(email, password)
        if not user:
            return jsonify({'error': 'Credenciales inválidas'}), 401

        # Aquí se asume que 'user' es una tupla donde el primer elemento es el user_id
        # y el segundo es el nombre de usuario (o cualquier campo identificativo)
        user_id = user[0]  # Suponiendo que el id de usuario es el primer valor
        user_name = user[1]  # Suponiendo que el nombre de usuario está en la segunda posición

        # Crear el token JWT, ahora con el nombre de usuario (o cualquier otro dato)
        token = jwt.encode({
            'user_id': user_id,
            'user_name': user_name,  # Añadir el nombre de usuario al token
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm='HS256')

        # Si el token es de tipo bytes, convertirlo a string
        if isinstance(token, bytes):
            token = token.decode('utf-8')

        return jsonify({'token': token, 'userName': user_name})  # Incluye 'userName' en la respuesta

    @staticmethod
    def register_user(email, password):
        existing = UserModel.find_user(email)
        if existing:
            return jsonify({'error': 'El correo ya está registrado'}), 409

        UserModel.create_user(email, password)
        return jsonify({'message': 'Usuario registrado correctamente'}), 201
