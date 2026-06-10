import json
import os
import random
from colorama import init, Fore, Back, Style
from tabulate import tabulate

init(autoreset=True)


class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.is_adopted = False
        self.__id = random.randint(1000, 9999)

    def display(self):
        status = "Adopted" if self.is_adopted else "Not Adopted"
        return [self.__id, self.name, self.age, self.breed, type(self).__name__, status]

    def mark_as_adopted(self):
        self.is_adopted = True

    def speak(self):
        print(Fore.WHITE + "Some sound!" + Style.RESET_ALL)

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
        print(Fore.YELLOW + Style.BRIGHT + "Woof!!!" + Style.RESET_ALL)


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

    def speak(self):
        print(Fore.CYAN + Style.BRIGHT + "Meow!!!" + Style.RESET_ALL)


class Parrot(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

    def speak(self):
        print(Fore.GREEN + Style.BRIGHT + "Mimicking!!!" + Style.RESET_ALL)


class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self):
        type_choice = input(Fore.WHITE + Style.NORMAL + "Enter Animal Type (Dog, Cat, Parrot): " + Style.RESET_ALL)
        name = input(Fore.WHITE + Style.NORMAL + f"Enter Name Of {type_choice}: " + Style.RESET_ALL)
        age = input(Fore.WHITE + Style.NORMAL + f"Enter Age Of {name}: " + Style.RESET_ALL)
        breed = input(Fore.WHITE + Style.NORMAL + f"Enter Breed Of {type_choice}: " + Style.RESET_ALL)

        if type_choice.upper() == "DOG":
            animal = Dog(name, age, breed)
        elif type_choice.upper() == "CAT":
            animal = Cat(name, age, breed)
        elif type_choice.upper() == "PARROT":
            animal = Parrot(name, age, breed)
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Animal Type!" + Style.RESET_ALL)
            return

        self.animals.append(animal)
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"{name} Added To Shelter Successfully!" + Style.RESET_ALL)

    def view_all(self):
        if not self.animals:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "No Animals In Shelter." + Style.RESET_ALL)
            return

        print("\n" + Fore.BLACK + Back.WHITE + "--- All Animals ---" + Style.RESET_ALL)
        table_data = [animal.display() for animal in self.animals]
        headers = [Style.BRIGHT + h + Style.RESET_ALL for h in ["ID", "Name", "Age", "Breed", "Type", "Status"]]
        print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))

    def view_by_type(self):
        type_choice = input(Fore.WHITE + Style.NORMAL + "Enter Animal Type (Dog, Cat, Parrot): " + Style.RESET_ALL)

        filtered = [a for a in self.animals if type(a).__name__.upper() == type_choice.upper()]

        if not filtered:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + f"No {type_choice} Found In Shelter." + Style.RESET_ALL)
            return

        print("\n" + Fore.BLACK + Back.WHITE + f"--- {type_choice.capitalize()}s In Shelter ---" + Style.RESET_ALL)
        table_data = [animal.display() for animal in filtered]
        headers = [Style.BRIGHT + h + Style.RESET_ALL for h in ["ID", "Name", "Age", "Breed", "Type", "Status"]]
        print(tabulate(table_data, headers=headers, tablefmt="pretty", disable_numparse=True))

    def mark_adopted(self):
        if not self.animals:
            print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "No Animals Available." + Style.RESET_ALL)
            return

        self.view_all()

        try:
            animal_id = int(input("\n" + Fore.CYAN + Style.BRIGHT + "Enter Animal ID To Mark As Adopted: " + Style.RESET_ALL))
            for animal in self.animals:
                if animal.get_id() == animal_id:
                    animal.mark_as_adopted()
                    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"{animal.name} Has Been Adopted!" + Style.RESET_ALL)
                    return
            print(Fore.RED + Style.BRIGHT + "Animal ID Not Found!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Please Enter A Valid Number." + Style.RESET_ALL)

    def save(self):
        try:
            with open("animals.json", "w") as f:
                json.dump([animal.to_dict() for animal in self.animals], f)
        except IOError as e:
            print(Fore.WHITE + Back.RED + f"Fatal Error: Failed To Save Animals. {e}" + Style.RESET_ALL)

    def load(self):
        if os.path.exists("animals.json"):
            try:
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
                        else:
                            continue
                        animal.is_adopted = animal_dict["is_adopted"]
                        self.animals.append(animal)
            except (json.JSONDecodeError, IOError) as e:
                print(Fore.WHITE + Back.RED + f"Fatal Error: Failed To Load Animals. {e}" + Style.RESET_ALL)


def main():
    shelter = Shelter()
    shelter.load()

    while True:
        print("\n" + Fore.BLACK + Back.WHITE + "--- Animal Shelter ---" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(1) Add New Animal" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(2) View All Animals" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(3) View Animals By Type" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(4) Mark Animal As Adopted" + Style.RESET_ALL)
        print(Fore.YELLOW + Style.NORMAL + "(5) Quit Animal Shelter" + Style.RESET_ALL)

        choice = input("\n" + Fore.CYAN + Style.BRIGHT + "Enter Your Choice: " + Style.RESET_ALL)

        if choice == "1":
            shelter.add_animal()
            shelter.save()
        elif choice == "2":
            shelter.view_all()
        elif choice == "3":
            shelter.view_by_type()
        elif choice == "4":
            shelter.mark_adopted()
            shelter.save()
        elif choice == "5":
            print(Fore.WHITE + Style.BRIGHT + "Bye! Thanks For Using The Animal Shelter!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Choice, Try Again!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()