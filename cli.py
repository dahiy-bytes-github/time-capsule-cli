import click
from database import session
from models import User, Capsule, Message

@click.group()
def cli():
    """Time Capsule CLI - Store and Retrieve Digital Time Capsules"""
    pass

@cli.command()
@click.argument("name")
def add_user(name):
    """Add a new user"""
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User '{name}' added successfully.")
    
@cli.command()
@click.argument("user_id", type=int)
@click.argument("name")
@click.argument("open_date")
def add_capsule(user_id, name, open_date):
    """Create a new time capsule"""
    capsule = Capsule(name=name, open_date=open_date, user_id=user_id)
    session.add(capsule)
    session.commit()
    print(f"Capsule '{name}' created for User ID {user_id}.")