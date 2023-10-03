#First have to know What annotations are ? => It's more like a soft type declaretaion or in the other words even after declaring a 
#type of input to a varriable diffrent type of value can be inserted into it where in type declaration it isn't supposed to
# FYI : Their is no way to declare a hard type for a variable in like declared type in c which makes it a staticly typed language 

var : str = "Hello"
var = 123 # Even after the warnig the code will run as it's a soft type declation it happens because python is dynamicly typed or in 
          # other words it set's type before compilation in PVM i.e python virtual machine through python interprater as python is both 
          # interprated and compiled like java used to be 
print(var)

var2 : str = 141

print(var2)

var3 : 'power'  # Even 'power' is an annotation though can't be checked using __annotaion__

# to check it's annotation 
from inspect import get_annotations

print(get_annotations(var2))


def function()->"This is passed using ->": # this will set annotation for a return statement
    
    return 

print(function.__annotations__ ) #This will return the string in the function line after -> in a dictionary

# EX -

def power(Voltage: 'in Volts'   , Current :'in Ampher' )-> 'in watts':
    return  Voltage*Current 

print(power(5,2))

print(power.__annotations__)

# Conclusion - F strings is much better.
# and annotations can be used to declare a varriable that's value might change according to the input of the varriable making it more varriable 
# or a dynamic varriable  
# even though python variables are dynamic
# their is no way to hardly declare a type # for a variable in python 