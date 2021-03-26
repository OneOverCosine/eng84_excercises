# an OOP implementation of FizzBuzz
class FizzBuzz():

    def __init__(self, fizz_value = 3, buzz_value = 5):
        # by default, these values will be 3 and 5
        self.fizz_value = fizz_value
        self.buzz_value = buzz_value

    def run_fizzbuzz(self, n):

        n = 100 # the number to get upto

        for i in range(1, n + 1): # to make sure 1 to n is printed
            if i % self.fizz_value == 0 and i % self.buzz_value == 0:
                print("FizzBuzz") # prints for multiples of 3 and 5 in this example
            elif i % self.fizz_value == 0:
                print("Fizz") # prints for multiples of 3 in this example
            elif i % self.buzz_value == 0:
                print("Buzz") # prints for multiples of 5 in this example
            else:
                print(i) # prints for all other values

# setting up the 'game' of fizz buzz
interview_problem = FizzBuzz() # there's no need to input values as defaults have been set up
interview_problem.run_fizzbuzz(100)