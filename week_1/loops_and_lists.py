# loops and lists

# Give the user an idea of how to run the programme
def print_help():
    print("\nType 'done' to finish entering names")
    print("Type 'list' to view the names you've entered so far")
    print("Type 'help' to see this help\n")


# prints each item in the list on a new line
def print_list(list):
    for item in list:
        print(item)

# will print all the list items that have an even length
def check_for_eveness(list):
    for item in list:
        if len(item) % 2 == 0: # this checks if the length of the word is divisible by 2
            print(f"{item} has a length of {len(item)}, and that's even")
        else:
            print(f"{item} has a length of {len(item)}, and that's not even")

count = 10 # initialise the count variable
for i in range(count):
    print("hello") # will print 'hello' 10 times in this example


names_list = [] # create an empty list for names

print("Enter some names")

while True:
    user_input = input("> ") # generic prompt as the user can enter commands
    
    if user_input.lower() == "done": # to move onto the next part of the programme
        break
    elif user_input.lower() == "help": # will show help
        print_help()
    elif user_input.lower() == "list": # will list the names already entered
        print_list(names_list)
    elif user_input == "":
        print("You must enter a value") # makes sure empty strings aren't added to the list
    else:
        names_list.append(user_input) # adds the name to the list


names_list_lower = [] # an empty list to hold the lowercased names

for name in names_list:
    names_list_lower.append(name.lower()) # changes all the names to lower case

check_for_eveness(names_list_lower)