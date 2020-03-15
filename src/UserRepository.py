class UserRepository:
    def __init__(self):
        self._my_list = []
    

    def add_new_user(self, user):
        self._my_list.append(user)