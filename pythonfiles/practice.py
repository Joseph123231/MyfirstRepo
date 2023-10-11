import math
variable1 = float(input("what's the radius of your circle "))
area = variable1**2 * math.pi
circumfrence = 2*math.pi*variable1
if variable1 > 0:
    print(" The area of your circle is ", area , " and the circumfrence is ", circumfrence,".")
if variable1 < 0:
    print("Please enter a number that is POSITIVE")
if variable1 == 0:
    print("Please use a number other then ZERO") 
if variable1 == None:
    print("Please enter a positive number")
    ### Need to make a scenario for input = nothing and input = letters ###


