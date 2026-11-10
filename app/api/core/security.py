from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


_hasher=PasswordHasher()
def hash_password(password:str)->str:
    return _hasher.hash(password)

def verify_password(db_hash_password:str,user_password:str):
    try:
        return _hasher.verify(db_hash_password,user_password)
    except VerifyMismatchError:
        return False