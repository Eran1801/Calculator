import re # A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern

print("Welcome to our Calculator")
print("When you want to reset the calculation just multiple by 0")
print("Type 'end' to exit\n")

previous = 0 # holds the result of the previously calculation
run = True

def perform_math () :
    global run # now we point to the 'run' global var outside the function, and change will be effect 
    global previous
    if previous == 0 : # if we just start to calaction 
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'end':
        run = False 
        print("Goodbye")
    else:
        equation = re.sub('[a-zA-z,/:{}=)""(&^%$#@!><\'_`;]', '', equation) # leaving just numbers and operators
        
        if previous == 0:
            previous = eval(equation)
        else:    
            previous = eval(str(previous)+equation) # make the calaction

while run :
    perform_math()

