input1 = 0
def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def mult(a,b):
    c = a*b
    return c
def div(a,b):
    c = a/b
    return c

while input1>=-1:
    print("""
1.add
2.sub
3.mult
4.divide
5.quit
    """)
    
    input1 = int(input("Enter your choice:"))
    if input1 == 5:
        print("Terminated!!!!
              ")
        break
    a = int(input("Enter first no:"))
    b = int(input("Enter secod no:"))
    
    if input1 == 1:
        print("addition is",add(a,b))
    elif input1 == 2:
        print("substraction is",sub(a,b))
    elif input1 == 3:
        print("multiplication is",mult(a,b))
    elif input1 == 4:
        print("division is",div(a,b))
    else:
        print("Invalid!!")
