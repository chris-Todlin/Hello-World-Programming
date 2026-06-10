""" 
    This is the classical hello world challange
    But here we are using the name of the user inputted
"""

def helloWorld():
    # askf- for the name
    print("What is your name? ")
    name = input() # save the name 
    
    # print the output using concatinations
    print("Hello, " + name + ", nice to meet you!")
    
# This is the trial case
helloWorld()

# imporving that of the name is not there it default to guest
def helloWorld2():
    print("What is your name? ")
    name = input() or "guest" # save the name or the guest 
    
    # print the output using concatinations
    print("Hello, " + ", nice to meet you!")
    
helloWorld2()

# imporving that there is no variable used
def helloWorld3():
    print("What is your name? ")
    
    # print the output using concatinations
    print("Hello, " + input() + ", nice to meet you!")

helloWorld3()