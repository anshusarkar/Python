def generator ():
    for i in range(1000): # In python yield is like return statement but it stops it's execution after one 
        yield i           # execution of the value to be returned 
                          # or in other words it would return only 1 then 2 and then 3 upto the target value
gen = generator()         # which get's done by passing the generator function in the next() function
                          # for every execution of next() function it will return the value + 1 upto the target \
print(next(gen))          # bUt the method is need to be passed as an object to the next() function
print(next(gen)) 
print(next(gen))


for i in gen :            # All generatable values can be genreted through a for loop 
    print(i)
    