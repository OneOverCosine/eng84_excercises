import datetime as dt

current_date = dt.datetime.now() # for consitency with calculations
# current_year = 2021

while True:
    age_input = input("How old are you? ") # don't forget to cast into an int!
    if age_input.isdigit():
        break
    else:
        print("Please enter a whole number!")

age = int(age_input)
calc_age = age # for use in calculations

while True:
    b_day_passed = input("Has your birthday already passed this year? (y/n) ")

    if b_day_passed.lower() == "y" or b_day_passed.lower() == "yes":
        break
    elif b_day_passed.lower() == "n" or b_day_passed.lower() == "no":
        calc_age += 1 # to account for the fact that their birthday for this year hasn't passes
        break
    else:
        print("Please enter 'y' or 'n'")


name = input("What is your name? ")

# calculate the year they were born
birth_year = current_date.year - calc_age

print(f"OMG {name}, you are {age} years old, so you were born in {birth_year}")

# Extra
leap_count = 0 # to calculate the days manually, taking into account leap days

for i in range(birth_year, current_date.year + 1):
    if i % 400 == 0:
        leap_count += 1
    elif i % 4 == 0 and i % 100 != 0:
        leap_count += 1

age_in_hours = age * (365 + leap_count) * 24

print(f"You've lived about {age_in_hours} hours")