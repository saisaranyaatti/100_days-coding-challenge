#LCM
def lcm(n1,n2):
    if n1>n2:
        great=n1
    else:
        great=n2
    while True:
        if great%n1==0 and great%n2==0:
            return great
            break
        great+=1
n1=int(input())
n2=int(input())
print(lcm(n1,n2))

#GCD
def gcd(n1,n2):
    if n1>n2:
        small=n2
    else:
        small=n1
    for i in range(1,small+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd
n1=int(input())
n2=int(input())
print(gcd(n1,n2))

#LCM and GCD by recursion
def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)
a=int(input())
b=int(input())
print(gcd(a,b))
print(lcm(a,b))




    
