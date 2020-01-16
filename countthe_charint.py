import sys
i = 0
while i >= -1:
    i = i + 1;
    input1 = input("Enter the upper or lower or digit to count : ")
    if input1.islower():
        print("It is lowercase")
        print(len(input1))
    elif (input1.isupper()==True):
        print("It is Uppercase")
        print("count of the case is: ",len(input1))
    elif input1.isdigit():
        print("It is a Digit")
        print(len(input1))
    elif i == -1 or input1 == -1:
        break
