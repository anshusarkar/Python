def fun_of_a_module():
    print("This function belengs to a module")
    return 0

# fun_of_a_module()  
# Now if the function is imported the defination of the function and the 
# execution of the function both would get called resulting double run of a the same function
# to prevent that 'if __name__ == "__main__" : ' get's used if it is to execute a function call
# in that module 

if __name__ == "__main__":
    fun_of_a_module ()
