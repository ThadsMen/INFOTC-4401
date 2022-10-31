pos0 = float(input("Please enter an initial position: "))

vel0 = float(input("Please enter an initial velocity: "))

acel = float(input("Please enter an acceleration: "))

time = float(input("Please enter a time: "))

pos1 = pos0 + (vel0*time) +(.5*acel*(time**2))

print(f"The final position of the object is {pos1}")