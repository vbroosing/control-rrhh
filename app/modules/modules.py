from .hashlib.encrypt import hash_password

# Seguridad
def hashed_password(password):
    hashed_password = hash_password(password)
    return hashed_password

# Transformación de datos