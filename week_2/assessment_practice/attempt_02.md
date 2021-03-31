### Task 01
```py
def greeting(name):
    return name
```

### Task 02
```py
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in num_list:
        print(num)
```

### Task 03
```py
if 7 == 7 and 9 > 1: print(True)
```

### Task 04
```py
num_list = [0, 1, 2, 3, 4]
num_tuple = (0, 1, 2, 3, 4)
# can't change a tuple as they are immutable
```

### Task 05
```py
a_dict = {
    "name": "James",
    "age": 18
}

for key, value in a_dict.items():
    print(key, value)
```

### Task 06
```py
class Katalyst:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Katalyst("Kata", 42)
student = Katalyst("Ash", 99)
print(person.name, person.age)
print(student.name, student.age)
```

### Task 07
```py
my_set = {1, 2, 3, 4}
```

### Task 08
```py
def is_me(name):
    if name == "Katalyst":
        return True
    return False
```

### Task 09 & Task 10
```py
class Human:
    def __init__(self):
        pass

    def breathe(self):
        return "Breathing"

class Student(Human):
    def __init__(self):
        super().__init__()

student = Student()
print(student.breathe())
```

### Task 11
```py
user_data = [0, 1, 2, 3, 4]

def is_list(data):
    if type(data) == list:
        return True
    return False
```

### Task 12
```py
def get_percentage(a, b):
    return (a/b) * 100
```

### Task 13
```py
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You can't divide by zero!"
```

### Task 14
```py
odds = [1, 3, 5, 7, 9]
evens = [0, 2, 4, 6, 8]

def combine_and_list(list1, list2):
    i = 0
    new_list = []
    while i < len(list1): # both lists are the same length
        if list1[i] % 2 == 0:
            new_list.append(list1[i])
            new_list.append(list2[i])
        else:
            new_list.append(list2[i])
            new_list.append(list1[i])
        i += 1

    for value in new_list:
        print(value)
```

### Task 15
```py
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
```

### Task 16
```py
print(shopping_list["yoghurt"])
```