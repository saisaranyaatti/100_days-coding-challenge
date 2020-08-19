#finding the sum of digits of a given number by using while loop
def digit_sum(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n//=10
    return sum
n=int(input("enter a number"))
print(digit_sum(n))

#finding the sum of digits of a given number by using for loop
def digit_sum(n):
    sum=0
    for i in n:
        sum+=int(i)
    return sum
n=input("enter a number")
print(digit_sum(n))


#finding the sum of digits of a given number by using recursion
def digit_sum(n):
    if n==0:
        return 0
    else:
        return (n%10)+digit_sum(n//10)
n=int(input("enter a number"))
print(digit_sum(n))



        
