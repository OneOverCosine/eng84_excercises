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
def is_dunni(name):
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