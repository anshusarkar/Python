# filter is function that takes a funtion and an iterable as a parameter and returns a filter obj based on the parametered funtion retun condition
# Syntax of which is filter ('function_parameter' , 'iterable_name')

detect_even= lambda x : x%2==0 

lst=[1,2,3,4,5,6]

newlst=tuple(filter(detect_even,lst))

print(newlst) 