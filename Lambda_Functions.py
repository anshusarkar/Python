#Lambda functions are a type of functions creation in which functions get's created in one line
# syntax : function_name = lambda parameters : return values of the parameters

inp=int(input("Enter a value : "))
squre = lambda x : x*x
avg = lambda x,y,z : (x+y+z)/3
print(squre(inp))
print(avg(3,2,4))
 
# Lamda functions get's used to pass function as a parameter for a function to maintain annonomasity
# syntax : def 'function_name'('Annoumous_Varriable' , values to be passed ):
#                           return fx(value)
#          print('function_name'(lambda_abbribriation , vales to be passed))





def cube(fx,value):
    return fx(value)
    
print(cube(lambda x : x*x*x , 3))

