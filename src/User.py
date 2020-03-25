class User:
    def __init__ (self, name = None, surname = None, password = None, amount = 0):
        self.name = name
        self.surname = surname
        self.password = password
        self.amount = amount

    
    def serialize(self):
        return {'name':self.name, 'surname':self.surname, 'password':self.password, 'amount':self.amount}

    @staticmethod
    def deserialize(serialized_user):
        User(serialized_user)
        return User
        
        
