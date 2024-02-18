# Conerting every 10th degit in range 10-100 from celsius to ferhenite

def fun(val)->int:
    return (val-32)*(5/9)

for i in range(10,110,10):
    fer = fun(i)
    print(f"The Value of {i}° celsius is ferhenite is : " , fer , "° ferhenite" )