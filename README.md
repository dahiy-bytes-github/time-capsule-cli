# Time Capsule CLI

## Overview
The **Time Capsule CLI** is a Python-based command-line application that allows users to store digital messages to be opened at a specific future date. The project uses an **Object-Relational Mapping (ORM)** system with SQLAlchemy to interact with a database, where users can create, manage, and view their messages, capsules, and users. The application follows **Object-Oriented Programming (OOP)** best practices and provides a simple yet powerful CLI for interacting with the stored data.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Setting Up the Database](#setting-up-the-database)
6. [How to Use](#how-to-use)
7. [CLI Commands](#cli-commands)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [License](#license)

## Features
- **User Management**: Users can be created, stored, and linked to multiple capsules.
- **Capsule Management**: Each user can store multiple capsules, each containing a future message.
- **Message Creation**: Users can write messages that are stored and linked to a specific date for retrieval.
- **Database Storage**: Uses SQLite for local storage, with SQLAlchemy ORM for handling database interactions.
- **Simple CLI Interface**: Easy-to-use command-line interface to interact with users, capsules, and messages.

## Technologies Used
- **Python 3.x**: The primary programming language for the project.
- **SQLAlchemy**: ORM used to manage database interactions.
- **SQLite**: Lightweight database for local storage.
- **Click**: Python package for creating command-line interfaces.
- **pytest**: Testing framework for verifying the correctness of the code.

## Project Structure
time_capsule_cli/ # Root directory ├── venv/ # Virtual environment (optional) ├── database.py # Database setup and configuration ├── models.py # ORM models (Capsule, Message, User) ├── cli.py # Main CLI script with commands ├── setup_db.py # Initializes the database schema ├── populate_data.py # Populates the database with initial data ├── requirements.txt # Python dependencies ├── README.md # Project documentation


 Installation  

### **1️⃣ Clone the Repository**  
Clone this repository to your local machine:  

```bash
git clone https://github.com/dahiy-bytes-github/time-capsule-cli.git
cd time_capsule_cli


python3 -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate virtual environment
Install Dependencies: Install the required dependencies from requirements.txt:

pip install -r requirements.txt
Verify Installation: You can verify everything is set up correctly by running the following:


python3 -m time_capsule_cli.cli
Setting Up the Database
Before using the CLI, you need to set up the database schema.

Initialize the Database: Run the following command to create the required tables in the database:

python3 setup_db.py
This will create an SQLite database (time_capsule.db) and the tables for Users, Capsules, and Messages.

Populate the Database: You can populate the database with some initial data using:

python3 populate_data.py
This script will insert sample users into the database.

How to Use
Once the database is set up, you can start using the application via the command line. The main interface is built using Click, which provides commands to manage users, capsules, and messages.

CLI Commands
Here are the available commands in the CLI:

Create a User:

python3 cli.py create-user --name "John Doe"
Creates a new user in the system.

List Users:

python3 cli.py list-users
Lists all users currently in the system.

Create a Capsule for a User:

python3 cli.py create-capsule --user-id 1 --date "2025-12-31" --message "Open this in one year."
Creates a new capsule for a specific user that will be opened on the specified date.

List Capsules for a User:

python3 cli.py list-capsules --user-id 1
Lists all capsules for a specific user.

Create a Message in a Capsule:

python3 cli.py create-message --capsule-id 1 --content "This is your message."
Creates a message inside a specified capsule.

View Messages in a Capsule:

python3 cli.py list-messages --capsule-id 1
Lists all messages inside a specified capsule.

Contributing
If you’d like to contribute to the project, follow these steps:

Fork the Repository: Fork the repository on GitHub to your own account.

Clone the Repository: Clone your forked repository to your local machine.

Create a Branch: Create a new branch to make your changes.

git checkout -b feature-branch
Make Changes and Commit: Make the necessary changes, then commit them:

git commit -m "Description of the changes"
Push Changes: Push your changes to your forked repository:

git push origin feature-branch
Submit a Pull Request: Go to the original repository and submit a pull request for review.

License
This project is licensed under the MIT License.

Acknowledgments
This project uses SQLAlchemy and SQLite for database management.
The project is built following best practices in Object-Oriented Programming (OOP) in Python.
