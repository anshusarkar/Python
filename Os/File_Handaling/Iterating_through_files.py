with open('b.txt') as file :
    for line in file :
        print(line.upper()) # Due to python's line by line execution there will be alaways a new line that would get printed each time iterating through the file 
        
with open('b.txt') as file:
    for line in file :
        print(line.strip()) # This fixex the problem

# Reading the file lines into a list 

file = open('b.txt')

line = file.readlines()
file.close()

line.sort()

print(line)

print(type(line))