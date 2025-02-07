from sqlalchemy.orm import sessionmaker
from datetime import datetime
from setup_db import engine, User, Capsule, Message

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add users
users = [
    User(name="Kwame Mensah"),
    User(name="Zainab Bello"),
    User(name="Thabo Mokoena"),
    User(name="Amina Yusuf"),
    User(name="Obafemi Adewale"),
    User(name="Fatoumata Keita"),
    User(name="Moses Chukwuma"),
    User(name="Tariq Abubakar"),
    User(name="Nia Okonkwo"),
    User(name="Dayo Eze"),
    User(name="Chinwe Mbatha"),
    User(name="Bakari Juma"),
    User(name="Adjoa Owusu"),
]

session.add_all(users)
session.commit()

# Fetch user IDs dynamically
user_ids = {user.name: user.id for user in session.query(User).all()}

# Add capsules
capsules = [
    Capsule(name="Memories of Youth", open_date=datetime.strptime("2030-05-01", "%Y-%m-%d").date(), user_id=user_ids["Kwame Mensah"]),
    Capsule(name="Letters to My Future Self", open_date=datetime.strptime("2028-09-12", "%Y-%m-%d").date(), user_id=user_ids["Zainab Bello"]),
    Capsule(name="Family Archive", open_date=datetime.strptime("2040-01-20", "%Y-%m-%d").date(), user_id=user_ids["Thabo Mokoena"]),
    Capsule(name="My Travel Diaries", open_date=datetime.strptime("2032-06-15", "%Y-%m-%d").date(), user_id=user_ids["Amina Yusuf"]),
    Capsule(name="Business Goals", open_date=datetime.strptime("2035-11-30", "%Y-%m-%d").date(), user_id=user_ids["Obafemi Adewale"]),
]

session.add_all(capsules)
session.commit()

print("✅ Database populated successfully!")

# Close session
session.close()
