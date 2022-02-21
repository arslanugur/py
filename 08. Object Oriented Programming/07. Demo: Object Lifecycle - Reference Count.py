from sys import getrefcount

class Dog:
    def __init__(self):
        print('Dog created!!')


def main() -> None:
    """
    Nothing!
    """
    reference_dog = getrefcount(Dog)
    print('Dog                 :', reference_dog)
    print('# Dog class start with x# of references')
    print('# in this example start with %i.' % reference_dog)
    print('# It happens in the compile time')
    print('# when Python build the class.')
    print('------------------------')

    print('charlie = Dog()')
    charlie = Dog()
    reference_dog = getrefcount(Dog)
    print('Dog                 :', getrefcount(Dog))
    print('charlie             :', getrefcount(charlie))
    print('# The dog is instantiated to Charlie.')
    print('# Charlie start with 2 references.')
    print('# Dog class increase by one: %i -> %i.' % (reference_dog - 1, reference_dog))
    print('------------------------')

    print('cat = charlie')
    cat = charlie
    reference_dog = getrefcount(Dog)
    print('Dog                 :', getrefcount(Dog))
    print('charlie             :', getrefcount(charlie))
    print('cat                 :', getrefcount(cat))
    print('# Copy Charlie into a new var: cat.')
    print('# *** Interesting things happen.')
    print('# Charlie increase by one: 2 -> 3.')
    print('# Cat has 3 references.')
    print('# Dog KEEP %i references.' % reference_dog)
    print('------------------------')

    print('bella = Dog()')
    bella = Dog()
    reference_dog = getrefcount(Dog)
    print('Dog                 :', getrefcount(Dog))
    print('bella               :', getrefcount(bella))
    print('# The dog is instantiated to Bella.')
    print('# Bella start with 2 references.')
    print('# Dog class increase by one: %i -> %i.' % (reference_dog - 1, reference_dog))
    print('------------------------')

    print('del charlie')
    del charlie
    reference_dog = getrefcount(Dog)
    print('Dog                 :', getrefcount(Dog))
    print('cat                 :', getrefcount(cat))
    print('# Delete the object Charlie.')
    print('# *** Interesting things happen.')
    print('# Cat decrease by one: 3 -> 2.')
    print('# Dog KEEP %i references.' % reference_dog)
    print('# ')
    print('------------------------')

    print('del bella')
    del bella
    reference_dog = getrefcount(Dog)
    print('Dog                 :', getrefcount(Dog))
    print('# Delete the object Bella.')
    print('# Dog decrease by one: %i -> %i.' % (reference_dog + 1, reference_dog))
    print('------------------------')

    print('del cat')
    del cat
    reference_dog = getrefcount(Dog)
    print('Dog                 :', getrefcount(Dog))
    print('# Delete the object cat.')
    print('# *** Interesting things happen.')
    print('# Dog decrease by one: %i -> %i' % (reference_dog + 1, reference_dog))
    print('# because Charlie and cat were')
    print('# the same object when we deleted')
    print('# Charlie it only decreased by one')
    print('# the reference of cat-charlie object')
    print('# cat had 2 references when we deleted')
    print('# cat it decreased to Zero the references')
    print('# also the Dog class decreased by one')
    print('# the references.')
    print('------------------------')


if __name__ == "__main__":
    main()
#


# Output:
"""
Dog                 : 5
# Dog class start with x# of references
# in this example start with 5.
# It happens in the compile time
# when Python build the class.
------------------------
charlie = Dog()
Dog created!!
Dog                 : 6
charlie             : 2
# The dog is instantiated to Charlie.
# Charlie start with 2 references.
# Dog class increase by one: 5 -> 6.
------------------------
cat = charlie
Dog                 : 6
charlie             : 3
cat                 : 3
# Copy Charlie into a new var: cat.
# *** Interesting things happen.
# Charlie increase by one: 2 -> 3.
# Cat has 3 references.
# Dog KEEP 6 references.
------------------------
bella = Dog()
Dog created!!
Dog                 : 7
bella               : 2
# The dog is instantiated to Bella.
# Bella start with 2 references.
# Dog class increase by one: 6 -> 7.
------------------------
del charlie
Dog                 : 7
cat                 : 2
# Delete the object Charlie.
# *** Interesting things happen.
# Cat decrease by one: 3 -> 2.
# Dog KEEP 7 references.
# 
------------------------
del bella
Dog                 : 6
# Delete the object Bella.
# Dog decrease by one: 7 -> 6.
------------------------
del cat
Dog                 : 5
# Delete the object cat.
# *** Interesting things happen.
# Dog decrease by one: 6 -> 5
# because Charlie and cat were
# the same object when we deleted
# Charlie it only decreased by one
# the reference of cat-charlie object
# cat had 2 references when we deleted
# cat it decreased to Zero the references
# also the Dog class decreased by one
# the references.
------------------------
"""




