m = [[5,5,9],[8,9,6],[1,5,6]] # This is an example of 2d matrix in python i.e. list of list  it's a 3X3 matrix

#print(m)

# Or it can be printed like of a matrix using two for loops 

for row in m:       # This iterates over rows or the lists in the list
    for ele in row:  # This iterates over the values in the rows or the lists 
        print(ele, end=' ') # This statement prints the vales iterated by the second for and addeding a new line chracter after the end of iteration of one list present in the list
    print() # This prints an empty list