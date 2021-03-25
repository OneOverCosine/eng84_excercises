def print_help():
    # gives user some pointers on how to use the programme
    print("== HELP ==")
    print("To add and item to the list, input its name and press enter.")
    print("To end the program enter 'exit'.")


print("=== Holiday List ===")
print("(For help, enter 'help')")

holiday_list = []

# the code within the while will keep running until the break
while True:
    user_input = input("> ") # a generic prompt since the user can enter commands

    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "help":
        print_help()
    elif user_input == "":
        print("Make sure you enter an item!")
    else:
        holiday_list.append(user_input) # a an item to the list


if holiday_list == []:
    # if there's nothing in the list, there's nothing to print
    print("\nYou have no items in your holiday list")
else:
    print("\n== Your List ==") # print the list
    for item in holiday_list:
        print(item)