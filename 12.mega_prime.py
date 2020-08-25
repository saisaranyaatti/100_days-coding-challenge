#mega prime
import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            break
    else:
        return n
def mega_prime(r):
    a=r
    c=0
    if prime(r)==r:
        print("prime")
        while r>0:
            rem=r%10
            if prime(rem)==rem:
                c+=1
            else:
                break
            r//=10
    else:
        print("not prime")
    if c==len(str(a)):
        print("mega prime")
    else:
        print("not mega prime")
r=int(input())
mega_prime(r)
