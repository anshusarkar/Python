l = ['A' , 'B' , 'C' ,'D']

count = 0

var = 2**4

for i in l :
    for j in l :
        if(i!=j):
            print(i , "and" , j)
            count += 1
            
if(var-count==4):
    print("w!")