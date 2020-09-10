def perfect_number(n):
    c=0
    for i in range(1,int(n//2)+1):
        if n%i==0:              
            c+=i
    if c==n:
        return "True"
    else:
        return "False"
n=int(input())
print(perfect_number(n))
