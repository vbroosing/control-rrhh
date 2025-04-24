import hashlib

def hash_password(password):
    """Genera el hash MD5 de una contraseña."""
    return hashlib.md5(password.encode()).hexdigest()
    
