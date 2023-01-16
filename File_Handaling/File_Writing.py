
fil=open(f"c.txt",'w')
fil.write("This context is added with write method")
fil.close()
#To close file automatacally use with key word 
with open("c.txt", 'a') as fil:
    fil.write("\nWith the help of the keyword with file closes automatically ")