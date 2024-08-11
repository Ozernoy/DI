'''
🌟 Exercise 2 : Dogs
Instructions
Create a class called Dog.
In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
Create a method called bark that prints the following string “<dog_name> goes woof!”.
Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
Print the details of his dog (ie. name and height) and call the methods bark and jump.
Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
Print the details of her dog (ie. name and height) and call the methods bark and jump.
Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
'''

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')

# Creating David's dog
davids_dog = Dog(name='Rex', height=50)
print(f"{davids_dog.name}, Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

# Creating Sarah's dog
sarahs_dog = Dog(name='Teacup', height=20)
print(f"{sarahs_dog.name}, Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Function to find the biggest dog
def biggest_dogo(*dogs):
    return max(dogs, key=lambda dog: dog.height)

# Find and print the name of the bigger dog
bigger_dog = biggest_dogo(davids_dog, sarahs_dog)
print(f"The bigger dog is {bigger_dog.name}.")
