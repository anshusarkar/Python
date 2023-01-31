class C1:
    def method():
        print("This is a method call of class c1 method")
class C2(C1): #To inherite a method of a class the entire class get's passed as a parameter for that class
    def method():
        print("This is a method call of class C1 through C2 class")
a = C1
a.method()
a2 = C2
a2.method()