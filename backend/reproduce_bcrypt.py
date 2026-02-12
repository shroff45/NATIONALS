from passlib.context import CryptContext
import sys

try:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    password = "Start123!"
    print(f"Hashing password: '{password}' (len={len(password)})")
    
    hash = pwd_context.hash(password)
    print(f"Hash: {hash}")
    
    verify = pwd_context.verify(password, hash)
    print(f"Verify: {verify}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
