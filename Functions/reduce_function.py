from functools import reduce

# reduce is function in functools tahat get's used to reduce a list items folowing a list's return result 
# syntax of which is reduce('function_parameter' , 'iterable_to_be_assinged')

sum_using_reduce = lambda x , y : x + y

lst = [1,2,3,4,5,6,7,8,9,]

sumed_lst=reduce(sum_using_reduce,lst)

print(sumed_lst)

