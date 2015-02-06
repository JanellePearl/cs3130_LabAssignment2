#CS3130 re lab/ Lab 2 Assignment
#Janelle Montgomery
#A python program that will read a phone number with a three-digit area code,
#and a seven digit local code. It will then accept it as long as their is 10 digits
#whether there is punctuation(-()) or not. The code aims to read the phone number
#using regular expressions
#Main program

import re

def main():
    phone()

#reads user input phone number, parses, and catches character errors
def phone():
    print('--')
    print('Phone Number\n')
    while True:
        print('Enter phone number: ')
        number=input()
            
        if len(number)<10:
            print('Please enter a valid 10 digit phone number.\n')

        else:
            try:
                phone=re.match(r'[(]*(\d{3})[) -]*(\d{3})[) -]*(\d{4})',number)
                one,two,three = phone.groups()
                print('Number is: (' + one + ') ' + two + ' ' + three + '\n')

            except AttributeError as ohno:
                print('Characters other than digits, hyphens, space and parentheses detected\n')
            

main()



