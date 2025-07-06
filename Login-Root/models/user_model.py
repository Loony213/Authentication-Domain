from utils.db import get_connection

class UserModel:
    @staticmethod
    def find_user(email, password=None):
        conn, cursor = get_connection()
        if password:
            cursor.execute("SELECT id FROM root WHERE email=? AND password=?", (email, password))
        else:
            cursor.execute("SELECT id FROM root WHERE email=?", (email,))
        return cursor.fetchone()

    @staticmethod
    def create_user(email, password):
        conn, cursor = get_connection()
        cursor.execute("INSERT INTO root (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
