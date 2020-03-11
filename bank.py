import pickle
import os.path

class Bank:
    def __init__ (self, name = None, password = None, ammount = 0):
        self.name = name
        self.password = password
        self.ammount = ammount

path = "C:\\Users\\Szymek\\Desktop\\Programowanie\\Python\\config_file_bank.txt"

if os.path.isfile(path):
    print ("File exist")
else:
    list_of_members = []
    with open (path, 'wb') as bank_config_file:
        pickle.dump(list_of_members, bank_config_file)


def read_from_file():
    global list_of_members
    list_of_members = []

    with open (path, 'rb') as config_dictionary_file:
        list_of_members = pickle.load(config_dictionary_file)
        print(list_of_members)

read_from_file()

def save_to_file():
    with open (path, 'wb') as bank_config_file:
        pickle.dump(list_of_members, bank_config_file)


def checking_user(self):
    return self.name, self.password, self.ammount

def create_account(name, password, ammount):
    user_already_exist = 0
    for i in list_of_members:
        if name == i.name:
            user_already_exist = 1
            login_name = i
    if user_already_exist == 1:
        print("Failed...")
        print("User ", name, " already exist!")
        input("\nPress Enter to continue...")
        return 0
    else:
        new_obj = Bank(name, password, ammount)
        print(new_obj.name, "account created!")
        input("\nPress Enter to continue...")
        return new_obj
    
def list_of_members_app(new_obj):
    list_of_members.append(new_obj)
    return list_of_members

def check_user():
    count = -1
    global exacly_user
    for i in list_of_members:
        count += 1
        print (count, ". ", i.name)
    spec = input("Choose user? >")
    spec = int(spec)
    exacly_user = list_of_members[spec]
    return exacly_user

def login():
    FLAG = 0
    global login_name
    print("LOGIN:")
    name = input("Enter your name: ")
    for i in list_of_members:
        if name == i.name:
            FLAG = 1
            login_name = i
    if FLAG == 0:
        print("User not found")
        input("\nPress Enter to continue...")
        return None    

    password = input("Enter your password: ")
    if not password == login_name.password:
        print("Wrong password!")
        return login()
    print(login_name.name,",logged-in!")
    account_mode()




##################
### LOGIN MENU ###
##################
def account_mode():
    log_ans=True
    while log_ans:
        print("\nYou are logged-in as, ", login_name.name)
        print ("------------------------------")
        print("[0]: Deposit")
        print("[1]: Withdraw")
        print("[2]: Transfer")
        print("[3]: Check account ballance")
        print("[4]: Log-out")
        print ("------------------------------\n")

        log_ans=input(">")
        if log_ans=="0": 
            deposit(login_name)

        elif log_ans=="1":
            withdraw(login_name)

        elif log_ans=="2":
            transfer(login_name)

        elif log_ans=="3":
            print("Account ballance: ", login_name.ammount, "$")
            input("\nPress Enter to continue...")

        elif log_ans=="4":
            print("Logged-out")
            input("\nPress Enter to continue...")
            log_ans = False

        elif log_ans !="":
            print("\n Not Valid Choice Try again") 

def deposit(self):
    print("You have ", login_name.ammount, "$")
    deposit_cash = int(input("How many dollars you want to deposit?\n> "))
    login_name.ammount += deposit_cash
    print("Done, now you have ", login_name.ammount, "$")
    print("---------------")
    input("\nPress Enter to continue...")

def withdraw(self):
    print("You have ", login_name.ammount, "$")
    withdraw_cash = int(input("How many dollars you want to withdraw?\n> "))
    if withdraw_cash > login_name.ammount:
        print("You do not have enough money!!!")
        print("---------------")
        input("\nPress Enter to continue...")
        return None

    login_name.ammount -= withdraw_cash
    print("Done, now you have ", login_name.ammount, "$")
    print("---------------")
    input("\nPress Enter to continue...")

def transfer(self):
    print("To whom to transfer money: ")
    to_transfer = check_user()
    if to_transfer == login_name:
        print("Not allowed to transfer money to youself!")
        print("---------------")
        input("\nPress Enter to continue...")
        return None

    print("You want transfer to: ", to_transfer.name)
    transfer_cash = int(input("How many dollars you want to transfer?\n> "))
    if transfer_cash > login_name.ammount:
        print("You do not have enough money!!!")
        print("---------------")
        input("\nPress Enter to continue...")
        return None

    print("You'll transfer ", transfer_cash, "$, to", to_transfer.name, "Confirm? Type 'yes'")
    confirm = input("> ")
    if confirm != "yes":
        print("Transfer failed!")
        input("\nPress Enter to continue...")
    else:
        login_name.ammount -= transfer_cash
        to_transfer.ammount += transfer_cash
        print("Transfer done!")
        input("\nPress Enter to continue...")




###################
#### MAIN MENU ####
###################
ans=True
while ans:
    print ("\nWelcome in BANK! What do you want to do?")
    print ("------------------------------")
    print ("[0]: Create new account")
    print ("[1]: Log-in to existing account")
    print ("[2]: Check user")
    print ("------------------------------\n")

    ans=input(">")
    if ans=="0": 
        new_account = create_account(input("New name: "), input("New password: "), 0)
        list_of_members_app(new_account)

    elif ans=="1":
        login()

    elif ans=="2":
        if len(list_of_members) == 0:
            print("NO ANY USERS")
            input("\nPress Enter to continue...")
        else:
            name, password, ammount = checking_user(check_user())
            print ("Name        -> ",name)
            print ("Password    -> ",password)
            print ("Ammount     -> ",ammount)
            input("\nPress Enter to continue...")

    #elif ans=="3":
    #    print (list_of_members, "<<<<it is list")

    elif ans !="":
        print("\n Not Valid Choice Try again")

save_to_file()