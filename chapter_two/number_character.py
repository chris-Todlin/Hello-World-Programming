""" 
    Count the number of characters in a string by the user
    Enter the string - Priompt the user to enter the string
    Dispay the string with the character
"""

# the function 
def countStringChars():
    try:
        # prompt the user to enter the string
        str1 = input("What is the input string?    ")
    
        # print the output already
        print(str1 + " has " + str(len(str1)) + " characters.")
    except Exception as e:
        print("An error occured : " + str(e))
        
# trial cases
countStringChars()