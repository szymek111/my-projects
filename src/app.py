#app.py
from userrepository import UserRepository

class App:
    def __init__(self):
        self.user_repo = UserRepository()

    def handle_user_input(self):

        user_input=input(">")

        if user_input=="0":
            self.user_repo.append_user(self.user_repo.add_new_user())

        if user_input=="1":
            self.user_repo.show_list_of_members()

        elif user_input !="":
            print("\n Not Valid Choice Try again")

    def run(self):

        flag = True
        while flag:

            self.user_repo.print_main_menu()

            self.handle_user_input()


