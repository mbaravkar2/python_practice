a = input('Enter the upper , lower , digit : ')
b = a.upper()
h = a.lower()
is_digit = True
if(a.isupper()):
    print("Upper Case")
elif (a.islower()):
    print("LowerCase")
#if b == a:
 #   print("Upper Character")
#elif h == a:
 #   print("Lower Character")
elif a.isdigit()==True:
    print("digit")
