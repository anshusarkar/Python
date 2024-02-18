import time
x =   0
var1 = time.time()
print("Bike starting noises.....\n")
time.sleep(3)
while x < 5:
    if x==1:
        print("Journey started !\n")
        time.sleep(3)
    print("Not there yet, x=" + str(x)) # Why type casting ? use  , varr matybe
    x = x + 1
    time.sleep(3)
    if x == 5:
        print("Arrived !")
print("x=" , x)
var2 = time.time()

print("Execution time is : " , var2 - var1)