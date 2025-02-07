from database import session
from models import User, Capsule, Message

# Adding some users
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

# Adding sample capsules
capsules = [
    Capsule(name="Memories of Youth", open_date="2030-05-01", user_id=1),
    Capsule(name="Letters to My Future Self", open_date="2028-09-12", user_id=2),
    Capsule(name="Family Archive", open_date="2040-01-20", user_id=3),
    Capsule(name="My Travel Diaries", open_date="2032-06-15", user_id=4),
    Capsule(name="Business Goals", open_date="2035-11-30", user_id=5),
]