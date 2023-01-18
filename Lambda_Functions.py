#Lambda functions are a type of functions creation in which functions get's created in one line 
# syntax : function_name = lambda parameters : return values of the parameters
inp=int(input("Enter a value : "))
squre = lambda x : x*x
avg = lambda x,y,z : (x+y+z)/3
print(squre(inp))
print(avg(3,2,4))