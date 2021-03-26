# Control flow with age restrictions

def check_age(age):

    # handling the flow of the programme based on the age the user enters
    if age >= 18:
        print(f"\nAt {age} you can:\n - Vote\n - Buy drinks\n - Drive\n\n")
    elif age == 17:
        print(f"\nYou can learn to drive from {age}.\n\n")
    elif age == 16:
        print(f"\nThere's not much you can do age {age}, though you could get married if your parents allow it.\n\n")
    elif age <= 15 and age >= 4:
        print(f"\nAt {age}, you should be focused on doing well at school.\n\n")
    else:
        print("You're too young to be worrying about this!")


age = 19
driver_licence = True

# this loop will run until the user enters 'exit'
while True:
    user_input = input("Enter your age to see what you can do\n(or type 'exit' to leave): ")

    if user_input.strip() == "":
        print("You must enter a value")
    elif user_input.isdigit():
        check_age(int(user_input))
    elif user_input.lower() == "exit":
        break
    else:
        print("Please enter a whole number!")