# Chapter 5: Object-Oriented Programming

## Introduction to object-oriented programming

Object-oriented programming (OOP) is a programming paradigm that is based on the concept of "objects". Objects are data structures that contain both data and functions, and they are used to represent real-world entities or concepts in a program.

OOP is designed to help developers write reusable, modular, and maintainable code. It allows developers to organize their code into classes and objects, which makes it easier to understand and maintain.

## Classes and objects

In object-oriented programming (OOP), a class is a template that defines the data and functions that an object will contain. Objects are then created from these classes, and are called instances of the class.

Here is an example of a simple class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')
```

This class defines a **`Person`** object with a **`name`** and **`age`** attribute, and a **`greet`** function that prints a greeting message.

To create an instance of this class, we can use the **`__init__`** method, which is a special method that is called when an object is created:

```python
person = Person('John', 30)
person.greet()
# Output: Hello, my name is John and I am 30 years old.
```

In this example, **`person`** is an instance of the **`Person`** class. It contains the data and functions defined in the class, and can be modified at runtime.

Objects can interact with each other through their functions. For example, we can create another object and have it call the **`greet`** function of the **`person`** object:

```python
class Dog:
    def bark(self, person):
        person.greet()
        print('Woof woof!')

dog = Dog()
dog.bark(person)
# Output: Hello, my name is John and I am 30 years old.
#         Woof woof!
```

## Inheritance and polymorphism

**Inheritance**

Inheritance is the ability of a class to inherit the attributes and methods of another class. This allows developers to create a new class that is a modified version of an existing class, without having to rewrite all of the code.

For example, consider the following classes:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print('Some generic animal sound')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species='Dog')

    def make_sound(self):
        print('Woof woof!')
```

In this example, the **`Dog`** class is a subclass of the **`Animal`** class. It inherits the **`name`** and **`species`** attributes and the **`make_sound`** method from the **`Animal`** class, and defines its own version of the **`make_sound`** method.

To create an instance of the **`Dog`** class, we can use the **`__init__`** method as follows:

```python
dog = Dog('Fido')
dog.make_sound()
# Output: Woof woof!
```

**Polymorphism**

Polymorphism is the ability of a class to take on multiple forms. This can be achieved through inheritance, where a subclass can override or extend the methods of its superclass.

For example, consider the following code:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print('Some generic animal sound')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species='Dog')
        self.breed = breed
    
    def make_sound(self):
        print('Woof woof!')

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species='Cat')
        self.breed = breed
    
    def make_sound(self):
        print('Meow meow!')

def make_sounds(animals):
    for animal in animals:
        animal.make_sound()

dog = Dog('Fido', 'Labrador')
cat = Cat('Fluffy', 'Siamese')

