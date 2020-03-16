#app.py
from userrepository import UserRepository

class App:
    def __init__(self):
        self.user_repo = UserRepository()


    def user_creation(self):
        self.user_repo.append_user(self.user_repo.create_user())

    def showing_users(self):
        self.user_repo.listing_users()

    def handle_user_input(self):

        user_input=input(">")

        if user_input=="0":
            self.user_creation()

        if user_input=="1":
            self.showing_users()

        elif user_input !="":
            print("\n Not Valid Choice Try again")

    def run(self):

        flag = True
        while flag:

            self.user_repo.print_main_menu()

            self.handle_user_input()


