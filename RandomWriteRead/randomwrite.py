from functools import total_ordering
import numbers
import random


def getNumbers():
    while(True):
        try:
            total_num = int(input("How many numbers would you like to generate? "))
            assert(total_num>0) #number must be greate than 0
            return total_num #return value if total_num is greater than 0
        except:
            print("Please enter a number greater than 0")
        
def getLowerBounds():
    while(True):
        try:
            lowerBound = int(input("What is the lower bound? ")) 
            assert(lowerBound>0) #makes sure lowerbound is greater than 0
            return lowerBound#return lowerbound if proper format
        except:
            print("Please enter a number greater than 0")

def getUpperBound(lowerBound):
    while(True):
        try:
            upperBound = int(input("what is the upper bound? "))
            assert(upperBound>0 and upperBound>lowerBound) #makes sure upper bound is more than 0 and greater than the lowerbound
            return upperBound
        except:
            print("Please enter a number greater than 0 and higher than the lower bound")

def generateNumbers(total,lowerBound,upperBound):
    numbers = [] #list to store numbers
    for number in range(total): #iterating through the total amount of numbers  requested
        numbers.append(random.randint(lowerBound,upperBound)) #adds a random number between the lower bound and upper bound every iteration
    return numbers


def main():

    total_num = getNumbers()
    lowerBound = getLowerBounds()
    upperBound = getUpperBound(lowerBound)
    numbers = generateNumbers(total_num,lowerBound,upperBound)

    with open('randomnum.txt','w+') as file: #opens file for writing, creates the file if it does not exist
        for i in range(total_num):
            file.write(str(numbers[i])+'\n') #writes numbers on new line 



if __name__=="__main__":
    main()