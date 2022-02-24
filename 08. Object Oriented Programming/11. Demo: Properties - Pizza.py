#so at this pizza place, I can call back and change my toppings, but they need to make sure that all pizzas go out with dough, cheese, and sauce, regardless of the toppings you choose or change
#they also only take cash.

# The idea behind @property here is that they give instances of the class some intrinsic value(s) that CAN be easily seen/accessed/used (unlike private methods), but they CAN'T BE MODIFIED.
# here, we define 2 @properties and one normal __init__ attribute

#in this script, which translates the customers order into the info that the cooks and cashiers need, specifies the toppins, all ingredients needed for the pizza to be made, and the payment method.

# self.toppings is an __init__ attribute, and can be accessed and changed at any time
# self.all_ingredients is an @property method, so it can be accessed but can't be modified... this one however inherits from the modifyable self.toppings attribute, so it will always contain 'dough', 'cheese', and 'sauce', plus whatever you want to do with the self.toppings, but I can't change it becuase I'm afraid I might forget to include the 'dough'
# self.payment is an @property method, so it can be accessed but it can't be modified. they only take cash, no negociating.

# I also created a special error-checking function so that the entire program would run through while still showing where errors would occur (ie when we try to change an @property)

class PizzaPizza:
    def __init__(self, toppings, size):
        self.toppings = toppings
        self.size = size
    @property
    def ingredients(self):
        return self.toppings + ["dough", "sauce", "cheese"]
    @property
    def payment(self):
        return "cash"


def order_slip(self):
    print(self.toppings)
    print(self.ingredients)
    print(self.payment)
    print("\n")


#hi.. I'd like an olive/anchovy 'pizzaaa'
my_pizza = PizzaPizza(["olives", "anchovies"], "large")
order_slip(my_pizza)

#waitwait... actually I want meatlovers instead!!
#@DIW
my_pizza.toppings = ["meatballs", "sausage", "pepparoni"]
order_slip(my_pizza)

#but because ingredients are an @propterty, I can't change them. because what if I forgot to add the dough again!?
try:
    my_pizza.ingredients = ["sauce", "cheese", "meatballs", "sausage", "pepparoni"]
except AttributeError:
    print("can't modify an @property! \n")
    order_slip(my_pizza)

#call back.. can i actually pay with cash instead? -NOPE: its an @property now
try:
    my_pizza.payment = "credit"
except AttributeError:
    print("can't modify an @property! \n")
    order_slip(my_pizza)
#


    
    
