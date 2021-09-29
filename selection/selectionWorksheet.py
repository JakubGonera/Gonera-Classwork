#Q2

print("Input pupil age")
age = input()

if age >= 10 and age < 19:
    print("Valid pupil age")
#endif
else:
    print("Invalid input: enter a value from 11 to 18")
#end else

#Q3
print("Input value of your order")
value = input()
print("Do you want next day delivery (Y/N)?")
nextDay = input()
if nextDay == 'Y':
    print("Your delivery charge is £5.00 and overall total charge is £", value + 5)
#endif
else:
    if value < 15:
        print("Your delivery charge is £3.50 and overall total charge is £", value + 3.5)
    #endif
    else:
        print("Your delivery charge is £0.00 and overall total charge is £", value)
    #end else
#end else

#Q4
print("Input exam score")
exam = input()
print("Input attendance percentage")
attendance = input()

grade = ''

if attendance > 90:
    if exam > 90:
            grade = 'A'
    #endif
    elif exam > 80:
        grade = 'B'
    #end elif
    elif exam > 70:
        grade = 'C'
    #end elif
    else:
        grade = 'F'
    #end else
#end if
else:
	grade = 'F'
#end else

if grade == 'F':
	print("Fail")
#end if
else:
	print("Grade =", grade)
#end else

#Q5 A

print("Is alarm on? (ON/OFF)")
trigger = input()
movementGround = input()
movementFirst = input()

if trigger == "ON":
    if movementGround:
        print("Intruder on ground floor")
    #end if
    if movementFirst: 
        print("Intruder on first floor")
    #end if
#end if

#Q5 B

print("Is alarm on? (ON/OFF)")
trigger = input()
movementGround = input()
movementFirst = input()

if trigger == "ON" and (movementFirst or movementGround):
    print("Intruder on ground floor")
#end if

#Q6

print("Choose car: \n 1: Economy Car \n2: Saloon Car \nSports Car")
car = input()
if car != 1 and car != 2 and car != 3:
	print("Invalid choice")
#end if
else:
    print("Do you want to proceed? (Y/N)")
    choice = input()
    if choice == "Y":
        print("You chosed to proceed.")
    #end if
    else:
        print("You chose to cancel.")
    #end else
#end if

#Q7

print("Do you have temperature?(Y/N)")
temp = input()
if temp == "Y":
    print("Do you have sore throat?(Y/N)")
    throat = input()
    if throat == "Y":
        print("You may have a throat infection")
    #end if
    else:
        print("Do you have cough?(Y/N)")
        cough = input()
        if cough == "Y":
            print("You have a chest infection")
        #end if
        else:
            print("You have a fever")
        #end else
    #end else
#end if
else:
    print("You don’t have a temperature")
#end else

