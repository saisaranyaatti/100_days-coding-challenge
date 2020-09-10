#collatz sequence
def collatz_sequence(n):
    print(n,end=" ")
    while n>1:
        if n%2==0:
            n//=2
            print(n,end=" ")
        else:
            n=n*3+1
            print(n,end=" ")
n=int(input())
collatz_sequence(n)

def collatz(n):
    if n==1:
        return 1
    if n%2==0:
        n1=n//2
    else:
        n1=n*3+1
    return str(n)+" "+str(collatz(n1))
n=int(input())
print(collatz(n))
