class Contact:  # класс контактов
    def __init__(self):
        self.name = ""
        self.phone_number = ""
        self.email = ""

    def get_all_data(self):  # метод получения всех данных контакта
        return self.name, self.phone_number, self.email


file_name = input("Название файла с контактами: ")
print()
contacts_file = open(file_name, encoding='utf-8')

contacts = []  # список всех контактов

for contact in contacts_file:
    contact_data = contact.replace(", ", ",").replace("\n", "").split(",")  # разделение контакта на составляющие

    current_contact = Contact()  # создание объекта класса
    current_contact.name = contact_data[0]
    current_contact.phone_number = contact_data[1]
    current_contact.email = contact_data[2]

    contacts.append(current_contact)  # заносим контакт в общий список


def show_all_contacts():
    for contact in contacts:
        print(contact.get_all_data())


def search_contacts():  # процедура поиска контакта по данным
    data = input("Введите данные о контакте через пробел: ").split()

    for contact in contacts:
        is_right_contact = True  # флаг для проверки контакта на совпадение
        for data_elem in data:
            if data_elem not in contact.get_all_data()[0].split() and data_elem not in contact.get_all_data():  # проверка на совпадение
                is_right_contact = False
        if is_right_contact:
            print(contact.get_all_data())


def show_defective_contacts():
    for contact in contacts:
        if "" in contact.get_all_data():
            print(contact.get_all_data())


def change_contact():  # метод для изменения данных контакта
    print("Выберите контакт по номеру")
    print("0 - отмена")
    for i in range(len(contacts)):  # выдача номера каждому контакту для удобства использования
        print(str(i + 1) + " -", contacts[i].get_all_data())

    contact_number = int(input("\nВведите номер контакта: "))

    if contact_number < 0 or contact_number >= len(contacts):  # проверка на корректность
        print("Такого номера нет\n")
        change_contact()
        return

    if contact_number == 0:  # номер для возврата в меню
        return

    contact_number -= 1  # возврат к порядку списка

    print("\nПредыдущие данные контакта: ", contacts[contact_number].get_all_data())
    print("Ничего не вводите, если хотите оставить данные поля прежними")

    name = input("Введите имя: ")
    if name != "":
        contacts[contact_number].name = name

    phone_number = input("Введите телефон: ")
    if phone_number != "":
        contacts[contact_number].phone_number = phone_number

    email = input("Введите почту: ")
    if email != "":
        contacts[contact_number].email = email

    print("Контакт изменён", contacts[contact_number].get_all_data())


print("Все контакты:")
show_all_contacts()
print()

while True:  # меню программы
    command = input("Введите команду: ")
    print()

    if command == "show all":
        show_all_contacts()

    elif command == "search":
        search_contacts()

    elif command == "defective":
        show_defective_contacts()

    elif command == "change":
        change_contact()

    elif command == "help":
        print("show all - показать все контакты")
        print("search - поиск контакта по данным")
        print("defective - показать неполноценные контакты")
        print("change - изменить контакт")
        print("quit - завершить программу")

    elif command == "quit":
        break

    else:
        print("Неизвестная команда, напишите help для просмотра всех команд")

    print()