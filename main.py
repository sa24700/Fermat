#•	Fermat's last theorem near miss calculator
#	main.py
#	N/A a list of any external files necessary to run your program
#	N/A a list of external files your program creates (If you list any external files, briefly explain what each of them contains.)
#	Shawn Amato
#	shawnlamato@lewisu.edu
#	CPSC-4400-LT1
#   2/4/23
#	This program takes user input of a desired power and upper range. It then uses these numbers to calculate nears misses
#       of Fermat's Last Theorem, and displays the lowest found near miss
#	N/A any resources you used to complete the program (Always give credit where credit is due; for example,
#   	if you used a website to check on an algorithm, list that here.)

# function to get the user's desired power
def getPow():
    powFlag = False # controls the while loop on line 18

    # loop to ensure a proper number is entered
    while powFlag == False :
        print("please choose a power that is 3 or higher.")
        inputPower =   input()  # hold the user input

        if inputPower.isnumeric() == False :
            print(inputPower + ' is not a number.')
        elif(int(inputPower) < 3 or int(inputPower) > 12):
            print(inputPower + ' is not a valid entry.')
        else:
            powFlag = True  # ending the while loop

    print(inputPower)
    return inputPower

# function to get the user's desired upper bounds number
def getK():
    intFlag = False # controls the while loop on line 38

    # loop to ensure a proper number is entered
    while intFlag == False:
        print("please choose a number, higher than 11, to search to .")
        inputIntLimit = input() # holds the user input
        if inputIntLimit.isnumeric() == False :
            print(inputIntLimit + ' is not a number.')

        elif int(inputIntLimit) < 11 :
            print(inputIntLimit + ' is not a valid entry.')
        else:
            intFlag = True  # ends the while loop
    print(inputIntLimit)
    return inputIntLimit


# function to generate the near misses
def missCalc(power, intLimit):

    lowest = [] # will hold the smallest near miss


    # loop for going through the x ** n values
    for x in range(10, int(intLimit)) :


            # loop to go through the y ** n values
            for y in range(10,  int(intLimit)):
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
                    print(f"x = {x}, y = {y}, z = {z}, miss = {miss}, percentage = {lowest[0] * 100}")

                elif temp < lowest[0] :
                    lowest[0] = temp
                    print(f"x = {x}, y = {y}, z = {z}, miss = {miss}, percentage = { lowest[0] * 100}")




print("Fermat's Theorem: x"+ chr(0x207F) + " + y" + chr(0x207F) + " != z"+ chr(0x207F))
power  = getPow()
intLimit  = getK()
missCalc(power, intLimit)


