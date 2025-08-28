import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

transpose = matrix.T
print(transpose)


# second method
mymatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tt_mymatrix = [
    [mymatrix[j][i] for j in range(len(mymatrix))] for i in range(len(mymatrix[0]))
]

print(tt_mymatrix)
