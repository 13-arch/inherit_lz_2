#13-arch


import hashlib

class Login:
    employees = {
        'senya': 'arseniy okun',
        'bobr': 'ilua bobro',
        'zoro': 'anton zorecki'
    }

    def __init__(self, name, surname, login):
        self.name = name
        self.surname = surname
        self.login = login

    def info(self):
        return f'Name: {self.name}, Surname: {self.surname}, Login: {self.login}'
    
    def is_employee(self):
        return self.login in self.employees


class Authorization(Login):
    def __init__(self, name, surname, login, password):
        super().__init__(name, surname, login)
        self.password = password
        self.is_hashed = False

    def info(self):
        return f'{super().info()}, Password: {"hashed" if self.is_hashed else self.password}'

    def hashing_pass(self):
        if not self.is_hashed:
            self.password = hashlib.sha256(self.password.encode()).hexdigest()
            self.is_hashed = True
        