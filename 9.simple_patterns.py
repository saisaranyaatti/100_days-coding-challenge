1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

1
22
333
4444
55555

n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()
        #or
n=int(input("enter a number"))
for i in range(1,n+1):
    print(str(i)*i)
        #or
n=int(input("enter a number"))
for i in range(1,n+1):
    print((10**i//9)*i)

    
*
**
***
****
*****

n=int(input("enter a number"))
for i in range(n+1):
    print("*"*i)

    
*****
****
***
**
*

n=int(input("enter a number"))
for i in range(n+1):
    print("*"*(n-i))
    #or
n=int(input("enter a number"))
for i in range(n+1):
    for j in range(n-i):
        print("*",end="")
    print()

    *
   **
  ***
 ****
*****
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print(chr(j+65),end="")
    print()

AAAAA
BBBBB
CCCCC
DDDDD
EEEEE

n=int(input("enter a number"))
for i in range(n):
    print(chr(i+65)*n)

A
BB
CCC
DDDD
EEEEE

n=int(input("enter a number"))
for i in range(n):
    print(chr(i+65)*(i+1))














