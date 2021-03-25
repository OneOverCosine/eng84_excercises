# loops and lists

def print_help():
    print("\nType 'done' to finish entering names")
    print("Type 'list' to view the names you've entered so far")
    print("Type 'help' to see this help\n")


def print_list(list):
    for item in list:
        print(item)

def check_for_eveness(list):
    pass # unsure for the moment

count = 10 # initialise the count variable
for i in range(count):
    print("hello") # will print 'hello' 10 times in this example


names_list = []

print("Enter some names")

while True:
    user_input = input("> ")
    
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


names_list_lower = []

for name in names_list:
    names_list_lower.append(name.lower()) # changes all the names to lower case

check_for_eveness(names_list_lower)