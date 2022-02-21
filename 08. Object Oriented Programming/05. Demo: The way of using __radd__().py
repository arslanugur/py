class A:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __radd__(self, other):
        return A(self.x + other.x, self.y + other.y)

one = A(1, 1)
sec = B(1, 1)
third = B(2, 3)

print('Type of object one,', type(one))
print('\nType of object sec,', type(sec))

if type(one) is type(sec):
    print('\nTrue, type of A() is same as type of B().')
else:
    print('\nFalse, A() and B() are different types.')

if type(sec) is type(third):
    print('\nTrue, objects sec and third are the same type created by class B.\n')
else:
    print('\nFalse, objects sec and third are different types.\n')

# The expression one + third is translated into one.__add__(third). 
# However, if one hasn't implemented __add__, and one and third are of different types, then third.__radd__(one) is called. 

new = one + third
print('Attributes of new object --> ', new.x, ',', new.y)



