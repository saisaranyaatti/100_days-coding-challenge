

#super prime
'''super_prime:the positon of the prime number from the starting prime is also prime then we call that prime as super prime''' 
#checking the number is super prime or not using for loop
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n
def super_prime(n):
    if prime(n)==n:
        c=0
        for i in range(n,1,-1):
            if prime(i)==i:
                c+=1
        print(c)
        if prime(c)==c:
            print("super prime")
        else:
         print("not super prime")
    else:
        print("not prime")
n=int(input("enter  a number"))
super_prime(n)


#checking the number is super prime or not using while loop
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n
def super_prime(n):
    if prime(n)==n:
        print("prime")
        i=n-1
        c=0
        while True:
            if i==1:
                break
            if prime(i)==i:
                c+=1
            i-=1
        print(c+1)
        if prime(c+1)==c+1:
            print("super prime")
        else:
            print("not")
    else:
        print("not prime")
n=int(input("enter a number"))
super_prime(n)

#checking the given number is super prime or not using lists
import math
def prime(n):
    if n>1:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                break
        else:
            return n
def super_prime(n):
    if prime(n)==n:
        l=[]
        for i in range(n,1,-1):
            if prime(i)==i:
                l.append(i)
        k=len(l)
        if prime(k)==k:
            print("super prime")
        else:
            print("not")
    else:
        print("not prime")
n=int(input("enter a number"))
super_prime(n)

            
