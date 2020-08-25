#nearest prime
import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            break
    else:
        return n
n=int(input())
def nearest_prime(n):
    for i in range(n-1,0,-1):
        if prime(i)==i:
            a=i
            break
    print(a)
    i=n+1
    while True:
        if prime(i)==i:
            b=i
            break
        i+=1
    print(b)
    if abs(n-a)>abs(n-b):
        print(b,"is nearest")
    elif abs(n-a)==abs(n-b):
        print(a,b,"both are near")
    else:
        print(a,"is near")
nearest_prime(n)

