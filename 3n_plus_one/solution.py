""" 
    This is the solution to face the one in the javascript counterpart
    Though, I am a beginner her, I would try
    
    Input is an integer n
    Output is a sequence of numbers 
    Process -> If even => divide by two 
            -> If odd => 3n +1
            -> if n is 1 terminate the program 
            -> Take care of the 0 or less than inputs
            -> Print the sequence out too
"""

def sequence_3n_1(n):
    # This track the count of the steps taken 
    stepsTaken = 0
    
    # just keeping the record of the number inputted
    numberInputted = n
    
    # inform the start of the sequence
    # print("\nTrial start with the sequence 3n + 1")
    
    # start the loop 
    while n > 0:
        # print(n, end=" ") # print the sequence 
        stepsTaken += 1 # add the count
        
        # now the process begins
        # did this so as to get the accurate number of steps and include the
        # first n and the last n more easily. Thus print at the start of the loop 
        # before any activity, then do the processes above mentioned
        if n == 1:
            break # if the 1 is arrived print, add the step and then break 
        
        # now the even and odd interplay 
        if n % 2 == 0:
            n /= 2 # even 
        else:
            n = 3*n + 1

    # the last good bye in the function 
    # print("\nIt took " + str(stepsTaken) + " steps to reach 1 from  the number(inputted) " + str(numberInputted))
    
    # treturn the number of steps taken 
    return stepsTaken
    

# giving it a test drive 
sequence_3n_1(22)