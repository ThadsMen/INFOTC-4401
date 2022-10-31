
from fileinput import filename
from itertools import count


def metricsOfNumbers(numbers):
    sum = 0
    count=0
    for number in numbers: #iterating through the list of numbers
        sum = sum + number #adding it all up
        count=count+1 #incrementing the count every iteration
    average = sum/count
    return { #returns dict to use to dispplay metrics
        'sum':sum,
        'count':count,
        'average':average,
        'max':max(numbers),
        'min':min(numbers),
        'range':max(numbers)-min(numbers)
    }

def displayContents(file,metrics):
    print(f"Filename: {file}")
    print(f"Sum: {metrics['sum']}")
    print(f"Count: {metrics['count']}")
    print(f"Average: {metrics['average']}")
    print(f"Maximum: {metrics['max']}")
    print(f"Minimum: {metrics['min']}")
    print(f"Range: {metrics['range']}")

def main():

    while(True):
        while(True):
            try:
                file = input("What file would you like to use? ") #error handling file opening
                with open(file,'r') as f:
                    numbers = [int(x) for x in f.readlines()] #converting every number to an int to perform math on 
                break
            except IOError:
                print("Error accessing file")

        metrics = metricsOfNumbers(numbers)
        displayContents(file,metrics)
        displayMore = input("Would you like to evaluate another file? (y/n) ")
        if(displayMore=='n'):
            break


if __name__ == "__main__":
    main()
