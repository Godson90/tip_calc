#!/usr/bin/python3

# Adesola A
# April 6 2020
# Tip calculator
# This program calculate the tip amount for the cost of meal


Repeat = True

while Repeat:
    Cost = float(input("Please enter cost of meal (Enter negative number to quit):"))
    if(Cost<0):
        print("Thank you for using the Tip calculator")
        break
        
    Percent = 10
    for tip in range(Percent,26,5):
        print("{0}% tip = ${1}".format(tip,tip*Cost/100))

                  

