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

    def use_stdin(self):
        uniq_no = len(self._my_list)
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        password = input("Enter password: ")
        return uniq_no, name, surname, password, 0

    def create_user(self):
        temp_new_user = User(self.use_stdin())
        return temp_new_user

    def append_user(self, user):
        self._my_list.append(user)
    
    def listing_users(self):
        print(self._my_list)