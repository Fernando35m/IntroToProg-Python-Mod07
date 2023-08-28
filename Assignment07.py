# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Exception Handling and Pickling demo
# Fernando Mendoza,August 27, 2023,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

import pickle
def demo(a):
    if a < 4:

        b = a/(a-3)    # throws ZeroDivisionError for a=3
try:
    demo(3)
except ZeroDivisionError:
    print("ZeroDivision Error Occurred and Handled")

# serializing this array using pick dump
x = [1, 2, 3, 4, 5]
file = open("PickleList.txt", "wb")  # wb is to write binary
pickle.dump(x, file)
file.close()

# de-serializing a binary file
file = open("PickleList.txt", "rb")  # rb is to read from binary
x = pickle.load(file)
print(x)
