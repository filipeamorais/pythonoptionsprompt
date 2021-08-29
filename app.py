from database import add_entry, view_entries

menu = """Please select:
1) Add new entry for today
2) View entries
3) Exit.

Your selection: """

Welcome = "Welcome to the programming diary!"

print (Welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("Invalid option, please try again!")  