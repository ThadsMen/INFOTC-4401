from Animals import Animal


def main():
    animals = [] #animal list to hold Animal Objects
    print("Welcom to the Animal Generator!")
    print("This program create animal objects")
    while(True):
        type = input("\nWhat type of animal would you like to create? ")
        name = input("What is the animal's name? ")
        animal = Animal(name,type) #creating new instance of Animal class
        animals.append(animal) #storing the object into the list

        displayMore = input("\nWould you like to add more animals? (y/n) ")
        if(displayMore=='n'):
            break
    print("Animal list")
    for animal in animals: #iterating through the list of animals and printing information
        print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")


if __name__ == "__main__":
    main()