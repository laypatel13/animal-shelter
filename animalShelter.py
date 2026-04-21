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
    pass