#fibnocci sequence
#0 1 1 2 3 5 8 13.............
#using for loop
def fibnocci(n):
    n1=0
    n2=1
    print(n1,n2,end=" ")
    for i in range(2,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
n=int(input("enter a number"))
fibnocci(n)

#using while loop
def fibnocci(n):    
    n1=0
    n2=1
    print(n1,n2,end=" ")
    i=2
    while i<n:
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
        i+=1
n=int(input("enter a number"))
fibnocci(n)



#using list
n=int(input())
l=[0,1]
for i in range(n-2):
    l.append(i+(i+1))
print(l)


    
    
