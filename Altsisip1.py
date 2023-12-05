## Programmer: Matthew Altsisi
## Purpose: to calculate volume and surface area of pyramid
## Python version: 3.10.2

print ("Welcome to the Pyramid Calculator!")
print ("----------------------------------")

import math
from math import sqrt

def main ():
    a = float(input("What is the length? "))
    h = float(input("What is the heigth? "))
    print ("------------------------")
    print ("The length you entered was: " + str(a) + "'")
    print ("The height you entered was: " + str(h) + "'")
    print ("--------------------------------")
    volume = round(a ** 2 * h/3, 3)
##figured out that this is where the round function needs to be
##round (volume, 3)## this funtion isnt working, idk how to do it... Figured it out!
    print ("The volume of the pyramid is: " + str(volume) + "'")
    s = round(sqrt(h ** 2 + (a/2) ** 2), 3)
## round (s, 3) again this is old code before
## print (s) just to check math is right
    surface = round(s * (a/2), 3)
##print (surface) again just checking math
    print ("The surface area of the triangles is: " + str(float(surface * 4)) + "'")
    print ("---------------------------------------------")
## print (float(surface * 4)) old code before i figured out how to print on one line
while True:
    main()
    question = input ("Do you want to try another set? (Y) (N) " )
    if question.upper() == "Y":
        print ("Lets go!")
    elif question.upper() == "N":
        print ("Goodbye!")
        break
## figured out how to repeat everything. Still dont know how to fool proof it.

##if question != ("Y" , "N"):
   ## print (input ("Try again! (Y) (N) "))
##input ("Do you want to try another set? (Y) (N) ")

##figured out how to repeat it, but now i dont know how to make it "Dumb- proof" incase someone doesnt enter a number.
    
##Wanted to try and repeat the function again, but didnt know how. Might try again later.
