m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Initialize a 2D list with zeros or any default value
mat = [[0 for i in range(n)] for i in range(m)]

# Populate the 2D list with user inputs
for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Enter the value for matrix no.1's [{i+1}][{j+1}] index : "))

# Print the 2D list
print("The matrix 1 is:")
for row in mat:
    print(row)
    
# Don't do mat2 = [[0,0],[0,0]] populate a 2d matrix even though list comprehansion is doing the same  ...
# As the values in the matrix won't change as a list is immutable in python meaning after initialization it can't be changed 
mat2 = [[0,0],[0,0]]
   
for i in range(2):
    for j in range(2):
        mat[i][j] = int(input(f"Enter the value for matrix no.2's [{i+1}][{j+1}] index : "))

print("The matrix 2 is:")
for row in mat2:
    print(row)