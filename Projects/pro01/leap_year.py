a = int(input("Enter a year which you need to find, Wheather is Leap year or Not:"))

if  a % 4 == 0:
    if  a % 100 == 0:
        if a % 400 == 0:
            print(a, "Is leap year")
        else:
            print(a, "Not a Leap year")
    else:
        print(a, "Is a leap year")
else:
    print(a, "Is a not leap year")