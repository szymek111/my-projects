#userrepository.py
from user import User
import json

class UserRepository:
    def __init__(self):
        self._users = {}


    def add_user(self, user):
        uniq_id = len(self._users)
        self._users[uniq_id] = user
        self.save_to_file()
        return uniq_id
    
    def list_users(self):
        print(self._users)

    def save_to_file(self):
        serialized_users = {}
        for user_id, user in self._users.items():
           serialized_users[user_id] = user.serialize()
        with open ('out.json', 'w') as f:
            json.dump(serialized_users, f)

    def load_users_from_file(self):
        try:
            with open ('out.json', 'r') as f:
                temp_user_dict = json.load(f)
                for user_id in temp_user_dict:
                    self._users[user_id] = User.deserialize(temp_user_dict[user_id])
        except IOError:
            print("\n\nWarning!!! File not loaded correctly!!!\n\n")

        
            


