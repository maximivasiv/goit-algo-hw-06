class Field:
    def __init__(self, value):
        self.value = value
class Name(Field):
    pass
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("Phone must contain only digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone not found")

    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if not phone:
            raise ValueError("Phone not found")

        self.remove_phone(old_number)
        self.phones.append(Phone(new_number))

    def __str__(self):
        phones = "; ".join(phone.value for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(dict):
    def add_record(self, record):
        self[record.name.value] = record

    def find(self, name):
        return self.get(name)

    def delete(self, name):
        if name in self:
            del self[name]

    def iterator(self, page_size=2):
        records = list(self.values())
        for i in range(0, len(records), page_size):
            yield records[i:i + page_size]
