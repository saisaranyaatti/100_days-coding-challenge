#special_prime
'''special_prime:a prime number is equal to the sum of two before consecutive numbers and 1 is equal to
that prime number then we call that prime as special prime. ex:19=11+7+1'''
import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            break
    else:
        return n
def nearest_prime(n):
    i=n-1
    while True:
        if prime(i):
            return i
        else:
            i-=1
    
def special_prime(n):
    if prime(n)==n:
        a=nearest_prime(n)
        b=nearest_prime(a)
        while True:
            if a+b+1==n:
                print("special_prime")
                break
            else:
                a=b
                b=nearest_prime(a)
            if a==2 or b==2:
                print("not special prime")
                break
    else:
        print("not prime")
n=int(input())
special_prime(n)
            
            
