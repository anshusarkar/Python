f = open("b.txt",'r') # read() method reads entire line while the function readline() reads only one line 
context = f.read()
var = f.readline() 
#print(context)
contex_line_10 = []
for contex_line_10 in range (10) :
    
    contex_line_10 = f.readlines()

print(contex_line_10)
f.close()    

    
        
#The readline() method reads a single line from the current position, the read() method reads from the current position until the end of the file