make_sounds([dog, cat])
# Output: Woof woof!
#         Meow meow!
```

In this example, we have defined an **`Animal`** class with a **`name`** and **`species`** attribute, and a **`make_sound`** function that prints a generic animal sound. We have then defined a **`Dog`** class that inherits from the **`Animal`** class, and has its own **`__init__`** method and **`make_sound`** function. The **`Dog`** class has a **`breed`** attribute and overrides the **`make_sound`** function to print a specific dog sound.

The **`dog`** object is an instance of the **`Dog`** class, which is a subclass of the **`Animal`** class. The **`dog`** object has the ability to take on multiple forms by inheriting the data and functions of the **`Animal`** class and by overriding the **`make_sound`** function with its own implementation.

Similarly, when the **`cat`** object is an instance of the **`Cat`** class, which is a subclass of the**`Animal`** class. The **`cat`** object has the ability to take on multiple forms by inheriting the data and functions of the **`Animal`** class and by overriding the **`make_sound`** function with its own implementation.

When the **`make_sound`** function is called on the **`cat`** object, it calls the **`make_sound`** function of the **`Cat`** class, which prints the specific cat sound "Meow meow!".

## Encapsulation and data hiding

Encapsulation is a key concept in object-oriented programming (OOP) that refers to the idea of bundling data and methods that operate on that data within a single unit, or object. Encapsulation helps to protect the data from outside access and modification, and it can also be used to implement data hiding.

You can use class definitions to implement encapsulation. For example:

```python
class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Insufficient funds')
```

Data hiding is a technique in object-oriented programming (OOP) that refers to the idea of keeping certain data and implementation details private within a class, so that they cannot be accessed or modified from outside the class. Data hiding helps to protect the integrity of the data and to prevent unintended modifications, and it is often used in conjunction with encapsulation to protect data and implementation details within an object.

In this example, we have defined a **`BankAccount`** class that has a **`name`** and **`balance`** attribute, as well as methods for depositing, withdrawing, and checking the balance. We have prefixed the **`name`** and **`balance`** attributes with **`__`**, which is a convention to indicate that these attributes should not be accessed or modified directly from outside the class.

To access or modify the **`name`** and **`balance`** attributes, we have defined methods such as **`get_balance`** and **`deposit`** that allow us to safely manipulate the data. This is an example of encapsulation and data hiding in action.


## Concurrency

Concurrency is a crucial concept in programming, allowing multiple tasks to make progress without waiting for each other to complete. Python provides several ways to handle concurrency, including threading, multiprocessing, and asynchronous programming.

##### 1. Threading

Threading is a technique where multiple threads run in the same memory space, allowing for lightweight concurrent execution. Python's `threading` module makes it easy to work with threads.

###### Example of Threading

```python
import threading

def print_numbers():
    for i in range(10):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()
```

##### 2. Multiprocessing

Multiprocessing involves running multiple processes simultaneously, each with its own memory space. This approach is particularly useful for CPU-bound tasks. Python's `multiprocessing` module supports creating and managing separate processes.

###### Example of Multiprocessing

```python
import multiprocessing

def square_numbers():
    for i in range(10):
        print(i * i)

# Creating a process
process = multiprocessing.Process(target=square_numbers)

# Starting the process
process.start()

# Waiting for the process to complete
process.join()
```

##### 3. Asynchronous Programming

Asynchronous programming allows you to write code that performs tasks without blocking the main execution flow. This is particularly useful for I/O-bound tasks like network operations or file reading/writing. Python's `asyncio` module provides tools for asynchronous programming.

###### Example of Asynchronous Programming

```python
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # Simulating a network request
    print("Done fetching")

async def main():
    await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data()
    )

# Running the async function
asyncio.run(main())
```

##### 4. Differences and Use Cases

- **Threading**: Best suited for I/O-bound tasks where the primary goal is to avoid blocking operations, such as file I/O or network requests. However, Python's Global Interpreter Lock (GIL) can limit the performance gains in CPU-bound tasks.

- **Multiprocessing**: Ideal for CPU-bound tasks where each process runs on its own CPU core. Since each process has its own memory space, there's no GIL limitation, leading to better performance in compute-intensive tasks.

- **Asynchronous Programming**: Excellent for I/O-bound and high-level structured network code. Asyncio is best used when you need to handle many simultaneous I/O operations, such as multiple network connections.

##### 5. Concurrency in Practice

In practice, choosing the right concurrency model depends on the specific requirements of your application:

- For web scraping, where you wait for HTTP responses, threading or asyncio can be highly effective.
- For data processing that involves heavy computations, multiprocessing can leverage multiple CPU cores for better performance.
- For building scalable web servers, asyncio offers an efficient way to handle numerous simultaneous connections.

##### 6. Libraries and Frameworks

Python offers several libraries and frameworks that simplify concurrency:

- **Threading**: `threading` module
- **Multiprocessing**: `multiprocessing` module
- **Asynchronous Programming**: `asyncio`, along with higher-level frameworks like `aiohttp` for asynchronous HTTP requests, and `Quart` for asynchronous web applications.
