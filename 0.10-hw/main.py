import re
from collections import UserDict
class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        # Валідація телефонного номера (10 цифр)
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(self.value):
            raise ValueError("Неправильний формат номера телефону")

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        # Використовуємо filter для створення нового списку без вказаного номера телефону
        self.phones = list(filter(lambda phone: phone.value != phone_value, self.phones))

    def edit_phone(self, old_phone_value, new_phone_value):
        for phone in self.phones:
            if phone.value == old_phone_value:
                phone.value = new_phone_value
                return  # Додано return, щоб зупинити пошук після редагування першого номера
        # Якщо немає відповідного номера телефону, викидаємо ValueError
        raise ValueError("Номер телефону не існує")

    def find_phone(self, phone_value):
        return next((phone for phone in self.phones if phone.value == phone_value), None)

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name_value):
        return self.data.get(name_value)

    def delete(self, name_value):
        if name_value in self.data:
            del self.data[name_value]
