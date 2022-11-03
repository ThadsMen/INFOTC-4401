
from Animals import *

def main():
    animals = [] #animal list to hold Animal Objects
    print("Welcom to the Animal Generator!")
    print("This program create animal objects")
    while(True):
        print("Would you like to create a mammal or a bird?")
        print("1. Mammal\n2. Bird")
        while True:
            try:
                animal = int(input("Which would you like to create? "))
                if animal<1 or animal>2:
                    raise ValueError()
                break
            except ValueError:
                print("Please enter a number 1 or 2")

        if animal == 1:
            type = input("\nWhat type of mammal would you like to create? ")
            name = input("What is the mammal's name? ")
            color = input("What color is the mammals's hair? ")
            mammal = Mammal(type,name,color)
            animals.append(mammal)

        if animal==2:
            type = input("\nWhat type of bird would you like to create? ")
            name = input("What is the bird's name? ")
            can_fly = input("Can the bird fly? ")
            bird = Bird(type,name,can_fly)
            animals.append(bird)

        displayMore = input("\nWould you like to add more animals? (y/n) ")
        if(displayMore=='n'):
            break
    print("\nAnimal list")
    for animal in animals: #iterating through the list of animals and printing information
        print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")


if __name__ == "__main__":
    main()