import json
import os
import random

class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.is_adopted = False
        self.__id = random.randint(1000, 9999)

    def display(self):
        status = "Adopted" if self.is_adopted else "Not adopted"
        print(f'ID: {self.__id} | Name: {self.name} | Age: {self.age} | Breed: {self.breed} | Status: {status}')

    def mark_as_adopted(self):
        self.is_adopted = True

    def speak(self):
        print('Some sound!')

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
            "is_adopted": self.is_adopted,
            "id": self.__id,
            "type": type(self).__name__
        }

    def get_id(self):
        return self.__id

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    def speak(self):
        print('Woof!!!')

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    def speak(self):
        print('Meow!!!')


class Parrot(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
    def speak(self):
        print('Mimicking!!!')


class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self):
        type_choice = input("What type of animal (Dog, Cat, Parrot): ")
        name = input(f"What is the name of {type_choice}: ")
        age = input(f"Enter the age of {name}: ")
        breed = input(f"Enter the breed of {type_choice}: ")

        if type_choice.upper() == "DOG":
            animal = Dog(name, age, breed)
        elif type_choice.upper() == "CAT":
            animal = Cat(name, age, breed)
        elif type_choice.upper() == "PARROT":
            animal = Parrot(name, age, breed)
        else:
            print("Invalid choice!")
            return

        self.animals.append(animal)
        print(f"{name} added to shelter!")

    def view_all(self):
        if not self.animals:
            print("There are no animals.")
        else:
            for animal in self.animals:
                animal.display()

    def view_by_type(self):
        type_choice = input("What type of animal (Dog, Cat, Parrot): ")
        if not self.animals:
            print("There are no animals!")
            return
        found = False
        for animal in self.animals:
            if type_choice.upper() == type(animal).__name__.upper():
                animal.display()
                found = True
        if not found:
            print(f"No {type_choice} found in shelter!")

    def mark_adopted(self):
        self.view_all()
        animal_id = int(input("Enter the ID of the animal to adopt: "))
        for animal in self.animals:
            if animal.get_id() == animal_id:
                animal.mark_as_adopted()
                print(f"{animal.name} has been adopted!")
                return
        print("Animal not found!")

    def save(self):
        animals_data = []
        for animal in self.animals:
            animals_data.append(animal.to_dict())
        with open("animals.json", "w") as f:
            json.dump(animals_data, f)

    def load(self):
        if os.path.exists("animals.json"):
            with open("animals.json", "r") as f:
                content = f.read()
                if content.strip() == "":
                    return
                animals_data = json.loads(content)
                for animal_dict in animals_data:
                    if animal_dict["type"] == "Dog":
                        animal = Dog(animal_dict["name"], animal_dict["age"], animal_dict["breed"])
                    elif animal_dict["type"] == "Cat":
                        animal = Cat(animal_dict["name"], animal_dict["age"], animal_dict["breed"])
                    elif animal_dict["type"] == "Parrot":
                        animal = Parrot(animal_dict["name"], animal_dict["age"], animal_dict["breed"])
                    animal.is_adopted = animal_dict["is_adopted"]
                    self.animals.append(animal)
