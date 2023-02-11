###############################################################################
## Program demonstrate multiply matrixes using the list comprehension        ## 
##                                                                           ##
###############################################################################
matrix_1 = [[11,52,73],[44,12,23],[10,15,12]]
matrix_2 = [[45,34,20],[48,56,67],[76,80,78]]

matrix_3 = [[sum(x * y for x, y in zip(matrix_1_row, matrix_2_col)) for matrix_2_col in zip(*matrix_2)] for matrix_1_row in matrix_1]

print(matrix_3)
