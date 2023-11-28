import re
from collections import UserDict
from datetime import datetime, timedelta
class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    @Field.value.setter
    def value(self, new_value):
        super().value = new_value
        self.validate_phone()

    def validate_phone(self):
        # Валідація телефонного номера (10 цифр)
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(self.value):
            raise ValueError("Неправильний формат номера телефону")
        
    def get_value(self):
        return f"Phone: {self.value}"
        
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_birthday()

    @Field.value.setter
    def value(self, new_value):
        super().value = new_value
        self.validate_birthday()

    def validate_birthday(self):
        # Валідація формату дня народження (YYYY-MM-DD)
        try:
            datetime.strptime(self.value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Неправильний формат дня народження")
        
    def get_value(self):
        return f"Birthday: {self.value}"

class Record:
    def __init__(self, name_value, birthday_value=None):
        self.name = Name(name_value)
        self.phones = []
        self.birthday = None
        if birthday_value:
            self.birthday = Birthday(birthday_value)

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
    
    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.now()
        next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
        return (next_birthday - today).days
    
    def get_value(self):
        result = [f"Name: {self.name.get_value()}"]
        if self.phones:
            result.append("Phones:")
            for phone in self.phones:
                result.append(f"  {phone.get_value()}")
        if self.birthday:
            result.append(f"Birthday: {self.birthday.get_value()}")
        return "\n".join(result)

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

    def iterator(self, n=1):
        # Генератор, що повертає уявлення для N записів
        records = list(self.data.values())
        for i in range(0, len(records), n):
            yield records[i:i + n]
