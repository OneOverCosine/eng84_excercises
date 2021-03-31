## To clear up space from the other file

### Task 01
- declare a funciton called 'greeting'
- takes a string argument and returns the user's name (in a greeting message)
```py
def greeting(name):
    return f"Hello {name}!"
```

### Task 02
- declare a list of numbers from 0 - 9
- iterate through it and print the list (slightly vague... print list as one or print each value?)
```py
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    print(num)
```

### Task 03
(My solution may be odd, as I missed the question)
- using boolean operators, print True if two statements are true
```py
if "a" == "b" and "c" == "d":
    print(True)
```

### Task 04
- create a list of five numbers, starting from zero
- create a tuple of five numbers, starting from zero
- change the value of the last index in the tuple
```py
num_list = [0, 1, 2, 3, 4]

# could also do
num_list2 = []
for i in range(5):
    num_list2.append(num) 

num_tuple = (num_list2)

# because tuples are immutable, you cannot chanage the
# value at any index.
```
Lists are mutable, so you would be able to change that value.

### Task 05
- create a dictionary with two key,value pairs
- first key: name, value: James
- second key: age: value: 18
- display the values and the keys
```py
person = {
    "name": "James",
    "age": 18
}

for key, value in person.items():
    print(key, value)
```

### Task 06
- create a class called Katalyst (my name)
- initialise the class to take two arguments
- create an object of that class
- create another object of the same class called student
- print the attributes
```py
class Katalyst:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

me = Katalyst("Cringe", "Katalyst")
student = Katalyst("Ash", "Fall")

print(me.arg1, me.arg2)
print(student.arg1, student.arg2)
```

### Task 07
- create a set with values from 1 to 4
```py
set_dec = {1, 2, 3, 4} # uses curly braces
# unlike other collections, sets are unordered
```

### Task 08
- create a method that takes one argument as a string (my name)
- if the name == "Katalyst" return true, else return false
```py
def is_katalyst(name):
    if name == "Katalyst":
        return True
    else:
        return False
```

### Task 09
- create a class called Human with one function called breathe that returns "breathing"
- create another class called Student that inherits from Human
- create a Student object and call the function from the parent class
```py
class Human:
    def breathe(self):
        return "Breathing"

class Student(Human):
    pass

student_object = Student()
print(student_object.breathe())
```

### Task 10
- write some code that allows you use the keyword ``super``
```py
# uses the above classes
class Student(Human):
    def __init__(self):
        super().__init__()
```
The super keyword refers to the parent class. In the above example it's used to 

### Task 11
- create a list called user_data and store numbers 0 to 4 in it
- create a function that takes an argument as a list
- the function returns True if the datatype is a list and False otherwise
```py
user_data = [0, 1, 2, 3, 4]

def is_list(data):
    if type(data) == "<class 'list'>":
        return True
    else:
        return False
```

## Task 12
- create a function called 'get_percentage' that takes two integers as arguments
- it should return the percentage of the two arguments
```py
def get_percentage(num1, num2):
    # idk if name is right
    return str((num1 / num2) * 100)
```

# Task 13
- create a function that takes two arguments as integers
- divide the first value by the second value and *return the outcome*
- if the second value is 0, throw an error with a message stating that you can't divide by zero
```py
def divide(num1, num2):
    try:
        return num1 / num2

    except ZeroDivisionError:
        return "You cannot divide by zero"
```

# Task 14
- write 5 odd numbers in a list
- write 5 even numbers in another list
- iterate through the lists to combine them and display the new list - write a function to do this
```py
odd_nums = [1, 3, 5, 7, 9]
even_nums = [0, 2, 4, 6, 8]

def combine_and_display(list1, list2):
    i = 0
    while i < len(list1): # this works as I know the contents + size of the list
        if list1[i] % 2 == 0: #
            print(list1[i])
            print(list2[i])
        else:
            print(list2[i])
            print(list1[i])

        i += 1

combine_and_display(odd_nums, even_nums)
```

### Task 15
- create a dictionary called shopping_list with three key, value pairs
- milk: £1; yoghurt: £1.15; ice cream: £2.38
- create a function that takes a dictionary as an argument
- iterate through the values of shoppping_list and add the values
- return the total cost
```py
shopping_list = {
    "milk": 1,
    "yoghurt": 1.15,
    "ice cream": 2.38
}

def calculate_total(shopping_list):
    total = 0
    for value in shopping_list.values():
        total += value
    return total

print("The total of the items in the list: £{:.2f}".format(calculate_total(shopping_list)))
```

### Task 16
- using the dictionary from the previous task, display the cost of yoghurt
```py
print(shopping_list["yoghurt"])
```