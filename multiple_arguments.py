# functions with variable number of arguments
# *args indicates that the function can have variable arguments number
# instead of *args, we can use any word that starts with * : for example *sree
def total_all(*args):
    return(sum(args))
    
print(total_all(2,3,4,5))  # 4 arguments -- 14
print(total_all(100, 200)) # 2arguments -- 300

"""
This is also valid
def total_all(*sree):
    return(sum(sree))
    
print(total_all(2,3,4,5))  # 4 arguments
print(total_all(100, 200)) # 2arguments



""" 
