import statistics

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
        'range':max(numbers)-min(numbers),
        'median':statistics.median(numbers),
        'mode':mode(numbers)
    }


def mode(numbers):
    number_count = {} #dict to hold the total number of occurences with each number
    mode_values = [] #initialized empty list to hold the numbers that appear the most
    max = 0 #used to determine the the number that appears the most
    for number in numbers:
        if number in number_count: #if the number is in the dict, increment by 1
            number_count[number]+=1
        else:
            number_count[number]=1 #else the number doesnt exist in the dict and add a new entry
        count = number_count[number]
        if(count>max): #if the count is greater than max then there is a new max
            max = count
    
    for number in number_count: #iterating through the dictiionary to determine if any of the numbers value is equal to the max occurences
        if(number_count[number]==max):
            mode_values.append(number)
    return mode_values


    



def displayContents(file,metrics):
    print(f"Filename: {file}")
    print(f"Sum: {metrics['sum']}")
    print(f"Count: {metrics['count']}")
    print(f"Average: {metrics['average']}")
    print(f"Maximum: {metrics['max']}")
    print(f"Minimum: {metrics['min']}")
    print(f"Range: {metrics['range']}")
    print(f"Median: {metrics['median']}")
    print(f"Mode: {metrics['mode']}")

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
        if(len(numbers)==0):
            print(f"There are no numbers in {file}") #error handling if an empty file is received
        else:
            metrics = metricsOfNumbers(numbers)
            displayContents(file,metrics)
        displayMore = input("Would you like to evaluate another file? (y/n) ")
        if(displayMore=='n'):
            break


if __name__ == "__main__":
    main()
