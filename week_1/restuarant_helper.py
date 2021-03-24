def display_menu(menu):
    for item in menu:
        print(item)


food_menu = ["chips", "steak", "baked beans", "bacon", "eggs", "ice cream", "curly fries"]

#display_menu(food_menu)

menu_choices = []
choice_count = 0

while choice_count < 3:
    choice_made = False

    print("== menu ==")
    display_menu(food_menu)
    choice = input(f"\nWhat would you like to order? ({choice_count}/3) ")

    for item in food_menu:
        if choice == item:
            menu_choices.append(item)
            choice_count += 1
            choice_made = True
            break
    
    if not choice_made:
        print("Please order something from the menu:")

print("\n== You have ordered ==")
display_menu(menu_choices)
