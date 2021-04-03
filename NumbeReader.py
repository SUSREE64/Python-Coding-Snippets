''' 
    This program converts given 4 digit integer to its equivalnet word format
    Author : Sree , Date : 3rd April 2021.
'''
## Global spcace to declare the functions and variables:
def two_digit(lst):
    first = digit_dict.get(lst[0]*10)
    second = digit_dict.get(lst[1])
    out_string = first +" "+ second
    return(out_string) 
digit_dict = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight',               9:'nine', 10:'ten',11:'eleven', 12 : 'twelve', 13:'thirteen', 14:'fourteen',                            15:'fifteen', 16:'sixteen', 17: 'seventeen',18:'eighteen', 19:'nineteen', 20:'twenty',                  30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
              80:'eighty', 90 : 'ninety'}    

def main():
    # Getting input from the key board : You can add validation later
    while True:
      try:
        num = int(input("Please give a number below 1000 : "))
        if (num>1000):
          print("Sorry ! enter a number below 1000 : ")          
          #continue
        else:
          break  
      except ValueError:
        print("Sorry, Did not under stand the input.")
        #better try again... Return to the start of the loop
        continue
      else:
        break   
    
    
    
    
    num = int(input("Please give a number below 1000 : "))
    
    print("Given number is : ", num)
    # Definfe necessary dictionaries
    keys = list(digit_dict.keys())
    if (num in keys):
      print(digit_dict.get(num))
    else:
         ## Get the individual digits of the number
        lst_num = [int(i) for i in list(str(num))]
         #two digit number : 
        if len(lst_num)==2:
          print(two_digit(lst_num)) 
        ## three digit number
        if len(lst_num)==3:
           hund_position = lst_num[0]
           first_step = digit_dict.get(hund_position)+ ' '+ 'hundred'
           ## formating final output  
           if (lst_num[1:2] in keys):
              tail_step = digit_dict.get(lst_num[1:2])
           else:      
              tail_step = two_digit(lst_num[1:])  
           if (lst_num[1] == 0 and lst_num[2]==0):
              print(first_step)
           else:  
              print(first_step + " " + tail_step)
# Entry point for the program
if __name__=="__main__":
    main()      
