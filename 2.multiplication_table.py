#printing multiplication table using for loop
n=int(input("enter a number"))
r1=int(input("enter starting range"))
r2=int(input("enter ending range"))
if r1<r2:
    for i in range(r1,r2+1,1):
        print(n,"*",i,"=",n*i)
else:
    for i in range(r1,r2-1,-1):
        print(n,"*",i,"=",n*i)



#printing multiplication table using while loop
n=int(input("enter a number"))
r1=int(input("enter starting range"))
r2=int(input("enter ending range"))
if r1<r2:
    while r1<=r2:
        print(n,"*",r1,"=",n*r1)
        r1+=1
else:
    while r1>=r2:
        print(n,"*",r1,"=",n*r2)
        r1-=1

