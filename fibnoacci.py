#first n fibnoacci numbers
# in fibnoacci numbers series, last digit is the sum of previous two last numbers. 
#[1,1,2,3,5,8,13,21,34,55....]
def getfiboacci(count):
    result = [1,1]
    while  (count >= len(result)):
        result.append(result[-1]+result[-2])
    return(result)
print(getfiboacci(10))  
