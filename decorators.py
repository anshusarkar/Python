# def function ():            # In python functon can be assinged to a variable 
#     print("Hello !")        # Which works as a container for that functoin like in line 2 that is called  
# function2 = function
# function2()

def a_function_that_takes_a_function_as_argument (fun): # This structure of a function is caleed decorators ....
    def x ():
        print("Decortions .... ")
        fun()
        print("Decortions .... ")
    return x


@a_function_that_takes_a_function_as_argument # With @ anotation and function name that decorats a  behavior of a function , changes according to ..
def a_randome_function ():                    # the decorator function 
    print("Hello !")

a_randome_function() # This function wont't just print Hello ! but also will print Decorators.....

@a_function_that_takes_a_function_as_argument
def another_function ():
    print("This is another function that is beeing decorated with decorators ! ")

another_function()

# This are equivalent to following ...

a_randome_function = a_function_that_takes_a_function_as_argument(a_randome_function) # This assingmnet cann't be done with any name 
                                                                                      # Have to be the name of the function that is to be modified
another_function = a_function_that_takes_a_function_as_argument(another_function)

# a_randome_function()

# another_function()