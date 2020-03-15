#app.py
from userrepository import UserRepository

class App:
    def __init__(self):
        self.user_repo = UserRepository()

    def run(self):

        ans = True
        while ans:
        
            print("###########################")
            print("[0] Create new user")
            print("[1] Check user-list")
            print("###########################")

            ans=input(">")

            if ans=="0":
                self.user_repo.append_user(self.user_repo.add_new_user())

            if ans=="1":
                self.user_repo.show_list_of_members()

            elif ans !="":
                print("\n Not Valid Choice Try again")
