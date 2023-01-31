class C1:
    def method():
        print("This is a method call of class C1 through C2 class")
class C2(C1): #To inherite a method of a class the entire class get's passed as a parameter for that class

    pass

a = C2
a.method()