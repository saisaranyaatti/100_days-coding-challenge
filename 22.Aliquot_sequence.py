#aliquot sequence
def aliquot_seq(n):
    print(n,end=" ")
    while n>1:
        c=0
        for i in range(1,int(n//2)+1):
            if n%i==0:
                c+=i
        print(c,end=" ")
        if n==c:
            break
        n=c
n=int(input())
aliquot_seq(n)


def aliquot_seq1(n):
    if n==1:
        return 1
    else:
        c=0
        for i in range(1,int(n//2)+1):
            if n%i==0:
                c+=i
        if n!=c:
            return str(n)+" "+str(aliquot_seq1(c))
        else:
            return n
n=int(input())
print(aliquot_seq1(n))
    
