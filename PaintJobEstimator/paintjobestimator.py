import math


getEstimate = True

while(getEstimate):

    while(True):
        try:
            square_feet = int(input("Please enter the square feet of wall space to be painted: "))
            if(square_feet<=0):
                print('Please enter a non-negative value greater than 0')
                continue
        except ValueError:
            print("Please enter a number")
        else:
            break

    while(True):
        try:
            paint_price = float(input("Please enter the price of the paint per gallon: "))
            if(paint_price<=0):
                print('Please enter a non-negative value greater than 0')
                continue
        except ValueError:
            print("Please enter a number")
        else:
            break

    gallons = math.ceil(square_feet/350)
    hours = (6*square_feet)/350
    paint_cost = gallons*paint_price
    labor_charges = 62.25 * hours
    total_costs = paint_cost+labor_charges

    print(f'The total number of gallons of paint needed is: {gallons}')
    print('The paint job will take {:.1f} hours'.format(hours))
    print('The paint will cost you ${:.2f}'.format(paint_cost))
    print('The labor costs ${:.2f}'.format(labor_charges))
    print('In total the paint job will cost ${:.2f}'.format(total_costs))

    another_estimate = input("\nWould you like to do another estimate? (y/n): ")
    if (another_estimate != "y"):
        getEstimate = False

    