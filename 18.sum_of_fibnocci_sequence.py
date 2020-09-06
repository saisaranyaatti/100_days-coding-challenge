#sum of fibnocci sequence in a given range using for loop
def fibnocci_sum(n):
    a=0
    b=1
    s=a+b
    for i in range(2,n):
        c=a+b
        s+=c
        a=b
        b=c
    return s
n=int(input())
print(fibnocci_sum(n))


#sum of fibnocci sequence in a given range using while loop
def fibnocci_sum(n):
    a=0
    b=1
    s=a+b
    i=2
    while i<n:
        s+=a+b
        a,b=b,a+b
        i+=1
    return s
n=int(input())
print(fibnocci_sum(n))
        
