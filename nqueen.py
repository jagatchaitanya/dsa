import numpy as np

def isvalid(matrix,row,col):
    num_rows = matrix.shape[0]
    if sum(matrix[row,:]) > 1:
        return False
    if sum(matrix[:,col]) > 1:
        return False
    for k in range(num_rows):
        if sum(matrix[np.array(range(k,num_rows)),np.array(range(num_rows-k))]) > 1:
            return False
    for k in range(num_rows):
        if sum(matrix[np.array(range(num_rows-k)),np.array(range(k,num_rows))]) > 1:
            return False
    for k in range(num_rows):
        if sum(matrix[np.array(range(num_rows-k)),np.flip(np.array(range(num_rows-k)))]) > 1:
            return False
    for k in range(num_rows):
        if sum(matrix[np.array(range(k,num_rows)),np.flip(np.array(range(k,num_rows)))]) > 1:
            return False
    return True

def nqueens(matrix, row):
    if row == matrix.shape[0]:
        return matrix.copy()
    for col in range(matrix.shape[1]):
        matrix[row,col] = 1
        if isvalid(matrix):
            result = nqueens(matrix,row+1)
            if result is not None:
                return result
        matrix[row,col] = 0
    return None

matrix = np.zeros((8,8))
print(nqueens(matrix,0))
    

    




  
