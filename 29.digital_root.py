'''Digital Root:digital root of a number is the recursive sum of its digits untill
we get a single digit number'''
'''ex:99999=45
   45=9'''
def Digital_root(n):
    while n>9:
        k=n
        s=0
        while k>0:
            r=k%10
            s+=r
            k//=10
        if s<=9:
            return s
            break
        else:
            n=s
    else:
        return n
n=int(input())
print(Digital_root(n))


#recursively
def digital_root(n):
    if n<=9:
        return n
    else:
        s=0
        while n>0:
            r=n%10
            s+=r
            n//=10
        return digital_root(s)
n=int(input())
print(digital_root(n))
            
            
