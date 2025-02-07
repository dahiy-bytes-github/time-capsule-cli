from database import engine, Base
from models import User, Capsule, Message  # Import models

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ Database schema initialized successfully.")
