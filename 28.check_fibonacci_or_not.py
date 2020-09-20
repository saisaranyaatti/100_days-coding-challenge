def fibnocci(n):
    a=0
    b=1
    c=0
    while True:
        c=a+b
        a,b=b,c
        if c==n:
            print("fibonacci")
            break
        if c>n:
            print("not fibonacci")
            break
            
n=int(input())
fibnocci(n)
