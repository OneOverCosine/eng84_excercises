# since I know what I need from the module, I only need to import one thing
from math import pi

# to define a class, use the 'class' keyword
class Calculator():
    def add(self, *args): # *args lets me take in any number of arguments
        if len(args) < 2:
            return "You need at least two values to add together"
        else:
            return sum(args) # return the sum of all the values inputted

    def subtract(self, num1, num2):
        return num1 - num2 # returns first value - second value

    def multiply(self, *args):
        if len(args) < 2:
            return "You need at least two values to multiply together"
        
        product = 1 # start at 1 as 1 * value = value - starting at 0 would create errors
        # multiplies all the values entered
        for num in args:
            product = product * num 
        return product

    def divide(self, num1, num2):
        
        # check for invalid inputs
        if num2 == 0:
            return "You cannot divide by 0"

        return num1 / num2

# To extend a class, include it in brackets the class definition
class Calculator_Extended(Calculator):  

    # You don't need to do anything extra for this class to inherit
    # Calculator's methods. You can move straight into writing unique
    # ones for this class
    
    def area_of_circle(self, radius):
        return 2 * pi * pow(radius, 2)
    
    def area_of_square(self, height):
        return pow(height, 2)

    def area_of_triangle(self, base, height):
        return (base * height) / 2

# creating an instance of Calculator
calcy = Calculator()

print('For addition, got:', calcy.add(1, 2, 3)) # should be 6
print('For subtraction, got:', calcy.subtract(4, 2)) # should be 2
print('For multiplication, got:', calcy.multiply(3, 7)) # 21
print('For division, got:', calcy.divide(49, 7)) # 7.0
print('For incorrect division, got:', calcy.divide(9, 0)) # won't allow this

print('\n')
# creating an instance of Calculator_Extended
mega_calcy = Calculator_Extended()

# It has all the functionality of Calculator
print('For addition, got:', mega_calcy.add(9, 10)) # 19
print('For subtraction, got:', mega_calcy.subtract(4, 2)) # 2
print('For multiplication, got:', mega_calcy.multiply(3, 7)) # 21
print('For division, got:', mega_calcy.divide(49, 7)) # 7.0
print('For incorrect division, got:', mega_calcy.divide(9, 0)) # won't allow this

rad = 2
height = 9
base = 11

# It also has access to all the new functions
print('\nAnd for the new functions:\n')
print('For a circle with radius {}, you get an area of {}'.format(rad, mega_calcy.area_of_circle(rad)))
print('For a square of height {}, you get an area of {}'.format(height, mega_calcy.area_of_square(height)))
print('For a triange of base {} and height {}, you get an area of {}'.format(base, height, mega_calcy.area_of_triangle(base, height)))