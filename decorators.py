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


@a_function_that_takes_a_function_as_argument # With @ anotation and function name that decorats a function behavior of that function changes ..
def a_randome_function ():
    print("Hello !")

a_randome_function() # This function wont't just print Hello ! but also will print decorators.....

@a_function_that_takes_a_function_as_argument
def another_function ():
    print("This is another function that is beeing decorated with decorators ! ")

another_function()