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
digit_dict = {0:'zero',1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight',
              9:'Nine', 10:'Ten',11:'Eleven', 12 : 'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen',
              16:'Sixteen', 17: 'Seventeen',18:'Eighteen', 19:'Nineteen', 20:'Twenty',
              30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
              80:'Eighty', 90 : 'Ninety'}    

def main():
    
    
    
    
    # Getting input from the key board 
    while True:
      try:
        num = int(input("Please give a number below 1000 : "))
      except ValueError:
          print("Sorry, Did not under stand the input.")
          continue
      else:
        if (num>=1000):
          print("Sorry ! enter a number below 1000 : ")          
          #continue
        else:
          break 
    
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
           first_step = digit_dict.get(hund_position)+ ' '+ 'Hundred'
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
