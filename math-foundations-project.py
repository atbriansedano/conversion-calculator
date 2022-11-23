from itertools import count
import random

def conversion_calculator():
    x=0

def matrix_calculator():
    x=0
  
    
def prime_calculator():
    x=0

def main():

    name = input("Please enter your name: ")

    while(1):
         
        print("""
        Hello, {}, please choose an option below:

        1. Number Conversion Calculator
        2. Matrix Calculator
        3. Prime, GCD, LCD
        4. Exit

        """.format(name))

        choice = input("Your choice: ")

        if choice == "1":
            conversion_calculator()
        elif choice == "2":
            matrix_calculator()
        elif choice == "3":
            prime_calculator()
        elif choice == "4":
            break
        else:
            print("ERROR: Invalid Input")

    print("Thank you for giving us an A! Goodbye {}".format(name))


            



        
        
        
