class A_class :# --------------------------------------------------->|
    def method(self):                               #                |
        print("\nThis method belongs to A_class\n") #                |
                                                    #                |
                                                    #                |
class B_class(A_class):#<--------------------------------------------|
    def method(self):                               #                |
        print(A_class().method(), "But called in B class \n")#      |   
                                                    #                |               
class C_class(A_class):#<--------------------------------------------|              
    def method(self):                               #                |
        print(A_class().method(), "But called in C class \n")#      |
                                                    #                |         
class D_class(A_class):#<--------------------------------------------|
    def method(self):                               #                |
        print(A_class().method(), "But called in D class \n")#      |
                                                    #                |         
                                                    #                |     
class E_class(A_class):#<--------------------------------------------|
    def method(self):
        print(super().method(), "But called in E class \n")
                
        
B = B_class() # This is a hierarchical inheritance as one class was inherited by many other classes
B.method()

C = C_class()
C.method() 

D = D_class()
D.method()

E = E_class()
E.method()


