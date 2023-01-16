f = open("a.txt",'r') #read() method reads entire line while the function readline() reads only one line 
context = f.read()
#print(context)
contex_line_10 = []
for contex_line_10 in range (10) :
    
    contex_line_10 = f.readlines()

print(contex_line_10)
f.close()    

    
        
