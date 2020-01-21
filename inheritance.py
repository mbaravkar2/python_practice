class f1:
    def feature(self):
        print("12gb snapdragon 645")
class f2(f1):
    def feature1(self):
        print("8gb snapdragon 450")

class f3(f2):
    def feature3(self):
        print("16gb snapdragon 885")

d1 = f3()
d1.feature()
d1.feature1()
d1.feature3()
