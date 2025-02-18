#This is a simple program that checks whether a given year is a leap year
Year=int(input("Enter the year you want to verify\n"))
if Year % 4==0:
    if Year % 100==0:
        if Year % 400 ==0:
            print(f"The year {Year} is a leap year")
        else:
            print(f"The year {Year} is not a leap year")
    else:
        print(f"The year {Year} is a leap year")
else:
    print(f"The year {Year} is not leap year")        