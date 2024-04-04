def decorator_factory(parameter):
    def decorator(func):
        def wrapper(*args, **kwargs): # As the args and kwargs are passed strings , lists and dictonaries can be passed a parameter to the decorator
            # Do something with parameter before calling the decorated function
            print("Decorator parameter:", parameter)  # How ever if we remove **kargs from the paramater and return statement the code would still accept the dictionaries as parameters parameter
            return func(*args, **kwargs)
        return wrapper
    return decorator


# A dictonary 

abc = {"a" : "Hello",
       "b" : "World",}

# Using the decorator factory to create a parameterized decorator

@decorator_factory([1,2,3,4])
def my_function():
    print("Inside my_function")
    
@decorator_factory("Hello, world!")
def my_function2():
    print("Inside my_function2")

@decorator_factory(abc)
def my_function3():
    print("Inside my_function3")


# Calling the decorated function
my_function()
my_function2()
my_function3()
