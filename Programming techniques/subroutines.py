#Q1
def multiples(table, startNum, endNum, pupilName):
    print("Hi,", pupilName, "... here is your times table")
    for i in range(startNum, endNum + 1):
        print(table, "x", i, "=", table * i)
    #next
#end procedure

print("What is your name?")
name = input()

print("Enter times table, start number and end number")

table = int(input())
startNum = int(input())
endNum = int(input())
multiples(table, startNum, endNum, name)

#Q3
def getPword(attempt):
    if attempt == 1:
        print("Enter password:")
    #endif
    else:
        print("Enter password again:")
    #endelse
    p = input()
    while len(p) < 6 or len(p) > 8:
        print("Error. Password must be 6 to 8 characters long")
        if attempt == 1:
            print("Enter password:")
        #endif
        else:
            print("Enter password again:")
        #endelse
        p = input()
    #next
    return p
#end function

p1 = getPword(1)
p2 = getPword(2)
while p1 != p2:
    print("Error - passwords do not match")
    p1 = getPword(1)
    p2 = getPword(2)
#next
print("Password change successfull")

#Q4
def parkACar(carPark):
    for x in carPark:
        for y in x:
            y.value = "empty"
        #next
    #next
#end procedure

def parkACar(carPark):
    print("Enter registration number and grid reference")
    reg = input()
    x = int(input())
    y = int(input())
    while carPark[x][y] != "empty":
        print("Place already taken, input grid reference number again")
        x = int(input())
        y = int(input())
    #next
    carPark[x][y] = reg
#end procedure

def removeACar(carPark):
    print("Input grid reference number")
    x = int(input())
    y = int(input())
    carPark[x][y] = "empty"
#end procedure

def displayCarParkGrid(carPark):
    for x in carPark:
        for y in x:
            print(y, end='')
        #next
        print('\n')
    #next
#end procedure