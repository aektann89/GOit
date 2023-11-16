contacts = {}

# Функції для обробки команд

def add_contact(data):
    try:
        name, number = data.split()
        contacts[name] = number
        return f"Contact {name} added with number {number}."
    except ValueError:
        return "Give me name and phone please."

def change_contact(data):
    try:
        name, number = data.split()
        if name in contacts:
            contacts[name] = number
            return f"Phone number for {name} changed to {number}."
        else:
            return f"Contact {name} not found."
    except ValueError:
        return "Give me name and phone please."

def phone_number(name):
    try:
        number = contacts[name]
        return f"The phone number for {name} is {number}."
    except KeyError:
        return f"Contact {name} not found."

def show_all_contacts():
    if contacts:
        all_contacts = "\n".join([f"{name}: {number}" for name, number in contacts.items()])
        return f"All contacts:\n{all_contacts}"
    else:
        return "No contacts available."

def goodbye():
    print("Good bye!")
    exit()

# Декоратор для обробки помилок введення

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper

# Головна функція (main)

@input_error
def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print(add_contact(command[len("add"):].strip()))
        elif command.startswith("change"):
            print(change_contact(command[len("change"):].strip()))
        elif command.startswith("phone"):
            print(phone_number(command[len("phone"):].strip()))
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            goodbye()
        else:
            print("Command not recognized.")

if __name__ == "__main__":
    main()
