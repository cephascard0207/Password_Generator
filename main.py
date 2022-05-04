import random
import string

#Start_Welcome
print('''
 _            _    
| |          | |   
| | ___   ___| | __
| |/ _ \ / __| |/ /
| | (_) | (__|   < 
|_|\___/ \___|_|\_\
''')
print("\nWelcome to the Password Generator!")
print("Created by Cephas Cardozo")
print("Developed using Python\n")

#password_digit_variables
password2 = random.randint(10,99)
password3 = random.randint(100,999)
password4 = random.randint(1000,9999)
password5 = random.randint(10000,99999)
password6 = random.randint(100000,999999)

#password_alphabet_variables
alphabets = random.choice(string.ascii_letters + string.digits)

#NOTICE
print("Alpha Numeric Code has not yet been created, its under development!\n-------------------------------------------------------------------\n")
  
#user_input_variable
user_main = input("Do you want a Numeric or Alpha-Numeric Password? \n\nType N for numeric or AN for Alpha Numeric, \n\nType here : ").lower()


#CONDITIONS

#user_input_passType
if user_main == "n":
  user_choice = int(input("How many digits do you want your password to be generated \n with? : 2, 3, 4, 5, 6\n\nType here : "))

elif user_main == "an":
      print("Alpha Numeric Code has not yet been created, its under development!")
  #alpha_num = input("How many alphanumeric digits do you want your password to be generated \n with? : 2, 3, 4, 5, 6\n\nType here : ")
  
#AlphaNumeric_Conditionals
#Coming Soon!


#Numeric_Conditionals
if user_choice == 2:
  print(password2)
elif user_choice == 3:
  print(password3)
elif user_choice == 4:
  print(password4)
elif user_choice == 5:
  print(password5)
elif user_choice == 6:
  print(password6)

