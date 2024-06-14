# Chapter 4: Working with Data

## Manipulating data

### Sorting Data

You can use the **`sorted`** function to sort a list or tuple in ascending order:

```python
# Define a list of integers
my_list = [5, 2, 7, 1, 3]

# Sort the list in ascending order
sorted_list = sorted(my_list)

# Define a tuple of strings
my_tuple = ('c', 'a', 'b')

# Sort the tuple in ascending order
sorted_tuple = sorted(my_tuple)
```

You can also use the **`sort`** method to sort a list in place:

```python
# Define a list of integers
my_list = [5, 2, 7, 1, 3]

# Sort the list in ascending order
my_list.sort()
```

### Filtering Data

You can use a list comprehension and a boolean condition to filter a list or tuple:

```python
# Define a list of integers
my_list = [5, 2, 7, 1, 3]

# Filter the list to get only even numbers
filtered_list = [x for x in my_list if x % 2 == 0]

# Define a tuple of strings
my_tuple = ('c', 'a', 'b')

# Filter the tuple to get only strings of length 2
filtered_tuple = tuple(x for x in my_tuple if len(x) == 2)
```

### Aggregating Data

You can use the **`sum`** function to get the sum of the items in a list or tuple:

```python
# Define a list of integers
my_list = [5, 2, 7, 1, 3]

# Get the sum of the items in the list
total = sum(my_list)

# Define a tuple of integers
my_tuple = (5, 2, 7, 1, 3)

# Get the sum of the items in the tuple
total = sum(my_tuple)
```

You can also use other functions such as min, max, and len to get the minimum, maximum, and length of a list or tuple.

## Reading and writing files

You can read and write files using the built-in **`open`** function and the file object it returns. Here is an example of how to read a file:

```python
# Open the file in read mode
with open('my_file.txt', 'r') as f:
  # Read the contents of the file into a variable
  file_contents = f.read()
  # Print the contents of the file
  print(file_contents)
```

In the example above, the **`open`** function is called with the file name and the mode 'r' (for read). The function returns a file object, which is stored in the **`f`** variable. The **`read`** method of the file object is then called to read the contents of the file into the **`file_contents`** variable. Finally, the contents of the file are printed using the **`print`** function.

Here is an example of how to write to a file:

```python
# Open the file in write mode
with open('my_file.txt', 'w') as f:
  # Write some text to the file
  f.write("Hello, world!")
```

In the example above, the **`open`** function is called with the file name and the mode 'w' (for write). The function returns a file object, which is stored in the **`f`** variable. The **`write`** method of the file object is then called to write the string "Hello, world!" to the file.

Note that the **`with`** statement is used to open the file and automatically close it when the block of code is finished executing. This is a recommended practice to ensure that the file is properly closed and released after you are done with it.



## Exception handling

Exception handling is a mechanism that allows you to handle errors and exceptions that may occur in your code. It allows you to write code that can gracefully handle unexpected input, errors, and exceptions, and it can help you to write more robust and reliable programs.

Here is an example of how to use the **`try`** and **`except`** statements to handle an exception:

```python
try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero')
```

In this example, we have used the **`try`** statement to enclose a block of code that may raise an exception. If an exception is raised, the code in the **`except`** block will be executed. In this case, we are handling the **`ZeroDivisionError`** exception, which is raised when trying to divide by zero.

You can also use the **`finally`** statement to execute a block of code *regardless* of whether an exception is raised or not. For example:

```python

try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    print('Exiting the program')
```

In this example, the code in the **`finally`** block will be executed regardless of whether an exception is raised or not.