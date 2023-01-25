###############################################################################
## Program demonstrate the use of comparison and logical operator in list    ##
## comprehension.                                                            ##
##                                                                           ##
###############################################################################

list_of_numbers = [100, 23, 153, 4533, -150, 175, 99, 200]

number_between_100_200 = [no for no in list_of_numbers if no > 100 and no < 200]
print(number_between_100_200)