from itertools import count

# An example of when a generator can be useful:
# Imagine you want to test a hacked version of the Collatz algorithm:
# at each step, 
# when n is odd, you will multiply it by a multiple of 3, being 3*k, and you want 'k' to increase by one everytime it's used.
# when n is even, you will devide it by a power of 2, being 2**p, and you want 'p' to increase by one everytime it's used.
# There are other way to do it, but using generators is quite convenient here.

# These two generators are prepared to produce an infinity of numbers, but they don't do anything until you want them to.
# next(your_generator) will produce the next output of your generator, then stop and wait for the next call.
# Memory and time are preserved, and also, you don't know how many numbers you'll need.
multiples_of_3_generator = (3*k for k in count(1))
powers_of_2_generator = (2**p for p in count(1))

# be carefull: if you want to re-use your generator later, it will keep memory of the previous calls you asked him:
print("the generator used on 10 iterations:")
for i in range(10):
  print(next(multiples_of_3_generator))
print()
# even if you rename it:
m3g = multiples_of_3_generator
print("renamed it ...")
for i in range(10):
  print(next(m3g))
print("... oups, it did not restart:")
print()

# A nice way to create a re-usable generator is to build a function with yield.
def multiples_of_3_generator():
  for k in count(1):
    yield 3*k

def powers_of_2_generator():
  for p in count(1):
    yield 2**p

# But then, you will need to create your generator from your yielding function, the usual mistake to avoid is the following:
print("the wrong way:")
for i in range(10):
  print(next(multiples_of_3_generator()))
print()
# The right way is:
m3gen = multiples_of_3_generator()
print("first generator:")
for i in range(10):
  print(next(m3gen))
print()
# Every call of the function will create a new generator, and thus it will start again with the first elements:
m3gen = multiples_of_3_generator()
print("new generator:")
for i in range(10):
  print(next(m3gen))
print()

# Let's use our generators in our bizarre collatz function.
# We don't know how our function will behave, let's imagine it will reach '1' as the usual Collatz does.
# That's the reason for "while coll!=1:"
# but if '1' is never reached, an infinite loop will occur (we don't like infinite loops).
# at each iteration, yield will send the current value of coll, but it's not produced until you call it, just as in the above generators. 
# With next(), you will call the next step of your generator's production. That way, you're safe and can try a number of iteration, let's see what 40 does !
def collhacked(n):
  coll = n
  gen_3m = multiples_of_3_generator()
  gen_2p = powers_of_2_generator()
  while coll!=1:
    if coll%2: coll = coll*next(gen_3m)+1
    else: coll //= next(gen_2p)
    yield coll

# let's try it with 311 as a starting 'n'
n = 311
funny_collatz_inspired_generator = collhacked(n)
print("trying our collhacked function:")
for i in range(40):
  print(next(funny_collatz_inspired_generator,"1 reached !"))



