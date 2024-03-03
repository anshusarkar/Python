import os
if os.path.exists("new_dir") == True:
    os.rmdir("new_dir")
#This code snippet changes the current working directory to new_dir. The second line prints the current working directory.
print(os.getcwd())
os.mkdir("new_dir")
os.chdir("new_dir")
print(os.getcwd())

#This code snippet creates a new directory called newer_dir. The second line deletes the newer_dir directory.
os.mkdir("newer_dir")
os.rmdir("newer_dir") # This will only delete empty directory

#This code snippet returns a list of all the files and sub-directories in the website directory.
print(os.getcwd())
os.chdir("/home/zero/Python")
print(os.listdir("Pandas")) # This will return a list of files and folders in a directory

# A function to check weather a file is a directory of a file

def check () :
    dir = str(input("Enter a directory name : "))
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)
        if os.path.isdir(fullname):
            print("{} is direcorty ".format(fullname))
        else:
            print("{} is a file".format(fullname))
check()

# os.listdir("directory_name") checks into the directory contains
# os.path.join("direcory_name", file_name) joins the file name with  and as the windows uses '\' i.e. backslash and linux uses '/' i.e. forwardslash namkes pathjoining platfrom independent
# os.path.isdir() checks weather a file is a direcory or not 