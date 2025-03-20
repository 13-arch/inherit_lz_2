#13-arch


class Login:
    def __init__(self,name,surname,login):
        self.n=name
        self.sn=surname
        self.l=login
    

    def info(self):
        print(f'ИМЯ:{self.n},ФАМИЛИЯ:{self.sn},ЛОГИН:{self.l}')


    def is_employee(self):
        