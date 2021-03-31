# task 15
# create a dictionary called shopping_list with three key, value pairs
# milk: £1; yogurht: £1.15; ice cream: £2.38
# create a function that takes a dictionary as an argument
# iterate through the values of shoppping_list and add the values
# return the total cost
shopping_list = {
    "milk": 1,
    "yogurht": 1.15,
    "ice cream": 2.38
}

def calculate_total(shopping_list):
    total = 0
    for value in shopping_list.values():
        total += value
    return total

print("The total of the items in the list: £{:.2f}".format(calculate_total(shopping_list)))

# task 16
# create a dictionary called shopping_list with three key, value pairs
# milk: £1; yogurht: £1.15; ice cream: £2.38
# display the cost of yogurht
print(shopping_list["yogurht"])