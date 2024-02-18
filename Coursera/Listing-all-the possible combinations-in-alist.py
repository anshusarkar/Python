l = ['A' , 'B' , 'C' ,'D']

count = 0

for i in l :
    for j in l :
        print(i , "and" , j)
        count += 1

var = 2**4

print("Number of possible combinations would be : " , 2**4)

if(count==var):
    print("W!")
    
# Now elemeniting A and A , B and B , C and C , D and D

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