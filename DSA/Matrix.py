# A matrix is an array of arrays or list of lists ... 

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] # a 3 x3 matrix

def print_matrix(*args):
    for row in args:
        for element in row:
            print(element , '\n')
        
        
print_matrix(matrix)