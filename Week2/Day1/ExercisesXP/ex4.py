'''
Exercise 4 : Afternoon at the Zoo
Instructions
Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called ramat_gan_safari and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)
'''

class Zoo:
    def __init__(self, zoo_name):
        # Initialize the zoo with a name and an empty list of animals
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        # Add the new animal to the list if it isn't already in the list
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        # Print all the animals in the zoo
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        # Remove the animal from the list if it exists
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        # Sort the animals alphabetically and group them by their first letter
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        current_letter = ''
        group_id = 1
        
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter != current_letter:
                # Start a new group if the first letter changes
                current_letter = first_letter
                grouped_animals[group_id] = [animal]
                group_id += 1
            else:
                # Add to the current group
                grouped_animals[group_id - 1].append(animal)
        
        self.animal_groups = grouped_animals

    def get_groups(self):
        # Print the animals in each group
        print("Animal groups:")
        for group_id, group in self.animal_groups.items():
            print(f"Group {group_id}: {group}")

# Example Usage
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Adding animals to the zoo
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

# Attempting to add a duplicate animal
ramat_gan_safari.add_animal("Giraffe")

# Displaying all animals in the zoo
ramat_gan_safari.get_animals()

# Selling an animal
ramat_gan_safari.sell_animal("Baboon")
ramat_gan_safari.get_animals()

# Sorting animals and grouping them
ramat_gan_safari.sort_animals()

# Displaying the groups of animals
ramat_gan_safari.get_groups()
