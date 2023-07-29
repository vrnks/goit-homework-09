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

# Функція додавання контакту
@input_error
def handle_add(command):
    _, name, phone = command.split()
    contacts[name.lower()] = phone
    return f"Contact {name} with phone number {phone} has been added."

# Функція зміни номера телефону контакту
@input_error
def handle_change(command):
    _, name, phone = command.split()
    contacts[name.lower()] = phone
    return f"The phone number for contact {name} has been changed to {phone}."

# Функція виведення номера телефону контакту
@input_error
def handle_phone(command):
    _, name = command.split()
    return f"The phone number for contact {name} is {contacts[name.lower()]}."

# Функція виведення всіх контактів
def handle_show_all():
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    """Цикл запит-відповідь"""
    print("Hello?")
    while True:
        command = input().strip().lower()
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(handle_hello())
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print(handle_add(command))
        elif command.startswith("change"):
            print(handle_change(command))
        elif command.startswith("phone"):
            print(handle_phone(command))
        elif command == "show all":
            print(handle_show_all())
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
