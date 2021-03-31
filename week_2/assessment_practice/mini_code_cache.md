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
- write the boolean operators
- if "a" == "b" and "c" == "d", print True
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