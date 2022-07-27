# This function adds multiple integers, concatenates strings, adds floaters.
# Dissimilar types of arguments are not allowed
# Arguments can be any number 

def calculate(*args):
    # error falg if all the elements are not similar ( either strings or numbers)
    for x in range (1, len(args)):
        if type(args[x])!= type(args[x-1]):
            return ("Sorry  - mixed types arguments not allowed")
    str_output = ''
    num_output = 0
    if (type(args[0]) == str):
        for item in args:
            str_output = str_output+item
        return(str_output) 
        
    if type(args[0] == 'int' or args[0] == 'float') :
        return (sum(args))
        
#Unit testing, test case all strings
print(calculate ("sree" , "nivas"))
#all integers
print(calculate(33,32))
#single integer
print(calculate(32))
#single string
print(calculate('sree'))
#mixed types
print(calculate('sree', 32))
#mixed types
print(calculate('sree', 32.2))
print(calculate(32, 32.3))
## all flolats
print(calculate(32.4, 33.0))
