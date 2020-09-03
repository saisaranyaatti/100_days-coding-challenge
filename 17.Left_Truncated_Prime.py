#Left Truncated Prime
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n
def left_truncated_prime(n):
    if prime(n)==n:
        c=0
        for i in range(1,len(str(n))):
            k=str(n)
            if prime(int(k[i:]))==int(k[i:]):
                c+=1
        if c==len(str(n))-1:
            print("left truncated prime")
        else:
            print("not left truncated prime")
            
    else:
        print("not prime")
n=int(input())
left_truncated_prime(n)



import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
                break
        else:
            return  True
def left_truncated_prime(n):
    if prime(n)==False:
        return False
    while n:
        if prime(n)==False:
            return False
        n%=10**(len(str(n))-1)
    return True
n=int(input())
print(left_truncated_prime(n))
                        
               
