def login(name, password):
    return _login(name, password)

def _login(name, password):
    if name == "admin" and password == "admin":
        return "Hello, admin!"
    else:
        return "Hello, guest!"

__all__ = ["login"]