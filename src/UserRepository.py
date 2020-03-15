#userrepository.py

class UserRepository:
    def __init__(self):
        self._my_list = []
    
    def add_new_user(self):
        from user import User

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