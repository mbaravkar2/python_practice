class calculator:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.y=b
    def setnum(self,x, y):
        self.a=x;
        self.b=y;
    def add(self):
        c=0
        c = self.a+self.b
        return c
    def sub(self):
        c=0
        
        c = self.a-self.b
        return c
    def mult(self):
        c=0
        c = self.a*self.b
        return c
    def div(self):
        c=0
        c = self.a/self.b
        return c

input1 = 0
cal = calculator()
while input1>=-1:
    print('''
               1.add
               2.sub
               3.mult
               4.div
               5.terminate
            ''')
    input1 = int(input("Enter your choice:"))
    if input1 == 5:
        break
    k = int(input("Enter first no:"))
    n = int(input("Enter secod no:"))
    cal.setnum(k, n)
    if input1 == 1:
        print("addition is",cal.add())
    elif input1 == 2:
        print("substraction is",cal.sub())
    elif input1 == 3:
        print("multiplication is",cal.mult())
    elif input1 == 4:
        print("division is",cal.div())
    elif input1 == 5:
        print("terminated")
        break
    else:
        print("Invalid!!")
