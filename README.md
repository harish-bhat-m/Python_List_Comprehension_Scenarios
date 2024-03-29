# Python List Comprehension - Scenarios
This repository to learn and understand the concept of Python List Comprehensiona and its use cases.

## What is list.
Before diving into the topic of list comprehension lets first understand what is list in Python. List in Python is a built-in data structure that is similar to array. Unlike array in C or Java, the list can hold mixture of objects which are of different data type. In other words list stores ordered collection of items which can be of different data types. Each item in the list has assigned a value and that value is called as index. It is important to note that the index always starts from zero.

## Now what is the list comprehension
The list comprehension is nothing but building a list using simpler syntax. It offers a way to implement a mathematical notation to generate a list from existing list. List comprehension is considerably a faster way to process the list than using the conventional way of using the list with the loop.

## Syntaxes and examples
Let's dive into the syntax </br>
```
list_variable_new = [variable for in list_varaible_old if condition]
```
<br> Although the syntax is not the complete syntax, the above syntax includes pretty much complete syntax. Let's see some real world examples and scenarios.

### Example 1 Split the letters from a string
Lets use the list comprehension for splitting the string into list of individual character. <br>
``` 
message = "Hello World"
new_message = [char for char in message]
print(new_message)
```
Here is the result of the above code snippet.
``` 
harish@HBM:python3 Example1.py
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'] 
```
 
### Example 2 Split the letters from a string and change the it to all upper case
In this example we will be converting the individual character of the list into upper case letter. Please find the code snippet for the same.
```
message = "hello world"
new_message = [char.upper() for char in message]
print(new_message)
```
When we run the above code we get the list with all the character converted into upper case letters.
```
harish@HBM:python3 Example2.py
['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
```

### Example 3 Conditional, Generate the even and odd numbers from 0 to 10
In this example we will extend our example of list comprehension by including the condition. We will write a program which will generate the list of odd and even numbers from set of natural numbers. Here is the code.

```
even = [number for number in range(10) if number % 2 == 0]
odd = [number for number in range(10) if number % 2 != 0]
print("The set of odd numbers between 0 to 10")
print(odd)
print("The set of even numbers between 0 to 10")
print(even)
```
Let's see the results of above code snippet
```
harish@HBM:python3 Example3.py
The set of odd numbers between 0 to 10
[1, 3, 5, 7, 9]
The set of even numbers between 0 to 10
[0, 2, 4, 6, 8]

```

### Example 4 Nested if statements in the list comprehension
In this example, we will look at yet another example of using the nested if condition in a list comprehension. In this example we will see if the numbers in a given list are perfectly divisible by 3 and 9.

```
natural_numbers = range(0,34)
div_3_9 = [number for number in natural_numbers if number % 3 == 0 if number % 9 ==0]
print(div_3_9)
```
Let's see the result of above list comprehension
```
harish@HBM:python3 Example4.py
[0, 9, 18, 27]
```

### Example 5 List comprehension with if... else 
In this example we will see another scenario where we use the if... else statement in the list comprehension. Here we will generate the list based which says a number in another list is odd or even.

```
natural_numbers = [1,6,7,3,75,78,99]
odd_even_list = ["Even" if num % 2 == 0 else "Odd" for num in natural_numbers]
print(natural_numbers)
print(odd_even_list)
```
While executing the above code snippet we get the below results

```
harish@HBM:python3 Example5.py
[1, 6, 7, 3, 75, 78, 99]
['Odd', 'Even', 'Odd', 'Odd', 'Odd', 'Even', 'Odd']
```

### Example 6 Using any functions in the list comprehension (generate the factorial in list).
In this example we will see how we can use any functions (built-in or user defined function) and build the list. In the below example, we will generate the factorial list.
```
import math

factorial_list = [math.factorial(n) for n in range(10)]
print (factorial_list)
```
Here is result of the above run

```
harish@HBM:python3 Example6.py
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
```

### Example 7 Using the comparison and logical operator in list comprehension.
Here we see a simple example of how we can use the comparison operator in the list comprehension.
In this example we will cull a list of numbers from the another list using the list comprehension technique, where the numbers are between 100 and 200.

