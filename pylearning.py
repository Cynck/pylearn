print('\tHello World\n') #\t creates
#an indent, \n makes a new line, and
#using \ before a character will 
#treat it differently, for example:
print("This is a double quote \", yet still in a double \nquoted print because of the backslash.")
print("""There once was a movie star icon
who preferred to sleep with the light on.
They learned how to code
a device that sure glowed
and lit up the night using Python!\n""")

firstName = input("What is your first name?\n")
firstName = firstName.upper()
lastName = input("What is your last name?\n")
lastName = lastName.upper()
print("Hello, " + firstName + " " + lastName +"!")
country = input("What country do you live in?\n")
country = country.upper()
print("Hello, " + firstName + " " + lastName + ", from " + country + ".\n")
#find counts the number of values before<<< the string entered, including spaces, and starts from 0, and the number given
#is where the first value of the given string is found. So, for example, print(testingNewFunction.find("peoples")) returns
#, because it starts at 0 from the "H", and ends at the "p" of peoples
testingNewFunction = "Heello, peoples of this country!"
print("This is going to be a function test.")
print(testingNewFunction)
print("The following number will be the amount of spaces from 'H', starting with 0,\n to the place 'p' occupies.")
print(testingNewFunction.find("peoples")) 
#Python can figure out the value of a variable on the fly when doing something like postalCode = input("Please tell
#us your postal code: "), it'll know it's value based on what the user inputs, however, some languages will need for the below.
postalCode = " "
postalCode = input("Please tell us your postal code: ")
print(postalCode.upper() + " is your postal code.")
#If you're using a function, it always<<< requires parenthesis.
length = 3
height = 5
area = length*height
message = "The answer is:"
print(message)
print(area)
print("\n")

age = "42"
#^ 42 is a string
#child_age = age/2 <<< this code produces an error, as 42 is a string and can't be used in calculations.
age = "42"
child_Age = int(age)/2
print(age + " is the age of the parent, " + str(child_Age) + " is the age of the child, making the parent\n "\
    + str(child_Age) + " when the child was birthed.")
#Shows proper usage of int making something a str and str making something an int
print("5+5= " + str(5+5))
print("15-5= " + str(15-5))
print("5*3= " + str(15*3))
print("15/3= " + str(15/3))
print("3**2= " + str(3**2))
print("43%5= " + str(43%5))
#PEMDAS applies<<< order of operations
#THE + CONNECTS TWO STRINGS<<<
#Another way to show is to have a placeholder. Don't know entire differences between float/decimal (%f & %d),
#float seems to be attachable to dec, dec seems to be attachable to whole. Float has decimals and decimal is wholes.
area = 6
print("The area of the square is %f" % area)
print("The area of the square is %.0f" % area)
print("The area of the square is %.02f" % area)
print("The area of the square is %03d" % area)
print("The area of the square is %3d" % area)
#break
print("My favorite number is %d!" % 42)
#Putting %10d will make the number placed after 10 spaces, useful for money formatting and such.
print("The cost of a wheelbarrow is %10d" % 45)
print("This is a longer string length than the \nprevious, and the value is %12d" % 65)

#Another way of using "placeholders", more common and useful method.
print("My favorite number is {0:.0f}".format(72))
print("Here are three numbers, {0:d}, {1:d}, {2:d}.".format(5,10,97))
area=100
print("The area of the square is {0:f}.".format(area))
print("The area of the square is {0:.0f}.\n".format(area))

#loan calc challenge
P = input("Input Principal/Loan: ")
P = int(P)
J = input("Input your annual interest rate in decimal form: ")
J = float(J)/12
N = input("Total number of payments: ")
N = int(N)*-1
M = P * (J/(1-(1+J)**N))
print("Your monthly payment is " + str(M))
#end challenge
import datetime
print(datetime.date.today())
#can store dates in variables
currentDate = datetime.date.today()
print(currentDate)
print("Year: " + str(currentDate.year))
print("Month: " + str(currentDate.month))
print("Day: " + str(currentDate.day))
#formatting dates
#   %a=weekday abrv. %A=weekday full %d= zero-padded day number %b=month abrv. %B= month full
#   %m=zero-padded month number
print(currentDate.strftime("%d %b, %Y"))
print(currentDate.strftime("%d %B, %y"))
#Using dates in a sentence
testDate = datetime.datetime.strptime("Sep 14, 2015", "%b %d, %Y").date()
print(testDate)
#advanced
eventDate = datetime.datetime.strptime("2 September, Sunday", "%d %B, %A").date() #.date() specifies date in particular, where time would also be shown
print(eventDate.strftime("Please attend our event on the %dnd of %B, on %A."))
# LOOK ON PHONE PICTURES, TAKEN AT 5:35, LETS GET BACK TO CALCULATING DAYS UNTIL YOUR BIRTHDAY, MAKING
#STRINGS INTO DATES.
#
#
#
#
#
#
#
#
#
#
# working with time 
currentTime = datetime.datetime.now()
print(currentTime.time()) #.time() specifies time in particular, where date would also be shown
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(datetime.datetime.strftime(currentTime, "%I:%M:%S"))
testTime = datetime.datetime.strptime("9:35:0", "%I:%M:%S").time() #.time() specifies time in particular
print(testTime)
