# August 27, 2023
# Foundations of Programming: Python
# Assignment 07
# GitHub
# GitHubURL
# Exception handling and Pickling
---
# Introduction
For our seventh assignment we had create a demo that would include exception handling and pickling. We had to do some research by ourselves and with our own creativity implement code to explain these two concepts.
Exceptions are one of two types of errors in Python. Errors are problems in a program due to which the program will stop execution. Exceptions are raised when some internal events occur which change the normal flow of the program. It is important to handle exceptions properly in the code using try-except blocks to gracefully handle errors and avoid an application crashing.
Exceptions are raised when the program is syntactically correct, but the code results in an error.
The pickle module allows you to take text data and put it into a file. It is used for serializing and de-serializing a Python object structure. What Pickle does is it “serializes” the object before writing it to a file. It is the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions or transport data over the network. Essentially to be able to allow data to be stored and transferred easily between different systems. This cuts down the storage size needed and makes it easier to transfer information over a network.
---
# Creating the script
The exception script is a division in which by mathematical definition any number divided by 0 is undefined and for Python this same rule applies, it will throw you the error “ZeroDivisionError: division by zero”. By using the following script, you can’t prevent your application from stopping abruptly if you know you will expect this division by 0 to happen.

def demo(a):
    if a < 4:

        b = a/(a-3)    # throws ZeroDivisionError for a=3
try:
    demo(3)
except ZeroDivisionError:
    print("ZeroDivision Error Occurred and Handled")


 
Python script run successfully on the terminal.

The following is the script for serializing and de-serializing data using the Python Pickering functions pickle.dump() and pickle.load()
 
 
Binary format 



Python script run successfully on the terminal.
---
# Summary
For both demos I found that geeksforgeeks.org and https://gkscientist.com/pickle-module-in-python/are great resources to explain these concepts. I find that a brief description to the point with very simple examples works best for me. It is always good to give more context, but it is easier for me to start with a very short and simple explanation of a concept and then build upon it in case you need to add complexity into your code.
I think both to the concepts will be extremely valuable for working with professional applications. 


