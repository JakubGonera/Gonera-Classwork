count = 0

while count < 3:
    print("Input password")
    str = input()
    if str == "Tues1212":
        print("Password accepted")
        break
    else:
        print("Password rejected")
    count += 1