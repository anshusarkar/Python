f = open("b.txt",'r') #read() method reads entire line while the function readline() reads only one line 
context = f.read()
var = f.readline() # reads only one line
#print(context)
contex_line_10 = []
for contex_line_10 in range (10) :
    
    contex_line_10 = f.readlines()

print(contex_line_10)
f.close()    

    
        
