from passlib.context import CryptContext

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto"):

class Hashing():
    @staticmethod
    def verify_password(password, hashed_password):
        return pass_context.verify(password, hashed_password)

    @staticmethod
    def hash_password(password):
        return pass_context.hash(password)
        
