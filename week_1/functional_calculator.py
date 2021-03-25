import math

class Calculator():
    def add(self, *args): # *args lets me take in any number of arguments
        if len(args) < 2:
            return "You need at least two values to add together"
        else:
            return sum(args)

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, *args):
        if len(args) < 2:
            return "You need at least two values to multiply together"
        
        product = 1
        for num in args:
            product = product * num
        return product

    def divide(self, num1, num2):
        if num2 == 0:
            return "You cannot divide by 0"

        return num1 / num2

class Calculator_Extended(Calculator):


    def area_of_circle(self, radius):
        return 2 * math.pi * pow(radius, 2)
    
    def area_of_square(self, height):
        return pow(height, 2)

    def area_of_triangle(self, base, height):
        return (base * height) / 2

calcy = Calculator()

print('For addition, got:', calcy.add(1, 2, 3)) # should be 6
print('For subtraction, got:', calcy.subtract(4, 2)) # should be 2
print('For multiplication, got:', calcy.multiply(3, 7)) # 21
print('For division, got:', calcy.divide(49, 7)) # 7.0
print('For incorrect division, got:', calcy.divide(9, 0)) # won't allow this

print('\n')
mega_calcy = Calculator_Extended()

print('For addition, got:', mega_calcy.add(9, 10)) # 19
print('For subtraction, got:', mega_calcy.subtract(4, 2)) # 2
print('For multiplication, got:', mega_calcy.multiply(3, 7)) # 21
print('For division, got:', mega_calcy.divide(49, 7)) # 7.0
print('For incorrect division, got:', mega_calcy.divide(9, 0)) # won't allow this

rad = 2
height = 9
base = 11

print('\nAnd for the new functions:\n')
print('For a circle with radius {}, you get an area of {}'.format(rad, mega_calcy.area_of_circle(rad)))
print('For a square of height {}, you get an area of {}'.format(height, mega_calcy.area_of_square(height)))
print('For a triange of base {} and height {}, you get an area of {}'.format(base, height, mega_calcy.area_of_triangle(base, height)))