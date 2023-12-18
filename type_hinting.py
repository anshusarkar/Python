var : int # This is called type hinting in python that only hints the type of a varriable to compiler and it dosn't makes any code run faster it'a misconception
var2 : float

var3 = int()


print(type(var3)) # that is called type casting that cast the variable into int() class 

def fun()-> None :  
    print(fun.__annotations__)
    
fun()