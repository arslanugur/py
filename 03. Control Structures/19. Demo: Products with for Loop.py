# Example: Which numbers in the list are a multiple of 3?
numbers = [1,3,5,7,9,11,13,15]

for number in numbers: 
# All the numbers in the list will be in the variable "number" so that multiple of 3 can be checked 
# We use a modulus, if the remainder is 0, the number is a multiple of 3 
    if (number%3==0): 
        print(number)


# Example: What is the sum of the numbers in the list of numbers?
numbers = [1,3,5,7,9,11,13,15]

total = 0               # Numbers will be added to this variable one by one
for number in numbers:  # Likewise, we should go through the list one by one 
# Each incoming number information is taken into the "total" variable, but the sum formula must be defined before entering the for loop. 
    total += number     # long version --->  total = total + number
# When the loop starts the "total" will be 1 
# It will add up with the second number in the list and the "total" = 1, and it will give the new "total" and the loop will continue like this. 
print('total: ', total)


# Example: square the odd numbers in a list of "numbers" 
numbers = [1,3,5,7,9,11,13,15]

for number in numbers:
# How do we know whether a number is odd or not?
# if the coming number from the loop is even (number %2 == 0) 
# but we need odd number therefore the return value is 1
    if (number %2 == 1):
# if the number is odd, the square of the reached number is taken 
        print(number ** 2)



# Example: Which of the cities has a maximum of 6 characters? 
cities = ['Angeles', 'Berlin', 'London', 'Amsterdam', 'Tokyo']
# we should go through the list one by one again 
for city in cities:
    if (len(city) <= 6):
        print(city)
# The character count of the incoming city is taken with len, if it equals 6 or smaller, print the city





#Examples: Products
products = [
    {'name': 'Samsung s5', 'Price': '3000' },
    {'name': 'Samsung s6', 'Price': '4000' },
    {'name': 'Samsung s7', 'Price': '5000' },
    {'name': 'Samsung s8', 'Price': '6000' },
    {'name': 'Samsung s9', 'Price': '7000' }
]
# Each list element - dictionary data type
# To go through with for loop

# Example: What is the sum of the prices of the products?
total = 0 #toplamı tutcağımız için bi değişken tanımlayalım
for product in products:
    # print(product)        # each dict data type comes out of the list and is written as a line.
    # print(product[price]) # only print the price
# we need to convert the prices of the incoming products from string type to integer 
    pris = int(product['Price'])
    total += pris
# döngüden çıktıktan sonra yazdır, total formülün altına print edersek her seferinde yazdırır bu gereksiz
# print it after exiting the loop, it prints every time when printing under the "total" formula, but this is unnecessary 
print(total)                # print('total product price', total)


# Example: Show products with a maximum price of 5000 from products 
for product in products:
    if (int(product['Price']) <= 5000):
        print(product['name'])  # we will reach the name of the product we have reached at that moment 
                                # products under 5000



 
