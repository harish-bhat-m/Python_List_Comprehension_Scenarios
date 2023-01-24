###############################################################################
## Program split the letters from the string and change the case to upper    ##
## using list comprehension                                                  ##
##                                                                           ##
###############################################################################

message = "hello world"
new_message = [char.upper() for char in message]
print(new_message)