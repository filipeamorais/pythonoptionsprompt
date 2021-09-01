from database import add_entry, view_entries

menu = """Please select:
1) Add new entry for today
2) View entries
3) Exit.

Your selection: """

Welcome = "Welcome to the programming diary!"

def promt_new_entry():
    entry_content = input("What have you learned today?  ")
    entry_date = input ("Enter the date: ")

    add_entry(entry_content, entry_date)

def view_entries (entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

print (Welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")  