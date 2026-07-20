from database.database import create_connection
from tools.security import hash_password, verify_password
from tools.validator import validate_username, validate_password


class AuthService:

    @staticmethod
    def register(username, password, role):

        if not validate_username(username):
            print("Username must be at least 4 characters.")
            return False

        if not validate_password(password):
            print("Password must be at least 6 characters.")
            return False

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE username = ?",
            (username,)
        )

        if cursor.fetchone():
            print("Username already exists.")
            connection.close()
            return False

        hashed = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users(username, password, role)
            VALUES (?, ?, ?)
            """,
            (username, hashed, role)
        )

        connection.commit()
        connection.close()

        print("Registration successful.")
        return True

    @staticmethod
    def login(username, password):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()
        connection.close()

        if not user:
            print("User not found.")
            return None

        if verify_password(password, user["password"]):
            print("Login successful.")
            return user

        print("Incorrect password.")
        return None
