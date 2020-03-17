#app.py
from userrepository import UserRepository
from user import User

class App:
    def __init__(self):
        self.user_repo = UserRepository()


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

        flag = True
        while flag:

            self.user_repo.print_main_menu()

            self.handle_user_input()

            #self.user_repo.save_to_file()


