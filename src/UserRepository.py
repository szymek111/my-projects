#userrepository.py
from user import User

class UserRepository:
    def __init__(self):
        self._my_list = []
    
    def print_main_menu(self):
            print("###########################")
            print("[0] Create new user")
            print("[1] Check user-list")
            print("###########################")

    def add_new_user(self):

        uniq_no = input("Enter UNIQ_NO: ")
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        password = input("Enter password: ")
        temp_new_user = User(uniq_no, name, surname, password, 0)
        return temp_new_user

    def append_user(self, user):
        self._my_list.append(user)
    
    def show_list_of_members(self):
        print(self._my_list)