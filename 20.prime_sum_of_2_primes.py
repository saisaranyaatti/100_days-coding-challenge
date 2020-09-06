#checking the prime number is sum of primes or not
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n
def check_prime_sum(n):
    if prime(n)==n and prime(n-2)==n-2:#check the given number and number-2 are primes or not
        return("num can be expressed as the sum of two primes",n-2,2)
    else:
        return("num cannot be expressed as the sum of two primes")
n=int(input())
print(check_prime_sum(n))
#checkig the prime number is the sum of primes or not
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n

def check_prime_sum(n):
    if prime(n)==n:
        c=0
        for i in range(n-1,1,-1):
            if prime(i)==i:
                for j in range(n-2,1,-1):
                    if prime(j)==j:
                        if i+j==n:
                            c+=1
                break
        if c==1:
            return (n,"can be expressed the sum of two primes",i,j)
        
        else:
            return (n,"canot be expressed as the sum of two primes")
                
    else:
        print(n,"is not prime")
n=int(input("enter a number"))
print(check_prime_sum(n))
                
