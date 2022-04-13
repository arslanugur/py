# SECTION 1
# In Python, the term packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease.
# This involves use of the modules setuptools and distutils.
# The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
# This directory goes into another directory containing the readme and license, as well as an important file called setup.py.
# Example directory structure:
folderA/                  # the Parent folder
   LICENSE.txt
   README.txt
   setup.py
   folderB/
      __init__.py
      codeexample.py
      codeexample2.py
# You can place as many script files in the directory as you need.

# this guide is a bit deprecated, because in late Python versions it is not necessary to add __init__.py, 
# Python 3.3+ has Implicit Namespace Packages which allow it to create a packages without an __init__.py file.

# Which file is placed in a directory to make it a package? ---> __init__.py

# Working with Python packages is really simple. 
# All you need to do is: 
# 1. Create a directory and give it your package's name. 
# 2. Put your classes in it. 
# 3. Create a __init__.py file in the directory

# SECTION 2
# The next step in packaging is to write the setup.py file.
# This contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip (name, version, etc.).
# Example of a setup.py file:
from distutils.core import setup

setup(
   name='codeexample', 
   version='0.1dev',
   packages=['codeexample',],
   license='MIT', 
   long_description=open('README.txt').read(),
)
# After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
# To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
# Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution.
# Use python setup.py register, followed by python setup.py sdist upload to upload a package.

# Finally, install a package with python setup.py install.

# Warning: In other resources you may encounter references to using python setup.py register and python setup.py upload. 
# These methods of registering and uploading a package are strongly discouraged 
# as it may use a plaintext HTTP or unverified HTTPS connection on some Python versions, 
# allowing your username and password to be intercepted during transmission.
# this is the link to it: https://packaging.python.org/tutorials/distributing-packages/#id74


# At first, you should understand this 3 words. 
# First, Pypl - this is python storage you can search and download https://pypi.org/ 
# Second, Command - This is command to run some process on shell script like powershell, bash shell. 
# Third, Distribution - Make your program or package ready to use someone or just yourself. 
# Especially Distribution is very vagueous words as alway. 'python setup.py sdist ' meaning source distribution. 
# 'python setup.py bdist(or bdist_wininst)' mening build a binary distribution 'python setup.py sdist upload' is doing upload package to pypl. 
# 'python setup.py register' meaning register your distributed program or package to pypl or etc. 
# To install this package, python setup.py install on your shell.


# What is the command used for bulding a source distribution? --> python setup.py sdist


https://www.sololearn.com/learning/1073/2490/5204/2 comments
   
   
   




