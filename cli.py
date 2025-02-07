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