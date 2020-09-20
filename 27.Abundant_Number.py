'''Abundant_Number:a number is called as abundant number if the sum of factors
of that number except it self is greater than that number'''
def Abundant_Number(n):
    s=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if n==i:
                s+=i
            else:
                s+=i+n//i
    print(s-n)
    if (s-n)>n:
        return "Abundant Number"
    else:
        return "Not Abundant Number"
n=int(input())
print(Abundant_Number(n))
