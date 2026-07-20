def validate_username(username: str) -> bool:
    """
    It CHecks for the user name weather it is at least 4 charaacters or not.
    """
    return len(username.strip()) >= 4

def validate_password(password: str) -> bool:
    """
    It Checks the password length.
    """
    return len(password) >= 8
