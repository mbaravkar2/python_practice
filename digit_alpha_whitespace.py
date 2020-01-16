a = input("Enter the alphabate or digtit or whitespace: ")
if a.isupper() or a.islower():
    print("It is a alphabates")
elif a.isdigit()==True:
    print("It is a digit")
elif a.isspace():
    print("whitespace")
else:
    print("Invalid !!!")
