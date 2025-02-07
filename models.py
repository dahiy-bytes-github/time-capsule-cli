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

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    capsules = relationship("Capsule", back_populates="user")

class Capsule(Base):
    __tablename__ = "capsules"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    open_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="capsules")
    messages = relationship("Message", back_populates="capsule")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    capsule_id = Column(Integer, ForeignKey("capsules.id"))
    encrypted_content = Column(String, nullable=False)
    capsule = relationship("Capsule", back_populates="messages")