class C1:
    def method():
       pass
class C2(C1):
    def method():
        print("This is a method call of class C1 through C2 class")
a = C2
a.method()