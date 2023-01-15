f = open("a.txt",'r') #To open a file a built in method of python get's used which fillows the 
                      # Following Syntax open("file name ",'operational command to be executed ')
                      # operational commands are = 'r', 'w', 'a'
                      # 'r'  for reading 
                      # 'w'  for writing
                      # 'a'  for appending
context = f.read()
print(context)                     