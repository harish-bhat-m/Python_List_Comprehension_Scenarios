###############################################################################
## Program demonstrate reversal of string using the list comprehension       ## 
##                                                                           ##
###############################################################################

input_string = "Hello World"
output_string = "".join([input_string[i] for i in range(len(input_string)-1, -1, -1)])
print(output_string)