#import system
import sys

def main():
    #ask the user to input a first and second number
    #remember to store as int
    l = int(input("Give me the first number: "))
    b = int(input("Give me the second number: "))
    
    #set the protocol for getting the perimeter and area
    perimeter = 2 * (l + b )
    area = l * b
    
    #print out the results
    print("The perimeter of the two numbers is " , perimeter)
    print("The area of the two given numbers is " , area)

#call it    
if __name__ == "__main__":
    main()
    
