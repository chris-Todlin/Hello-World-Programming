""" 
    This is the program to calculate the tip
        ->  The user enters the bill and tip percentage
        -> I do the calculation
        -> I print the tip and the total bill
"""

# Start
# introduce the program
print('Welcome to Tip calculator')
print("If you want to exit, enter 'exit' in the repeat section")

# The main program to loop around it
while True:
    try:
        
        # enter the bill and teh tip percent
        print("\nEnter the bill amount: ")
        bill = int(input())
        print("Enter the tip percent: ")
        tipPercent = int(input())
        
        # some condition if the tip percent is positive and amount is greater than 0
        if bill < 0 or tipPercent < 0:
            print("Check your inputs for correct actialization")
            print("\nPlease try again!")
            continue
        
        # else cacluate the tip 
        tipAmount = bill * (tipPercent/100)
        totalBill = bill + tipAmount
        
        # print the output to see the result
        print("The tip Amount is : " + str(tipAmount))
        print("The total bill Amount: " + str(totalBill))
        
        # Ask the user to exit
        print("Do you want to exit? (y/n)")
        repeatControl = input()
        
        # the decision block
        if repeatControl.lower() == 'y':
            break
        
        # else tell the user you are starting again 
        print("\nStarting again...")
    except ValueError:
        print("Please enter the correct value")