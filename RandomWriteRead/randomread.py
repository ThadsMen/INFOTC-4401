def readFile():
    try:
        with open('randomnum.txt','r') as file: 
            numbers = file.readlines() #reads file line by line and returns a list of lines
        return numbers
    except IOError:
        print("Error file not found") 

def displayNumbers(numbers):
    print("List of random numbers in randomnum.txt") #formatting the display properly
    for number in numbers:
        print(number)
    print('Random number count ' + str(len(numbers)))

def main():
    numbers = readFile()
    displayNumbers(numbers)

if __name__=="__main__":
    main()