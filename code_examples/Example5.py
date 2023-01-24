###############################################################################
## Program demonstrate the use of if else statement in list comprehension.   ##
##                                                                           ##
###############################################################################

natural_numbers = [1,6,7,3,75,78,99]
odd_even_list = ["Even" if num % 2 == 0 else "Odd" for num in natural_numbers]
print(natural_numbers)
print(odd_even_list)