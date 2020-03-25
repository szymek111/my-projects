#app.py
from userrepository import UserRepository
from user import User
import json

class App:
    def __init__(self):
        self.user_repo = UserRepository()


    def print_main_menu(self):
            print("###########################")
            print("[0] Create new user")
            print("[1] Check user-list")
            print("###########################")

    def user_creation(self):
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        password = input("Enter password: ")
        temp_new_user = User(name, surname, password, 0)
        self.user_repo.add_user(temp_new_user)

    def show_users(self):
        self.user_repo.list_users()

    def handle_user_input(self):

        user_input=input(">")

        if user_input=="0":
            self.user_creation()

        if user_input=="1":
            self.show_users()

        elif user_input !="":
            print("\n Not Valid Choice Try again")

    def run(self):
        self.user_repo.load_users_from_file()

        flag = True
        while flag:
            self.print_main_menu()

            self.handle_user_input()


