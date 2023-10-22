def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0]

    if name in contacts:
        phone = contacts[name]
        return phone
    else:
        return "Contact not found."


def show_all(args, contacts):
    if len(contacts) == 0:
        return "No contacts."
    else:
        formatted_contacts = []

        for name, phone in contacts.items():
            formatted_contacts.append(f'{name}: {phone}')

        return "\n".join(formatted_contacts)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
