


from email import message
from xmlrpc.client import ResponseError


translation ={ #global dict to encode and decode characters
    'a':'0',
    'b':'1',
    'c':'2',
    'd':'3',
    'e':'4',
    'f':'5',
    'g':'6',
    'h':'7',
    'i':'8',
    'j':'9',
    'k':'!',
    'l':'@',
    'm':'#',
    'n':'$',
    'o':'%',
    'p':'^',
    'q':'&',
    'r':'*',
    's':'(',
    't':')',
    'u':'-',
    'v':'+',
    'w':'<',
    'x':'>',
    'y':'?',
    'z':'='
}



def getPrompt():
    while True: #continuously getting a response every iteration through
        print("Welcome to the Secret Message Encoder/Decoder")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        while True:#ensuring the response is a number and is between 1-3
            try:
                response = input("What would you like to do? ")
                assert(int(response)>0 and int(response)<4)
                response = int(response)
                break
            except:
                print(response + " is not a valid choice")


        if response==1:
            encode()
        elif response==2:
            decode()
        elif response==3:
            break

def encode():
    message = input("\nEnter a message to encode: ") #getting the message to encode
    for letter in message:#iterating through each letter to translate
        if letter in translation:
            message = message.replace(letter, translation[letter]) #if the letter is a key in the dict, then replace it with its value
    print("Encoded message: "+message + '\n')

def decode():
    key_list = list(translation.keys()) #getting list of keys
    val_list = list(translation.values()) #getting list of values
    message = input("\nEnter a message to decode: ")
    for letter in message:
        if letter in val_list:
            message = message.replace(letter, key_list[val_list.index(letter)]) #using index of letter in the value list to get the key from the key list
    print("Decoded message: "+message + '\n')


def main():
    getPrompt()


if __name__=="__main__":
    main()
