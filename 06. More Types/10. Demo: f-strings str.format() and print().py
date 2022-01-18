# version from 3.5 to 3.7, f-strings that
# were introduced in Python 3.6 are now available.
#
# These examples compare f-strings with the string.format() method.
#
# For completeness, the use of the print() function is also compared.
#
# Turn phone sideways for better view.
#
# More info at: https://realpython.com/python-f-strings/
# See also: https://www.python.org/dev/peps/pep-0498/

import platform as p

# verify Python version
print("Current Python version:")
print(p.python_version(), p.python_build()[1])
print()

# assign example variables
a = "apple"
b = "banana"
m = 10
n = 25
lst = [a, m, n]
print(f"a = '{a}'")
print(f"b = '{b}'")
print("m =", m)
print("n =", n)
print(f"lst = {lst}")
print()
print()

# compare using simple interpolation
print("=== string.format() with simple interpolation ===")
print()
print('print("I will eat {} {}s and {} {}s.".format(m, a, n, b))')
print("output: ", end="")
print("I will eat {} {}s and {} {}s.".format(m, a, n, b))
print()
print()
print("=== f-string with simple interpolation ===")
print()
print('print(f"I will eat {m} {a}s and {n} {b}s.")')
print("output: ", end="")
print(f"I will eat {m} {a}s and {n} {b}s.")
print()
print()
print("=== print() with simple interpolation ===")
print()
print('print("I will eat", m, a + "s and", n, b + "s.")')
print("output: ", end="")
print("I will eat", m, a + "s and", n, b + "s.")
print()
print()

# compare using a math expression
print("=== string.format() with a math expression ===")
print()
print('print("{} + {} = {} but {} + {} = {}.".format(m, n, m + n, a, b, a + b))')
print("output: ", end="")
print("{} + {} = {} but {} + {} = {}.".format(m, n, m + n, a, b, a + b))
print()
print()
print("=== f-string with a math expression ===")
print()
print('print(f"{m} + {n} = {m + n} but {a} + {b} = {a + b}.")')
print("output: ", end="")
print(f"{m} + {n} = {m + n} but {a} + {b} = {a + b}.")
print()
print()
print("=== print() with a math expression ===")
print('print(m, "+", n, "=", m + n, "but", a, "+", b, "=", a + b + ".")')
print("output: ", end="")
print(m, "+", n, "=", m + n, "but", a, "+", b, "=", a + b + ".")
print()
print()

# compare using an 'if'...'else' expression
print("=== string.format() with an 'if'...'else' expression ===")
print()
print('print("Yes, we have {}{}s!".format("" if b in lst else "no ", b))')
print("output: ", end="")
print("Yes, we have {}{}s!".format("" if b in lst else "no ", b))
print()
print()
print("=== f-string with an 'if'...'else' expression ===")
print()
print("""print(f"Yes, we have{' ' if b in lst else ' no '}{b}s!")""")
print("output: ", end="")
print(f"Yes, we have{' ' if b in lst else ' no '}{b}s!")
print()
print()
print("=== print() with an 'if'...'else' expression ===")
print()
print('print("Yes, we have", "" if b in lst else "no", b + "s!")')
print("output: ", end="")
print("Yes, we have", "" if b in lst else "no", b + "s!")



# Output:
"""
Current Python version:
3.8.11 Aug 17 2021 03:04:29

a = 'apple'
b = 'banana'
m = 10
n = 25
lst = ['apple', 10, 25]


=== string.format() with simple interpolation ===

print("I will eat {} {}s and {} {}s.".format(m, a, n, b))
output: I will eat 10 apples and 25 bananas.


=== f-string with simple interpolation ===

print(f"I will eat {m} {a}s and {n} {b}s.")
output: I will eat 10 apples and 25 bananas.


=== print() with simple interpolation ===

print("I will eat", m, a + "s and", n, b + "s.")
output: I will eat 10 apples and 25 bananas.


=== string.format() with a math expression ===

print("{} + {} = {} but {} + {} = {}.".format(m, n, m + n, a, b, a + b))
output: 10 + 25 = 35 but apple + banana = applebanana.


=== f-string with a math expression ===

print(f"{m} + {n} = {m + n} but {a} + {b} = {a + b}.")
output: 10 + 25 = 35 but apple + banana = applebanana.


=== print() with a math expression ===
print(m, "+", n, "=", m + n, "but", a, "+", b, "=", a + b + ".")
output: 10 + 25 = 35 but apple + banana = applebanana.


=== string.format() with an 'if'...'else' expression ===

print("Yes, we have {}{}s!".format("" if b in lst else "no ", b))
output: Yes, we have no bananas!


=== f-string with an 'if'...'else' expression ===

print(f"Yes, we have{' ' if b in lst else ' no '}{b}s!")
output: Yes, we have no bananas!


=== print() with an 'if'...'else' expression ===

print("Yes, we have", "" if b in lst else "no", b + "s!")
output: Yes, we have no bananas!
"""



