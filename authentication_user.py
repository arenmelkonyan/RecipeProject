from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import base64
import re
import logging

engine = create_engine("sqlite:///users.db", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def register():
    print("Registering the new user:")
    username = input("Enter username: ")
    user = session.query(User).filter_by(username=username).first()
    if user:
        print("This nickname is already in use,please try another one! ")
        return
    print(f"Entered username is: {username}")
    while True:
        password = input("Enter password: ")
        if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", password):
            print("Entered password must be at least 8 chars and contain minimum one uppercase char,please try again!")
        else:
            break
    print("Password entered successfully! ")
    encoded_password = base64.b64encode(password.encode()).decode()
    user = User(username=username, password=encoded_password)
    session.add(user)
    session.commit()
    print("Registration successful!")


def login():
    username = input("Please,enter a username: ")
    password = input("Please,enter a password: ")
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        encoded_password = user.password
        decoded_password = base64.b64decode(encoded_password.encode()).decode()
        if decoded_password == encoded_password:
            print("Login was successful!")
        else:
            print("Invalid username or password,please try again!")
    else:
        print("Invalid username or password,pleasee try again!")


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting from the account")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
