# holding in variables to allow for easy editing
fizz = 3
buzz = 5

n = 100 # the number to get upto

for i in range(1, n + 1): # to make sure 1 to n is printed
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz") # prints for multiples of 3 and 5 in this example
    elif i % fizz == 0:
        print("Fizz") # prints for multiples of 3 in this example
    elif i % buzz == 0:
        print("Buzz") # prints for multiples of 5 in this example
    else:
        print(i) # prints for all other values