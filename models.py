from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet
import os
from database import Base

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
    capsules = relationship("Capsule", back_populates="user", cascade="all, delete")

class Capsule(Base):
    __tablename__ = "capsules"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    open_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="capsules")
    messages = relationship("Message", back_populates="capsule", cascade="all, delete")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    capsule_id = Column(Integer, ForeignKey("capsules.id"), nullable=False)
    encrypted_content = Column(String, nullable=False)
    capsule = relationship("Capsule", back_populates="messages")
    
    def set_content(self, content):
        """Encrypt and store the message content"""
        self.encrypted_content = cipher.encrypt(content.encode()).decode()

    def get_content(self):
        """Decrypt and retrieve the message content"""
        return cipher.decrypt(self.encrypted_content.encode()).decode()
