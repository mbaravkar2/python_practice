year = int(input("Enter year: "))
if year/400:
    print("Is a leap year")
elif year/100:
    print("Is not leap year ")
elif year/4:
    print("Is a leap year.")
else:
    print("Is not leap year")
