###############################################################################
## Program generate the odd and even list using the list comprehension       ##
##                                                                           ##
###############################################################################

even = [number for number in range(10) if number % 2 == 0]
odd = [number for number in range(10) if number % 2 != 0]
print("The set of odd numbers between 0 to 10")
print(odd)
print("The set of even numbers between 0 to 10")
print(even)