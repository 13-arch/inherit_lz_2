from inherit import Login


def main(): #создаем функцию
    first=Login('Andrey','korovai','andrkorov')
    first.info()
if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию