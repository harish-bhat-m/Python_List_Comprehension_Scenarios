###############################################################################
## Program demonstrate reversal of string using the list comprehension       ## 
##                                                                           ##
###############################################################################
from itertools import groupby
input_string = "aabbbzzzzzzttttttt"
output_string = "".join([str(len(list(grp)))+ let for let,grp in groupby(input_string)])
print (output_string)