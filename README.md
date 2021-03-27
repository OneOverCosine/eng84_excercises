# Python Excercises
## Tasks
### [Week 1](./week_1/)
- [Date of Birth Calculator](./week_1/birth_date_calculator.py)
- [Restuarant Waiter Helper Programme](./week_1/restuarant_helper.py)
- [Holiday List](./week_1/holiday_list.py)
- [Fizz Buzz (Updated to OOP)](./week_1/fizzbuzz.py)
- [Scrabble (OOP)](./week_1/scrabble.py)
- [Functional Calculator (OOP)](./week_1/functional_calculator.py)
- [Loops and Lists](./week_1/loops_and_lists.py)
- [Control Flow](./week_1/control_flow.py)
- [Hero Story](./week_1/hero_story.py)  
---
## Date of Birth Calculator
To define the variables ``age`` and ``name`` I could have done this at the beginning of the document and given them placeholder values.
```python
age = -1 # This is so I know immediately if something has gone wrong with later assignments
name = ""
```

Instead I chose to declare the variables as I took the user's input. This made checking the user's input easier for me.
```python
while True:
    age_input = input("How old are you? ") # don't forget to cast into an int!
    if age_input.isdigit(): # if the age entered is a digit, then we can move onto the next part of the programme
        break
    else:
        print("Please enter a whole number!")
```

The ``while`` keyword above signifies the beginning of a loop. Using ``while True`` will mean that the code inside of the while will run until the loop is exited. In this case that happens when the user inputs a whole number value. The ``break`` keyword exits the loop.  

After receiving the user's age, I do a check to see if their birthday has passed, as that changes the calculation I need to make. To only run certain code under specific conditions, use the ``if`` keyword. If you have multiple conditions, ``elif`` (else + if) and ``else`` can be used.
```python
# this is within a while loop
b_day_passed = input("Has your birthday already passed this year? (y/n) ")

    if b_day_passed.lower() == "y" or b_day_passed.lower() == "yes":
        break
    elif b_day_passed.lower() == "n" or b_day_passed.lower() == "no":
        calc_age += 1 # to account for the fact that their birthday for this year hasn't passed
        break
    else:
        print("Please enter 'y' or 'n'")
```

Getting the input for the name is much the same as the age input, though I don't bother with a loop for checks as names can be anything. I also calulate the user's birth year.
```python
name = input("What is your name? ")

# calculate the year they were born
birth_year = current_date.year - calc_age
```
For the ``current_date`` variable I imported the ``datetime`` module. This is used to make working with dates and times easier. There are a lot of useful premade methods that come with it. For example, ``current_date`` is holding the value for ``datetime.datetime.now()``. This is a timestamp that holds the current date and time (from when the code was executed). In the code above, using ``.year`` allows me to extract the current year from that 'now' timestamp.  
  
  Now I print out a message to the user using ``print()``.
```python
print(f"OMG {name}, you are {age} years old, so you were born in {birth_year}")
```
The text inside ``{these}`` are the names of the variables I want to print out. Notice that 'f' just before the string? That shows that this is a formatted string.  

## Restuarant Waiter Helper Programme
(I will not be going over the whole programme. Only concepts not covered already will be looked into to avoid redundancy)  
In Python, you create lists using square brackets ``[]``
```python
food_menu = ["chips", "steak", "baked beans", "bacon", "eggs", "ice cream", "curly fries"]

menu_choices = [] # you can create empty lists too
```

To add items to a list, use the ``append()`` method.
```python
menu_choices.append(item) # item it the thing you're adding to the list
```
You can access an item from the list using its index. ``food_menu[0]`` would get "chips". You can also loop through each item in a list.
```python
def display_menu(menu):
    # for displaying any list
    for item in menu:
        print(item)
```
The above function will take a list as an argument and print out each value on a new line.  

Note that to declare a function in Python, you use the ``def`` keyword. The syntax to call it elsewhere is ``display_menu(menu_list)``. Functions are useful for reducing the amount of code a programmer need to write. In this example I knew that I would be printing multiple lists throughout the runtime of this programme. Without the function, I would need to repeat something similar to the following code every time I wanted to display a list to the user.
```python
for item in list_name:
    print(item)
```
True, there's not much code there, but if I were to extend the programme I would have twice as many lines of code on my hands.

## Holiday List
Everything used in the holiday list programme has been covered in the previous section(s).

## FizzBuzz (OOP)
FizzBuzz is a classic programming problem that doesn't require most of what I've used to solve it. This task requires the implementation of OOP, hence the extra work.  

A class in an object that has attributes (variables) and methods (functions/behaviours) associated with it. These classes can pass down those attributes and methods to other classes (called children or subclasses), but that functionallity won't be present in this example.  
To declare a class in Python, use the keyword ``class``. This is similar to declaring functions, though there are a few differences.
```python
class FizzBuzz():

    def __init__(self, fizz_value = 3, buzz_value = 5):
        # by default, these values will be 3 and 5
        self.fizz_value = fizz_value
        self.buzz_value = buzz_value

    # (truncated for space)
```
That ``__init__(self, ...)`` function is how to set up the class's attributes. To set up methods, you just declare them inside of the class (and make sure to include ``self`` in the perameters)
```python
  def run_fizzbuzz(self, n):

        n = 100 # the number to get upto

        for i in range(1, n + 1): # to make sure 1 to n is printed
            if i % self.fizz_value == 0 and i % self.buzz_value == 0:
                # (truncated for space)
```