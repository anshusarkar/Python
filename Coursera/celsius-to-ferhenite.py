# Conerting every 10th degit in range 10-100 from ferhenite to celsius

def fun(val)->int:
    return (val-32)*(5/9)

for i in range(10,110,10):
    cel = fun(i)
    #print(f"The Value of {i}° ferhenite in celsius is : " , fer , "° ferhenite" )
    print("{:>3}° F | {:>6.2f}° C".format(i,cel))