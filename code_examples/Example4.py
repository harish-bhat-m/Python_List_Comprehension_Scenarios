###############################################################################
## Program demonstrate the use of if statement in list comprehension.        ##
##                                                                           ##
###############################################################################

natural_numbers = range(0,34)
div_3_9 = [number for number in natural_numbers if number % 3 == 0 and  number % 9 ==0]
print(div_3_9)