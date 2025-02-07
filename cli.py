import click
from datetime import datetime
from database import get_session
from models import User, Capsule, Message

@click.group()
def cli():
    """Time Capsule CLI - Store and Retrieve Digital Time Capsules"""
    pass

@cli.command()
@click.argument("name")
def add_user(name):
    """Add a new user"""
    session = get_session()
    try:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

@cli.command()
@click.argument("user_id", type=int)
@click.argument("name")
@click.argument("open_date")
def add_capsule(user_id, name, open_date):
    """Create a new time capsule"""
    session = get_session()
    try:
        open_date = datetime.strptime(open_date, "%Y-%m-%d").date()
        capsule = Capsule(name=name, open_date=open_date, user_id=user_id)
        session.add(capsule)
        session.commit()
        print(f"Capsule '{name}' created for User ID {user_id}.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

@cli.command()
@click.argument("capsule_id", type=int)
@click.argument("content")
def add_message(capsule_id, content):
    """Add a message to a time capsule"""
    session = get_session()
    try:
        message = Message(capsule_id=capsule_id)
        message.set_content(content)
        session.add(message)
        session.commit()
        print("Message added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

@cli.command()
def list_users():
    """List all users"""
    session = get_session()
    try:
        users = session.query(User).all()
        for user in users:
            print(f"{user.id}: {user.name}")
    finally:
        session.close()

@cli.command()
@click.argument("capsule_id", type=int)
def view_messages(capsule_id):
    """View all messages in a time capsule"""
    session = get_session()
    try:
        messages = session.query(Message).filter_by(capsule_id=capsule_id).all()
        if messages:
            for message in messages:
                print(f"- {message.get_content()}")
        else:
            print("No messages found for this capsule.")
    finally:
        session.close()

if __name__ == "__main__":
    cli()
