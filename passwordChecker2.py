# for the sake of ths program, let us build a python project to check and validate some passwords from a set of requirements
# This project has been sucessfully complete

import numbers
import numpy
import symbol
import string


password = input("Enter a strong password: ")
pass_length = len(password) # this should actually return an integer



# let us use nested if statements to try and solve this problem

if (pass_length >= 8):
    def strong_pass():
        passw = ""
        for letters in password:
            if (letters.isupper()):
                passw += password
                
                
                if (letters.isalpha()):
                    passw += ""
                    
                    if (letters.isalnum() or letters.isupper()):
                        passw += ""

                    print("This is your new and unique password: ", "\r")
                    return passw
                    

        else:
            print("ERR, please retry a new password- because your password does not meet the standard requirements")
                

                
                    
    print(strong_pass())
else:
    print("oops! The password length should be a minimum of 8 characters")



        






































