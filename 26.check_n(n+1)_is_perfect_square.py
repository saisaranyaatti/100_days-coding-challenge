def check(n):
    n=int(str(n)+str(n+1))
    k=n**0.5
    return k.is_integer()
n=int(input())
print(check(n))
