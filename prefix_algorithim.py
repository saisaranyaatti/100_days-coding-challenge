#without prefix algorithim
n=int(input())
l1=list(map(int,input().split()))
t=int(input())
for i in range(t):
    sum=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        sum+=l1[i]
    print(sum)
'''by using this methodology it raises time limit error'''
'''so we prefer prefix algorithim to execute code in less time'''
#with prefix algorithim
n=int(input())
l=list(map(int,input().split()))
p=[]#prefix array 
p.append(l[0])#initial position element of prefix array is the initial postion element in given array
for i in range(1,n):
    p.append(l[i]+p[i-1])#from second positon the prefix array stores the sum of elements from initial position to that postion it self
print(p)
t=int(input())#number of test cases
for i in range(t):
    l,r=map(int,input().split())#starting and ending positions
    sum=p[r]#sum is the element at ending position in prefix array(i:e r)
    if l>0:#if starting position > 0 then the sum of elemnts from starting position to ending postion is the element at the ending position(r)-the element at the starting postion-1(l-1)
        sum=p[r]-p[l-1]
    print(sum)

