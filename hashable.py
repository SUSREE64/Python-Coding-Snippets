#A list of various data types and thier hashablity check and hash values. 
collection = [{'a':1, 'b':2}, 100, 1.5, "hello", [1,2,3], (2,3), "s", True, False, range(10), 3+10j, None]

for element in collection:
    print(element, type(element))
    try:
        hash(element)
    except Exception as er:
        print(er)
    else:
        print('Hashable and hashvalue is ', hash(element))
    print("-----------")
