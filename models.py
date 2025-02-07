from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet
import os
from database import Base, session

# Generate encryption key 
KEY_FILE = "secret.key"
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_FILE, "rb") as f:
    ENCRYPTION_KEY = f.read()

cipher = Fernet(ENCRYPTION_KEY)
