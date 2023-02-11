###############################################################################
## Program demonstrate add/substract matrix using the list comprehension     ## 
##                                                                           ##
###############################################################################
matrix_1 = [[11,52,73],[44,12,23],[10,15,12]]
matrix_2 = [[45,34,20],[48,56,67],[76,80,78]]

matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print(matrix_3)
