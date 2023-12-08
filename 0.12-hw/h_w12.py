import cmd
import pickle
from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Ім'я не повинно бути пустим")
        super().__init__(value)


class Phone(Field):
    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Повинно бути 10 цифр')

    @Field.value.setter
    def value(self, value):
        self.validate(value)
        super(Phone, Phone).value.__set__(self, value)


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        self.__value = datetime.strptime(value, '%Y.%m.%d').date()


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        if birthday:
            self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"
    

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print(f"Phone number '{phone_number}' already exists for '{self.name.value}'.")



class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_by_name(self, name):
        name = name.lower()
        matches = [record for record in self.data.values() if record.name.value.lower() == name]
        return matches

    def find_by_phone(self, phone_number):
        matches = [record for record in self.data.values() if any(phone.value == phone_number for phone in record.phones)]
        return matches

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def dump(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            pass


class Controller(cmd.Cmd):
    def __init__(self, address_book):
        super(Controller, self).__init__()
        self.book = address_book
        self.file = "address_book.pkl"
        self.book.load(self.file)

    def do_exit(self, arg):
        self.book.dump(self.file)
        return True

    def do_add(self, arg):
        while True:
            try:
                name = input("Enter contact name: ")
                birthday = input("Enter birthday (YYYY.MM.DD): ")

                record = Record(name, birthday)
                self.book.add_record(record)

                phone_number = input("Enter phone number to add: ")
                record.add_phone(phone_number)

                print(f"Contact '{name}' added with phone number {phone_number}.")
                break  # Вихід із циклу при успішному виконанні
            except ValueError as e:
                print(f"Error: {e}")
                print("Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")






    def do_find_by_name(self, arg):
        name = input("Enter contact name to find: ")
        matches = self.book.find_by_name(name)
        if matches:
            print(f"Contacts found for name '{name}':")
            for match in matches:
                print(match)
        else:
            print(f"No contacts found for name '{name}'.")

    def do_find_by_phone(self, arg):
        phone_number = input("Enter phone number to find: ")
        matches = self.book.find_by_phone(phone_number)
        if matches:
            print(f"Contacts found for phone number '{phone_number}':")
            for match in matches:
                print(match)
        else:
            print(f"No contacts found for phone number '{phone_number}'.")

    def do_delete(self, arg):
        name = input("Enter contact name to delete: ")
        self.book.delete_record(name)
        print(f"Contact '{name}' deleted.")

    def do_list(self, arg):
        for record in self.book.data.values():
            print(record)

    def do_save(self, arg):
        file_path = input("Enter file path to save: ")
        self.book.dump(file_path)
        print(f"Address book saved to {file_path}.")

    def do_load(self, arg):
        file_path = input("Enter file path to load: ")
        self.book.load(file_path)
        print(f"Address book loaded from {file_path}.")


if __name__ == "__main__":
    address_book = AddressBook()
    controller = Controller(address_book)
    controller.cmdloop()
