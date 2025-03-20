from inherit import Authorization


def main(): #создаем функцию
    user = Authorization('arseniy', 'okun', 'senya', 'mypassword')
    print(user.info())
    print("Is employee:", user.is_employee())
    user.hashing_pass()
    print(user.info())
if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию