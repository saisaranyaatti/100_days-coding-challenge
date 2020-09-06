#before nearest fibnocci for given number
def before_near_fib(n):
    a=0
    b=1
    while n>=b:
        c=a+b
        a=b
        b=c
    return a
n=int(input())
print(before_near_fib(n))


#after nearest fibnocci for a given number
def after_near_fib(n):
    a=0
    b=1
    while n>=b:
        c=a+b
        a=b
        b=c
    return b
n=int(input())
print(after_near_fib(n))



#near fibnocci number for a given number
def near_fibnocci(n):
    a=0
    b=1
    while n>=b:
        c=a+b
        a=b
        b=c
    if abs(a-n)>abs(b-n):
        return b
    return a
n=int(input())
print(near_fibnocci(n))
