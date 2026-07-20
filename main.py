from database.database import initialize_database
from authentication.auth import AuthService


def option():

    while True:
        print("\n           QUIZ MANAGEMENT ")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            print("\nRoles")
            print("1. Admin")
            print("2. Student")
            role_choice = input("Choose role: ")
            role = "admin" if role_choice == "1" else "student"
            AuthService.register(username, password, role)
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = AuthService.login(username, password)
            if user:
                print(f"\nWelcome {user['username']}!")
                if user["role"] == "admin":
                    print("Opening Admin Dashboard...")
                else:
                    print("Opening Student Dashboard...")
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

def main():
    initialize_database()
    option()

if __name__ == "__main__":
    main()