```
list_of_numbers = [100, 23, 153, 4533, -150, 175, 99, 200]

number_between_100_200 = [no for no in list_of_numbers if no > 100 and no < 200]
print(number_between_100_200)

```
Here is the result
```
harish@HBM:python3 Example7.py
[153, 175]
```

### Example 8 Using the membership operator in the list comprehension.
The membership operators are used to test if the sequence is present in the object or not. Example of membership operators are 'in' and 'not in'. Lets see and example how this can be used in the list comprehension with an example. We have list of different objects in the list, we will separate out all the fruit items from the original list. Let's dive into the code snippet.

```
fruits = ['apple', 'citrus', 'orange', 'banana', 'mango', 'grapes', 'berries']

list_of_food = ["rice", 'weat', 'mango', 'apple', 'onion', 'barley', 'millet']

list_of_fruits = [food for food in list_of_food if food in fruits]
print(list_of_fruit)
```
Here is the result
```
harish@HBM:python3 Example8.py
['mango', 'apple']
```
Similarly, we can make use of 'not in' operator.

### Example 9 How to flatten the two dimension list using list comprehension.
Here we will go through a code snippet, which will flatten the two dimension list using the python list comprehension.

```
two_d_list = [[1,2,3],[4,5,6],[7,8,9]]
one_d_list = [number for inner_list in two_d_list for number in inner_list]
print(two_d_list)
print(one_d_list)
```
While running the above code snippet, we get the following result

```
harish@HBM:python3 Example9.py
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 10 Reverse the string using the list comprehension
Here will go through one of the way to reverse the string using list comprehension. Here we get the index in reverse order and build the list in reverse order. Using the string join method we will build the string using the reverse list.
```
input_string = "Hello World"
output_string = "".join([input_string[i] for i in range(len(input_string)-1, -1, -1)])
print(output_string)
```

Below is the result of the above run.
```ss
harish@HBM:python3 Example10.py
dlroW olleH
```

### Example 11. Print the string in shorthand form "aaabbddeeee" as 3a3b3d4es
This is typical interview question to generate the shorthand notation for the repeating elements in the string. Let's use the list comprehension to solve the problem. Here we are using a groupby function from itertool library, the groupby fucntion will create the sub iterator grouped by value. Then we will append the letter after getting the individual groups length after converting it to the list.
```
from itertools import groupby
input_string = "aabbbzzzzzzttttttt"
output_string = "".join([str(len(list(grp)))+ let for let,grp in groupby(input_string)])
print (output_string)
```
The run reveals the below shorthand string.
```
harish@HBM:python3 Example11.py
2a3b6z7t
```

### Example 12 Add the two square matrix using the list comprehension.
This is pretty simple example which adds the two square matrix using list comprehension.
```
matrix_1 = [[11,52,73],[44,12,23],[10,15,12]]
matrix_2 = [[45,34,20],[48,56,67],[76,80,78]]

matrix_3 = [[matrix_1[i][j]+ matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print(matrix_3)
```
The result is here.
```
harish@HBM:python3 Example12.py
[[56, 86, 93], [92, 68, 90], [86, 95, 90]]
```

### Example 13 Matrix multiplication using the list comprehension.
In this example we see how to the matrix multiplication using the list comprehension. The last for loop that is ```for matrix_1_row in matrix_1``` gives the individual list from 'matrix_1', the second last loop that is ```for matrix_2_col in zip(*matrix_2)``` gives the transposed individual list (column) from the matrix_2. The loop ``` for x, y in zip(matrix_1_row, matrix_2_col)``` packs the row of matrix_1 with column of matrix_2 and finally we sum these multiplication.

```
matrix_1 = [[11,52,73],[44,12,23],[10,15,12]]
matrix_2 = [[45,34,20],[48,56,67],[76,80,78]]

matrix_3 = [[sum(x * y for x, y in zip(matrix_1_row, matrix_2_col)) for matrix_2_col in zip(*matrix_2)] for matrix_1_row in matrix_1]

print(matrix_3)
```
Here is the result of the matrix multiplication
```
harish@HBM:python3 Example13.py
[[8539, 9126, 9398], [4304, 4008, 3478], [2082, 2140, 2141]]
```



