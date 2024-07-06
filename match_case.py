# match case usage
a = 10
b = 20

user_input = input("Enter add or multiply: ")

match user_input:
    case 'add':
       print("Add  {},{}".format(a,b),"result = ", a+b)
    case 'multiply':
        print("Multply {},{}".format(a,b),"result = ", a*b)
