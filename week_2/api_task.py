import requests

class API:

    def __init__(self):
        self.url = "https://www.metaweather.com/api/location/search/?query=" + self.get_user_place()
        self.response = self.connect()


    def greet_user(self):

        user_name = input("Enter your name: ")

        print(f"Hello, {user_name}!")

    def get_user_place(self):
        user_input = input("Enter a city: ")

        message = f"You entered {user_input}. Is that correct? (y/n) "

        while True:
            user_input = input(message)

            if user_input.lower() == "y" or user_input == "yes":
                return user_input.lower()
            else:
                message = "Enter a city: "

    def connect(self):
        response = requests.get(self.url)

        if response:
            print("You connected with a status code of", response.status_code)
        else:
            print("Connection unsuccessful with a code of", response.status_code)
        
        return response

my_api = API()
# print(my_api.url)

print(my_api.response)