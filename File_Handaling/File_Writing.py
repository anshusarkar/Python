
fil=open("b.txt",'w')                                                          # write() method writes lines tha are being passed 
fil.write("This context is added with write method")                           # with open("filename") as 'file_variable' : opens files and closes their after
fil.close()                                                                    # writelines() writes lines that are passed to it as list parameters
#To close file automatacally use with key word                                 # If all of the methods are used all at a time they replaces each others context 
with open("b.txt", 'a') as fil:                                                 
    fil.write("\nWith the help of the keyword with file closes automatically ")
fil = open("b.txt",'w')
lines = [
    "Hello this is line one \n"
    "This is line two \n"
    "This is line three \n"
    "Above three lines are written using writelines() method \n"
]
fil.writelines(lines)
