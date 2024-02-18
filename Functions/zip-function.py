# A zip function takes one or more iterable as an argument and zips them in to one iterable 
# type cast is must, which can be type of any iterable

l = ['A', 'B' ,'C' ,'D']
l2 = ['I' , 'II' , 'III','IV']

zipped_list = list(zip(l2 , l)) #list of tuple

zipped_dictionary = dict(zip(l2 , l)) # a dictionary 

zipped_set= set(zip(l2 ,l)) # a set of tuples

zipped_tupple = tuple(zip(l2 ,l)) # a tuple of tuples

print(zipped_list)

print(zipped_dictionary)

print(zipped_set)

print(zipped_tupple)