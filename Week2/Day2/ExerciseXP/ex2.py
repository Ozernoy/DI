'''
🌟 Exercise 2 : Dogs
Instructions
Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class.
'''

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}"
        elif my_power < other_power:
            return f"{other_dog.name} wins the fight against {self.name}"
        else:
            return "It's a tie!"

dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Max", 4, 25)
dog3 = Dog("Rex", 6, 30)

# Running methods
print(dog1.bark())          # Buddy is barking
print(dog2.run_speed())     # Max's run speed
print(dog3.run_speed())     # Rex's run speed

# Fighting between dogs
print(dog1.fight(dog2))     # Buddy vs Max
print(dog2.fight(dog3))     # Max vs Rex
print(dog1.fight(dog3))     # Buddy vs Rex
