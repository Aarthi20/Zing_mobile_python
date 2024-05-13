class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.mobile = ""

    def set_values(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.mobile = input("Enter mobile number: ")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_mobile(self):
        return self.mobile

# Create an instance of the Person class
person = Person()

# Set values using user input
person.set_values()

# Print values using getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Mobile:", person.get_mobile())
