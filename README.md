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


