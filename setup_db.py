from database import Base, engine

Base.metadata.drop_all(engine)  # Resets the database
Base.metadata.create_all(engine)

print("Database schema initialized successfully.")
