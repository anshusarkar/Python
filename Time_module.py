import time as t 

def func()->None:
    for _ in range(0,100000):
        _ += 1
        #t.sleep(1) # adds 1 secs of dealy 
        
var1 = t.time()
func()
var2 = t.time()

print("The execution time for the function is : " , var2-var1 , " secs")