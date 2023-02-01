#•	Fermat's Last Theorem Near Miss Calculator
#	main.py

#	N/A a list of any external files necessary to run your program
#	N/A a list of external files your program creates (If you list any external files, briefly explain what each of them contains.)
#	Shawn Amato / Nikos Palivos
#	shawnlamato@lewisu.edu / nikos.palivos@lewisu.edu
#	CPSC-4400-LT1
#   2/4/23
#	This program takes user input of a desired power and upper range. It then uses these numbers to calculate nears misses
#       of Fermat's Last Theorem, and displays the lowest found near miss
#	N/A any resources you used to complete the program (Always give credit where credit is due; for example,
#   	if you used a website to check on an algorithm, list that here.)

# function to close the application
def exitCondition():
    exitFlag = False # flag to control the loop on line 18

    while exitFlag == False:
        choice = input("Press Y to exit. ") # holds the user input for the given command.

        if choice.lower() == 'y':
            exitFlag = True



# function to get the user's desired power
def getPow():
    powFlag = False # controls the while loop on line 32

    # loop to ensure a proper number is entered
    while powFlag == False :
        inputPower =  input("Choose a power that is 3 or higher: ")  # hold the user input

        if inputPower.lstrip('-').isdigit() == False :
            print(inputPower + ' is not a number.')
        elif(int(inputPower) < 3 or int(inputPower) > 12):
            print(inputPower + ' is not a valid entry.')
        else:
            powFlag = True  # ending the while loop

    return inputPower

# function to get the user's desired upper bounds number
def getK():
    intFlag = False # controls the while loop on line 49

    # loop to ensure a proper number is entered
    while intFlag == False:
        inputIntLimit = input("Choose a number that is 11 or higher: ") # holds the user input
        if inputIntLimit.lstrip('-').isdigit() == False :
            print(inputIntLimit + ' is not a number.')

        elif int(inputIntLimit) < 11 :
            print(inputIntLimit + ' is not a valid entry.')
        else:
            intFlag = True  # ends the while loop
    return inputIntLimit


# function to generate the near misses
def missCalc(power, intLimit):

    lowest = [] # will hold the smallest near miss
    lowestMiss = 0 # holds the lowest miss so it can be used in print statements

    # loop for going through the x ** n values
    for x in range(10, int(intLimit) + 1) :


            # loop to go through the y ** n values
            for y in range(10,  int(intLimit) + 1 ):
                total = x ** int(power) + y ** int(power) # holds the value of x**n + y**n
                z = 1   # will be used in the while loop to determine z**n
                lower = 0 # will hold the z**n when it comes time to find if total - (z+1)**n or z**n - total is smaller

                # loop to go through the z ** n values
                while z ** int(power) <= total :
                    lower = z ** int(power)
                    z += 1 # incrementing z value

                upper = z ** int(power) # assigning (z+1)**n value to upper
                #print(f"x = {x}, y = {y}, z = {z}, lower = {lower}, total = {total}, upper = {upper})")
                if total - lower < upper - total :
                    z -= 1 #decrementing z by one to get correct z value for print statement
                    miss = total - lower
                    temp = miss / total
                else :
                    miss = upper - total
                    temp = miss / total


                if len(lowest) == 0 :
                    lowest.append(temp)
                    lowestMiss = miss
                    print(f"x = {x}, y = {y}, z = {z}, miss = {lowestMiss}, percentage = {lowest[0] * 100}")

                elif temp < lowest[0] :
                    lowest[0] = temp
                    lowestMiss = miss
                    print(f"x = {x}, y = {y}, z = {z}, miss = {lowestMiss}, percentage = {lowest[0] * 100}")

    print("")
    print(f"The smallest near miss is {lowestMiss} with a percentage of {lowest[0] * 100}")






print("Fermat's last theorem near miss calculator")
print("CPSC-44000-LT1: Software Engineering")
print("Assignment 1 - Group 4")
print()
print("Fermat's Theorem: x"+ chr(0x207F) + " + y" + chr(0x207F) + " <> z"+ chr(0x207F))
print()
power  = getPow()
intLimit  = getK()
missCalc(power, intLimit)
exitCondition()

