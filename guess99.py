i = 0
guess = 99
while i>=-1:
    a = int(input("Enter no to guess:"))
    i += 1

    if guess == a:
            print("Congratulation")
            break
    elif a > 99:
        print("Greater no")
    elif a == -1:
        break
    elif a < 99:
        print("Lesser no")
    
