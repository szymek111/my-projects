#userrepository.py
from user import User
import json

class UserRepository:
    def __init__(self):
        self._users = {}
    
    def print_main_menu(self):
            print("###########################")
            print("[0] Create new user")
            print("[1] Check user-list")
            print("###########################")


    def add_user(self, user):
        uniq_id = len(self._users)
        self._users[uniq_id] = user
        print(uniq_id)
        return uniq_id
    
    def list_users(self):
        print(self._users)

    #def save_to_file(self):

        
            


