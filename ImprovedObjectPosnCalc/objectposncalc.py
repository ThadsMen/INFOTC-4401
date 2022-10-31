
game = True
while(game):

    while(True):
        try:    
            pos0 = float(input("Please enter an initial position: \n"))
            break
        except:
            print("Error please enter a valid position")

    while(True):
        try:    
            vel0 = float(input("Please enter an initial velocity: "))
            break
        except:
            print("Error please enter a valid velocity")

    while(True):
        try:    
            acel = float(input("Please enter an acceleration: "))
            break
        except:
            print("Error please enter a valid acceleration")


    while(True):
        try:    
            time = float(input("Please enter a time: "))
            assert time>0
            break
        except:
            print("Error please enter a valid time")
            
    pos1 = pos0 + (vel0*time) +(.5*acel*(time**2))

    print(f"The final position of the object is {pos1}")

    while(True):
        prompt = input("Would you like to perform another calculation? y/n: ")
        if(prompt!='y'):
            game=False
            break
        else:
            break

