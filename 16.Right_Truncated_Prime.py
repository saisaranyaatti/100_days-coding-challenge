#Right_Truncated_Prime
'''239=it has to be prime
   23=it has to prime
   2=it has to prime       by truncated the right side digit the remaining digit has to be prime then that is called as right truncated prime'''
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n
def right_truncated_prime(n):
    if prime(n)==n:
        print("prime")
        c=0
        k=n//10
        while k>0:
            if prime(k)==k:
                c+=1
            k//=10
        if c==len(str(n))-1:
            print("right truncated prime")
        else:
            print("not right truncated prime")
    else:
        print("not prime")
n=int(input())
right_truncated_prime(n)
            
