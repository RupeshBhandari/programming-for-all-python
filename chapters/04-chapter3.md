# Chapter 3: Working with Data Structures

## Lists

- Lists are ordered collections of items that can be of any data type (e.g. integers, strings, objects, etc.)
- Lists are defined using square brackets [] and items are separated by commas
- Lists are mutable, meaning you can change their contents by adding, removing, or modifying items

Here are some examples of how to work with lists:

```python
# Define a list
my_list = [1, 2, 3, 4]

# Access an item in the list
item = my_list[2] # item is 3

# Modify an item in the list
my_list[3] = 5

# Add an item to the end of the list
my_list.append(6)

# Remove an item from the list
my_list.remove(4)
```

## Tuples

- Tuples are similar to lists, but they are immutable, meaning you cannot modify their contents once they are created
- Tuples are defined using parentheses () and items are separated by commas

Here is an example of how to work with tuples:

```python
# Define a tuple
my_tuple = (1, 2, 3)

# Access an item in the tuple
item = my_tuple[1] # item is 2

# Cannot modify items in a tuple
my_tuple[1] = 4 # this will raise a TypeError
```

## Dictionaries

A dictionary is a collection of key-value pairs that is unordered, changeable, and does not allow duplicates. Dictionaries are also known as associative arrays or hash maps.

Here is an example of how to create a dictionary:

```python
# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

In this example, we have created an empty dictionary called **`my_dict`** and then added three key-value pairs to it. The keys are **`'name'`**, **`'age'`**, and **`'city'`**, and the corresponding values are **`'John'`**, **`30`**, and **`'New York'`**, respectively.

You can also create a dictionary using the **`dict()`** function and a sequence of key-value pairs, like this:

```python
# Create a dictionary using the dict() function
my_dict = dict([('name', 'John'), ('age', 30), ('city', 'New York')])

print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

To access the values in a dictionary, you can use the square brackets notation and the key of the value you want to access, like this:

```python
# Access a value in the dictionary
print(my_dict['name'])  # Output: 'John'
print(my_dict['age'])   # Output: 30
print(my_dict['city'])  # Output: 'New York'
```

You can also use the **`get()`** method to access the values in a dictionary, which returns a default value if the key is not found in the dictionary:

```python
# Access a value in the dictionary using the get() method
print(my_dict.get('name'))  # Output: 'John'
print(my_dict.get('age'))   # Output: 30
print(my_dict.get('city'))  # Output: 'New York'

# Access a value with a key that does not exist in the dictionary
print(my_dict.get('country', 'United States'))  # Output: 'United States'
```

You can also update the values in a dictionary, add new key-value pairs, and delete key-value pairs using the assignment operator, the **`update()`** method, and the **`del`** statement, respectively.

## Sets

Sets are unordered collections of unique items. Sets are defined using curly braces {} and items are separated by commas. Sets are mutable, meaning you can add or remove items. Here are some examples of how to work with sets:

```python
# Define a set
my_set = {1, 2, 3}

# Add an item to the set
my_set.add(4)

# Remove an item from the set
my_set.remove(2)

# Check if an item is in the set
if 3 in my_set:
  print("3 is in the set")
```
