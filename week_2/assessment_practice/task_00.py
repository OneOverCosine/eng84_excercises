# task 08
# create a method that takes one argument as a string (my name)
# if the name == "Dunni" return true, else return false

def is_dunni(name):
    if name == "Dunni":
        return True
    else:
        return False

print(is_dunni("Dunni"))

# Task 09
# create a class called Human with one function called breathe that returns "breathing"
# create another class called Student that inherits from Human
# create a Student object and call the function from the parent class

class Human:
    def breathe(self):
        return "Breathing"

class Student(Human):
    pass

student_object = Student()
print(student_object.breathe())