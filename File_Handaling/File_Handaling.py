f = open("a.txt",'r') #To open a file a built in method of python get's used which fillows the 
                      # Following Syntax open("file name ",'operational command to be executed ')
                      # operational commands are = 'r', 'w', 'a'
                      # 'r'  for reading 
                      # 'w'  for writing
                      # 'a'  to add lines after writing a file 'a' get's passed
context = f.read()
print(context)                     
f.close()

f=open("a.txt",'w')
f.write("Hello _ File managemant\n")
f.close()

f=open("a.txt",'a')
f.write("Hello _ This sentence is added using appemding")