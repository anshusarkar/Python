# the in which a list get's populated with values though a loop in one line at it's time of intialization is called a list comprehansion

lis = [0 for _ in range(10)] # a list of 10 consecutive zeros

lis2 = [10 for i in range(10)] # a list of 10 consecutive tens

print(lis)

print(lis2)

# list comprehansion is alternative to the follwoing way 

lis3 = []

for i in range(5):
    lis3.append(1)
    
print(lis3)


# conclusion list-comprehansion is what ternary is for if-else and lamda functions are for convetional functions 
# where as it's for genral way of populating list with same values .