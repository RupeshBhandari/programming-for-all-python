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

### Different File Modes in Python

Python provides various file modes to work with files depending on your needs — whether it's reading, writing, or both. Here's a quick reference:

| Mode   | Description |
|--------|-------------|
| `'r'`   | Open text file for **reading**. Raises an error if the file does not exist. |
| `'r+'`  | Open for **reading and writing**. Raises an error if the file does not exist. |
| `'w'`   | Open for **writing**. Truncates the file if it exists. Creates a new file if it doesn't. |
| `'w+'`  | Open for **reading and writing**. Truncates the file if it exists. Creates a new file if it doesn't. |
| `'a'`   | Open for **writing**. Appends data to the end of the file. Creates the file if it doesn't exist. |
| `'a+'`  | Open for **reading and writing**. Appends data to the end. Creates the file if it doesn't exist. |
| `'rb'`  | Open for **reading in binary mode**. Raises an error if the file doesn't exist. |
| `'rb+'` | Open for **reading and writing in binary mode**. Raises an error if the file doesn't exist. |
| `'wb'`  | Open for **writing in binary mode**. Truncates the file if it exists. Creates a new one if not. |
| `'wb+'` | Open for **reading and writing in binary mode**. Truncates the file if it exists. Creates a new one if not. |
| `'ab'`  | Open for **appending in binary mode**. Creates the file if it doesn't exist. |
| `'ab+'` | Open for **reading and appending in binary mode**. Creates the file if it doesn't exist. |

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

### Built-in Exceptions in Python

Python has a rich set of built-in exceptions that are raised when errors occur during execution. Here's a handy reference table:

| Exception              | Description |
|------------------------|-------------|
| `ArithmeticError`         | Raised when an error occurs in numeric calculations. |
| `AssertionError`          | Raised when an `assert` statement fails. |
| `AttributeError`          | Raised when attribute reference or assignment fails. |
| `Exception`               | Base class for all exceptions. |
| `EOFError`                | Raised when the `input()` method hits an end-of-file condition (EOF). |
| `FloatingPointError`      | Raised when a floating point calculation fails. |
| `GeneratorExit`           | Raised when a generator is closed using `close()`. |
| `ImportError`             | Raised when an imported module does not exist. |
| `IndentationError`        | Raised when indentation is not correct. |
| `IndexError`              | Raised when an index of a sequence is out of range. |
| `KeyError`                | Raised when a key is not found in a dictionary. |
| `KeyboardInterrupt`       | Raised when the user interrupts program execution (e.g., Ctrl+C). |
| `LookupError`             | Base class for lookup errors like `IndexError` and `KeyError`. |
| `MemoryError`             | Raised when the program runs out of memory. |
| `NameError`               | Raised when a variable is not defined. |
| `NotImplementedError`     | Raised when an abstract method is not overridden in an inherited class. |
| `OSError`                 | Raised when a system-related operation fails. |
| `OverflowError`           | Raised when a numeric result exceeds the allowed range. |
| `ReferenceError`          | Raised when a weak reference is no longer valid. |
| `RuntimeError`            | Raised for unspecified runtime errors. |
| `StopIteration`           | Raised to signal the end of iteration. |
| `SyntaxError`             | Raised when a syntax error is detected. |
| `TabError`                | Raised when inconsistent use of tabs and spaces is detected. |
| `SystemError`             | Raised when a system-related internal error occurs. |
| `SystemExit`              | Raised when `sys.exit()` is called. |
| `TypeError`               | Raised when an operation is applied to an object of inappropriate type. |
| `UnboundLocalError`       | Raised when a local variable is referenced before assignment. |
| `UnicodeError`            | Base class for Unicode-related errors. |
| `UnicodeEncodeError`      | Raised when a Unicode encoding error occurs. |
| `UnicodeDecodeError`      | Raised when a Unicode decoding error occurs. |
| `UnicodeTranslateError`   | Raised when a Unicode translation error occurs. |
| `ValueError`              | Raised when a function receives the right type but an inappropriate value. |
| `ZeroDivisionError`       | Raised when division or modulo by zero is attempted. |