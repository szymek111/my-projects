class User:
    def __init__ (self, uniq_no, name = None, surname = None, password = None, amount = 0):
        self.uniq_no = uniq_no
        self.name = name
        self.surname = surname
        self.password = password
        self.amount = amount