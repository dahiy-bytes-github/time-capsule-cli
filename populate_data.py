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