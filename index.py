"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old. I am {self.gender}.")

# Create an instance of the Person class
person = Person("Alice", 30, "female")
person.introduce()


"""
class Individual:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old. I am {self.gender}.")


def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    return Individual(name, age, gender)

# Get user input and create a Person object
user = get_user_info()
user.introduce()



