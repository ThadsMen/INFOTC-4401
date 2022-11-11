import datetime
import math
import time

class Tweet:

    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()


    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        current = time.time()
        time_since = current - self.__age
        if time_since < 60:
            return str(math.floor(time_since)) + 's'
        elif time_since < 3600:
            return str(math.floor(time_since/60)) + 'm'
        elif time_since < 216000:
            return str(math.floor(time_since/3600)) +'hrs'

def createTweet():
    name = input("\nWhat is your name? ")
    while True:
        try:
            text = input("What would you like to tweet? ")
            if len(text)>140:
                raise ValueError()
            break
        except ValueError:
            print("Tweets can only be 140 characters!")
            
    tweet = Tweet(name,text)
    print(f"{name}, your tweet has been saved\n")
    return tweet

def getRecentTweets(tweets):
    if len(tweets)==0:
        print("\nThere are no tweets to display\n")
        return

    counter = 0
    for tweet in tweets:
        print(f"\n{tweet.get_author()} - {tweet.get_age()}\n{tweet.get_text()}\n")
        counter+=1
        if counter==5:
            break


def searchTweet(tweets):

    if len(tweets)==0:
        print("\nThere are no tweets to search\n")
        return
    key = input("\nWhat would you like to search for? ")
    tweets.reverse()
    counter = 0
    for tweet in tweets:
        if key in tweet.get_text():
            counter+=1
            print(f"\n{tweet.get_author()} - {tweet.get_age()}\n{tweet.get_text()}\n")
    if counter ==0:
        print(f"\nNo tweets found with {key}\n")
    


def main():
    tweets = [] #animal list to hold Animal Objects
    while(True):
        print("Tweet Menu")
        print("-—————")
        print("1. Make a Tweet\n2. View Recent Tweets\n3. Search Tweets\n4. Quit")
        while True:
            try:
                choice = int(input("What would you like to do? "))
                if choice<1 or choice>4:
                    raise ValueError()
                break
            except ValueError:
                print("Please enter a number 1-4")

        match choice:
            case 1:
                tweets.append(createTweet())
            case 2:
                getRecentTweets(tweets)
            case 3:
                searchTweet(tweets)
            case 4:
                break
        

if __name__=="__main__":
    main()
        