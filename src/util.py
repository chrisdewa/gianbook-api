from passlib.context import CryptContext


pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_pwd(password: str, hashed: str) -> bool:
    return pwd_ctx.verify(password, hashed)

def hash_pwd(password: str) -> str:
    return pwd_ctx.hash(password)

