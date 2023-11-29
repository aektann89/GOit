from collections import UserDict
from datetime import datetime



class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        if not isinstance(new_value, str) or not new_value.isdigit() or len(new_value) != 10:
            raise ValueError("Invalid phone number format")
        self._value = new_value

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Invalid birthday format, use YYYY-MM-DD')
        
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        self._value = new_value

class Record:
    def __init__(self, name, birthday=None):
        super().__init__(name)
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone:
            found_phone.value = new_phone
        else:
            raise ValueError(f"Phone number {old_phone} not found in record")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.now().date()
        next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()
        return (next_birthday - today).days

    def __str__(self):
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, item_number):
        count = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}'
            count += 1
            if count >= item_number:
                yield result
                count = 0
                result = ''