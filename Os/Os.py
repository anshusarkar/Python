import os

# For this program to run first run the File_writing.py script

# renaming a file 

os.rename("b.txt", "a.txt") # "old_file_name", "new_file_name"

# Checking if a file exists

print(os.path.exists("a.txt"))

#print(os.path.exists('b.txt'))

# Checking the size of the file 

print(os.path.getsize("a.txt"),"Bytes")

# To find the timestamp for a file

print(os.path.getmtime("a.txt")) # This would print a timestamp in this case unix timestamp that prints number of seconds since 1st january 1970 because before that no digital was ever created

# Checking the time when the file was written

import datetime

timestamp = os.path.getmtime('a.txt') 

print(datetime.datetime.fromtimestamp(timestamp))

# To find the absolute path of the os

print(os.path.abspath("a.txt"))

# removing a file 

#os.remove("b.txt")





