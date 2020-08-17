# checking whether the given number is prime or not by using for loop
n=int(input("enter a number"))
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(n,"is not a prime number")
        break
else:
    print(n,"is a prime number")
#checking whether the given number is prime or not by using while loop
n=int(input("enter a number"))
i=2
while i<=int(n**0.5):
    if n%i==0:
        print(n,"is not a prime number")
        break
    i+=1
else:
    print(n,"is a prime number")
    
