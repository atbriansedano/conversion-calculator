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
        
            decimal = int(input("\n        Enter a decimal number: "))
 
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

            hexadecimal = input("\n        Enter a hexadecimal number: ")

            
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

            oct = input("\n        Enter a decimal number: ")

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

            binary = ''.join(str(x) for x in binary)
            print("""
    *-----------------------------------------------* 
        Octal: {}
        Octal to Decimal: {}               
        Octal to Binary: {}  
        Octal to Hexadecimal: {}
    *-----------------------------------------------*""".format(oct, decimal, 0, 0))
            break
           
        elif choice == "4":
            
            #------------------------------------------------------------#
            #                 Binary to Dec, Hex, Oct                    #
            #------------------------------------------------------------# 

            binary = input("\n        Enter a binary number: ")

            #------------------------------------------------------------#
            #                Binary to Decimal                           #
            #------------------------------------------------------------# 

            binArr = list(binary)
            decimal = 0

            n = len(binary)
            for x in binArr:
                decimal += (int(x) * (2**(n-1)))
                n -= 1 
            
            #------------------------------------------------------------#
            #                   Binary to Hex                            #
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
            #                   Binary to Oct                            #
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
        Binary: {}
        Binary to Decimal: {}               
        Binary to Hexadecimal: {}
        Binary to Octal: {}  
    *-----------------------------------------------*""".format(binary, decimal, hexadecimal, octal))

            break
        elif choice == "5":

            break
        else:
            print("\nERROR: Invalid Input")
        break
    print("     Back to main menu:\n")
    check = input("     y/n: ")
    if check == 'n':
        conversion_calculator()

def matrix_calculator():

    while(1):
        print("""
            *---------------------------------*
            |Welcome to the Matrix Calculator |
            *---------------------------------*

            To start please choose between a function:

            1. Addition
            2. Subtraction
            3. Multiplication
            4. Transpose
            5. Exit
                """)
        choice = input("        Your choice: ")

        if choice == '1':

            matSize = int(input("        Please enter a digit (2-4): "))

            print("\n**** NOTE: Matrix A and B will be a {}x{} matrix. ****\n".format(matSize, matSize))
            
            totalIndex = matSize * matSize

            print("Please fill in the matrix:  ({} digits for each matrix)\n\nMatrix A:\n".format(totalIndex))

            matA = []
            matB = []
            matC = []

            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matA.append(num)
                i+=1
            
            print("\nMatrix B:\n")
            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matB.append(num)
                i+=1
            
            i = 0
            while i < totalIndex:
                num = matA[i] + matB[i]
                matC.append(num)
                i+=1
           
               
            if matSize == 2:

                print("\n*---------------------*\n    A - B = C:\n")
                print("     | {} {} |\n     | {} {} |".format(matC[0],matC[1],matC[2],matC[3]))
                print("*---------------------*\n")
            
            if matSize == 3:
   
                print("\n*---------------------*\n    A + B = C:\n")
                print("     | {} {} {} |\n     | {} {} {} |\n     | {} {} {} |".format(matC[0],matC[1],matC[2],matC[3],matC[4],matC[5],matC[6],matC[7],matC[8]))
                print("*---------------------*\n")
            
            if matSize == 4:

                print("\n*---------------------*\n    A + B = C:\n")
                print("     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |".format(matC[0],
                matC[1],matC[2],matC[3],matC[4],matC[5],matC[6],matC[7],matC[8],matC[9],
                matC[10],matC[11],matC[12],matC[13],matC[14],matC[15]))
                print("*---------------------*\n")
        
        if choice == '2':

            matSize = int(input("        Please enter a digit (2-4): "))

            print("\n**** NOTE: Matrix A and B will be a {}x{} matrix. ****\n".format(matSize, matSize))
            
            totalIndex = matSize * matSize

            print("Please fill in the matrix:  ({} digits for each matrix)\n\nMatrix A:\n".format(totalIndex))

            matA = []
            matB = []
            matC = []

            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matA.append(num)
                i+=1
            
            print("\nMatrix B:\n")
            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matB.append(num)
                i+=1
            
            i = 0
            while i < totalIndex:
                num = matA[i] - matB[i]
                matC.append(num)
                i+=1
           
            if matSize == 2:

                print("\n*---------------------*\n    A - B = C:\n")
                print("     | {} {} |\n     | {} {} |".format(matC[0],matC[1],matC[2],matC[3]))
                print("*---------------------*\n")

            if matSize == 3:
   
                print("\n*---------------------*\n    A - B = C:\n")
                print("     | {} {} {} |\n     | {} {} {} |\n     | {} {} {} |".format(matC[0],matC[1],matC[2],matC[3],matC[4],matC[5],matC[6],matC[7],matC[8]))
                print("*---------------------*\n")
            
            if matSize == 4:

                print("\n*---------------------*\n    A - B = C:\n")
                print("     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |".format(matC[0],
                matC[1],matC[2],matC[3],matC[4],matC[5],matC[6],matC[7],matC[8],matC[9],
                matC[10],matC[11],matC[12],matC[13],matC[14],matC[15]))
                print("*---------------------*\n")
        
        if choice == '3':
            
            matSize = int(input("        Please enter a digit (2-4): "))

            print("\n**** NOTE: Matrix A and B will be a {}x{} matrix.**** \n".format(matSize, matSize))
            
            totalIndex = matSize * matSize

            print("Please fill in the matrix:  ({} digits for each matrix)\n\nMatrix A:\n".format(totalIndex))

            matA = []
            matB = []
            matC = []

            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matA.append(num)
                i+=1
            
            print("\nMatrix B:\n")
            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matB.append(num)
                i+=1
            
            if matSize == 2:
                index = matA[0]*matB[0]+matA[1]*matB[2]
                matC.append(index)
                index = matA[0]*matB[1]+matA[1]*matB[3]
                matC.append(index)
                index = matA[2]*matB[0]+matA[3]*matB[2]
                matC.append(index)
                index = matA[2]*matB[1]+matA[3]*matB[3]
                matC.append(index)

                print("\n*---------------------*\n    A x B = C:\n")
                print("     | {} {} |\n     | {} {} |".format(matC[0],matC[1],matC[2],matC[3]))
                print("*---------------------*\n")
            
            if matSize == 3:
                index = (matA[0]*matB[0])+(matA[1]*matB[3])+(matA[2]*matB[6])
                matC.append(index)
                index = (matA[0]*matB[1])+(matA[1]*matB[4])+(matA[2]*matB[7])
                matC.append(index)
                index = (matA[0]*matB[2])+(matA[1]*matB[5])+(matA[2]*matB[8])
                matC.append(index)

                index = (matA[3]*matB[0])+(matA[4]*matB[3])+(matA[5]*matB[6])
                matC.append(index)
                index = (matA[3]*matB[1])+(matA[4]*matB[4])+(matA[5]*matB[7])
                matC.append(index)
                index = (matA[3]*matB[2])+(matA[4]*matB[5])+(matA[5]*matB[8])
                matC.append(index)

                index = (matA[6]*matB[0])+(matA[7]*matB[3])+(matA[8]*matB[6])
                matC.append(index)
                index = (matA[6]*matB[1])+(matA[7]*matB[4])+(matA[8]*matB[7])
                matC.append(index)
                index = (matA[6]*matB[2])+(matA[7]*matB[5])+(matA[8]*matB[8])
                matC.append(index)

                print("\n*---------------------*\n    A x B = C:\n")
                print("     | {} {} {} |\n     | {} {} {} |\n     | {} {} {} |".format(matC[0],matC[1],matC[2],matC[3],matC[4],matC[5],matC[6],matC[7],matC[8]))
                print("*---------------------*\n")
            
            if matSize == 4:
                index = (matA[0]*matB[0])+(matA[1]*matB[4])+(matA[2]*matB[8])+(matA[3]+matB[12])
                matC.append(index)
                index = (matA[0]*matB[1])+(matA[1]*matB[5])+(matA[2]*matB[9])+(matA[3]+matB[13])
                matC.append(index)
                index = (matA[0]*matB[2])+(matA[1]*matB[6])+(matA[2]*matB[10])+(matA[3]+matB[14])
                matC.append(index)
                index = (matA[0]*matB[3])+(matA[1]*matB[7])+(matA[2]*matB[11])+(matA[3]+matB[15])
                matC.append(index)

                index = (matA[4]*matB[0])+(matA[5]*matB[4])+(matA[6]*matB[8])+(matA[7]+matB[12])
                matC.append(index)
                index = (matA[4]*matB[1])+(matA[5]*matB[5])+(matA[6]*matB[9])+(matA[7]+matB[13])
                matC.append(index)
                index = (matA[4]*matB[2])+(matA[5]*matB[6])+(matA[6]*matB[10])+(matA[7]+matB[14])
                matC.append(index)
                index = (matA[4]*matB[3])+(matA[5]*matB[7])+(matA[6]*matB[11])+(matA[7]+matB[15])
                matC.append(index)

                index = (matA[8]*matB[0])+(matA[9]*matB[4])+(matA[10]*matB[8])+(matA[11]+matB[12])
                matC.append(index)
                index = (matA[8]*matB[1])+(matA[9]*matB[5])+(matA[10]*matB[9])+(matA[11]+matB[13])
                matC.append(index)
                index = (matA[8]*matB[2])+(matA[9]*matB[6])+(matA[10]*matB[10])+(matA[11]+matB[14])
                matC.append(index)
                index = (matA[8]*matB[3])+(matA[9]*matB[7])+(matA[10]*matB[11])+(matA[11]+matB[15])
                matC.append(index)

                index = (matA[12]*matB[0])+(matA[13]*matB[4])+(matA[14]*matB[8])+(matA[15]+matB[12])
                matC.append(index)
                index = (matA[12]*matB[1])+(matA[13]*matB[5])+(matA[14]*matB[9])+(matA[15]+matB[13])
                matC.append(index)
                index = (matA[12]*matB[2])+(matA[13]*matB[6])+(matA[14]*matB[10])+(matA[15]+matB[14])
                matC.append(index)
                index = (matA[12]*matB[3])+(matA[13]*matB[7])+(matA[14]*matB[11])+(matA[15]+matB[15])
                matC.append(index)

                print("\n*---------------------*\n    A x B = C:\n")
                print("     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |".format(matC[0],
                matC[1],matC[2],matC[3],matC[4],matC[5],matC[6],matC[7],matC[8],matC[9],
                matC[10],matC[11],matC[12],matC[13],matC[14],matC[15]))
                print("*---------------------*\n")
        
        elif choice == '4':
            
            matSize = int(input("        Please enter a digit (2-4): "))

            print("\n**** NOTE: Matrix will be a {}x{} matrix. ****\n".format(matSize, matSize))
            
            totalIndex = matSize * matSize

            print("Please fill in the matrix:  ({} digits for each matrix)\n\nMatrix A:\n".format(totalIndex))

            matA = []
            matC = []

            i = 0
            while i < totalIndex:
                num = int(input("Enter: "))
                matA.append(num)
                i+=1
            
            if matSize == 2:
                print("\n*---------------------*\n    Orignal Matrix:\n")
                print("     | {} {} |\n     | {} {} |".format(matA[0],matA[1],matA[2],matA[3]))
                print("*---------------------*\n    Transposed Matrix:")
                print("     | {} {} |\n     | {} {} |".format(matA[0],matA[2],matA[1],matA[3]))
            
            if matSize == 3:
                print("\n*---------------------*\n    Orignal Matrix:\n")
                print("     | {} {} {} |\n     | {} {} {} |\n     | {} {} {} |".format(matA[0],matA[1],matA[2],matA[3],matA[4],matA[5], matA[6], matA[7],matA[8]))
                print("*---------------------*\n    Transposed Matrix:")
                print("     | {} {} {} |\n     | {} {} {} |\n     | {} {} {} |".format(matA[0],matA[3],matA[6],matA[1],matA[4],matA[7],matA[2],matA[5],matA[8]))
            
            if matSize == 4:
                print("\n*---------------------*\n    Orignal Matrix:\n")
                print("     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |".format(matA[0],
                matA[1],matA[2],matA[3],matA[4],matA[5], matA[6], matA[7],matA[8],
                matA[9],matA[10],matA[11],matA[12],matA[13], matA[14], matA[15]))
                print("*---------------------*\n    Transposed Matrix:\n")
                print("     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |\n     | {} {} {} {} |".format(matA[0],
                matA[4],matA[8],matA[12],matA[1],matA[5], matA[9], matA[13],matA[2],matA[6],
                matA[10],matA[14],matA[3],matA[7],matA[11], matA[15]))

        elif choice == '5':
            break
        else:
            break
    print("     Back to main menu:\n")
    check = input("     y/n: ")
    if check == 'n':
        matrix_calculator()
    
def prime_calculator():  
    while(1):
        print("""
            *--------------------------------*
            |Welcome to the Prime Calculator |
            *--------------------------------*

            To start please choose between a function:

            1. Prime Number
            2. GCD
            3. LCM
            4. Exit
                """)
        choice = input("        Your choice: ")

        if choice == '1':

            #------------------------------------------------------------#
            #                  Prime Factorization                       #
            #------------------------------------------------------------#
            num1 = int(input("        Please enter a number: "))
            num2 = int(input ("        Please enter another number: "))

            num1Arr = []
            num2Arr = []

            while num1 % 2 == 0:
                num1Arr.append(2)
                num1 = num1/2

            for i in range(3, int(math.sqrt(num1))+1,2):
                while num1%i==0:
                    num1Arr.append(i)
                    num1 = num1/i
            if num1 > 2:
                num1Arr.append(num1)

            
            while num2 % 2 == 0:
                num2Arr.append(2)
                num2 = num2/2
                
            for i in range(3, int(math.sqrt(num2))+1,2):
                while num2%i==0:
                    num2Arr.append(i)
                    num2 = num2/i
            if num2 > 2:
                num2Arr.append(num2)

            print("""
    *-------------------------------------------------------* 
        Prime Factorization of Number 1: {}
        Prime Factorization of Number 2: {}
    *-------------------------------------------------------*""".format(num1Arr,num2Arr))

        elif choice == '2':

            #------------------------------------------------------------#
            #                 Greates Common Denominator                 #
            #------------------------------------------------------------#

            num1 = int(input("        Please enter a number: "))
            num2 = int(input("        Please enter another number: "))

            if num1 == 0 or num2 == 0:
                print("ERROR: Both numbers must be non zero") 
                break
            if num1 == num2:
                print("""
    *-----------------------------------------------* 
        Greatest Common Denominator is: {}
    *-----------------------------------------------*""".format(num1))

            if num1 > num2:
                lesser = num2
            else:
                lesser = num1
            
            for x in range(1, lesser + 1):
                if (num1%x) == 0 and (num2%x) == 0:
                    result = x

            print("""
    *-----------------------------------------------* 
        Greatest Common Denominator is: {}
    *-----------------------------------------------*""".format(result))
        elif choice == '3':

            #------------------------------------------------------------#
            #                 Lowest Common Multiple                     #
            #------------------------------------------------------------#
            num1 = int(input("        Please enter a number: "))
            num2 = int(input("        Please enter another number: "))

            if num1 > num2:
                greater = num1
            else:
                greater = num2

            while(True): 
                if((greater % num1 == 0) and (greater % num2 == 0)):
                    result = greater
                    break
                greater += 1

            print("""
    *-----------------------------------------------* 
        Lowest Common Multiple is: {}
    *-----------------------------------------------*""".format(result))
            
        elif choice == '4':
            break
        else:
            print("ERROR: invalid input")
            break
    print("     Back to main menu:\n")
    check = input("     y/n: ")
    if check == 'n':
        prime_calculator()

def main():
    name = input("Please enter your name: ")

    while(1):
         
        print("""
        *-----------------------------------------------*
         Welcome {}, please choose an option below: 
        *-----------------------------------------------*

        1. Number Conversion Calculator
        2. Matrix Calculator
        3. Prime, GCD, LCM
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


        