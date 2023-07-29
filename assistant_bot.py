# Словник для зберігання контактів
contacts = {}

# Декоратор для обробки помилок введення користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please provide name and phone number separated by a space."
    return inner


"""Функції обробники команд"""

@input_error
def handle_hello():
    return "How can I help you?"

# Очищення даних від користувача
def clean_input(command):
    command = command.strip().lower()
    return command.split()

# Функція додавання контакту
@input_error
def handle_add(command):
    _, name, phone = clean_input(command)
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} has been added."

# Функція зміни номера телефону контакту
@input_error
def handle_change(command):
    _, name, phone = clean_input(command)
    contacts[name] = phone
    return f"The phone number for contact {name} has been changed to {phone}."

# Функція виведення номера телефону контакту
@input_error
def handle_phone(command):
    _, name = clean_input(command)
    return f"The phone number for contact {name} is {contacts[name]}."

# Функція виведення всіх контактів
def handle_show_all():
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

COMMANDS = {
    'add': handle_add,
    'change': handle_change,
    'phone': handle_phone,
}

def handle_command(command):
    if command == 'hello':
        return handle_hello()
    elif command == 'show all':
        return handle_show_all()
    tokens = command.split()
    operation = tokens[0].lower()
    if operation in COMMANDS:
        return COMMANDS[operation](command)
    else:
        return "Invalid command. Please try again."

def main():
    """Цикл запит-відповідь"""
    print("Hello?")
    while True:
        command = input().strip().lower()
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print(handle_command(command))
if __name__ == "__main__":
    main()
