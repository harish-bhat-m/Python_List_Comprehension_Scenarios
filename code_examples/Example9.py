###############################################################################
## Program demonstrate flattening of two dimension matrix using list         ## 
## comprehension.                                                            ##
##                                                                           ##
###############################################################################

two_d_list = [[1,2,3],[4,5,6],[7,8,9]]
one_d_list = [number for inner_list in two_d_list for number in inner_list]
print(two_d_list)
print(one_d_list)