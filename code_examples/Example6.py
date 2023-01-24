###############################################################################
## Program demonstrate the use of built-in function in list comprehension.   ##
##                                                                           ##
###############################################################################

import math

factorial_list = [math.factorial(n) for n in range(10)]
print (factorial_list)