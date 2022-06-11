# 01. Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")



# 02. Python If-Else
if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")



# 03. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a + b)
    print(a - b)
    print(a * b)



# 04. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)



# 05. Loops
if __name__ == '__main__':
    n = int(input())

    num = 0
    while num < n:
        print(pow(num, 2))
        num += 1



# 06. Print Function
if __name__ == '__main__':
    n = int(input())
    
    num = 1
    while num <= n:
        print(num, end='')
        num += 1



# 07. Write a Function
def is_leap(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))


