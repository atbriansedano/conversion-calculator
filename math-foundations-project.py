from itertools import count
import math
import random
from sre_parse import HEXDIGITS

def conversion_calculator():
    
    while(1):
         
        print("""
        *-------------------------------------------*
        |Welcome to the Number Conversion Calculator|
        *-------------------------------------------*

        To start please choose a number type:

        1. Decimal
        2. Hexadecimal
        3. Octal
        4. Binary
        5. Exit
            """)
        
        choice = input("        Your choice: ")
        print("\n    *-----------------------------------------------*")

        if choice == "1":

            #------------------------------------------------------------#
            #                  Decimal to Bin, Hex, Oct                  #
            #------------------------------------------------------------#
        
            decimal = int(input("\n        Enter a decimal digit: "))
 
            #------------------------------------------------------------#
            #                  Decimal to binary                         #
            #------------------------------------------------------------#
            binary = []

            binRes = decimal

            while binRes >= 1:

                if (binRes % 2) == 0:
                    binary.append(0)            
                else:
                    binary.append(1)

                binRes = math.trunc(binRes/2)

            while len(binary) < 8:
              binary.append(0)
            
            binary.reverse()

            binary = ''.join(str(x) for x in binary)

            #------------------------------------------------------------#
            #                   Decimal to Hex                           #
            #------------------------------------------------------------#

            hexDigits = ['A', 'B', 'C', 'D', 'E', 'F']
            hexadecimal = []

            div = decimal

            while div >= 1:
                if div < 16:
                    if div > 9:
                        hexadecimal.append(hexDigits[div-10])
                    else:
                        hexadecimal.append(div)         
                    break
                rem = div%16
                div = math.trunc(div/16)
                if rem > 9:
                    hexadecimal.append(hexDigits[rem-10])
                else:
                    hexadecimal.append(rem)
                

            hexadecimal.reverse()
            hexadecimal = ''.join(str(x) for x in hexadecimal)

             #------------------------------------------------------------#
             #                   Decimal to Oct                           #
             #------------------------------------------------------------#
 
            octal = []

            divOct = decimal

            while divOct >= 1:
                if divOct < 8:
                    octal.append(divOct)         
                    break
                rem = divOct%8
                octal.append(rem)
                divOct = math.trunc(divOct/8)
                
            octal.reverse()
            octal = ''.join(str(x) for x in octal)

            print("""
    *-----------------------------------------------* 
        Decimal: {}
        Decimal to Binary: {}               
        Decimal to Hexadecimal: {} 
        Decimal to Octal: {}
    *-----------------------------------------------*""".format(decimal, binary, hexadecimal, octal))

            break

        elif choice == "2":

            #------------------------------------------------------------#
            #              Hexadecimal to Bin, Dec, Oct                  #
            #------------------------------------------------------------#

            hexadecimal = input("\n        Enter a hexadecimal digit: ")

            
             #------------------------------------------------------------#
             #                   Hex to Decimal                           #
             #------------------------------------------------------------#

            formatHex = []
            hexArray = list(hexadecimal)
            decimal = 0
            for x in hexArray:
                if x == 'A' or x == 'a':
                    formatHex.append(10)
                elif x == 'B' or x == 'b':
                    formatHex.append(11)
                elif x == 'C' or x == 'c':
                    formatHex.append(12)
                elif x == 'D' or x == 'd':
                    formatHex.append(13)
                elif x == 'E' or x == 'e':
                    formatHex.append(14)
                elif x == 'F' or x == 'f':
                    formatHex.append(15)
                else:
                    formatHex.append(int(x))
            print(formatHex)
            n = len(hexArray)
            for x in formatHex:
                decimal += (x * (16**(n-1)))
                n -= 1 
            
             #------------------------------------------------------------#
             #                   Hex to Binary                            #
             #------------------------------------------------------------#

             #FIX HEX TO BINARY, FISRT VARIABLE SHOWS FLIPPED   
            binHex = ['0000','0001', '0010', '0011', '0100', '0101', '0110', '0111', 
                      '1000', '1001', '1010', '1011', '1100','1101', '1110', '1111']
            
            binary = []

            for x in formatHex:
                binary.append(binHex[x])

            binary = ' '.join(str(x) for x in binary)

             #------------------------------------------------------------#
             #                   Hex to Octal                             #
             #------------------------------------------------------------#

            octal = []

            divOct = decimal

            while divOct >= 1:
                if divOct < 8:
                    octal.append(divOct)         
                    break
                rem = divOct%8
                octal.append(rem)
                divOct = math.trunc(divOct/8)
                
            octal.reverse()
            octal = ''.join(str(x) for x in octal)
    
                
            print("""
    *-----------------------------------------------* 
        Hexadecimal: {}
        Hexadecimal to Decimal: {}               
        Hexadecimal to Binary: {}  
        Hexadecimal to Octal: {}
    *-----------------------------------------------*""".format(hexadecimal, decimal, binary, octal))
            break
            
        elif choice == "3":

            #------------------------------------------------------------#
            #                 Octal to Bin, Dec, Hex                     #
            #------------------------------------------------------------#

            oct = input("\n        Enter a decimal digit: ")

            #------------------------------------------------------------#
            #                 Octal to Decimal                           #
            #------------------------------------------------------------#
            octArr = list(oct)
            decimal = 0
            n = len(octArr)
            for x in octArr:
                decimal += (int(x) * (8**(n-1)))
                n -= 1

            #------------------------------------------------------------#
            #                 Octal to Binary                            #
            #------------------------------------------------------------# 

            binary = []

            binRes = decimal

            while binRes >= 1:

                if (binRes % 2) == 0:
                    binary.append(0)            
                else:
                    binary.append(1)

                binRes = math.trunc(binRes/2)

            while len(binary) < 8:
              binary.append(0)
            
            binary.reverse()

            binary = ''.join(str(x) for x in binary)

            #------------------------------------------------------------#
            #                 Octal to Hexadecimal                       #
            #------------------------------------------------------------# 

            hexDigits = ['A', 'B', 'C', 'D', 'E', 'F']
            hexadecimal = []

            div = decimal

            while div >= 1:
                if div < 16:
                    if div > 9:
                        hexadecimal.append(hexDigits[div-10])
                    else:
                        hexadecimal.append(div)         
                    break
                rem = div%16
                div = math.trunc(div/16)
                if rem > 9:
                    hexadecimal.append(hexDigits[rem-10])
                else:
                    hexadecimal.append(rem)
                

            hexadecimal.reverse()
            hexadecimal = ''.join(str(x) for x in hexadecimal)

            print("""
    *-----------------------------------------------* 
        Octal: {}
        Octal to Decimal: {}               
        Octal to Binary: {}  
        Octal to Hexadecimal: {}
    *-----------------------------------------------*""".format(oct, decimal, binary, hexadecimal))
            break
           
        elif choice == "4":
            
            #------------------------------------------------------------#
            #                 Octal to Hexadecimal                       #
            #------------------------------------------------------------# 
            
            #Bin to Dec, Oct, Hex

            break
        elif choice == "5":
            
            break
        else:
            print("\nERROR: Invalid Input")
        break


def matrix_calculator():
    x=0
  
    
def prime_calculator():
    x=0


def main():
    name = input("Please enter your name: ")

    while(1):
         
        print("""
        *-------------------------------------------*
        |Welcome {}, please choose an option below: |
        *-------------------------------------------*

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
            print("\nERROR: Invalid Input")

    print("Thank you for giving us an A! Goodbye {}".format(name))

main()


        