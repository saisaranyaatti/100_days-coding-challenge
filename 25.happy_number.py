#Happy Number

'''19=1**2+8**2=82
82=8**2+2**2=68
68=6**2+8**2=100
100=1**2+0**2+0**2=1
so 19 is happy number'''
def happy_num(n):
    while n>9:
        k=n
        c=0
        while k>0:
            rem=k%10
            c+=rem**2
            k//=10
        n=c
    return n==1 or n==7
n=int(input())
print(happy_num(n))
            
