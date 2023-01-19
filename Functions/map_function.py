cube = lambda x : x*x*x 

# map() is a function that get's used to map a function in a iterable like list instet of iterating it with a loop 
# Syntax of thew map() is map('function_name','iterable_name')
# map while assing to a varriable will alaways reaturn a 'map' object
# To make the map object an iterable type have to declear it's type i.e have to type cast it to an iterable

li = [1,2,3,4,5,6]

new_list = list(map(cube,li))

print(new_list)