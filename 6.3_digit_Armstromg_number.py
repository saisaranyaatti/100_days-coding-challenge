def armstrong(n):
    temp=n
    sum=0
    while n>0:
        rem=n%10
        sum+=rem**3
        n//=10
    if sum==temp:
        return True
    else:
        return False
n=int(input("enter a number"))
print(armstrong(n))

def armstrong(n):
    sum=0
    for i in n:
        sum+=int(i)**3
    if sum==int(n):
        return True
    else:
        return False
n=input("enter a number")
print(armstrong(n))


def armstrong(n):
    if n==0:
        return 0
    else:
        return (n%10)**3+armstrong(n//10)
n=int(input("enter a number"))
if(armstrong(n)==n):
    print("True")
else:
    print("False")


    
    
    
