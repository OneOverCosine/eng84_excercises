#14
shopping_list = {
    "milk": 1,
    "yoghurt": 1.15,
    "ice cream": 2.38
}

def list_total(shopping_list):
    total = 0
    for item in shopping_list.values():
        total += item
    return total

print("£{0:.2g}".format(list_total(shopping_list)))