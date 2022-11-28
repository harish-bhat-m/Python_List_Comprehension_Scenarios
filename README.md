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

### Example1 Split the letters from a string
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
 
 