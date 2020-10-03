#decimal to binary conversion
def decimal_binary(n):
    s=''
    while n>0:
        r=n%2
        s+=str(r)
        n//=2
    return s[::-1]
n=int(input("enter a decimal value"))
print(decimal_binary(n))


#binary to decimal conversion
def binary_decimal(n):
    i=0
    s=0
    while n>0:
        r=n%10
        s+=r*2**i
        n//=10
        i+=1
    return s
n=int(input("enter a binary value"))
print(binary_decimal(n))


#decimal to octal conversion
def decimal_octal(n):
    s=''
    while n>0:
        r=n%8
        s+=str(r)
        n//=8
    return s[::-1]
n=int(input("enter a decimal value"))
print(decimal_octal(n))


#octal to decimal conversion
def octal_decimal(n):
    i=0
    s=0
    while n>0:
        r=n%10
        s+=r*8**i
        n//=10
        i+=1
    return s
n=int(input("enter a octal value"))
print(octal_decimal(n))





#decimal to hexadecimal conversion
def decimal_hexadecimal(n):
    s=''
    while n>0:
        r=n%16
        if r in range(10,16):
            s+=chr(55+r)
        else:
            s+=str(r)
        n//=16
    return s[::-1]
n=int(input("enter a decimal value"))
print(decimal_hexadecimal(n))



#hexadecimal to decimal
def hexadecimal_decimal(n):
    s=0
    j=len(n)-1
    for i in range(len(n)):
        if n[i].isalpha():
            s+=(ord(n[i])-55)*16**j
            j-=1
        else:
            s+=int(n[i])*16**j
            j-=1
    return s
n=input("enter hexadecimal value")
print(hexadecimal_decimal(n))

            
            

            













