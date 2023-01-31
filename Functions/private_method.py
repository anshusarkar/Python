class A : # To create a private method in python two '__' (Under scores) get's used 
                 # Which raises an error making the method private
                 # To use the method Class name get's used as an prefix for tht method for that method call
    def __method(self):
        print("This  private method is printed with the help of name mangaling !")

a=A() 
#a.__method()          # This method is now private
#a._A__method()        # This is Called " Name mangeling "