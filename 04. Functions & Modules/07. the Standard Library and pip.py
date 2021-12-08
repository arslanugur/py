# There are three main types of modules in Python, 
# those you write yourself, those you install from external sources, and those that are preinstalled with Python.
# The last type is called the standard library, and contains many useful modules. 
# Some of the standard library's useful modules include .. 
          # .. string, re (regular expressions), datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

# Tasks that can be done by the standard library include ..
          # .. string parsing, data serialization, testing, debugging and manipulating dates, emails, command line arguments, and much more!

# Python's extensive standard library is one of its main strengths as a language.


# the STANDARD LIBRARY
# Python Preinstalled Modules
# Some of the modules in the standard library are written in Python, and some are written in C.
              # The original Python is written in C and the Python interpreter can import C modules for improved performance, primarily. 
              # Also, there are existing C programs that can be used without having to write everything in Python.
# Most are available on all platforms, but some are Windows or Unix specific. 

# We won't cover all of the modules in the standard library; there are simply too many. 
# The complete documentation for the standard library is available online at www.python.org.
              # https://docs.python.org/3.2/library/index.html


# MODULES
# Many third-party Python modules are stored on the Python Package Index (PyPI).
# The best way to install these is using a program called pip. 
# This comes installed by default with modern distributions of Python. 
# If you don't have it, it is easy to install online. Once you have it, installing libraries from PyPI is easy. 
# Look up the name of the library you want to install, go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name. 
# Once you've done this, import the library and use it in your code.

# Using pip is the standard way of installing libraries on most operating systems, but some libraries have prebuilt binaries for Windows. 
# These are normal executable files that let you install libraries with a GUI the same way you would install other programs.
# It's important to enter pip commands at the command line, not the Python interpreter.

# https://en.wikipedia.org/wiki/List_of_Python_software

# What does PyPI stand for?  -->  Python Package Index


# Example: Date and Time Module 
# The program shows the use of date and time module for manipulating and formatting dates and times. 
import time
import datetime

print("Time in seconds since epoch:")
print(time.time())

print("\nCurrent date and time:")
print(datetime.datetime.now())

print("\nFormatting the current date and time using strftime():")
print(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

print("\nOr formatting it like this:")
print(datetime.datetime.now().strftime("%d-%m-%y and %H:%M"))

print("\nCurrent Year:")
print(datetime.datetime.now().strftime("%Y"))

print("\nCurrent Month of the year:")
print(datetime.datetime.now().strftime("%B"))

print("\nWeek number of the year:")
print(datetime.date.today().strftime("%W"))

print("\nWeekday of week:")
print(datetime.date.today().strftime("%w"))

print("\nDay of the year:")
print(datetime.datetime.now().strftime("%j"))

print("\nDay of the month:")
print(datetime.datetime.now().strftime("%d"))

print("\nDay of the week:")
print(datetime.datetime.now().strftime("%A"))

print("\nTime tuple for local time:")
print(time.localtime(time.time()))

print("\n Formatting it in readable form:")
print(time.asctime( time.localtime(time.time()) ))

print("\nWeekday of a certain date:")
my_date=datetime.date(1996,7,19) #yyyy-mm-dd.
print(my_date.strftime("%A"))



