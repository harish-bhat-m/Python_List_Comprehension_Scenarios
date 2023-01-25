###############################################################################
## Program demonstrate the use of membership operator in list comprehension. ##
##                                                                           ##
###############################################################################

fruits = ['apple', 'citrus', 'orange', 'banana', 'mango', 'grapes', 'berries']

list_of_food = ["rice", 'weat', 'mango', 'apple', 'onion', 'barley', 'millet']

list_of_fruits = [food for food in list_of_food if food in fruits]
print(list_of_fruit)