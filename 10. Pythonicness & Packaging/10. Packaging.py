In Python, the term packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease.
This involves use of the modules setuptools and distutils.
The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as an important file called setup.py.
Example directory structure:
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

