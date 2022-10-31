import random


class Animal:

    def __init__(self, name, type):
        self.__name = name
        self.__animal_type = type
        num = random.choice([1, 2,3]) #selects a number from 1-3
        if num==1:
            self.__mood = "happy"
        elif num==2:
            self.__mood = "hungry"
        elif num==3:
            self.__mood = "sleepy"

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood

def main():
    tiger = Animal("Benny","Tiger")
    print(tiger.get_animal_type())
    print(tiger.get_name())
    print(tiger.check_mood())

if __name__ == "__main__":
    main()