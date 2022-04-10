# Enter a number or a range spaced by a blanck space to verify.. 
# if a number is prime or if you want to get a range of prime numbers respectively.
from functools import reduce

def prime(x):
    return x>=2 and not list(filter(lambda i: x%i==0 and x!=2, range(2,x//2+1)))

def first(p):

    if p<1 or int(p)!=p:
        print("-"*len("|Enter an integer greater than 0.|")+"\n|Enter an integer greater than 0.|\n"+"-"*len("|Enter an integer greater than 0.|"))
    else:
        def f(n):
            c=0
            l=2
            while n!=c:
                if prime(l):
                    yield l
                    c+=1
                l+=1
    
        return list(f(p))

def prime_division(n):
    choix = list(filter(prime, range(2,n//2+1)))
    base=[]
    ex=[]
    #resp = {}
    
    c=0
    
    for elem in choix:
        if n%elem==0:
            base.append(elem)
        while n%elem==0:
            c+=1
            n=n//elem
        ex.append(c)
        c=0
        
    #for l in range(0,len(base)):
        #resp[base[l]]=list(filter(lambda z: z!=0, ex))[l]
        
    return {base:exp for base,exp in zip(base,(b for b in exp if b!=0))}

def int_from_prime_div(y):
    return int(reduce(lambda c,q:c*q, (k*v for (k,v) in y.items())))

#only the code after this line will be executed if you run this program. This is the script.
#-------------------------------------------------------------------------------------------

if __name__=="__main__":
    
    r = list(map(lambda i:int(i), input().split(" ")))
        
    if len(r)!=1:
        res = list(filter(prime, range(r[0],r[1]+1)))
        print("-"*len(f"|The prime numbers from {r[0]} to {r[1]} are: {res if res else 'none'} .|"))
        
        print(f"|The prime numbers from {r[0]} to {r[1]} are: {res if res else 'none'} .|")
        
        print("-"*len(f"|The prime numbers from {r[0]} to {r[1]} are: {res if res else 'none'} .|"))
    else:
        print("-"*len(f"|{r[0]} is{' ' if prime(r[0]) else ' not '}a prime number.|"))
        
        print(f"|{r[0]} is{' ' if prime(r[0]) else ' not '}a prime number.|")
        
        print("-"*len(f"|{r[0]} is{' ' if prime(r[0]) else ' not '}a prime number.|"))
#



